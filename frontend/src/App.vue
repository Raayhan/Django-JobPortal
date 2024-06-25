<template>
  <nav class="bg-gray-800">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
          <!-- Mobile menu button-->
          <button type="button" @click="isOpenMobile = !isOpenMobile"
            class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
            aria-controls="mobile-menu" aria-expanded="false">
            <span class="absolute -inset-0.5"></span>
            <span class="sr-only">Open main menu</span>
            <!--
            Icon when menu is closed.

            Menu open: "hidden", Menu closed: "block"
          -->
            <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <!--
            Icon when menu is open.

            Menu open: "block", Menu closed: "hidden"
          -->
            <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
              aria-hidden="true">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
          <div class="flex text-white text-xl tracking-widest flex-shrink-0 items-center font-bold">
            <router-link to="/">DJobs</router-link>
           
          </div>
          <div class="hidden sm:ml-6 sm:block">
            <div class="flex space-x-4">
              <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
              <router-link to="/"
                class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Jobs</router-link>
              <router-link to="/applications" v-if="$store.state.isAuthenticated"
                class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Applications</router-link>

            </div>
          </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">


          <!-- Profile dropdown -->
          <div class="relative ml-3 flex">
            <template v-if="!$store.state.isAuthenticated">
              <router-link class="relative flex rounded-full bg-gray-800 text-white text-sm mr-4" to="/sign-in">Sign
                in</router-link>
            </template>

            <template v-if="$store.state.isAuthenticated">
              <div>
                <button @click="isOpen = !isOpen" class="relative flex rounded-full bg-gray-800 text-white text-sm"
                  id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                  <span class="absolute -inset-1.5"></span>
                  <span class="sr-only">Open user menu</span>
                  {{ currentUser ? currentUser.first_name + ' ' + currentUser.last_name : 'Loading...' }}
                  <span v-if="!isOpen">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                      stroke="currentColor" class="size-4 ml-1">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
                    </svg>
                  </span>
                  <span v-else>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="size-4 ml-1">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
                    </svg>

                  </span>


                </button>
              </div>


              <div v-if="isOpen"
                class="absolute right-0 z-10 mt-6 w-48 duration-300 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
                role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                <!-- Active: "bg-gray-100", Not Active: "" -->
                <ul>
                  <li class="hover:bg-indigo-100"><router-link @click="isOpen = false" to="/profile" class="block px-4 py-2 text-sm text-gray-700"
                      role="menuitem" tabindex="-1" id="user-menu-item-0">Account</router-link></li>
                  <li class="hover:bg-indigo-100"> <button @click="logout()"
                      class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1"
                      id="user-menu-item-2">Sign out</button></li>
                </ul>



              </div>
            </template>

          </div>
        </div>
      </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div v-if="isOpenMobile" class="sm:hidden" id="mobile-menu">
      <div class="space-y-1 px-2 pb-3 pt-2">
        <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
        <router-link to="/"
          class=" text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium"
          aria-current="page">Jobs</router-link>
        <router-link to="/applications" v-if="$store.state.isAuthenticated"
          class="text-gray-300 hover:bg-gray-700 hover:text-white rounded-md px-3 py-2 text-sm font-medium">Applications</router-link>
      </div>
    </div>
  </nav>
  <router-view />
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      isOpen: false,
      isOpenMobile: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common["Authorization"] = `Token ${token}`
    }
    else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    logout() {

      this.isOpen = false
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")
      
      this.$store.commit('removeToken')
      this.$router.push('/sign-in')

    }
  },
  
}
</script> -->
