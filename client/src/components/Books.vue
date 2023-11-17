<template>
  <div class="scanner">
    <div v-if="books_found" v-for="book of book_list">
      <BookCard :book="book" />
    </div>
  </div>
</template>
  
<script>
  import BookCard from '@/components/BookCard.vue'
  
  export default {
    name: "Books",
    components: {
      BookCard
    },
    data(){
        return {
            book_list: [],
            books_found: false,
            offset: 0,
            end_of_local: false
        }
    },
    methods: {
      async get_local_books() {
        const response = await fetch('/api/books?' + new URLSearchParams({
          offset: this.offset
        }), {
          method: 'get',
          mode: 'cors',
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        const bookSearchResponse = await response.json()
        if (bookSearchResponse.status !== 'success') {
            this.$toast.open({message: bookSearchResponse.data, type: "error"})
            return
        }
        this.book_list.push(...bookSearchResponse.data)
        this.books_found = true
        this.offset += 50
        if (bookSearchResponse.data.length < 50) {
            this.end_of_local = true
        }
      }
    },
    mounted() {
        this.get_local_books()
    }
  }
</script>
  
<style>

</style>