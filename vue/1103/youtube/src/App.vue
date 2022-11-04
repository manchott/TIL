<template>
  <div class="vuetube-wrap">
    <div class="container">
      <div class="d-flex justify-content-center">
        <h1 class="mt-3 text-primary">SSAFY TUBE</h1>
        <section v-if="isSelectedVideo" class="mt-2">
          <div class="ratio ratio-16x9">
            <iframe :src="videoSrc" frameborder="0"></iframe>

          </div>
          <div class="detail">
            <h4>{{ videoTitle }}</h4>
          </div>

        </section>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyC0Ta2h0MtfU2k4u_wyI_7yq0rByQuNkr8'

export default {
  name: 'App',
  created() {
    axios.get(URL, {
      params: {
        key: API_KEY,
        type: 'video',
        part: 'snippet',
        q: '아이유',
      }
    })
      .then(result => {
        this.videos = result.data.items
        this.selectedVideo = this.videos[0]
      })
      .catch(error => console.log(error))
  },
  components: {},
  props: {},
  data: function() {
    return{
      videos: [],
      selectedVideo: {},
    }
  },
  computed: {
    videoSrc(){
      return `https://youtube.com/embed/${this.selectedVideo.id.videoId}`
    },
    videoTitle() {
      return _.unescape(this.selectedVideo.snippet.title)
    },
    isSelectedVideo(){
      return !!Object.keys(this.selectedVideo).length
    }
  }
}

</script>

<style>

</style>

