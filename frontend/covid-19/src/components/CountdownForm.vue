<template>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12" sm="6" md="4">
          <v-text-field v-model="target" label="何を"></v-text-field>
        </v-col>
        <v-col cols="12" sm="6" md="4">
          <v-menu
            v-model="isOpen"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="computedDateFormatted"
                label="いつまでに"
                prepend-icon="event"
                readonly
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="targetDate"
              @input="isOpen = false"
              color="light-blue accent-2"
              locale="ja"
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "CountdownForm",
  data: () => ({
    target: "緊急事態宣言解除",
    targetDate: new Date().toISOString().substr(0, 10),
    isOpen: false
  }),
  computed: {
    computedDateFormatted(): string | null {
      return this.formatDate(this.targetDate);
    }
  },
  methods: {
    formatDate(date: string): string | null {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${year}/${month}/${day}`;
    }
  }
});
</script>

<style></style>
