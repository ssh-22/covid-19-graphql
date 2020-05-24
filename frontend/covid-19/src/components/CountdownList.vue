<template>
  <CountdownForm />
</template>

<script lang="ts">
import Vue from "vue";
import CountdownForm from "./CountdownForm.vue";
import { CountdownInterface } from "../interfaces";
import { defineComponent, reactive, watchEffect } from "@vue/composition-api";
export default defineComponent({
  name: "CountdownList",
  components: {
    CountdownForm,
  },
  setup() {
    const countdowns = reactive<CountdownInterface[]>([]);

    const addCountdown = (countdown: CountdownInterface) => {
      const target = countdown.target;
      const targetDate = countdown.targetDate;
      const newCountdown = { target, targetDate };
    };

    const deleteCountdown = (id: number) => {
      console.log(id);
    };

    const fetchData = async () => {
      console.log("debug");
      //   const res = await axios.get(CountdownGetAPI.develop);
      //   const newCountdowns: CountdownInterface[] = res.data;
    };

    watchEffect(() => {
      fetchData();
    });

    return {
      countdowns,
    };
  },
});
// export default Vue.extend({
//   name: "CountdownList",
//   components: {
//     CountdownForm,
//   },
//   methods: {
//     addCountdown(countdown: CountdownInterface) {
//       const target = countdown.target;
//       const targetDate = countdown.targetDate;
//       const newCountdown = { target, targetDate };
//     },
//     deleteCountdown(id: number) {
//       console.log(id);
//     },
//   },
// });
</script>

<style></style>
