<template>
    <div class="book-card">
        <div @click="book_card_transition">
            <p>Title: {{ book.title }}</p>
            <Transition name="fade">
              <div v-if="show">
                  <p>Authors: {{ book.authors }}</p>
                  <p>Published: {{ book.published_date }}</p>
                  <p>Description: {{ book.description }}</p>
                  <p>Page Count: {{ book.page_count }}</p>
                </div>
            </Transition>
            <img v-bind:src="book.thumbnail">
            <p>QTY: {{ book.count }}</p>
        </div>
        <button @click="add_remove_book('add')">Add</button>
        <button @click="add_remove_book('remove')">Remove</button>
    </div>
</template>

<script>
  
  export default {
    name: "BookCard",
    props: ['book'],
    data() {
        return {
            show: false
        }
    },
    methods: {
        async add_remove_book(change) {
            const response = await fetch(`/api/book/${this.book.upc}/change-count`, {
                method: 'PATCH',
                mode: 'cors',
                credentials: 'omit',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "count": change
                })
            })
            const book_count_change_response = await response.json()
            if (book_count_change_response.status !== "success") {
                this.$toast.open({message: book_count_change_response.data, type: "error"})
                return
            }
            switch(change) {
                case "add":
                    this.book.count ++
                    break;
                case "remove":
                    this.book.count --
                    break;
                default:
                    break;
            }
            this.$toast.open({message: "Thank you!"})
        },
        book_card_transition () {
            this.show = !this.show
        }
    }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>