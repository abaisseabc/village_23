<template>
  <div class="main-page">
    <mpBanner/>
    <mpDescription/>
    <mpRooms/>
    <mpNews/>
    <mpContacts/>
    <mpFooter/>
  </div>
</template>

<script>
import mpBanner from "@/components/main-page/mpBanner.vue";
import mpDescription from "@/components/main-page/mpDescription.vue";
import mpRooms from "@/components/main-page/mpRooms.vue";
import mpNews from "@/components/main-page/mpNews.vue";
import mpContacts from "@/components/main-page/mpContacts.vue";
import mpFooter from "@/components/main-page/mpFooter.vue";

export default {
  name: "MainPage",
  components: {
    mpBanner,
    mpDescription,
    mpRooms,
    mpNews,
    mpContacts,
    mpFooter,
  },
}
</script>