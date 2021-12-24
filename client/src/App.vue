<template>
  <component
    @pass-scores="passScores"
    @changeView="changeView"
    :is="activeView"
    :score="score"
    :highScore="highScore"
    :mode="mode"
  />
</template>

<script>
import Home from "./views/Home.vue";
import Game from "./views/Game.vue";
import GameOver from "./views/GameOver.vue";

export default {
  name: "App",
  components: {
    Game,
    Home,
    GameOver,
  },
  data() {
    return {
      activeView: "GameOver",
      score: 0,
      highScore: 0,
      mode: "light"
    };
  },
  methods: {
    changeView(view) {
      this.activeView = view;
    },
    passScores(scores) {
      this.score = scores.score;
      this.highScore = scores.highScore;
    },
    changeAppearance(system) {
      if (system.matches) {
        this.mode = "dark"
      } else {
        this.mode = "light"
      }
    }
  },
  created() {
    const sysAppearance = window.matchMedia("(prefers-color-scheme: dark)")
    this.changeAppearance(sysAppearance)

    sysAppearance.addEventListener('change', this.changeAppearance)
  }
};
</script>
