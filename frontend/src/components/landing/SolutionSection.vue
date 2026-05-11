<template>
  <section class="solution">
    <div class="inner">
      <div class="char-col">
        <PonchoChar mood="thinking" :size="160" />
      </div>
      <div class="text-col">
        <div class="section-label">The Solution</div>
        <h2>Always <em>prepared</em>, never <em>overdressed</em>.</h2>
        <div class="feature-grid">
          <div class="feature-card">
            <div class="icon">🌤️</div>
            <h4>Weather-aware</h4>
            <p>Real-time forecast + temperature drive every suggestion.</p>
          </div>
          <div class="feature-card">
            <div class="icon">🎨</div>
            <h4>Style-aware</h4>
            <p>Tell us your vibe - casual, smart, sporty, layered.</p>
          </div>
          <div class="feature-card">
            <div class="icon">💬</div>
            <h4>Conversational</h4>
            <p>Ask follow-ups. Refine. Adjust. It's a chat, not a form.</p>
          </div>
          <div class="feature-card">
            <div class="icon">⚡</div>
            <h4>Instant</h4>
            <p>One question. One outfit. Walk out the door.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'
</script>

<style scoped>
.solution {
  width: 100%;
  background: var(--mint);
  padding: 80px 32px;
}

.inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1.6fr;
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

.char-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.feature-card {
  background: white;
  border-radius: 14px;
  padding: 16px;
  border: 1px solid var(--light);
  box-shadow: 0 2px 12px rgba(2, 119, 189, 0.08);
}

.feature-card .icon {
  font-size: 24px;
  margin-bottom: 6px;
}

.feature-card h4 {
  font-size: 13px;
  font-weight: 800;
  color: var(--dark);
  margin: 0 0 4px;
}

.feature-card p {
  font-size: 12px;
  color: var(--mid);
  margin: 0;
  line-height: 1.4;
}
</style>
