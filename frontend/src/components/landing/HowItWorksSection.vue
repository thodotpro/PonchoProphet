<template>
  <section class="how-it-works">
    <div class="container">
      <p class="section-label">Simple as 1-2-3</p>
      <h2>How it <em>works</em></h2>
      <div class="steps">
        <div class="connector-line"></div>
        <div v-for="(step, i) in steps" :key="i" class="step">
          <div class="step-number">{{ i + 1 }}</div>
          <div class="step-content">
            <h3>{{ step.title }}</h3>
            <p>{{ step.body }}</p>
          </div>
          <div class="step-char">
            <PonchoChar :mood="step.mood" :size="72" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'

const steps = [
  {
    title: '📍 Set your location',
    body: 'Allow location access or type your city. Poncho Prophet pulls real-time, hyperlocal weather data instantly.',
    mood: 'thinking',
  },
  {
    title: '🤖 Ask Poncho',
    body: 'Tell us your vibe - casual layers, work-smart, sporty. Poncho reads the weather and maps it to your style.',
    mood: 'excited',
  },
  {
    title: '👗 Step out in style',
    body: 'Get a full outfit breakdown in seconds. No second-guessing. Weather-proof, every time.',
    mood: 'happy',
  },
]
</script>

<style scoped>
.how-it-works {
  background: var(--cloud);
  padding: 80px 32px;
}

.container {
  max-width: 720px;
  margin: 0 auto;
  text-align: center;
}

.section-label {
  font-family: 'Nunito', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--teal);
  margin-bottom: 12px;
}

h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.4rem;
  color: var(--dark);
  margin-bottom: 56px;
}

h2 em {
  font-style: italic;
  color: var(--teal);
}

.steps {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 40px;
  text-align: left;
}

.connector-line {
  position: absolute;
  left: 36px;
  top: 36px;
  bottom: 36px;
  width: 2px;
  background: linear-gradient(to bottom, var(--sky), var(--teal));
  z-index: 0;
}

.step {
  display: flex;
  align-items: center;
  gap: 24px;
  position: relative;
  z-index: 1;
}

.step-number {
  flex-shrink: 0;
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--deep), var(--teal));
  color: white;
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}

.step-content {
  flex: 1;
}

.step-content h3 {
  font-family: 'Nunito', sans-serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--dark);
  margin-bottom: 8px;
}

.step-content p {
  font-family: 'Nunito', sans-serif;
  font-size: 0.95rem;
  color: var(--mid);
  line-height: 1.6;
  margin: 0;
}

.step-char {
  flex-shrink: 0;
}

@media (max-width: 600px) {
  h2 {
    font-size: 1.8rem;
    margin-bottom: 40px;
  }

  .connector-line {
    display: none;
  }

  .step {
    flex-wrap: wrap;
    gap: 16px;
  }

  .step-char {
    display: none;
  }
}
</style>
