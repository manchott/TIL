<template>
  <div class="border">
    <h1>내가 만든 컴포넌트!</h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'
export default {
  name:'MyComponent',
  components: {
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터!!',
    }
  },
  methods:{
    parentGetEvent: function(childData) {
      console.log(childData)
      console.log('용돈 없어!!')
    },
    getDynamicData: function(childInputData) {
      console.log(`사용자의 입력은 ${childInputData}입니다`)
    }
  }
}
</script>
<style>
  .border {
    border: solid 1px black;
  }
</style>