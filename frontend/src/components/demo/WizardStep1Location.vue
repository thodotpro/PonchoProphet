<!-- Step 1: ask the visitor where they are. -->
<template>
  <section class="step">
    <div class="card">
      <div class="char-wrap">
        <PonchoChar mood="thinking" :size="130" aria-label="Thinking Poncho" />
      </div>

      <h1 class="heading">Where are you?</h1>
      <p class="sub">Tell me your city so I can check the weather.</p>

      <form class="form" @submit.prevent="onSubmit">
        <input
          v-model="location"
          type="text"
          class="input"
          placeholder="City, country — e.g. Graz, Austria"
          autocomplete="off"
          autofocus
        />
        <button
          type="submit"
          class="next-btn"
          :disabled="!canAdvance"
        >
          Next &rarr;
        </button>
      </form>
    </div>

    <button type="button" class="skip-link" @click="skip">skip wizard</button>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import PonchoChar from '../shared/PonchoChar.vue'
import { useWizard } from '../../composables/useWizard.js'

const { location, advance, skip } = useWizard()

const canAdvance = computed(() => location.value.trim() !== '')

function onSubmit() {
  if (!canAdvance.value) return
  advance()
}
</script>

<style scoped>
.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  padding: 24px 0;
}
.card {
  width: 100%;
  background: #fff;
  border-radius: 24px;
  padding: 36px 32px 32px;
  box-shadow: 0 12px 36px rgba(2, 119, 189, 0.12);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 12px;
  border: 1px solid var(--light);
}
.char-wrap {
  margin-top: -8px;
  margin-bottom: 4px;
}
.heading {
  font-family: 'Playfair Display', serif;
  font-size: 34px;
  font-weight: 700;
  color: var(--deep);
  margin: 0;
}
.sub {
  font-family: 'Nunito', sans-serif;
  color: var(--mid);
  font-size: 16px;
  margin: 0 0 12px;
}
.form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-top: 6px;
}
.input {
  width: 100%;
  font-family: 'Nunito', sans-serif;
  font-size: 17px;
  padding: 14px 18px;
  border: 2px solid var(--light);
  border-radius: 14px;
  background: var(--cloud);
  color: var(--dark);
  outline: none;
  transition: border-color 0.2s ease, background 0.2s ease;
}
.input:focus {
  border-color: var(--teal);
  background: #fff;
}
.next-btn {
  font-family: 'Nunito', sans-serif;
  font-size: 18px;
  font-weight: 800;
  padding: 14px 24px;
  border: none;
  border-radius: 14px;
  background: var(--deep);
  color: #fff;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(2, 119, 189, 0.28);
  transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.2s ease;
}
.next-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  background: var(--teal);
}
.next-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  box-shadow: none;
}
.skip-link {
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
</style>
