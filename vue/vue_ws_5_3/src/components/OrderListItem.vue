<template>
  <li>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      this.$store.commit('addOrder', this.menu)
    },
  },
}
</script>

<style>
</style>