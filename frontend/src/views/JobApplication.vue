<template>

    <div class="text-center text-gray-600 text-2xl my-6">Apply for :
        <span class="text-indigo-800">{{ job.title }}</span>
    </div>
    <div class="text-center text-gray-600 mt-14 text-sm">
        Please fill out below information before submitting your application

    </div>
    <div class=" w-full md:w-3/12 mx-auto mt-6">
        <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
            <InputField id="name" label="Name" type="text" v-model="form.name" readonly />
            <InputField id="email" label="Email" type="email" v-model="form.email" readonly />
            <InputField id="phone" label="Phone" type="text" v-model="form.phone" placeholder="Enter Phone" />
            <div class="mb-3">
                <label :for="cv" class="block text-gray-500 font-bold mb-2">
                    Attach CV
                </label>
                <input :id="cv" type="file" @change="handleFileUpload"
                    class=" p-2 rounded border border-gray-400 focus:outline-blue-700 w-full block" />
            </div>
            <InputField id="expected_salary" label="Expected Salary" type="number" v-model="form.expected_salary"
                placeholder="Enter Expected Salary" />
            <InputField id="notes" label="Notes (Optional)" type="text" v-model="form.notes"
                placeholder="Enter Additional Notes" />
            <div class="" v-if="form.errors.length">
                <ul v-for="error in form.errors" v-bind:key="error">
                    <li class="bg-red-100 text-red-800 mb-2 ring-1 ring-red-200 text-center rounded p-2">{{ error }}
                    </li>
                </ul>

            </div>
            <button type="submit"
                :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-700': !isSubmitting }"
                :disabled="isSubmitting" class="mb-4 text-white flex justify-center w-full rounded p-3 mt-4">Submit
                Application</button>
        </form>

    </div>

</template>
<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
import InputField from '@/components/InputField.vue'

export default {
    name: 'JobApplication',
    data() {
        return {
            job: {},
            form: {
                name: '',
                email:'',
                phone:'+88',
                cv: null,
                expected_salary: '',
                notes: '',
                errors: []
            },
            isSubmitting: false,
            cv:null
        }
    },
    props: {
        category_slug: {
            type: String,
            required: true
        },
        job_slug: {
            type: String,
            required: true
        }
    },
    components: {
        InputField
    },
    mounted() {
        this.setInitialName();
        this.getJobDetails()
    },
    computed: {
        ...mapGetters(['currentUser']),
    },
    watch: {
        currentUser(newUser) {
            if (newUser) {
                this.form.name = `${newUser.first_name} ${newUser.last_name}`;
                this.form.email = `${newUser.email}`;
            }
        }
    },
    methods: {

        handleFileUpload(event) {
            this.form.cv = event.target.files[0];
        },
        setInitialName() {
            if (this.currentUser) {
                this.form.name = `${this.currentUser.first_name} ${this.currentUser.last_name}`;
                this.form.email = `${this.currentUser.email}`;
            }
        },
        
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
        async handleSubmit() {
            this.form.errors = []
            if (this.name === '') {
                this.form.errors.push('Name can not be blank')
            }
            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const formData = new FormData();
                formData.append('name', this.form.name);
                formData.append('email', this.form.email);
                formData.append('phone', this.form.phone);
                formData.append('cv', this.form.cv); 
                formData.append('expected_salary', this.form.expected_salary);
                formData.append('notes', this.form.notes);
                
                try {
                    
                    const category_slug = this.$route.params.category_slug
                    const job_slug = this.$route.params.job_slug
                    const token = localStorage.getItem('token');  // Adjust based on your auth implementation
                    const response = await axios.post(`/api/v1/jobs/${category_slug}/${job_slug}/apply`, formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                            "Authorization": `Token ${token}`
                        }
                    });
                    const toPath = '/applications';
                    this.$router.push(toPath);

                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.form.errors.push(`${error.response.data[property]}`);
                        }
                    } else {
                        this.form.errors.push('Something went wrong. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                }
            }


        },


    }
   
}
</script>