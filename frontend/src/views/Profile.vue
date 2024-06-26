<template>
    <h1 class="text-xl text-gray-500 ml-4 mt-12 border-l-4 border-gray-500 w-3/12"> &nbsp; &nbsp;{{ currentUser ?
        currentUser.first_name + ' ' + currentUser.last_name : 'Loading...' }}'s Profile</h1>


    <div class=" w-4/12 mx-auto mt-6">
        <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <InputField id="first_name" label="First Name" type="text" v-model="form.first_name" />
                </div>
                <div>
                    <InputField id="last_name" label="Last Name" type="text" v-model="form.last_name" />
                </div>
            </div>


            <InputField id="email" label="Email" type="email" v-model="form.email" />
            <div class="" v-if="form.errors.length">
                <ul v-for="error in form.errors" :key="error">
                    <li class="bg-red-100 text-red-800 mb-2 ring-1 ring-red-200 text-center rounded p-2">{{
                        error }}
                    </li>
                </ul>

            </div>
            <div class="flex justify-end">
                <button type="submit"
                    :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-800': !isSubmitting }"
                    :disabled="isSubmitting" class="mb-4 text-white hover:bg-indigo-900 text-sm flex justify-center w-30 rounded p-2 mt-2">
                    Update Account
                </button>
            </div>


        </form>

    </div>
    <div class=" w-4/12 mx-auto mt-6">
        <form @submit.prevent="handleSubmitPassword" enctype="multipart/form-data">
            <div class="grid grid-cols-2 gap-2">
                <div>
                    <InputField id="newpassword" label="New Password" type="password" v-model="form.newpassword" placeholder="Enter New Password" required />
                </div>
                <div>
                    <InputField id="newpassword2" label="Confirm Password" type="password" v-model="form.newpassword2" placeholder="Re-type New Password" required/>
                </div>
            </div>


            <InputField id="password" label="Current Password" type="password" v-model="form.password" placeholder="Enter Current Password" required />
            <div class="" v-if="form.passworderrors.length">
                <ul v-for="error in form.passworderrors" :key="error">
                    <li class="bg-red-100 text-red-800 mb-2 ring-1 ring-red-200 text-center rounded p-2">{{
        error }}
                    </li>
                </ul>

            </div>
            <div class="flex justify-end">
                <button type="submit"
                    :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-800': !isSubmitting }"
                    :disabled="isSubmitting" class="mb-4 text-white text-sm hover:bg-indigo-900 flex justify-center w-30 rounded p-2 mt-2">
                    Update Password
                </button>
            </div>


        </form>

    </div>



</template>
<script>
import InputField from '@/components/InputField.vue'
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
    name: 'Profile',
    data() {
        return {

            form: {

                first_name: '',
                last_name:'',
                email: '',
                errors: [],
                passworderrors:[],
                newpassword: '',
                newpassword2: '',
                password:'',
            },
            isSubmitting: false,
        }
    },
    components: {
        InputField
    },

    computed: {
        ...mapGetters(['currentUser']),
    },
    watch: {
        currentUser(newUser) {
            if (newUser) {

                this.form.first_name = `${newUser.first_name}`;
                this.form.last_name = `${newUser.last_name}`;
                this.form.email = `${newUser.email}`;

            }
        }
    },
    methods: {
        setInitialData() {
            if (this.currentUser) {
                this.form.first_name = `${this.currentUser.first_name}`;
                this.form.last_name = `${this.currentUser.last_name}`;
                this.form.email = `${this.currentUser.email}`;

            }
        },
        async handleSubmit() {
            this.form.errors = []

            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const formData = new FormData();

                formData.append('first_name', this.form.first_name);
                formData.append('last_name', this.form.last_name);
                formData.append('email', this.form.email);


              
                try {
                    const token = localStorage.getItem('token');

                    // Adjust based on your auth implementation
                    const response = await axios.patch('/api/v1/user/update/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                            "Authorization": `Token ${token}`
                        }
                    });
                    this.$store.dispatch('fetchUser'); // Refresh the current user data
                    alert('Profile updated successfully');
                    // const toPath = '/profile';
                    // this.$router.push(toPath);

                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.form.errors.push(`${error.response.data[property]}`);
                        }
                    } else {
                        console.error('API request error:', error);
                        this.form.errors.push('Something went wrong with API. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                }
            }
        },
        async handleSubmitPassword() {
            this.form.passworderrors = []

            if (!this.form.passworderrors.length) {
                this.isSubmitting = true;
                const formData = new FormData();

                formData.append('current_password', this.form.password);
                formData.append('new_password', this.form.newpassword);
                formData.append('re_new_password', this.form.newpassword2);


               
                try {
                    const token = localStorage.getItem('token');

                    // Adjust based on your auth implementation
                    const response = await axios.post('/api/v1/users/set_password/', formData, {
                        headers: {
                            "Content-Type": "multipart/form-data",
                            "Authorization": `Token ${token}`
                        }
                    });

                    this.form.password = ''
                    this.form.newpassword = ''
                    this.form.newpassword2 =''
                    alert('Password updated successfully');
                  

                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.form.passworderrors.push(`${error.response.data[property]}`);
                        }
                    } else {
                        console.error('API request error:', error);
                        this.form.passworderrors.push('Something went wrong with API. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                    
                }
            }
        }
    },
    mounted() {
        this.setInitialData();
        document.title = 'Profile | Djobs'
    },

}
</script>