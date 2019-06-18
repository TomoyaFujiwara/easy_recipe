<template>
  <div id="app">
    <div id="recipe_list" v-for="item in recipe_list">
      <recipe :item="item"></recipe>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Recipe from './components/Recipe.vue';

let URL_BASE = 'http://127.0.0.1:5000';
let url = '/api/v1/users/test_id';

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
      console.log(res.data)
      this.recipe_list = res.data
    } catch (e) {
      console.error(e)
    }
  }
};
</script>
