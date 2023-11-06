<template>
    <header>
        <a href="#home">Home</a>
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        {{ something }}
    </header>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      something: '12'
    }
  }
}
</script>

<style scoped>
header {
    width: 100%;
    background-color: #1fad03;
    overflow: hidden;
    position: fixed;
    top: 0;
}
a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
a:hover {
  background: #ddd;
  color: black;
}
</style>