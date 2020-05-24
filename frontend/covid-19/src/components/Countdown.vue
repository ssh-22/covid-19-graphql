<template></template>

<script lang="ts">
import { defineComponent, onMounted, onUnmounted } from "@vue/composition-api";
import moment from "moment";
import { CounterInterface, CountdownInterface } from "../interfaces";
export default defineComponent({
  name: "Countdown",
  setup({ target, targetDate }: CountdownInterface) {
    const counter: CounterInterface = {
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
    };

    onMounted(() => {
      const timerId = setInterval(() => {
        const diff = moment(targetDate).diff(moment());
        const duration = moment.duration(diff);
        const days = Math.floor(duration.asDays());
        const hours = duration.hours();
        const minutes = duration.minutes();
        const seconds = duration.seconds();
        // setCounter({
        //   days,
        //   hours,
        //   minutes,
        //   seconds
        // });
      }, 1000);
    });

    onUnmounted(() => {
      //   clearInterval(timerId);
    });

    return {
      target,
      counter,
    };
  },
});
</script>

<style></style>
