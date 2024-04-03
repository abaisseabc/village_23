<template>
  <div class="news-page">
    <mpFooter/>

    <div class="news-page__header">Новости</div>

    <div class="news-page__news">
      <router-link
          class="news-page__news_new"
          v-for="newItem in news"
          :key="newItem.slug"
          :to="{ name: 'NewPage', params: { newSlug: newItem.slug }}"
      >
        <img :src="newItem.get_image">
        <h1>{{ newItem.title }}</h1>
        <p>{{ newItem.description.slice(0, 50) }}...</p>
      </router-link>
    </div>
    <mpFooter/>
  </div>
</template>

<script>
import axios from "axios";

import mpFooter from "@/components/main-page/mpFooter.vue";

export default {
  name: "NewsPage",
  components: {
    mpFooter,
  },
  mounted() {
    this.getAllNews();
  },
  data() {
    return {
      news: []
    }
  },
  methods: {
    async getAllNews() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/all_news")
          .then(response => {
            this.news = response.data;
          })
          .catch(err => console.log(err))
    }
  },
}
</script>