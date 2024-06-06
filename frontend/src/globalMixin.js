export default {
  computed: {
    currentUser() {
      return this.$store.getters.currentUser;
    }
  },
  created() {
    if (!this.currentUser) {
      this.$store.dispatch('fetchUser');
    }
  }
};