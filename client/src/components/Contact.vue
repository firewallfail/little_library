<template>
    <div class="form">
        <p>Send us a message</p>
        <textarea v-model="message" name="text" wrap="soft"> </textarea><br><br>
        <button :disabled="message" @click="send_message">Submit</button>
    </div>
</template>

<script>
  
  export default {
    name: "Contact",
    data() {
        return {
            message: ''
        }
    },
    methods: {
      async send_message() {
        const response = await fetch('/api/contact', {
          method: 'post',
          mode: 'cors',
          body: JSON.stringify({
            'message': this.message
          }),
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        const message_sent = await response.json()
        if (message_sent.status !== 'success') {
            this.$toast.open({message: message_sent.data, type: "error"})
            return
        }
        this.$toast.open({message: 'Message Sent'})
        this.message = ''
      }
    }
}
</script>

<style scoped>
div.form
{
    display: block;
    text-align: center;
}
textarea
{
    display: inline-block;
    text-align: left;
    padding-bottom: 6rem;
    width: 80%
}
</style>