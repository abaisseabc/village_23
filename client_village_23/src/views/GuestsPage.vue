<template>
  <div class="guests-page">
    <gpNavBar/>

    <div class="guests-page__header">Для жильцов</div>

    <div class="guests-page__service">

      <div class="guests-page__service_first_lvl">
        <div>
          <label>Введите ваш ID</label> <br>
          <input v-model="service['guest_id_service']" style="width: 1030px;">
        </div>
      </div>

      <div class="guests-page__service_second_lvl">
        <div>
          <label>Выберите услугу</label> <br>
          <select class="guests-page__service_second_lvl__input" v-model="service['service_name']">
            <option
                class="guests-page__service_second_lvl__input"
                value="Заменить полотенца"
            >Заменить полотенца
            </option>
            <option
                class="guests-page__service_second_lvl__input"
                value="Убраться"
            >Убраться
            </option>
            <option
                class="guests-page__service_second_lvl__input"
                value="Принести воды"
            >Принести воды
            </option>
            <option
                class="guests-page__service_second_lvl__input"
                value="Починить оборудование"
            >Принести воды
            </option>
            <option
                class="guests-page__service_second_lvl__input"
                value="Починить оборудование"
            >Заказать такси
            </option>
          </select>
        </div>
        <div>
          <button @click="orderRoomService">Заказать</button>
        </div>
      </div>
    </div>
    <gpNavBar/>
  </div>
</template>

<script>
import axios from "axios";

import gpNavBar from "@/components/guests-page/gpNavBar.vue";

export default {
  name: "GuestsPage",
  components: {
    gpNavBar,
  },
  data() {
    return {
      service: {
        "guest_id_service": "",
        "service_name": "",
      }
    }
  },
  methods: {
    async orderRoomService() {
      await axios
          .post("http://127.0.0.1:8000/api/v1/services/", this.service)
          .then(response => {
            if (response.status === 201) {
              console.log(response);
            }
          })
          .catch(err => console.log(err))
    },
  }
}
</script>