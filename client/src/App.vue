<template>
  <component @pass-scores="passScores" @changeView="changeView" :is="activeView" :score="score" :highScore="highScore" />
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
      score: 0,
      highScore: 0
    }
  },
  methods: {
    changeView(view) {
      this.activeView = view
    },
    passScores(scores) {
      this.score = scores.score
      this.highScore = scores.highScore
    }
  }
};
</script>
