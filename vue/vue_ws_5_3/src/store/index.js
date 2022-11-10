import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '라떼',
        price: 3000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?latte'
      },
      {
        title: '오렌지주스',
        price: 3000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?orangejuice'
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 0,
        selected: false,
      },
      {
        name: 'medium',
        price: 500,
        selected: false,
      },
      {
        name: 'large',
        price: 1000,
        selected: false,
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function (state) {
      const selectedMenu = state.menuList.filter(menu => menu.selected === true)
      const selectedSize = state.sizeList.filter(size => size.selected === true)
      console.log(selectedMenu, selectedSize)
      // state.orderList.push(selectedMenu)
      // state.orderList.push(selectedSize)
    },
    updateMenuList: function (state, selectedMenu) {
      state.menuList = state.menuList.map(menu => {
        if(menu === selectedMenu){
          menu.selected = true
        } else{
          menu.selected = false
        }
        return menu
      })
    },
    updateSizeList: function (state, selectedSize) {
      state.sizeList = state.sizeList.map(size => {
        if(size === selectedSize){
          size.selected = true
        } else{
          size.selected = false
        }
        return size
      })
    },
  },
  actions: {
  },
  modules: {
  }
})