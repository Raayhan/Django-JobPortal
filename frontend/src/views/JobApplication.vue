<template>

    <div class="text-center text-gray-600 text-2xl my-6">Apply for :
        <span class="text-indigo-800">{{ job.title }}</span>
    </div>
    <div class="text-center text-gray-600 mt-14 text-sm">
        Please fill out below information before submitting your application

    </div>
    <div class=" w-full md:w-3/12 mx-auto mt-6">
        <form @submit.prevent="handleSubmit">
            <InputField id="name" label="Name" type="text" v-model="form.name" readonly />
            <InputField id="email" label="Email" type="email" v-model="form.email" readonly />
            <InputField id="phone" label="Phone" type="number" v-model="form.phone" placeholder="Enter Phone" />
            <InputField id="cv" label="Attach CV" type="file" v-model="form.cv" />
            <InputField id="expected_salary" label="Expected Salary" type="number" v-model="form.expected_salary" placeholder="Enter Expected Salary" />
            <InputField id="notes" label="Notes (Optional)" type="text" v-model="form.notes" placeholder="Enter Additional Notes" />
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
                phone:'',
                cv: '',
                expected_salary: '',
                notes:'',
                errors: []
            },
            isSubmitting: false
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
                const formData = {
                    name: this.form.name,
                    
                };
                try {
                    const response = await axios.post("/api/v1/token/login", formData);
                    const token = response.data.auth_token;
                    this.$store.commit('setToken', token);
                    localStorage.setItem("token", token);
                    await this.$store.dispatch('fetchUser');
                    const toPath = this.$route.query.to || '/applications';
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