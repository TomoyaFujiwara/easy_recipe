<template>
  <md-button class="md-fab right-bottom create-button">
    <md-icon>add</md-icon>
  </md-button>
</template>

<style>
.create-button {
  background-color: #0336FF !important;
  color: white !important;
}

.right-bottom {
  position: fixed !important;
  bottom: 0 !important;
  right: 0 !important;
}
</style>

<script>
export default {
  name: "CreateButton",
  components: {}
};
</script>
