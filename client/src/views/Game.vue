<template>
  <div>
    <nav
      class="navbar is-flex is-flex-direction-row is-justify-content-space-between is-align-items-center"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">
        <a class="navbar-item" @click="$emit('change-view', 'Home')">
          <Logo width="112" height="28" />
        </a>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <h2 class="title is-3 mb-0">Which YouTube video has more dislikes?</h2>
      <div></div>
      <div class="p-2">Score: {{score}}</div>
    </nav>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column"><Card 
          :key="videoA.reloads" 
          :template="videoA" 
          @template="setObjects" 
          @compare-dislikes="compareDislikes(videoA, videoB)" /></div>
          <div class="column"><Card 
          :key="videoB.reloads" 
          :template="videoB" 
          @template="setObjects" 
          @compare-dislikes="compareDislikes(videoB, videoA)"/></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Logo from "../components/Logo.vue";
import Card from "../components/Card.vue";

export default {
  components: {
    Logo,
    Card,
  },
  data() {
    return {
      videoA: {
        label: "A",
        id: "",
        dislikes: 0,
        reloads: 0
      },
      videoB: {
        label: "B",
        id: "",
        dislikes: 0,
        reloads: 0
      },
      // this will keep track of the video ids used in each session
      videos: [],
      score: 0,
      // i might not need this property depending on the how the function that will compare the dislikes will be implemented
      selectedCard: null
    };
  },
  methods: {
    setObjects(thing) {
      if (thing.label === "A") {
        this.videoA = thing
      } else {
        this.videoB = thing
      }
    },
    keepTabs(val) {
      if(this.videos.includes(val.id)) {
        val = {...val, reloads: val.reloads + 1}
        return
      } else {
        this.videos = [...this.videos, val.id]
        return
      }
    },
    compareDislikes(selectedVid, unselectedVid) {
      if (selectedVid.dislikes > unselectedVid.dislikes) {
        this.score++
        this.rerenderBoth()
        return selectedVid
      } else {
        this.$emit('pass-score', this.score)
        this.$emit('change-view', 'GameOver')
      }
    },
    rerender(card) {
      if(card.label === 'A') {
        this.videoA = {...this.videoA, reloads: this.videoA.reloads + 1}
      } else  {
        this.videoB = {...this.videoB, reloads: this.videoB.reloads + 1}
      }
    },
    rerenderBoth() {
      this.rerender({label: 'A'})
      this.rerender({label: 'B'})
    }
  },
  created() {
  },
  watch: {
    videoA(val) {
      this.keepTabs(val)
    },
    videoB(val) {
      this.keepTabs(val)
    }
  },
  emits: ["change-view", "pass-score"],
};
</script>

<style lang="scss" scoped></style>
