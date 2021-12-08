<template>
  <div id="body">
    <section class="section">
      <div class="container is-flex is-flex-direction-column is-align-items-center is-justify-content-center">
        <h3 class="title is-3 has-text-centered">Welcome to</h3>
        <Logo classProp="is-spaced is-1" />
        <h2 class="subtitle is-3">Which YouTube video has more dislikes?</h2>
        <p class="content is-medium">This game was created to remind people that YouTube used to show the number of dislikes.</p>
        <button @click="$emit('change-view', 'Game')" class="button is-success is-large is-rounded">
          Lets Goooo! &nbsp; <i class="fas fa-arrow-alt-circle-right"></i>
        </button>
      </div>
    </section>
  </div>
</template>

<script>
import Logo from "../components/Logo.vue";

export default {
  name: "Home",
  components: {
    Logo,
  },
};
</script>

<style lang="scss" scoped>
#body {
  height: 100vh;
  background-size: cover;
  background-position: center;
  text-shadow: 0 0.05rem 0.1rem rgba(0, 0, 0, 0.5);
  box-shadow: inset 0 0 5rem rgba(0, 0, 0, 0.5);
}

.section {
  height: 100vh;
}

.container {
  height: 100%;
}
</style>
