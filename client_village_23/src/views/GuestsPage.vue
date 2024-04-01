<template>
  <div class="guests-page">
    <gpNavBar/>

    <div class="guests-page__header">Для жильцов</div>

    <div class="guests-page__service">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Введите номер комнаты</label> <br>
          <input>
        </div>
        <div>
          <label>Введите ваш ID</label> <br>
          <input>
        </div>
      </div>

      <div class="guests-page__service_second_lvl">
        <div>
          <label>Выберите усулгу</label> <br>
          <input class="guests-page__service_second_lvl__input">
        </div>
        <div>
          <button>Заказать</button>
        </div>
      </div>
    </div>
    <gpNavBar/>
  </div>
</template>

<script>
import gpNavBar from "@/components/guests-page/gpNavBar.vue";

export default {
  name: "GuestsPage",
  components: {
    gpNavBar,
  },
}
</script>

<style scoped lang="scss">

</style>