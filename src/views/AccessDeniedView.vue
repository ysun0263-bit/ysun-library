<template>
  <div class="row">
    <div class="col-12 col-md-8 col-lg-6 offset-md-2 offset-lg-3">
      <div class="alert alert-danger shadow-sm">
        <h1 class="h3">Access Denied</h1>
        <p>You must be logged in to access this page.</p>
        <router-link class="btn btn-danger" to="/login">
          Go to Login
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
