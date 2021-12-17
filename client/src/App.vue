<template>
  <component @pass-score="passScore" @changeView="changeView" :is="activeView" :score="score" />
</template>

<script>
import Home from "./views/Home.vue";
import Game from './views/Game.vue'
import GameOver from './views/GameOver.vue'

export default {
  name: "App",
  components: {
    Game,
    Home,
    GameOver
  },
  data() {
    return {
      activeView: 'Game',
      score: 0
    }
  },
  methods: {
    changeView(view) {
      this.activeView = view
    },
    passScore(score) {
      this.score = score
    }
  }
};
</script>
