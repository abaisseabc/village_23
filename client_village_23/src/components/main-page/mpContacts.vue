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

      </div>
      <div class="main-page_contacts__data_map">
        <div style="position:relative;overflow:hidden;"><a
            href="https://yandex.ru/maps/org/village23/72641937051/?utm_medium=mapframe&utm_source=maps"
            style="color:#eee;font-size:12px;position:absolute;top:0px;">Village23</a><a
            href="https://yandex.ru/maps/35/krasnodar/category/hotel/184106414/?utm_medium=mapframe&utm_source=maps"
            style="color:#eee;font-size:12px;position:absolute;top:14px;">Гостиница в Краснодаре</a>
          <iframe
              src="https://yandex.ru/map-widget/v1/?ll=38.938114%2C45.047132&mode=search&oid=72641937051&ol=biz&z=18.15"
              width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "mpContacts",
}
</script>