import Vue from "vue";
import VueCompositionApi from "@vue/composition-api";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import "material-design-icons-iconfont/dist/material-design-icons.css";
import { createProvider } from "./vue-apollo";

Vue.config.productionTip = false;

Vue.use(VueCompositionApi);

new Vue({
  vuetify,
  apolloProvider: createProvider(),
  render: h => h(App)
}).$mount("#app");
