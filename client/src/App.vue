<template>
  <navbar></navbar>
  <scanner></scanner>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
// import Register from '@/components/Register.vue'
import Scanner from '@/components/Scanner.vue'

export default {
  name: 'App',
  components: {
    Scanner,
    Navbar
  },
  mounted() {
    console.log('mounted')
  }
}
</script>

<style scoped>

</style>
