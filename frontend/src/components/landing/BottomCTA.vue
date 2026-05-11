<template>
  <div class="bottom-cta">
    <router-link to="/demo" class="bottom-cta__link">
      Get my outfit →
    </router-link>
  </div>
</template>

<script setup>
</script>

<style scoped>
.bottom-cta {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  max-width: 420px;
  background: linear-gradient(135deg, var(--deep), var(--teal));
  border-radius: 9999px;
  box-shadow: 0 12px 32px rgba(2, 119, 189, 0.35);
  padding: 18px 28px;
  z-index: 100;
  text-align: center;
}

.bottom-cta__link {
  display: block;
  color: #ffffff;
  font-weight: 700;
  text-decoration: none;
  font-size: 1.1rem;
  letter-spacing: 0.01em;
}

.bottom-cta__link:hover,
.bottom-cta__link:focus {
  color: #ffffff;
}
</style>
