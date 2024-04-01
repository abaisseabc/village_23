<template>
  <div class="main-page_banner__navbar">
    <router-link class="main-page_banner__navbar_village" to="/">Village</router-link>
    <router-link to="/">Главная</router-link>
    <router-link to="/">Забронировать</router-link>
    <router-link to="/">Для жильцов</router-link>
    <router-link to="/news">Новости</router-link>
    <router-link to="/contact">Контакты</router-link>
  </div>
</template>

<script>
export default {
  name: "mpNavBar",
}
</script>