<template>
  <div class="item menu" @click="pickMenu">
      <img :src="menu.image" alt="">
      <p>{{ menu.title }} </p>
      <p>{{ menu.price }}원</p>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    pickMenu(event){
      const menus = document.querySelectorAll(".menu")
      menus.forEach(menu => {
        if(menu.classList.contains("selected-item")){
          menu.classList.remove("selected-item")
        }
      })
      event.currentTarget.classList.toggle("selected-item")
      this.$store.commit('updateMenuList', this.menu)
    }
  }
}
</script>

<style>

</style>