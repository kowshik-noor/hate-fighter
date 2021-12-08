<template>
  <h1 :class="classProp" class="title is-italic p-2">H8 FIGHTER</h1>
</template>

<script>
export default {
  props: {
    classProp: String,
  },
};
</script>

<style lang="scss" scoped>
h1 {
  color: white;
  background: rgb(234, 51, 35);
  width: fit-content;
  border-radius: 20px;
}
</style>
