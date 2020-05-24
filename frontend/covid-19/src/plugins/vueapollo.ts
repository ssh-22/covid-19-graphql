import Vue from "vue";
import ApolloClient from "apollo-client";
import Cookies from "js-cookie";
import { InMemoryCache } from "apollo-cache-inmemory";
import { HttpLink } from "apollo-link-http";
import VueApollo from "vue-apollo";

const cache = new InMemoryCache();
const link = new HttpLink({
  uri: "http://localhost:8000/graphql/",
  credentials: "include",
  headers: {
    "X-CSRFToken": Cookies.get("csrftoken"),
  },
});

const apolloClient = new ApolloClient({ cache, link });

Vue.use(VueApollo);

export default apolloClient;
