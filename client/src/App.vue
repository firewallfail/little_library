<template>
  <navbar></navbar>
  <register></register>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Register from '@/components/Register.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Register
  },
  mounted() {
    console.log('mounted')
  }
}
</script>

<style scoped>

</style>
