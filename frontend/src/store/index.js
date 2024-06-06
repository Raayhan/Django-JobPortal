import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    isLoading: false,
    user: null,
  },
  getters: {
    currentUser: (state) => state.user,
  },
  mutations: {
    initializeStore(state) {

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        axios.defaults.headers.common["Authorization"] = "Token " + state.token
      }
      else {
        state.token = ''
        state.isAuthenticated = false
        state.user = null
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
      axios.defaults.headers.common["Authorization"] = `Token ${token}`
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
      state.user = null
      delete axios.defaults.headers.common["Authorization"]
    },
    setUser(state, user) {
      state.user = user
    }
  },
  actions: {
    async fetchUser({ commit }) {
      try {
        const response = await axios.get('/api/v1/user/');
        commit('setUser', response.data);
      } catch (error) {
        console.error("Failed to fetch user details:", error);
      }
    }
  },
  modules: {
  }
})
