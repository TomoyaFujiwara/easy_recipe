<template>
  <div class="card bg-transparent">
    <img class="card-img-top" src="https://pingendo.com/assets/photos/wireframe/photo-1.jpg">
    <img class="card-img-top" :src="recipe.image_url">
    <div class="card-body">
      <strong>{{recipe.name}}</strong>
      <!-- <p>{{recipe.describe}}</p> -->
      <!-- <div class="d-flex justify-content-between align-items-center">
        <div class="btn-group">
          <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
          <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
        </div>
        <small class="text-muted">9 mins</small>
      </div>-->
    </div>
  </div>
  <!-- <div>
    <p>{{recipe.name}}</p>
    <p>{{recipe.site_url}}</p>
    <p>{{recipe.image_url}}</p>
    <ul>
      <li v-for="ingredient in recipe.ingredients">{{ingredient.name}}</li>
    </ul>
    <ul>
      <li v-for="procedure in recipe.procedures">{{procedure.name}}</li>
    </ul>
  </div>-->
</template>

<style>
.card-img-top {
  width: 100%;
  height: auto;
  object-fit: cover;
}
</style>

<script>
export default {
  name: "RecipeOverview",
  props: ["recipe"],
};
</script>
