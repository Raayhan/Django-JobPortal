<template>
    <div
        class="border border-indigo-200 bg-indigo-50 p-4 mx-1 rounded shadow duration-100 mb-4 max-h-56 min-h-56 relative">
        <div class="text-indigo-800 font-bold mb-2">{{ job.title }}</div>
        <div class="text-sm text-red-800 flex mb-2">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-4 mr-1">
                <path
                    d="M11.584 2.376a.75.75 0 0 1 .832 0l9 6a.75.75 0 1 1-.832 1.248L12 3.901 3.416 9.624a.75.75 0 0 1-.832-1.248l9-6Z" />
                <path fill-rule="evenodd"
                    d="M20.25 10.332v9.918H21a.75.75 0 0 1 0 1.5H3a.75.75 0 0 1 0-1.5h.75v-9.918a.75.75 0 0 1 .634-.74A49.109 49.109 0 0 1 12 9c2.59 0 5.134.202 7.616.592a.75.75 0 0 1 .634.74Zm-7.5 2.418a.75.75 0 0 0-1.5 0v6.75a.75.75 0 0 0 1.5 0v-6.75Zm3-.75a.75.75 0 0 1 .75.75v6.75a.75.75 0 0 1-1.5 0v-6.75a.75.75 0 0 1 .75-.75ZM9 12.75a.75.75 0 0 0-1.5 0v6.75a.75.75 0 0 0 1.5 0v-6.75Z"
                    clip-rule="evenodd" />
                <path d="M12 7.875a1.125 1.125 0 1 0 0-2.25 1.125 1.125 0 0 0 0 2.25Z" />
            </svg>

            {{ job.company }}
        </div>
        <div class="grid grid-cols-2 gap-4 mb-1">
            <div class="text-sm text-gray-600 flex">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-4 mr-1">
                    <path fill-rule="evenodd"
                        d="m11.54 22.351.07.04.028.016a.76.76 0 0 0 .723 0l.028-.015.071-.041a16.975 16.975 0 0 0 1.144-.742 19.58 19.58 0 0 0 2.683-2.282c1.944-1.99 3.963-4.98 3.963-8.827a8.25 8.25 0 0 0-16.5 0c0 3.846 2.02 6.837 3.963 8.827a19.58 19.58 0 0 0 2.682 2.282 16.975 16.975 0 0 0 1.145.742ZM12 13.5a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"
                        clip-rule="evenodd" />
                </svg>
                {{ job.location }}

            </div>
            <div class="text-sm text-gray-600 flex">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-4 mr-1">
                    <path fill-rule="evenodd"
                        d="M7.5 5.25a3 3 0 0 1 3-3h3a3 3 0 0 1 3 3v.205c.933.085 1.857.197 2.774.334 1.454.218 2.476 1.483 2.476 2.917v3.033c0 1.211-.734 2.352-1.936 2.752A24.726 24.726 0 0 1 12 15.75c-2.73 0-5.357-.442-7.814-1.259-1.202-.4-1.936-1.541-1.936-2.752V8.706c0-1.434 1.022-2.7 2.476-2.917A48.814 48.814 0 0 1 7.5 5.455V5.25Zm7.5 0v.09a49.488 49.488 0 0 0-6 0v-.09a1.5 1.5 0 0 1 1.5-1.5h3a1.5 1.5 0 0 1 1.5 1.5Zm-3 8.25a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Z"
                        clip-rule="evenodd" />
                    <path
                        d="M3 18.4v-2.796a4.3 4.3 0 0 0 .713.31A26.226 26.226 0 0 0 12 17.25c2.892 0 5.68-.468 8.287-1.335.252-.084.49-.189.713-.311V18.4c0 1.452-1.047 2.728-2.523 2.923-2.12.282-4.282.427-6.477.427a49.19 49.19 0 0 1-6.477-.427C4.047 21.128 3 19.852 3 18.4Z" />
                </svg>
                {{ job.experience }} Years

            </div>
        </div>
        <div class="grid grid-cols-2 gap-4 mb-2">
            <div class="text-sm text-gray-600 flex"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                    fill="currentColor" class="size-4 mr-1">
                    <path
                        d="M10.464 8.746c.227-.18.497-.311.786-.394v2.795a2.252 2.252 0 0 1-.786-.393c-.394-.313-.546-.681-.546-1.004 0-.323.152-.691.546-1.004ZM12.75 15.662v-2.824c.347.085.664.228.921.421.427.32.579.686.579.991 0 .305-.152.671-.579.991a2.534 2.534 0 0 1-.921.42Z" />
                    <path fill-rule="evenodd"
                        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 6a.75.75 0 0 0-1.5 0v.816a3.836 3.836 0 0 0-1.72.756c-.712.566-1.112 1.35-1.112 2.178 0 .829.4 1.612 1.113 2.178.502.4 1.102.647 1.719.756v2.978a2.536 2.536 0 0 1-.921-.421l-.879-.66a.75.75 0 0 0-.9 1.2l.879.66c.533.4 1.169.645 1.821.75V18a.75.75 0 0 0 1.5 0v-.81a4.124 4.124 0 0 0 1.821-.749c.745-.559 1.179-1.344 1.179-2.191 0-.847-.434-1.632-1.179-2.191a4.122 4.122 0 0 0-1.821-.75V8.354c.29.082.559.213.786.393l.415.33a.75.75 0 0 0 .933-1.175l-.415-.33a3.836 3.836 0 0 0-1.719-.755V6Z"
                        clip-rule="evenodd" />
                </svg>
                {{ job.salary }} ৳</div>
            <div class="text-sm text-gray-600 flex">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-4 mr-1">
                    <path fill-rule="evenodd"
                        d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM12.75 6a.75.75 0 0 0-1.5 0v6c0 .414.336.75.75.75h4.5a.75.75 0 0 0 0-1.5h-3.75V6Z"
                        clip-rule="evenodd" />
                </svg>
                {{ formatDate(job.deadline) }}

            </div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4">
            <div class="text-xs text-green-800 hover:underline hover:font-bold">
                <router-link :to="job.category_name"> #{{ job.category_name }}</router-link>
            </div>
            <div class="flex justify-end text-xs text-gray-500">Published on: {{ formatDate(job.date_added) }}</div>
        </div>
        <div class="flex text-xs mt-2 absolute bottom-3">
            <router-link :to="job.get_absolute_url"
                class="mr-2 bg-indigo-800 text-white p-2 rounded hover:bg-indigo-900">View
                Details</router-link>
            <router-link v-if="!isAlreadyApplied" :to="job.get_absolute_url + `apply`"
                class="bg-green-800 text-white p-2 rounded hover:bg-green-900">Apply Now</router-link>

            <span v-else class="flex items-center align-middle text-green-800"> <svg xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5 mr-0.5">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>
                Already Applied</span>
        </div>

    </div>

</template>
<script>
import moment from 'moment'
import axios from 'axios'

export default {
    name: 'JobBox',
    data() {
        return {
            isAlreadyApplied : false
      }  
    },
    props: {
        job: Object
    },
    mounted() {
        if (this.isAuthenticated) {
            this.checkApplication()
        }  
    },
    methods: {
        formatDate(date) {
            return moment(date).format('DD-MM-YYYY');
        },
        checkApplication() {
            const job_id = this.job.id;
            const user_id = `${this.currentUser.id}`;
            axios.get(`/api/v1/applications/check/${user_id}/${job_id}/`)
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
        }
    }


}
</script>