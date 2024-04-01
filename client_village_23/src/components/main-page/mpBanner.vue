<template>
  <div class="main-page_banner">
    <mpNavBar/>

    <div class="main-page_banner__header">
      Rest Hotel Village in the <br> Heart of the City
    </div>

    <div class="main-page_banner__booking">
      <div>
        <input type="date">
      </div>
      <div>
        <input type="date">
      </div>
      <div class="main-page_banner__booking_link">
        <router-link to="/booking">Забронировать</router-link>
      </div>
    </div>

  </div>
</template>

<script>
import mpNavBar from "./mpNavBar.vue";

export default {
  name: "mpBanner",
  components: {
    mpNavBar,
  },
}
</script>

<style lang="scss">
.main-page_banner {
  background: url("../../assets/imgs/banner_bg.png") center center/cover no-repeat;
}
</style>