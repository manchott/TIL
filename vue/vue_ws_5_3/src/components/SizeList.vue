<template>
  <div class="inside-box">
    <h2 style="">2. 사이즈를 고르세요.</h2>
    <sizeListItem
      v-for="(size, index) in sizeList"
      :key="index"
      :size="size"
    />
  </div>
</template>

<script>
import SizeListItem from '@/components/SizeListItem'
export default {
  name: 'SizeList',
  components: {
    SizeListItem
  },
  computed: {
    sizeList: function () {
      return this.$store.state.sizeList
    },
  },
}
</script>

<style>

.h2{
  text-align: end;
}
</style>