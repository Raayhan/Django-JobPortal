<template>
  <div class="about">
    <h1 class="text-3xl text-gray-500 ">My Applications</h1>
    <p v-if="currentUser">Hello, {{ currentUser.first_name }} {{ currentUser.last_name}}!</p>
    <div class="text-xl text-gray-600 flex justify-center">You're in Dashboard now</div>
  </div>
</template>
<script>

export default {
  name: 'applications',
  mounted() {
    
    document.title = 'Applications | DIJobs';
  },
  

}
</script>