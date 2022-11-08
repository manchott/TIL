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
        selected: true,
        image: `<https://source.unsplash.com/featured/?americano>`
      },
    ],
    sizeList: [
      {
        name: 'small',
        price: 500,
        selected: true,
      },
      {
        name: 'medium',
        price: 700,
        selected: true,
      },
      {
        name: 'large',
        price: 1000,
        selected: true,
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function () {},
    updateSizeList: function () {},
  },
  actions: {
  },
  modules: {
  }
})