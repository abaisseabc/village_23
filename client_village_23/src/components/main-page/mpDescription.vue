<template>
  <div class="main-page_description">

    <div class="main-page_description__header">
      Гостиница village - это не просто
      <br>
      сеть гостиниц, это стиль жизни
    </div>

    <div class="main-page_description__content">

      <div class="main-page_description__content_main">
        <div class="main-page_description__content_main_desc">
          Мы стремимся предоставить не <br> только комнаты для отдыха, но <br>
          и пространство, где комфорт <br> сочетается с высоким уровнем <br> обслуживания.
        </div>

        <div class="main-page_description__content_main_link">
          <router-link to="/booking">Забронировать</router-link>
        </div>

        <div class="main-page_description__content_main_imgs">
          <img src="@/assets/icons/right_icon.svg" alt="right_icon" style="margin-right: 20px;">
          <img src="@/assets/icons/left_icon.svg" alt="left_icon">
        </div>
      </div>

      <div class="main-page_description__content_imgs">
        <img src="@/assets/imgs/description_img_1.png" style="padding-right: 30px;">
        <img src="@/assets/imgs/description_img_2.png">
      </div>
    </div>

    <div class="main-page_description_img"></div>
  </div>
</template>

<script>
export default {
  name: "mpDescription",
}
</script>

<style lang="scss">
.main-page_description_img {
  background: url("@/assets/imgs/description_img_3.png") center center/cover no-repeat;
  min-height: 800px;
}
</style>