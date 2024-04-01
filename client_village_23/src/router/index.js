import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: () => import("../views/MainPage.vue"),
  },
  {
    path: "/news",
    name: "NewsPage",
    component: () => import("../views/NewsPage.vue"),
  },
  {
    path: "/new/:newSlug",
    name: "NewPage",
    component: () => import("../views/NewPage.vue"),
    props: true,
  },
  {
    path: "/contact",
    name: "ContactPage",
    component: () => import("../views/ContactPage.vue"),
  },
  {
    path: "/guests",
    name: "GuestsPage",
    component: () => import("../views/GuestsPage.vue"),
  },
  {
    path: "/booking",
    name: "BookingPage",
    component: () => import("../views/BookingPage.vue"),
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
