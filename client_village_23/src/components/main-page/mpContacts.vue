<template>
  <div class="main-page_contacts">

    <div class="main-page_contacts__header">Контакты</div>

    <div class="main-page_contacts__data">
      <div class="main-page_contacts__data_info">

        <div class="main-page_contacts__data_info_block">
          <div class="main-page_contacts__data_info_block_label">Город:</div>
          <div class="main-page_contacts__data_info_block_desc">Краснодар</div>
        </div>

        <div class="main-page_contacts__data_info_block">
          <div class="main-page_contacts__data_info_block_label">Адрес:</div>
          <div class="main-page_contacts__data_info_block_desc">ул. им. Каляева, 86</div>
        </div>

        <div class="main-page_contacts__data_info_block">
          <div class="main-page_contacts__data_info_block_label">Телефон:</div>
          <div class="main-page_contacts__data_info_block_desc">+7 (928) 4-211-211</div>
        </div>

        <div class="main-page_contacts__data_info_block">
          <div class="main-page_contacts__data_info_block_label">E-mail:</div>
          <div class="main-page_contacts__data_info_block_desc">village23kras@yandex.ru</div>
        </div>

        <div class="main-page_contacts__data_info_block">
          <div class="main-page_contacts__data_info_block_label">График работы:</div>
          <div class="main-page_contacts__data_info_block_desc">00:00 - 00:00</div>
        </div>

        <div class="main-page_contacts__data_info_block__ex">
          <div class="main-page_contacts__data_info_block__ex__label">
            Остались вопросы? Оставьте заявку <br> и мы скоро свяжемся с вами
          </div>
          <div class="main-page_contacts__data_info_block__ex__input">
            <input
                placeholder="Номер телефона"
                v-model="formattedPhoneNumber"
            >
            <img
                src="@/assets/icons/arrow.svg"
                alt="send request"
                @click="requestCall"
            >
          </div>
        </div>

      </div>
      <div class="main-page_contacts__data_map">
        <div style="position:relative;overflow:hidden;"><a
            href="https://yandex.ru/maps/org/village23/72641937051/?utm_medium=mapframe&utm_source=maps"
            style="color:#eee;font-size:12px;position:absolute;top:0px;">Village23</a><a
            href="https://yandex.ru/maps/35/krasnodar/category/hotel/184106414/?utm_medium=mapframe&utm_source=maps"
            style="color:#eee;font-size:12px;position:absolute;top:14px;">Гостиница в Краснодаре</a>
          <iframe
              src="https://yandex.ru/map-widget/v1/?ll=38.938114%2C45.047132&mode=search&oid=72641937051&ol=biz&z=18.15"
              width="900" height="500" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "mpContacts",
  data() {
    return {
      dataRequestCall: {
        "phone_number": "",
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
    async requestCall() {
      if (this.isValidPhoneNumber) {
        this.dataRequestCall["phone_number"] = this.phoneNumber;
        await axios
            .post("http://127.0.0.1:8000/api/v1/call_requests/", this.dataRequestCall)
            .then(response => {
              if (response.data.status === 201) {
                console.log(response.data);
              }
            })
            .catch(err => console.log(err))
      }
    },
  },
}
</script>