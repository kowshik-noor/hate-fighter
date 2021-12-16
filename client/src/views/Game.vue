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
      <div></div>
    </nav>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column"><Card :key="videoA.reloads" :template="videoA" @template="printObject"/></div>
          <div class="column"><Card :key="videoB.reloads" :template="videoB" @template="printObject"/></div>
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
      score: 0
    };
  },
  methods: {
    printObject(thing) {
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
    },
    videos(val) {
      console.log(val)
    }
  },
  emits: ["change-view"],
};
</script>

<style lang="scss" scoped></style>
