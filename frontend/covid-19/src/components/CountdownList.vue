<template>
  <CountdownForm />
</template>

<script lang="ts">
import Vue from "vue";
import CountdownForm from "./CountdownForm.vue";
export default Vue.extend({
  name: "CountdownList",
  components: {
    CountdownForm,
  },
});
</script>

<style></style>
