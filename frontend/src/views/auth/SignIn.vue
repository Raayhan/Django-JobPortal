<template>
    <div class="bg-gray-100 p-6 min-h-screen">
        <div class="flex mt-8">
            <span class="mx-auto text-gray-500 mb-4 text-2xl"> Sign in to your account</span>
        </div>
        <div class=" w-full md:w-3/12 mx-auto mt-4">
            <form @submit.prevent="handleSubmit">
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="form.username" />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="form.password" />
                <div class="" v-if="form.errors.length">
                    <ul v-for="error in form.errors" v-bind:key="error">
                        <li class="bg-red-100 text-red-800 mb-2 ring-1 ring-red-200 text-center rounded p-2">{{ error }}
                        </li>
                    </ul>

                </div>
                <button type="submit" :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-700': !isSubmitting }"
                    :disabled="isSubmitting" class="mb-4 text-white flex justify-center w-full rounded p-3 mt-4">Sign
                    in</button>
            </form>
            <span>Don't have an account? </span>
            <router-link class="text-blue-700 font-bold hover:underline" to="/sign-up">Sign up</router-link> to create
            one
        </div>
    </div>

</template>

<script>
import InputField from '@/components/InputField.vue'
import axios from 'axios'

export default {
    name: 'SignIn',
    components: {
        InputField
    },
    data() {
        return {
            form: {
                username: '',
                password: '',
                errors: []
            },
            isSubmitting: false
        };
    },
    methods: {
        async handleSubmit() {
            this.form.errors = []
            if (this.form.username === '') {
                this.form.errors.push('Username is required')
            }
            if (this.form.password === '') {
                this.form.errors.push('Password is required')
            }
            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const formData = {
                    username: this.form.username,
                    password: this.form.password
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
            
           
        }
    },
    mounted() {
        document.title = 'Sign in | Djobs'
    }
}
</script>