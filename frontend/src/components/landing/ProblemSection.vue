<template>
  <section class="problem">
    <div class="inner">
      <div class="text-col">
        <div class="section-label">The Problem</div>
        <h2>Standing in front of the wardrobe, <em>again</em>?</h2>
        <ul class="pain-list">
          <li>Caught in the rain without a jacket - again</li>
          <li>Layered up for nothing - it warmed up by lunch</li>
          <li>Sweating in a sweater on the way to class</li>
          <li>Standing frozen at the bus stop, underdressed</li>
        </ul>
      </div>
      <div class="char-col">
        <PonchoChar mood="worried" :size="160" />
      </div>
    </div>
  </section>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'
</script>

<style scoped>
.problem {
  width: 100%;
  background: #fff8f6;
  padding: 80px 32px;
}

.inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 48px;
  align-items: center;
}

.section-label {
  font-size: 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--teal);
  margin-bottom: 12px;
}

h2 {
  font-family: 'Playfair Display', serif;
  font-size: 34px;
  font-weight: 700;
  color: var(--deep);
  line-height: 1.2;
  margin-bottom: 24px;
}

h2 em {
  font-style: italic;
  color: var(--deep);
}

.pain-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.pain-list li {
  padding: 12px 16px;
  margin-bottom: 10px;
  background: white;
  border-radius: 12px;
  border-left: 4px solid var(--coral);
  font-size: 15px;
  font-weight: 600;
  color: var(--mid);
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.char-col {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
