<template>
  <div class="item size" @click="pickSize">
      <p>{{ size.name }} </p>
      <p>{{ size.price }}원</p>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    pickSize(event){
      const sizes = document.querySelectorAll(".size")
      sizes.forEach(size => {
        if(size.classList.contains("selected-item")){
          size.classList.remove("selected-item")
        }
      })
      event.currentTarget.classList.toggle("selected-item")
      this.$store.commit('updateSizeList', this.size)
    }
  }
}
</script>

<style>
</style>