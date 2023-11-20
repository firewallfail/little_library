<template>
    <Transition name="fade">
        <div class="side_nav">
            <router-link to="/">Scan</router-link>
            <router-link to="/books">Books</router-link>
            <router-link to="/about">About</router-link>
            <router-link v-if="$NTFY_ENABLED" to="/contact">Contact</router-link>
        </div>
    </Transition>
</template>
  
<script>
export default {
    name: 'SideNavbar',
    data() {
        return {
        }
    },
    methods: {
    }
}
</script>

<style scoped>
.side_nav {
    display: flex;
    flex-direction: column;
    position: fixed;
    height: 100%;
    width: 70%;
    color: #f2f2f2;
    max-width: 20rem;;
    background-color: #243E36;
    z-index: 1;
}
.side_nav a {
    color: #f2f2f2;
    padding-top: 1.3rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    padding-bottom: 1.3rem;
    text-decoration: none;
}

.side_nav a:hover {
    background: #7CA982;
    color: black;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>