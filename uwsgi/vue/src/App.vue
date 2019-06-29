<template>
  <div>
    <app-header></app-header>
    <detail v-show="modalVisible" @close="closeModal" :recipe="modalRecipe"/>
    <div id="recipe_list_body" class="container py-5 mt-5 bg-white">
      <div class="row">
        <div
          class="d-frex col-md-4 col-lg-3 p-3"
          v-for="recipe in recipe_list"
          @click="openModal(recipe)"
        >
          <overview v-bind:recipe="recipe"></overview>
        </div>
      </div>
    </div>
    <create-btn/>
  </div>
</template>

<script>
import axios from "axios";
import Header from "./components/Header.vue";
import RecipeOverview from "./components/RecipeOverview.vue";
import RecipeDetail from "./components/RecipeDetail.vue";
import CreateButton from "./components/CreateButton.vue";

export default {
  name: "App",
  data: function() {
    return {
      recipe_list: [],
      modalVisible: false,
      modalRecipe: null
    };
  },
  created: async function() {
    axios
      .get("http://localhost:5000/api/v1/users/test_id")
      .then(response => {
        this.recipe_list = JSON.parse(response.data).results;
      })
      .catch(error => {
        console.log(error.response);
      });
  },
  methods: {
    openModal(recipe) {
      this.modalRecipe = recipe;
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;
    }
  },
  components: {
    "overview": RecipeOverview,
    "detail": RecipeDetail,
    "app-header": Header,
    "create-btn": CreateButton
  }
};
</script>
