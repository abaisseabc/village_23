<template>
  <div class="main-page_rooms">

    <div class="main-page_rooms__room">

      <div class="main-page_rooms__room__right">

        <div class="main-page_rooms__room__type_rus">
          {{ rooms[0]["room_type"]["type_rus"] }}
        </div>

        <div class="main-page_rooms__room__type">
          {{ rooms[0]["room_type"]["type"] }}
        </div>

        <div class="main-page_rooms__room__description">
          {{ rooms[0]["room_type"]["description"] }}
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Вид из окна:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[0]["view_window"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Размер:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[0]["size"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Тип кровати:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[0]["size"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Цена:</div>
          <div class="main-page_rooms__room__parameters_parameter">от {{ rooms[0]["price"] }} ₽</div>
        </div>

        <div class="main-page_rooms__room__booking">
          <router-link to="/">Забронировать</router-link>
        </div>
      </div>

      <div class="main-page_rooms__room__image">
        <img :src="rooms[0]['get_image']" alt="room image">
      </div>
    </div>

    <div class="main-page_rooms__room">

      <div class="main-page_rooms__room__image">
        <img :src="rooms[1]['get_image']" alt="room image">
      </div>

      <div class="main-page_rooms__room__left">

        <div class="main-page_rooms__room__type_rus">
          {{ rooms[1]["room_type"]["type_rus"] }}
        </div>

        <div class="main-page_rooms__room__type">
          {{ rooms[1]["room_type"]["type"] }}
        </div>

        <div class="main-page_rooms__room__description">
          {{ rooms[1]["room_type"]["description"] }}
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Вид из окна:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[1]["view_window"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Размер:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[1]["size"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Тип кровати:</div>
          <div class="main-page_rooms__room__parameters_parameter">{{ rooms[1]["type_bed"] }}</div>
        </div>

        <div class="main-page_rooms__room__parameters">
          <div class="main-page_rooms__room__parameters_label">Цена:</div>
          <div class="main-page_rooms__room__parameters_parameter">от {{ rooms[1]["price"] }} ₽</div>
        </div>

        <div class="main-page_rooms__room__booking">
          <router-link to="/">Забронировать</router-link>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "mpRooms",
  mounted() {
    this.getRooms();
  },
  data() {
    return {
      rooms: [],
    }
  },
  methods: {
    async getRooms() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/rooms/")
          .then(response => {
            if (response.status === 200) {
              this.rooms = response.data;
            }
          })
          .catch(err => console.log(err))
    },
  },
}
</script>