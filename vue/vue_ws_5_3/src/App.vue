<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <div class="box">
      <MenuList/>
      <SizeList/>
    </div>
    <button
      @click=""
    >장바구니 담기</button>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
  },
  methods: {
    
  }
}
</script>

<style>
@import url(http://fonts.googleapis.com/earlyaccess/notosanskr.css);
#app{
  width: 90%;
  display: flex;
  flex-direction: column;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif;
  margin: 2% auto;
}
h1{
  font-size: 5vw;
}
ul {
  list-style: none;
}
img{
  border-radius: 20%;
  padding: 5px;
  width: 6vw;
  height: 6vw;
  object-fit: cover;
}
button {
  margin: 2vw 0;
  padding: 1vw 0;
  font-size: 1.5vw;
  color: white;
  border-radius: 5px;
  background-color: #00755E;
  border: 0;
  
}

.box{
  justify-content: space-evenly;
  display: flex;
  background-color: whitesmoke;
  border-radius: 5px;
}
.inside-box{
  margin: 2% 0;
  padding-left: 2%;
  padding-right: 2%;
  border-radius: 5px;
  font-size: 2vw;
  width: 44%;
  text-align: start;
  background-color: white;
}
.item{
  border: solid black 1px;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px; /* Some padding */
  margin-bottom: 3%;
}
.selected-item{
  color: white;
  background-color: #00755E;

}

</style>
