<!-- Small subtle "back to home" link, top-left of DemoView. -->
<template>
  <router-link to="/" class="back-home">&larr; Back to home</router-link>
</template>

<script setup>
</script>

<style scoped>
.back-home {
  display: inline-block;
  font-family: 'Nunito', sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--mid);
  text-decoration: none;
  padding: 6px 10px;
  border-radius: 8px;
  transition: color 0.2s ease, background 0.2s ease;
}
.back-home:hover {
  color: var(--deep);
  background: rgba(2, 119, 189, 0.06);
}
</style>
