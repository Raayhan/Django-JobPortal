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
          <tr v-if="applications.length === 0">
            <td></td>
            <td></td>
            <td></td>
            <td class="py-6">
              No Applications Found
            </td>

          </tr>
          <tr v-else v-for="application in applications" v-bind:key="application.id" v-bind:application="application"
            class="bg-white border-b">
            <th scope="row" class="px-6 py-2 font-medium text-gray-900 whitespace-nowrap">
              <router-link class="text-indigo-800 hover:underline" :to="application.job.get_absolute_url"> {{
                application.job.title }}</router-link>
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
              <button type="button" @click="showModal(application)"
                class="bg-red-700 text-white px-2 py-1 text-xs rounded hover:bg-red-800">Withdraw</button>
            </td>
          </tr>

        </tbody>
      </table>
    </div>


  </div>
  <BaseModal :show="showModalFlag">
    <div class="p-12">
      <div class="text-xl text-center text-red-800 font-medium">Withdraw Confirmation !</div>

      <div class="py-2 text-sm text-center">Are you sure you want to withdraw the application? <br>Please note, once it
        is withdrawn you can not revert it.</div>
      <div class="flex justify-center mt-4">
        <form @submit.prevent="handleSubmit">

          <input id="id" type="hidden" v-model="form.id" />
          <button type="submit" :class="{ 'bg-red-500 animate-pulse': isSubmitting, 'bg-red-700': !isSubmitting }"
            :disabled="isSubmitting" class="px-2 py-1 font-medium w-20 rounded-l mr-1 text-white hover:bg-red-800">
            Confirm
          </button>
        </form>

        <button type="button" class="bg-gray-700 px-2 py-1 font-medium w-20 rounded-r text-white hover:bg-gray-800"
          @click="hideModal">
          Close
        </button>
      </div>


    </div>
  </BaseModal>
</template>
<script>
import axios from 'axios'
import moment from 'moment';
import { ref } from 'vue';
import BaseModal from '@/components/BaseModal.vue'

export default {
  name: 'Applications',
  components: {
    BaseModal
  },
  data() {
    return {
      applications:[],
      statuses: {
        '0': { class: 'text-xs text-violet-700 bg-violet-100 font-bold tracking-wide capitalized rounded py-1 px-2', text: 'Application Received' },
        '1': { class: 'text-xs text-yellow-700 bg-yellow-100 font-bold capitalized tracking-wide rounded py-1 px-2', text: 'Under Consideration' },
        '2': { class: 'text-xs text-green-700 bg-green-100 font-bold capitalized tracking-wide rounded py-1 px-2', text: 'Accepted' },
        '3': { class: 'text-xs text-red-700 bg-red-100 font-bold capitalized tracking-wide rounded py-1 px-2', text: 'Rejected' },

      },
      activeApplication: null,
      form: {
        id: '',
        errors: []
      },
      isSubmitting: false,
      showModalFlag: false,
    }
    
  },
  mounted() {
    document.title = 'Applications | DJobs';
    this.getApplications()
    

  },
  methods: {

    showModal(application) {
      this.activeApplication = application;
      this.form.id = application.id; // Set the form id to the application id
      this.showModalFlag = true;
    },
    hideModal() {
      this.showModalFlag = false;
    },

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

    handleSubmit() {
      this.isSubmitting = true;
      const token = localStorage.getItem('token');
      try {
        // Send DELETE request to delete the application
        axios.delete(`api/v1/applications/withdraw/${this.form.id}`, {
          headers: {
           
            "Authorization": `Token ${token}`
          }
        });

        this.applications = this.applications.filter(app => app.id !== this.form.id);
        this.showModalFlag = false;
        //this.$router.push('/applications');
      } catch (error) {
        this.form.errors = error.response ? error.response.data.errors : ['An error occurred'];
      } finally {
        this.isSubmitting = false;
      }
    },


    formatDate(date) {

      return moment(date).format('DD/MM/YYYY');
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