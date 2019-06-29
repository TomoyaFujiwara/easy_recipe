<template>
  <nav id="navbar" class="navbar fixed-top navbar-dark bg-dark">
    <div class="d-flex justify-content-around col-xs-12 col-sm-4 col-md-4 col-lg-4">
      <a href="#" class="navbar-brand d-flex align-items-center">
        <i class="fa d-inline fa-camera mr-2"></i>
        <strong>EasyRecipe</strong>
      </a>
    </div>
    <div
      class="container d-flex col-xs-12 col-sm-8 col-md-8 col-lg-8 justify-content-xs-center justify-content-sm-end justify-content-lg-end"
    >
      <div
        class="searchbar d-flex col-xs-12 col-sm-12 col-lg-8 justify-content-sm-end justify-content-center align-items-center"
      >
        <input class="search_input bg-light" type="text" name placeholder="Search...">
        <a href="#" class="search_icon">
          <i class="fas fa-search"></i>
        </a>
      </div>
    </div>
  </nav>
</template>

<style>
.search_input {
  border: 0;
  outline: 0;
  background: none;
  width: 0;
  height: 30px;
  caret-color: transparent;
  line-height: 40px;
  transition: width 0.4s linear;
  padding: 0;
  border-radius: 5px;
}

.searchbar:hover > .search_input {
  border: 0;
  padding: 0 10px;
  width: 80%;
  caret-color: red;
  transition: width 0.4s linear;
}

.searchbar:hover > .search_icon {
  color: #e74c3c;
}

.search_icon {
  height: 40px;
  width: 40px;
  float: right;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}
</style>

<script>
export default {
  name: "Header"
};
</script>
