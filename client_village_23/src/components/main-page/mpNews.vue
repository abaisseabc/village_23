<template>
  <div class="main-page_news">

    <div class="main-page_news__header">
      <div class="main-page_news__header_title">Новости</div>
      <div class="main-page_news__header_link">
        <router-link to="/news">Все новости</router-link>
      </div>
    </div>

    <div class="main-page_news__news">
      <router-link
          class="main-page_news__news_new"
          v-for="newItem in news"
          :key="newItem.slug"
          :to="{ name: 'NewPage', params: { newSlug: newItem.slug }}"
      >
        <img :src="newItem['get_image']" alt="new photo">
        <h1> {{ newItem["title"] }} </h1>
        <p> {{ newItem["description"].slice(0, 100) }}... </p>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";


export default {
  name: "mpNews",
  mounted() {
    this.getNews();
  },
  data() {
    return {
      news: [],
    }
  },
  methods: {
    async getNews() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/latest_news")
          .then(response => {
            console.log(response)
            this.news = response.data;
          })
          .catch(err => console.log(err))
    },
  },
}
</script>