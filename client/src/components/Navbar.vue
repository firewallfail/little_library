<template>
  <div class="navbar">
    <header>
      <img @click="menu" src="@/icons/icons8-menu-48.png" alt="hamburger menu">
      <router-link to="/">Scan</router-link>
      <router-link to="/books">Books</router-link>
      <router-link to="/about">About</router-link>
      <router-link v-if="$NTFY_ENABLED" to="/contact">Contact</router-link>
    </header>
    <SideNavbar v-if="side_nav_on" />
  </div>

</template>

<script>
import SideNavbar from '@/components/SideNavbar.vue'

export default {
  name: 'Navbar',
  components: {
    SideNavbar
  },
  data() {
    return {
      side_nav_on: false
    }
  },
  methods: {
    menu() {
      console.log(this.side_nav_on)
      this.side_nav_on = !this.side_nav_on
    }
  }
}
</script>

<style scoped>
.navbar {
    width: 100%;
    height: 4rem;
    background-color: #243E36;
    overflow: hidden;
    position: fixed;
    top: 0;
    z-index: 100;
}

header {
  display: flex;
  max-width: 30rem;
  border-right: 1rem;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
}
img {
  display: flex;
  height: 50%;
}
.navbar a {
    color: #f2f2f2;
    padding-top: 1.3rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    padding-bottom: 1.3rem;
    text-decoration: none;
}

.navbar a:hover {
    background: #7CA982;
    color: black;
}

</style>