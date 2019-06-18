<template>
  <div id="app">
    <ul>
      <recipe v-for="item in recipe_list"></recipe>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import Recipe from './components/Recipe.vue';

var URL_BASE = 'http://127.0.0.1:5000';
var url = '/api/v1/users/test_id';

export default {
  name: 'App',
  data() {
    return {
      recipe_list: []
    };
  },
  components: {
    Recipe
  },
  async created() {
    try {
      let res = await axios.get(URL_BASE + url)
      this.search_list = res.data
    } catch (e) {
      console.error(e)
    }
  }
};
</script>
