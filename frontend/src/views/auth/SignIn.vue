<template>
    <div class="bg-gray-100 p-6 min-h-screen">
        <div class="flex mt-24">
            <span class="mx-auto text-gray-500"> Sign in to your account</span>
        </div>
        <div class=" w-full md:w-2/12 mx-auto mt-4 text-xs">
            <form @submit.prevent="handleSubmit">
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="formData.username" />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="formData.password" />
                    <button type="submit" class="bg-indigo-700 mb-4 text-white flex justify-center w-full rounded p-2 text-xs">Sign in</button>
            </form>
            <span>Don't have an account? </span>
            <router-link class="text-blue-700 font-bold hover:underline" to="/sign-up">Sign up</router-link> to create one
        </div>
    </div>

</template>

<script>
import InputField from '@/components/InputField.vue'
export default {
    name: 'SignIn',
    components: {
        InputField
    },
    data() {
        return {
            formData: {
                username: '',
                password: ''
            }
        };
    },
    methods: {
        handleSubmit() {
            console.log(this.formData);
            // Handle form submission logic here
        }
    },
    mounted() {
        document.title = 'Sign in | DIJobs'
    }
}
</script>