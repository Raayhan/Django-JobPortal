<template>
    <div class="p-8">
        <div class="bg-gray-100 p-8 rounded">
            <div class="text-xl text-indigo-800 font-bold mb-6">{{ job.title }}</div>
            <div class="text-red-800 flex mb-2">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-5 mr-1">
                    <path
                        d="M11.584 2.376a.75.75 0 0 1 .832 0l9 6a.75.75 0 1 1-.832 1.248L12 3.901 3.416 9.624a.75.75 0 0 1-.832-1.248l9-6Z" />
                    <path fill-rule="evenodd"
                        d="M20.25 10.332v9.918H21a.75.75 0 0 1 0 1.5H3a.75.75 0 0 1 0-1.5h.75v-9.918a.75.75 0 0 1 .634-.74A49.109 49.109 0 0 1 12 9c2.59 0 5.134.202 7.616.592a.75.75 0 0 1 .634.74Zm-7.5 2.418a.75.75 0 0 0-1.5 0v6.75a.75.75 0 0 0 1.5 0v-6.75Zm3-.75a.75.75 0 0 1 .75.75v6.75a.75.75 0 0 1-1.5 0v-6.75a.75.75 0 0 1 .75-.75ZM9 12.75a.75.75 0 0 0-1.5 0v6.75a.75.75 0 0 0 1.5 0v-6.75Z"
                        clip-rule="evenodd" />
                    <path d="M12 7.875a1.125 1.125 0 1 0 0-2.25 1.125 1.125 0 0 0 0 2.25Z" />
                </svg>
                {{ job.company }}
            </div>
            <div class="grid grid-cols-1 md:grid-cols-6 gap-4 bg-orange-100 p-4 mb-8 rounded border border-orange-200">
                <div class="text-orange-800">
                    <b>Location :</b> {{ job.location }}
                </div>

                <div class="text-orange-800">
                    <b>Experience :</b> {{ job.experience }} Years
                </div>
                <div class="text-orange-800">
                    <b>Category :</b> {{ job.category_name }}
                </div>
                <div class="text-orange-800">
                    <b>Salary :</b> {{ job.salary }}৳
                </div>
                <div class="text-orange-800">
                    <b>Deadline :</b> {{ formatDate(job.deadline) }}
                </div>
                <div class="text-orange-800">
                    <b>Published :</b> {{ formatDate(job.date_added) }}
                </div>
            </div>

            <div class="text-gray-500 font-bold">Job Description & Requirements</div>
            <div v-html="job.description"
                class="text-gray-600 ml-6 mt-4 overflow-y-auto overflow-x-hidden max-h-[45vh]">

            </div>



        </div>
        <div class="flex justify-center mt-6">
            <router-link v-if="!isAlreadyApplied" :to="job.get_absolute_url+`apply`"
                class="bg-green-800 text-white text-center w-40 py-2 rounded hover:bg-green-900">Apply Now</router-link>
            <span v-else class="bg-green-800 opacity-50 text-white text-center w-40 py-2 rounded"> 
                Already Applied</span>
        </div>


    </div>


</template>
<script>
import axios from 'axios'
import moment from 'moment'

export default {
    name: 'JobDetails',
    data() {
        return {
            job: {},
            isAlreadyApplied: false,
            jobId: null,
        }
    },
    mounted() {
        this.getJobDetails().then(() => {
            if (this.isAuthenticated) {
                this.checkApplication()
            }  
        });
        
    },
    methods: {
        async getJobDetails() {
            this.$store.commit('setIsLoading',true)
            const category_slug = this.$route.params.category_slug
            const job_slug = this.$route.params.job_slug

            await axios
                .get(`/api/v1/jobs/${category_slug}/${job_slug}`)
                .then(response => {
                    this.job = response.data
                    document.title = this.job.title + ' | Djobs'
                    this.jobId = this.job.id;
                    
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        },
        async checkApplication() {
            const job_id = this.jobId;
            const user_id = `${this.currentUser.id}`;
           
            await axios.get(`/api/v1/applications/check/${user_id}/${job_id}/`)
                .then(response => {
                    if (response.data.applied) {
                        // User has already applied for the job
                        // Modify Apply button accordingly
                        this.isAlreadyApplied = true;
                    } else {
                        // User has not applied for the job
                        // Modify Apply button accordingly
                        this.isAlreadyApplied = false;
                    }
                })
                .catch(error => {
                    console.error('Error checking application status:', error);
                });
        },
        
        formatDate(date) {

            return moment(date).format('DD-MM-YYYY');
        }
        
       
    }

}
</script>