<template>
  <div class="contact-page">
    <mpFooter/>
    <mpContacts/>
    <mpFooter/>
  </div>
</template>

<script>
import mpFooter from "@/components/main-page/mpFooter.vue";
import mpContacts from "@/components/main-page/mpContacts.vue";

export default {
  name: "ContactPage",
  components: {
    mpFooter,
    mpContacts,
  }
}
</script>