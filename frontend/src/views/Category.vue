<template>
    <div class="grid grid-cols-4 mx-4 mt-6">
        <JobBox v-for="job in category.jobs" v-bind:key="job.id" v-bind:job="job"></JobBox>
    </div>
</template>
<script>
import axios from 'axios'
import JobBox from '@/components/JobBox.vue'
export default {
    name: 'Category',
    data() {
        return {
            category: {
                jobs: []
            }
        }
    },
    components: {
        JobBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const category_slug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)
            await axios
                .get(`/api/v1/jobs/${category_slug}/`)
                .then(response => {
                    this.category = response.data
                    document.title = this.category.name + ' | Djobs'
                })
                .catch(error => {
                    console.log(error)
                    
                })
            this.$store.commit('setIsLoading', false)


        }
    }
}
</script>