<template>
  <div>
    <CountdownForm />
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <div v-if="countdowns">
      <v-list-item v-for="countdown of countdowns" :key="countdown.id">
        <v-list-item-content>
          {{ countdown.target }} まで あと {{ countdown.targetDate }}
        </v-list-item-content>
      </v-list-item>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { defineComponent, reactive, watchEffect } from "@vue/composition-api";
import gql from "graphql-tag";
import { useQuery, useResult } from "@vue/apollo-composable";

import CountdownForm from "./CountdownForm.vue";
import { CountdownInterface } from "../interfaces";

export default defineComponent({
  name: "CountdownList",
  components: {
    CountdownForm,
  },
  setup() {
    const { result, loading, error } = useQuery(gql`
      query {
        allCountdowns {
          id
          target
          targetDate
        }
      }
    `);

    const countdowns = useResult(result);

    return {
      countdowns,
      loading,
      error,
    };
  },
});
</script>

<style></style>
