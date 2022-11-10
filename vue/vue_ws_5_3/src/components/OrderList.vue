<template>
  <div class="box">
    <div class="order-box">
      <h2>주문 내역</h2>
      <p>총 1건:</p>
      <OrderListItem
        v-for="(order, index) in orderList"
        :key="index"
        :order="order"
      />
    </div>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'
export default {
  name: 'OrderList',
  components: {
    OrderListItem
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    // totalOrderCount: function () {
    // },
    // totalOrderPrice: function () {
    // },
  },
}
</script>
<style>
.order-box{
  border: 2vw 2vw;
  text-align: start;
  
  background-color: whitesmoke;
  border-radius: 5px;
  height: 500px;
  width: 90%;
}

</style>