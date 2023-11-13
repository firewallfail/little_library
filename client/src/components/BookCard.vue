<template>
    <div class="book-card">
      <p>Title: {{ book.title }}</p>
      <p>Authors: {{ book.authors }}</p>
      <p>Published: {{ book.published_date }}</p>
      <p>Description: {{ book.description }}</p>
      <p>Page Count: {{ book.page_count }}</p>
      <p>QTY: {{ book.count }}</p>
      <img v-bind:src="book.thumbnail">
    </div>
</template>

<script>
  
  export default {
    name: "BookCard",
    props: ['book'],
    setup(props) {
        console.log(props)
    }
}
</script>

<style>
  .book-card {
    border: 5px solid black;
    border-radius: 2rem;
    padding: 2rem;
    margin: 2rem;
  }
</style>