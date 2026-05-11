<!-- Step 2: pick a vibe — 2x2 grid of style cards that auto-advance. -->
<template>
  <section class="step">
    <div class="char-wrap">
      <PonchoChar mood="excited" :size="120" aria-label="Excited Poncho" />
    </div>

    <h1 class="heading">Pick your vibe</h1>
    <p class="sub">Tap a card and we'll dress you for the weather.</p>

    <div class="grid">
      <button
        v-for="opt in options"
        :key="opt.label"
        type="button"
        class="style-card"
        @click="pick(opt)"
      >
        <span class="card-icon">{{ opt.icon }}</span>
        <span class="label">{{ opt.label }}</span>
        <span class="subtitle">{{ opt.subtitle }}</span>
      </button>
    </div>

    <div class="actions">
      <button type="button" class="back-link" @click="back">&larr; back</button>
      <button type="button" class="skip-link" @click="skip">skip wizard</button>
    </div>
  </section>
</template>

<script setup>
import { useWizard } from '../../composables/useWizard.js'

const { style, advance, skip, back } = useWizard()

const options = [
  {
    label: 'Casual',
    subtitle: 'jeans, tee, easy day',
    icon: '👕',
    preset: 'casual, comfortable, jeans and tee',
  },
  {
    label: 'Smart',
    subtitle: 'polished, business casual',
    icon: '👔',
    preset: 'smart, polished, business casual',
  },
  {
    label: 'Sporty',
    subtitle: 'athletic, ready to move',
    icon: '🏃',
    preset: 'sporty, athletic, ready to move',
  },
  {
    label: 'Layered',
    subtitle: 'warm, ready for cold',
    icon: '🧥',
    preset: 'warm, layered, ready for cold',
  },
]

function pick(opt) {
  style.value = opt.preset
  advance()
}
</script>

<style scoped>
.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 24px 0;
}
.char-wrap {
  margin-bottom: 4px;
}
.heading {
  font-family: 'Playfair Display', serif;
  font-size: 34px;
  font-weight: 700;
  color: var(--deep);
  margin: 0;
  text-align: center;
}
.sub {
  font-family: 'Nunito', sans-serif;
  color: var(--mid);
  font-size: 16px;
  margin: 0 0 12px;
  text-align: center;
}
.grid {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 4px;
}
.style-card {
  background: #fff;
  border: 2px solid var(--light);
  border-radius: 20px;
  padding: 20px 16px 18px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  font-family: 'Nunito', sans-serif;
  box-shadow: 0 6px 18px rgba(2, 119, 189, 0.08);
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
}
.card-icon {
  font-size: 48px;
  line-height: 1;
  margin-bottom: 4px;
}
.style-card:hover {
  transform: translateY(-3px);
  border-color: var(--teal);
  box-shadow: 0 12px 28px rgba(2, 119, 189, 0.16);
}
.label {
  font-family: 'Playfair Display', serif;
  font-size: 22px;
  font-weight: 700;
  color: var(--deep);
  margin-top: 6px;
}
.subtitle {
  font-size: 13px;
  color: var(--mid);
  font-weight: 600;
}
.actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-top: 12px;
  padding: 0 4px;
}
.skip-link,
.back-link {
  background: none;
  border: none;
  font-family: 'Nunito', sans-serif;
  font-size: 14px;
  font-weight: 600;
  color: var(--mid);
  text-decoration: underline;
  cursor: pointer;
  padding: 6px 10px;
}
.skip-link:hover {
  color: var(--coral);
}
.back-link:hover {
  color: var(--deep);
}

@media (max-width: 480px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
</style>
