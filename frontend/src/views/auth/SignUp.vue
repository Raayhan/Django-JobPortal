<template>
    <div class="bg-gray-100 p-6 min-h-screen">
        <div class="flex mt-24">
            <span class="mx-auto text-gray-500"> Sign up for an account</span>
        </div>
        <div class=" w-full md:w-2/12 mx-auto mt-4 text-xs">
            <form @submit.prevent="handleSubmit">
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="formData.username" />
                <InputField id="email" label="Email" type="email" placeholder="Enter Email" v-model="formData.email" />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="formData.password" />
                <InputField id="confirm-password" label="Confirm Password" type="password" placeholder="Confirm Password"
                    v-model="formData.password2" />
                <button type="submit"
                    class="bg-indigo-700 mb-4 text-white flex justify-center w-full rounded p-2 text-xs">Sign
                    in</button>
            </form>
            <span>Already have an account? </span>
            <router-link class="text-blue-700 font-bold hover:underline" to="/sign-in">Sign in</router-link> to create
            one
        </div>
    </div>

</template>

<script>
import InputField from '@/components/InputField.vue'
export default {
    name: 'SignUp',
    components: {
        InputField
    },
    data() {
        return {
            formData: {
                username: '',
                email: '',
                password: '',
                password2: '',
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
        document.title = 'Sign up | DIJobs'
    }
}
</script>