<template>
  <div>
    <p>{{item.name}}</p>
    <p>{{item.site_url}}</p>
    <p>{{item.image_url}}</p>
    <ul>
      <li v-for="ingredient in item.ingredients">{{ingredient.name}}</li>
    </ul>
    <ul>
      <li v-for="procedure in item.procedures">{{procedure.name}}</li>
    </ul>
  </div>
</template>


<script>

export default {
  name: 'Recipe',
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
    };
  },
  components: {
  },
};
</script>
