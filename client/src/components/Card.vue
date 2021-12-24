<template>
  <div class="card" :class="mode">
    <div class="card-image">
      <!-- <figure class="image is-4by3">
        <img
          src="https://bulma.io/images/placeholders/1280x960.png"
          alt="Placeholder image"
        />
      </figure> -->
      <div id="dislike-counter" 
      class="is-overlay is-flex is-justify-content-center 
      is-align-items-center"
      v-if="showDislikes">
        <h1 class="title is-1">
          <vue3-autocounter 
          :startAmount="0"
          :endAmount="dislikes"
          :duration="1"/>
        </h1>
      </div>
      <iframe
        width="652"
        height="506"
        :src="'https://www.youtube-nocookie.com/embed/' + id + '?controls=1'"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-4" :class="mode === 'dark' ? 'has-text-white' : ''">{{title}}</p>
          <p class="subtitle is-6" :class="mode === 'dark' ? 'has-text-white-ter' : ''">{{channelName}}</p>
        </div>

        <div>
          <button
          @click="$emit('compare-dislikes')" 
          class="button is-large is-rounded is-success is-outlined">
            <i class="fas fa-crosshairs"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    template: Object,
    showDislikes: Boolean,
    mode: String
  },
  data() {
    return {
      id: "",
      title: "",
      channelName: "",
      dislikes: 0
    }
  },
  methods: {
    async fetchVideo() {
      const res = await fetch('http://127.0.0.1:5000/api')
      const data = await res.json()
      return JSON.parse(data)
    },
    onClick() {

    }
  },
  async created() {
    const video = await this.fetchVideo()

    this.id = video["video_id"]
    this.title = video["title"]
    this.channelName = video["channel_name"]
    this.dislikes = video["dislikes"]

    this.$emit('template', {
      label: this.template.label,
      id: this.id,
      dislikes: this.dislikes,
      reloads: this.template.reloads
    })
  }
};
</script>

<style lang="scss" scoped>
#dislike-counter {
  background-color: rgba(224, 219, 219, 0.753);
}

.dark {
  background-color: rgb(49,52,66);
  box-shadow: 0 0.5em 1em -0.125em rgba(white, 0.1), 0 0px 0 1px rgba(white, 0.02);
}

</style>
