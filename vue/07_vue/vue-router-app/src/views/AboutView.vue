<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- <router-link :to="{name: 'home'}">선언적 방식 홈으로</router-link>
    <button @click="toHome">프로그래밍 방식 홈으로</button><br> -->
    <input 
      type="text"
      @keyup.enter="goToHello"
      v-model="userInput"
      >
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      userInput: null,
    }
  },
  methods: {
    toHome() {
      this.$router.push({name: 'home'})
    },
    goToHello() {
      this.$router.push({ name: 'hello', params: {userName: this.userInput}})
    }
  }
}
</script>
