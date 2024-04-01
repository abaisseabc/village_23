<template>
  <div class="main-page_footer">
    <router-link to="/" class="main-page_footer__village" style="font-size: 20px;">Village</router-link>
    <router-link to="/" style="padding-top: 10px">Главная</router-link>
    <router-link to="/" style="padding-top: 10px">Забронировать</router-link>
    <router-link to="/" style="padding-top: 10px">Для жильцов</router-link>
    <router-link to="/news" style="padding-top: 10px">Новости</router-link>
    <router-link to="/" style="padding-top: 10px">Контакты</router-link>
  </div>
</template>

<script>
export default {
  name: "mpFooter",
}
</script>