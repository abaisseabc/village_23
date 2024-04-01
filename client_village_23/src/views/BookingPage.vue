<template>
  <div class="booking-page guests-page">
    <gpNavBar/>
    <div class="guests-page__header">Бронирование</div>

    <div class="guests-page__service">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Заезд</label> <br>
          <input type="date">
        </div>
        <div>
          <label>Выезд</label> <br>
          <input type="date">
        </div>
      </div>

      <hr style="width: 1030px;">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Имя</label> <br>
          <input>
        </div>
        <div>
          <label>Телефон</label> <br>
          <input>
        </div>
      </div>

      <div class="booking-page__btn">
        <button>Отправить</button>
      </div>
    </div>
    <gpNavBar/>
  </div>
</template>

<script>
import gpNavBar from "@/components/guests-page/gpNavBar.vue";

export default {
  name: "BookingPage",
  components: {
    gpNavBar,
  },
}
</script>