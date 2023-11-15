<template>
  <div class="scanner">
    <div id="reader" class="video"></div>
    <div v-if="barcode">
      <button @click="search_book_barcode">
        Look Up: {{ barcode }}
      </button>
    </div>
    <div v-if="!book_found">
      <input v-model="book_query" placeholder="Book Title"/>
      <button v-if="book_query" @click="search_book_query">Look Up: {{ book_query }}</button>
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
      on_scan_success(decoded_text, decoded_result) {
        this.barcode = decoded_text
        // Handle on success condition with the decoded text or result.
        console.log(`Scan result: ${decoded_text}`);
      },
      async search_book_barcode() {
        const response = await fetch(`http://localhost:8000/api/book/scan/${this.barcode}`, {
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
      },
      async search_book_query() {
        const response = await fetch('http://localhost:8000/api/book/search?' + new URLSearchParams({
          query: this.book_query
        }), {
          method: 'get',
          mode: 'cors',
          credentials: 'omit'
        })
        const bookSearchResponse = await response.json()
        this.book_list = bookSearchResponse.data
        this.book_found = true
      }
    },
    mounted() {
      // let instance = this.$toast.open({message: 'test'});
      let html5QrcodeScanner = new Html5QrcodeScanner("reader",
                                                      { fps: 10,
                                                        qrbox: {width: 140, height: 100},
                                                        formatsToSupport: [ Html5QrcodeSupportedFormats.EAN_13 ]
                                                      }
                                                      );
        html5QrcodeScanner.render(this.on_scan_success);
    }
  }
</script>
  
<style>
  .video {
    width: 100%;
    background-color: #F1F7ED;
    outline: 5px solid black;
    margin-bottom: 1rem;
    /* border-radius: 1rem; */
  }
</style>