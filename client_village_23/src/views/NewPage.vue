<template>
  <div class="new-page">
    <mpFooter/>

    <div class="new-page__new">
      <div class="new-page__new_data">
        <div class="new-page__new_data__header"> {{newObject.title}} </div>
        <div class="new-page__new_data__description">{{newObject.description}}</div>
      </div>

      <div class="new-page__new_img">
        <img :src="newObject.get_image">
      </div>
    </div>
    <mpFooter/>
  </div>
</template>

<script>
import axios from "axios";

import mpFooter from "@/components/main-page/mpFooter.vue";

export default {
  name: "NewPage",
  props: ["newSlug"],
  components: {
    mpFooter,
  },
  mounted() {
    this.getNew();
  },
  data() {
    return {
      newObject: null,
    }
  },
  methods: {
    async getNew() {
      await axios
          .get(`http://127.0.0.1:8000/api/v1/news/${this.newSlug}`)
          .then(response => {
            this.newObject = response.data;
          })
          .catch(err => console.log(err))
    }
  },
}
</script>

<style scoped lang="scss">

</style>