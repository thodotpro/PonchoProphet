<template>
  <footer class="landing-footer">
    <div class="logo">Poncho <span>Prophet</span></div>
    <p class="tagline">Smart weather &amp; style · Never be underdressed again</p>
    <div class="char-wrap">
      <PonchoChar mood="waving" :size="80" />
    </div>
    <p class="copyright">© 2025 Poncho Prophet</p>
  </footer>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'
</script>

<style scoped>
.landing-footer {
  background: var(--dark);
  padding: 48px 32px;
  text-align: center;
}

.logo {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  color: white;
  margin-bottom: 8px;
}

.logo span {
  color: var(--sky);
}

.tagline {
  font-family: 'Nunito', sans-serif;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  margin-bottom: 0;
}

.char-wrap {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.copyright {
  font-family: 'Nunito', sans-serif;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.3);
  margin-top: 16px;
  margin-bottom: 0;
}
</style>
