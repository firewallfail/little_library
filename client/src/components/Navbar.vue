<template>
  <div class="navbar">
    <header>
      <router-link to="/">Scan</router-link>
      <router-link to="/books">Books</router-link>
      <router-link to="/about">About</router-link>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
    }
  }
}
</script>

<style scoped>

</style>