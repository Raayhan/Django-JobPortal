<template>
  <div class="about">
    <h1 class="text-xl text-gray-500 ml-4 mt-12 border-l-4 border-gray-500 w-3/12"> &nbsp; &nbsp;My Applications</h1>



    <div class="relative overflow-x-auto px-16 mt-12 rounded">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400 border-b">
          <tr>
            <th scope="col" class="px-6 py-3">
              Title
            </th>
            <th scope="col" class="">
              Company
            </th>
            <th scope="col" class="">
              Location
            </th>
            <th scope="col" class="">
              Status
            </th>
            <th scope="col" class="">
              Submitted
            </th>
            <th scope="col" class="">
              Deadline
            </th>
            <th scope="col" class="">
              Action
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="application in applications" v-bind:key="application.id" v-bind:application="application"
            class="bg-white border-b">
            <th scope="row" class="px-6 py-2 font-medium text-gray-900 whitespace-nowrap">
              <router-link class="text-indigo-800 hover:underline" :to="application.job.get_absolute_url"> {{ application.job.title }}</router-link>
              </th>
            <td class="">
              {{ application.job.company }}
            </td>
            <td class="">
              {{ application.job.location }}
            </td>
            <td class="">
              <span :class="statusClass(application.status)">{{ statusText(application.status) }}</span>
            </td>
            <td class="">
              {{ formatDate(application.created_at) }}
            </td>
            <td class="">
              {{ formatDate(application.job.deadline) }}
            </td>
            <td class="">
              <button class="text-red-700 font-bold underline">Withdraw</button>
            </td>
          </tr>

        </tbody>
      </table>
    </div>


  </div>
</template>
<script>
import axios from 'axios'
import moment from 'moment';

export default {
  name: 'Applications',
  data() {
    return {
      applications:[],
      statuses: {
        '0': { class: 'text-xs text-violet-700 bg-violet-100 font-bold tracking-wider capitalized rounded py-1 px-2', text: 'Application Received' },
        '1': { class: 'text-xs text-yellow-700 bg-yellow-100 font-bold capitalized tracking-wider rounded py-1 px-2', text: 'Under Consideration' },
        '2': { class: 'text-xs text-green-700 bg-green-100 font-bold capitalized tracking-wider rounded py-1 px-2', text: 'Accepted' },
        '3': { class: 'text-xs text-red-700 bg-red-100 font-bold capitalized tracking-wider rounded py-1 px-2', text: 'Rejected' },

      },
    }
    
  },
  mounted() {
    document.title = 'Applications | DJobs';
    this.getApplications()
    

  },
  methods: {

    async getApplications() {
      this.$store.commit('setIsLoading', true)
      const token = localStorage.getItem('token');
      await axios
        .get('api/v1/applications/user', {
          headers: {
            "Content-Type": "multipart/form-data",
            "Authorization": `Token ${token}`
          }
        })
        .then(response => { this.applications = response.data })
        .catch(error => {
          console.log(error)

        })
      this.$store.commit('setIsLoading', false)
      //console.table(this.applications)
       
    },

    formatDate(date) {

      return moment(date).format('DD-MM-YYYY');
    },
    statusClass(status) {
      return this.statuses[status]?.class || '';
    },
    statusText(status) {
      return this.statuses[status]?.text || 'Unknown';
    },
    

  }
  

}
</script>