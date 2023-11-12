<template>
  <div id="reader" style="width: 100%; height: 50%" class="video"></div>
  <div v-if="barcode">
    <button @click="searchBook">
      Look Up: {{ barcode }}
    </button>
  </div>
</template>
  
<script>
  import {Html5QrcodeScanner} from "html5-qrcode"
  
  export default {
    name: "Scanner",
    data(){
        return {
            barcode: "123123"
        }
    },
    methods: {
      onScanSuccess(decodedText, decodedResult) {
        this.barcode = decodedText
        // Handle on success condition with the decoded text or result.
        console.log(`Scan result: ${decodedText}`, decodedResult);
      },
      async searchBook() {
        const response = await fetch(`http://localhost:8000/api/book/scan/123123`, {
          method: 'get',
          mode: 'cors',
          credentials: 'omit',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        const bookSearchResponse = await response.json()
        const book = bookSearchResponse.data


        console.log(book)
      }
    },
    mounted() {
      let html5QrcodeScanner = new Html5QrcodeScanner("reader", { fps: 10, qrbox: 180 });
        html5QrcodeScanner.render(this.onScanSuccess);
    }
  }
</script>
  
<style>
  .video {
    width: 100%;
  }
</style>