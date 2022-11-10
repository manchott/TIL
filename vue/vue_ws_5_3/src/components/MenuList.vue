<template>
  <div class="inside-box">
    <h2>1. 음료를 고르세요.</h2>
    <MenuListItem
      v-for="(menu, index) in menuList"
      :key="index"
      :menu="menu"
    />
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'
export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
  },
}
</script>

<style>

</style>