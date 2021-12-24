<template>
  <div>
    <div class="body" :class="mode">
      <section class="section">
        <div
          class="container is-flex is-flex-direction-column is-align-items-center is-justify-content-center"
        >
          <h1 class="title is-1 is-spaced" :class="mode === 'dark' ? 'has-text-white' : ''">Game Over</h1>
          <h2 class="subtitle is-3" :class="mode === 'dark' ? 'has-text-light' : ''">Your score is {{ score }}</h2>
          <h2 class="subtitle is-3" :class="mode === 'dark' ? 'has-text-light' : ''">Your high score is {{ highScore }}</h2>
          <button @click="$emit('change-view', 'Game')"
            class="button is-success is-large is-rounded"
            :class="mode === 'dark' ? 'is-light' : ''">
              Play Again &nbsp; <i class="fas fa-redo-alt"></i></button>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    score: Number,
    highScore: Number,
    mode: String
  },
};
</script>


<style lang="scss" scoped>
.body {
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

.dark {
    background-color: rgb(49,52,66);
}
</style>