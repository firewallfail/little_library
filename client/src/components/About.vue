<template>
    <div class="about-card" @click="expand_text('purpose')">
        <Transition name="fade">
            <div>
                <p>
                    <img class="icon" v-if="show.purpose" src="@/icons/icons8-compress-arrow-50.png" alt="compress arrow">
                    <img class="icon" v-if="!show.purpose" src="@/icons/icons8-expand-arrow-50.png" alt="expand arrow">
                    Purpose
                </p>
                <div v-if="show.purpose">
                    <p>
                        This site is intended to be used as a quick way to check what books are currently in the library.
                        I thought of this as a way to make the library more accessible to people that may not be able to visit frequently.
                    </p>
                </div>
            </div>
        </Transition>
    </div>
    <div class="about-card" @click="expand_text('books')">
        <Transition name="fade">
            <div>
                <p>
                    <img class="icon" v-if="show.books" src="@/icons/icons8-compress-arrow-50.png" alt="compress arrow">
                    <img class="icon" v-if="!show.books" src="@/icons/icons8-expand-arrow-50.png" alt="expand arrow">
                    Books
                </p>
                <div v-if="show.books">
                    <p>
                        Selecting Books will show you all the books that are currently in the library. This relies on
                        the comunity keeping it up to date. We'll do our best to make inventory adjustments from time
                        to time.
                    </p>
                </div>
            </div>
        </Transition>
    </div>
    <div class="about-card" @click="expand_text('scan')">
        <Transition name="fade">
            <div>
                <p>
                    <img class="icon" v-if="show.scan" src="@/icons/icons8-compress-arrow-50.png" alt="compress arrow">
                    <img class="icon" v-if="!show.scan" src="@/icons/icons8-expand-arrow-50.png" alt="expand arrow">
                    Scan
                </p>
                <div v-if="show.scan">
                    <p>
                        Selecting Scan will bring you to a page with a barcode scanner. This relies on a pretty good image
                        of the books barcode and the api for book lookup being accurate. If a scan returns a different book
                        than expected you can also search for the book manually.
                    </p>
                </div>
            </div>
        </Transition>
    </div>
    <div class="about-card" @click="expand_text('compatibility')">
        <Transition name="fade">
            <div>
                <p>
                    <img class="icon" v-if="show.compatibility" src="@/icons/icons8-compress-arrow-50.png" alt="compress arrow">
                    <img class="icon" v-if="!show.compatibility" src="@/icons/icons8-expand-arrow-50.png" alt="expand arrow">
                    Compatibility
                </p>
                <div v-if="show.compatibility">
                    <p>
                        Chrome has built in barcode scanning on mobile which seems to have the best results. Firefox also has barcode scanning
                        built in but it seems to be less reliable. Safari hasn't been tested yet so that's in the air. Scanning from a computer
                        is very unreliable and manual search is likely faster and easier.
                    </p>
                </div>
            </div>
        </Transition>
    </div>
    <div class="about-card" @click="expand_text('url')">
        <Transition name="fade">
            <div>
                <p>
                    <img class="icon" v-if="show.url" src="@/icons/icons8-compress-arrow-50.png" alt="compress arrow">
                    <img class="icon" v-if="!show.url" src="@/icons/icons8-expand-arrow-50.png" alt="expand arrow">
                    URL
                </p>
                <div v-if="show.url">
                    <p>
                        I bought the domain as a joke, at this point I'm too invested in it to bother migrating
                        everything to a more sensible domain.
                    </p>
                </div>
            </div>
        </Transition>
    </div>
    <p class="icons-8">Icons by <a class="link-text" href="https://icons8.com/">Icons8</a></p>
</template>

<script>
  
  export default {
    name: "About",
    data() {
        return {
            show: {}
        }
    },
    methods: {
        expand_text(container) {
            this.show[container] = !this.show[container]
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