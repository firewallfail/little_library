<template>
    <div>bunch of text</div>
    <button @click="login">login</button>
    <button @click="logout">logout</button>
</template>

<script>
async function login2() {
  let username = 'test9'
  let email = username
  let password = 'clubmed7'
  let token = ''
  const response = await fetch('http://localhost:8000/api/user/login', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: username,
      password: password,
      email: email
    })
  })
  const token_res = await response.json()
  token = token_res.data.token
  console.log(token)
  return token
}
async function logout2(token) {
  console.log('happening')
  const out = await fetch('http://localhost:8000/api/user/logout', {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'x-access-token': token
    }
  })
  document.cookie = 'session' + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

export default {
  name: 'Register',
  data() {
    return {
      something: '12',
      username: '',
      password: '',
      public_id: '',
      token: ''
    }
  },
  methods: {
    async logout(event) {
      const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUsInB1YmxpY19pZCI6IjllODQ4ODZjLTI0N2YtNGU3YS04MTUzLTUxZWEyMzYxNzBkNCIsImVtYWlsIjoidGVzdDkiLCJ1c2VybmFtZSI6InRlc3Q5In0.42oMYkBfnlNCPiodROMEGjwRaIbZW5OjGoogUyshmQw'
      logout2(token)
    },
    async login(event) {
      login2()
    }
  },
  beforeMount() {
    // this.token = await login()
  },
  mounted() {
    // const unlogged = await logout(this.token)
    // document.cookie = 'session' +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }
}
</script>

<style scoped>

</style>