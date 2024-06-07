<template>
 
  <div class="grid grid-cols-1 md:grid-cols-3 mx-4 mt-6">
    <JobBox v-for="job in latestJobs" v-bind:key="job.id" v-bind:job="job"></JobBox>
  </div>

</template>

<script>
import axios from 'axios'
import JobBox from '@/components/JobBox.vue'

export default {
  name: 'Home',
  data() {
    return {
      latestJobs: []
    }
  },
  components: {
    JobBox
  },
  mounted() {
    this.getLatestJobs()
    document.title = 'Home | DJobs'
  },
  methods: {
    async getLatestJobs() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('api/v1/latest-jobs')
        .then(response => { this.latestJobs = response.data })
        .catch(error => {
          console.log(error)
          
        })
      this.$store.commit('setIsLoading', false)
      //console.table(this.latestJobs)
    }
  }
  
}
</script>
