<template>
  <div class="about">
    <h1 class="text-3xl bg-indigo-200">This is application page</h1>
    <p v-if="currentUser">Hello, {{ currentUser.username }}!</p>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'applications',
  mounted() {
    
    document.title = 'Applications | DIJobs';
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  created() {
    if (!this.currentUser) {
      this.$store.dispatch('fetchUser');
    }
  }

}
</script>