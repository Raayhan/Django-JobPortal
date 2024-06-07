<template>
    <div class="bg-gray-100 p-6 min-h-screen">

        <div class="flex mt-8">
            <span class="mx-auto text-gray-500 mb-4 text-2xl"> Sign up for an account</span>
        </div>
        <div class=" w-full md:w-3/12 mx-auto mt-4">
            <form @submit.prevent="handleSubmit">
                <InputField id="first_name" label="First Name" type="text" placeholder="Enter First Name"
                    v-model="form.first_name" required />
                <InputField id="last_name" label="Last Name" type="text" placeholder="Enter Last Name"
                    v-model="form.last_name" required />
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="form.username" required />
                <InputField id="email" label="Email" type="email" placeholder="Enter Email" v-model="form.email" />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="form.password" required />
                <InputField id="confirm-password" label="Confirm Password" type="password"
                    placeholder="Confirm Password" v-model="form.password2" required />
                <div v-if="form.errors.length" class="bg-red-100 text-red-800 ring-1 ring-red-200 rounded p-4">
                    <ul class="list-disc">
                        <li v-for="(error, index) in form.errors" :key="index" class=" mb-2 ml-2">
                            {{ error }}
                        </li>
                    </ul>
                </div>
                <button type="submit"
                    :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-700': !isSubmitting }"
                    :disabled="isSubmitting" class="mb-4 text-white flex justify-center w-full rounded p-3 mt-4">Sign
                    up</button>
            </form>
            <span>Already have an account? </span>
            <router-link class="text-blue-700 font-bold hover:underline" to="/sign-in">Sign in</router-link> to create
            one
        </div>

    </div>

</template>

<script>
import InputField from '@/components/InputField.vue'
import axios from 'axios'

export default {
    name: 'SignUp',
    components: {
        InputField
    },
    data() {
        return {
            form: {
                first_name: '',
                last_name:'',
                username: '',
                email: '',
                password: '',
                password2: '',
                errors: []
            },
            isSubmitting: false
        };
    },
    methods: {
        async handleSubmit() {
            //console.table(this.form);
            this.form.errors = []
            
            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const form = {
                    first_name: this.form.first_name,
                    last_name: this.form.last_name,
                    username: this.form.username,
                    email:this.form.email,
                    password: this.form.password,
                };
                try {
                    //console.table(form)
                    const response = await axios.post("/api/v1/users/", form);
                    this.$router.push('/sign-in')

                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {
                            
                            const errors = error.response.data[property];
                            if (Array.isArray(errors)) {
                                errors.forEach(err => this.form.errors.push(err));
                            } else {
                                this.form.errors.push(errors);
                            }
                        }
                    } else {
                        this.form.errors.push('Something went wrong. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                }
            }


            // Handle form submission logic here
        }
    },
    mounted() {
        document.title = 'Sign up | DJobs'
    }
}
</script>