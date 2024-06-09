<template>

    <h1>Apply for : {{ job.title }}</h1>

</template>
<script>
import axios from 'axios'

export default {
    name: 'JobApplication',
    data() {
        return {
            job: {}
        }
    },
    mounted() {
        this.getJobDetails()
    },
    methods: {
        async getJobDetails() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug
            const job_slug = this.$route.params.job_slug

            await axios
                .get(`/api/v1/jobs/${category_slug}/${job_slug}`)
                .then(response => {
                    this.job = response.data
                    document.title = this.job.title + ' | Djobs'
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },


    }
   
}
</script>