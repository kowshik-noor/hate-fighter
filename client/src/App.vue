<template>
  <component @changeView="changeView" :is="activeView" />
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
      activeView: 'Game'
    }
  },
  methods: {
    changeView(view) {
      this.activeView = view
    }
  }
};
</script>
