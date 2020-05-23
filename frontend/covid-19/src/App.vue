<template>
  <v-app>
    <v-content>
      <CountdownForm />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import CountdownForm from "./components/CountdownForm.vue";
export default Vue.extend({
  name: "App",
  components: {
    CountdownForm
  },

  data: () => ({
    //
  })
});
</script>
