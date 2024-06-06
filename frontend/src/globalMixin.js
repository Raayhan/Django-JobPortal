export default {
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
    },
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    }
  },
  created() {
   
     if (this.isAuthenticated) {
      if (!this.currentUser) {
        this.$store.dispatch('fetchUser');
      }
    }
    
   
  }
};