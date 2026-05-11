<template>
  <section class="hero">
    <div class="hero-inner">
      <div class="logo-badge">
        <span>🌦️ Poncho Prophet</span>
      </div>

      <h1>Dress for the<br><em>weather.</em> Always.</h1>

      <p class="hero-subtitle">
        Smart outfit recommendations based on real-time weather - tailored to your style.
      </p>

      <div class="hero-character">
        <PonchoChar mood="excited" :size="170" />
      </div>

      <router-link to="/demo" class="cta-button">
        Try It Free →
      </router-link>

      <!-- Weather widget slot — populated in slice 04 -->
      <div class="weather-widget-slot">
        <HeroWeatherWidget />
      </div>
    </div>
  </section>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'
import HeroWeatherWidget from './HeroWeatherWidget.vue'
</script>

<style scoped>
.hero {
  position: relative;
  width: 100%;
  overflow: hidden;
  background: linear-gradient(160deg, var(--deep) 0%, var(--teal) 60%, var(--sky) 100%);
  padding: 80px 32px 100px;
  text-align: center;
}

.hero::before {
  content: '';
  position: absolute;
  top: -120px;
  right: -120px;
  width: 480px;
  height: 480px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.07);
  pointer-events: none;
}

.hero::after {
  content: '';
  position: absolute;
  bottom: -100px;
  left: -100px;
  width: 360px;
  height: 360px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  pointer-events: none;
}

.hero-inner {
  position: relative;
  z-index: 1;
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo-badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 50px;
  padding: 8px 20px;
  margin-bottom: 28px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.logo-badge span {
  color: white;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.hero h1 {
  font-family: 'Playfair Display', serif;
  font-size: 52px;
  font-weight: 700;
  color: white;
  line-height: 1.1;
  margin-bottom: 16px;
}

.hero h1 em {
  font-style: italic;
  color: var(--sun);
}

.hero-subtitle {
  color: rgba(255, 255, 255, 0.88);
  font-size: 18px;
  font-weight: 600;
  max-width: 460px;
  margin: 0 auto 32px;
  line-height: 1.5;
}

.hero-character {
  margin: 0 auto 32px;
  position: relative;
  z-index: 2;
}

.cta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: white;
  color: var(--deep);
  font-family: 'Nunito', sans-serif;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: 0.3px;
  padding: 16px 36px;
  border-radius: 50px;
  text-decoration: none;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.18);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 36px rgba(0, 0, 0, 0.24);
  color: var(--deep);
}

.cta-button:focus-visible {
  outline: 2px solid var(--sun);
  outline-offset: 3px;
}

/* Reserved space for the live weather widget — populated by slice 04. */
.weather-widget-slot {
  margin-top: 32px;
  min-height: 80px;
}
</style>
