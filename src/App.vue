<template>
  <div class="app-shell">
    <BHeader />

    <main class="container py-5">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import BHeader from './components/BHeader.vue'
</script>

<style>
body {
  background-color: #f6f8fb;
}

.app-shell {
  min-height: 100vh;
}
</style>
