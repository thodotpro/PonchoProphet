<!-- frontend/src/App.vue -->
<!-- Root component — its only job is to render ChatWindow.
     Keeping App.vue this thin is intentional: if you later want
     to add a sidebar, a header, or a router, you add it here
     without touching any chat logic. -->

<template>
  <div class="app">
    <ChatWindow />
  </div>
</template>

<script setup>
import ChatWindow from './components/ChatWindow.vue'
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: system-ui, sans-serif;
  background: #f5f5f5;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.app {
  width: 100%;
  max-width: 680px;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>