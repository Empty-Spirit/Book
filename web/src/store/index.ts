import { createStore } from "vuex";

export const vuexStore = createStore({
  // 定义所需要的状态
  state: {
    isLoading: false,
    userName: ""
  },
  // 同步修改state，里面都是方法  不能异步操作
  // 第一个参数是state，第二个是需要修改的值
  mutations: {
    changeIsLoading(state, val) {
        state.isLoading = val;
    },

    getUserNmae(state, data) {
        state.userName = data;
    }
  },
  // 异步提交mutation，不能直接修改state只能通过提交mutation进行提交
  // 第一个参数是store，第二个参数是修改的值
  actions: {},
  // 模块化
  modules: {},
});

export const piniaStore = createStore({});
