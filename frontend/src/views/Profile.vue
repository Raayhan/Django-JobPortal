<template>
    <h1 class="text-xl text-gray-500 ml-4 mt-12 border-l-4 border-gray-500 w-3/12"> &nbsp; &nbsp;{{ currentUser ?
        currentUser.first_name + ' ' + currentUser.last_name : 'Loading...' }}'s Profile</h1>

    <div class=" w-full md:w-3/12 mx-auto mt-6">
        <form @submit.prevent="handleSubmit" enctype="multipart/form-data">
            
            <InputField id="email" label="Email" type="email" v-model="form.email" />
            
            
           
            
            <div class="" v-if="form.errors.length">
                <ul v-for="error in form.errors" :key="error">
                    <li class="bg-red-100 text-red-800 mb-2 ring-1 ring-red-200 text-center rounded p-2">{{ error }}
                    </li>
                </ul>

            </div>
            <button type="submit"
                :class="{ 'bg-indigo-500 animate-pulse': isSubmitting, 'bg-indigo-700': !isSubmitting }"
                :disabled="isSubmitting"
                class="mb-4 text-white flex justify-center w-full rounded p-3 mt-8">
               Update
            </button>

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
                
                email: '',
                errors: []
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
                
                this.form.email = `${newUser.email}`;
                
            }
        }
    },
    methods: {
        setInitialData() {
            if (this.currentUser) {
                this.form.email = `${this.currentUser.email}`;
                
            }
        },
        async handleSubmit() {
            this.form.errors = []
           
            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const formData = new FormData();
                
                formData.append('email', this.form.email);
                

                for (let [key, value] of formData.entries()) {
                    console.log(`${key}: ${value}`);
                }
                try {
                    const token = localStorage.getItem('token');  

                     // Adjust based on your auth implementation
                    const response = await axios.patch('/api/v1/users/me/', formData, {
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
        }
    },
    mounted() {
        this.setInitialData();
    },

}
</script>