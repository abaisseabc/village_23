<template>
  <div class="booking-page guests-page">
    <gpNavBar/>
    <div class="guests-page__header">Бронирование</div>

    <div class="guests-page__service">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Заезд</label> <br>
          <input type="date" v-model="bookingData['check_in_date']">
        </div>
        <div>
          <label>Выезд</label> <br>
          <input type="date" v-model="bookingData['check_out_date']">
        </div>
      </div>

      <hr style="width: 1030px;">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Имя</label> <br>
          <input placeholder="Введите ваше имя" v-model="bookingData['first_name']">
        </div>
        <div>
          <label>Телефон</label> <br>
          <input placeholder="Введите ваш телефон" v-model="formattedPhoneNumber">
        </div>
      </div>

      <div class="booking-page__btn">
        <button @click="bookRoom">Отправить</button>
      </div>
    </div>
    <gpNavBar/>
  </div>
</template>

<script>
import axios from "axios";

import gpNavBar from "@/components/guests-page/gpNavBar.vue";

export default {
  name: "BookingPage",
  components: {
    gpNavBar,
  },
  data() {
    return {
      bookingData: {
        "check_in_date": Date(),
        "check_out_date": Date(),
        "first_name": "",
        "phone": "",
      },
      phoneNumber: "",
      isValidPhoneNumber: true,
    }
  },
  computed: {
    formattedPhoneNumber: {
      get() {
        return this.phoneNumber;
      },
      set(value) {
        const formattedValue = value.replace(/\D/g, '');

        const formattedNumber = formattedValue.replace(/^(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})$/, '8-$2-$3-$4-$5');

        const regex = /^8-\d{3}-\d{3}-\d{2}-\d{2}$/;
        this.isValidPhoneNumber = regex.test(formattedNumber);

        this.phoneNumber = formattedNumber;
      }
    },
  },
  methods: {
    async bookRoom() {
      this.bookingData["phone"] = this.phoneNumber;
      await axios
          .post("http://127.0.0.1:8000/api/v1/bookings/", this.bookingData)
          .then(response => {
            if (response.status === 201) {
              console.log(response);
            }
          })
          .catch(err => console.log(err))
    },
  },
}
</script>