<template>
  <div class="guests-page_navbar">
    <router-link to="/" class="main-page_footer__village" style="font-size: 20px;">Village</router-link>
    <router-link to="/" style="padding-top: 10px">Главная</router-link>
    <router-link to="/booking" style="padding-top: 10px">Забронировать</router-link>
    <router-link to="/guests" style="padding-top: 10px">Для жильцов</router-link>
    <router-link to="/news" style="padding-top: 10px">Новости</router-link>
    <router-link to="/contact" style="padding-top: 10px">Контакты</router-link>
  </div>
</template>

<script>
export default {
  name: "gpNavBar"
}
</script>

<style scoped lang="scss">

</style>