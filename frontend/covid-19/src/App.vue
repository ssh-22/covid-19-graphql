<template>
  <v-app>
    <v-content>
      <CountdownList />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import CountdownList from "./components/CountdownList.vue";
export default Vue.extend({
  name: "App",
  components: {
    CountdownList
  },

  data: () => ({
    //
  })
});
</script>
