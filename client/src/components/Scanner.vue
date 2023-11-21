<template>
  <div class="scanner">
    <div id="reader" class="video"></div>
    <div v-if="barcode">
      <button @click="search_book_barcode">
        Look Up: {{ barcode }}
      </button>
    </div>
    <div ref="searchContainer" style="padding-top: 2rem;">
      <input class="bookSearch" v-model="book_query" v-on:keyup="delayed_search_book_query" placeholder="Search Books"/>
    </div>
    <div v-if="book_found" v-for="book of book_list">
      <BookCard :book="book" />
    </div>
  </div>
</template>
  
<script>
  import {Html5QrcodeScanner, Html5QrcodeSupportedFormats} from "html5-qrcode"
  import BookCard from '@/components/BookCard.vue'
  
  export default {
    name: "Scanner",
    components: {
      BookCard
    },
    data(){
        return {
            barcode: "",
            book_list: [],
            book_found: false,
            book_query: ""
        }
    },
    methods: {
      scroll_to_search() {
        const search = this.$refs.searchContainer
        if (search) {
          this.$nextTick(() => {
            search.scrollIntoView({behavior: 'smooth'})
          })
        }
      },
      on_scan_success(decoded_text, decoded_result) {
        this.barcode = decoded_text
        // Handle on success condition with the decoded text or result.
        console.log(`Scan result: ${decoded_text}`);
      },
      async search_book_barcode() {
        const response = await fetch(`/api/book/scan/${this.barcode}`, {
          method: 'get',
          mode: 'cors',
          credentials: 'omit',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        const bookSearchResponse = await response.json()
        this.book_list = [bookSearchResponse.data]
        this.book_found = true
        this.scroll_to_search()
      },
      async search_book_query() {
        const response = await fetch('/api/book/search?' + new URLSearchParams({
          query: this.book_query
        }), {
          method: 'get',
          mode: 'cors',
          credentials: 'include'
        })
        const bookSearchResponse = await response.json()
        this.book_list = bookSearchResponse.data
        this.book_found = true
        this.scroll_to_search()
      },
      delayed_search_book_query() {
        if (this.timer) {
          clearTimeout(this.timer)
          this.timer = null
        }
        this.timer = setTimeout(() => {
          this.search_book_query()
        }, 800)
      }
    },
    mounted() {
      let qrboxDimensions = function(viewfinderWidth, viewfinderHeight) {
        const width = viewfinderHeight * 0.4
        const height = width * 0.5
        return {
          width: width,
          height: height
        }
      }
      let html5QrcodeScanner = new Html5QrcodeScanner("reader",
                                                      { fps: 2,
                                                        qrbox: qrboxDimensions,
                                                        formatsToSupport: [ Html5QrcodeSupportedFormats.EAN_13 ]
                                                      }
                                                      );
        html5QrcodeScanner.render(this.on_scan_success);
    }
  }
</script>
  
<style scoped>
  .video {
    width: 100%;
    background-color: #F1F7ED;
    outline: 5px solid black;
    margin-bottom: 1rem;
  }

  .bookSearch {
    border: 5px solid #C2A83E;
    background-color: #F1F7ED;
    border-radius: 2rem;
    padding: 2rem;
    outline: none;
  }
</style>