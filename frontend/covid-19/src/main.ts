import Vue from "vue";
import VueCompositionApi from "@vue/composition-api";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import apolloClient from "./plugins/vueapollo";
import { provide } from "@vue/composition-api";
import { DefaultApolloClient } from "@vue/apollo-composable";
import "material-design-icons-iconfont/dist/material-design-icons.css";

Vue.config.productionTip = false;

Vue.use(VueCompositionApi);

new Vue({
  vuetify,
  setup() {
    provide(DefaultApolloClient, apolloClient);
  },
  render: (h) => h(App),
}).$mount("#app");
