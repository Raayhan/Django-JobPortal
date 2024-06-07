<template>
  <h1 class="flex justify-center text-2xl text-gray-400 my-4">Latest Hot Jobs</h1>
  <div class="grid grid-cols-4 gap-4">
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
    document.title = 'Home | DIJobs'
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
