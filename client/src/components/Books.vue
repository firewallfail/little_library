<template>
  <div class="scanner">
    <label for="sort">Sort by: </label> 
    <select v-model="sort_choice" @change="on_sort_change($event)">
      <option v-for="sort in sort_options" v-bind:values="{id: sort.id, text: sort.text}">{{ sort.text }}</option>
    </select>
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
        sort_choice: '',
        sort_options: [
          {id: 1, text: 'Title', Title: 'title'},
          {id: 2, text: 'Published', Published: 'published_date'},
          {id: 3, text: 'Author', Author: 'authors'},
        ],
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
      },
      on_sort_change(event) {
        const sort_strategy = {
          Title: 'title',
          Author: 'authors',
          Published: 'published_date'
        }
        this.book_list.sort((a, b) => {
          const sort_method = sort_strategy[event.target.value]
          const val_a = a[sort_method]
          const val_b = b[sort_method]
          if (val_a < val_b) {
            return -1
          }
          if (val_a > val_b) {
            return 1
          }
          return 0
        })
      }
    },
    mounted() {
        this.get_local_books()
    }
  }
</script>
  
<style scoped>

</style>