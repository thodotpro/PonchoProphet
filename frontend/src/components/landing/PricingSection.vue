<template>
  <section class="pricing">
    <div class="container">
      <p class="section-label">Choose your plan</p>
      <h2>Always free to <em>start</em></h2>
      <div class="plans">
        <div
          v-for="plan in plans"
          :key="plan.name"
          :class="['plan-card', { popular: plan.popular }]"
        >
          <div v-if="plan.popular" class="popular-badge">⭐ Most Popular</div>
          <div class="plan-icon">{{ plan.icon }}</div>
          <h3 class="plan-name">{{ plan.name }}</h3>
          <div class="plan-price">{{ plan.price }}</div>
          <ul class="plan-features">
            <li v-for="feature in plan.features" :key="feature">{{ feature }}</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const plans = [
  {
    name: 'Basic Weather',
    price: 'Free',
    icon: '☀️',
    popular: false,
    features: [
      'Real-time local weather',
      'Daily outfit suggestion',
      'Feels-like temperature',
    ],
  },
  {
    name: 'Style Premium',
    price: '$2.99/mo',
    icon: '👗',
    popular: true,
    features: [
      'Everything in Basic',
      'Custom wardrobe uploads',
      'Personalised style matching',
      'Smart accessory reminders',
    ],
  },
  {
    name: 'Prophet Pro',
    price: '$4.99/mo',
    icon: '🌍',
    popular: false,
    features: [
      'Everything in Premium',
      'Multi-city packing lists',
      'Severe weather alerts',
      'Priority support',
    ],
  },
]
</script>

<style scoped>
.pricing {
  background: linear-gradient(160deg, #0277bd 0%, #00bcd4 100%);
  padding: 80px 32px;
  text-align: center;
}

.container {
  max-width: 960px;
  margin: 0 auto;
}

.section-label {
  font-family: 'Nunito', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--sun);
  margin-bottom: 12px;
}

h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2.4rem;
  color: white;
  margin-bottom: 48px;
}

h2 em {
  font-style: italic;
}

.plans {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  align-items: start;
}

.plan-card {
  position: relative;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 32px 24px;
  color: white;
  text-align: left;
}

.plan-card.popular {
  background: white;
  border-color: white;
  color: var(--dark);
  transform: translateY(-8px);
}

.popular-badge {
  position: absolute;
  top: -14px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--sun);
  color: var(--dark);
  font-family: 'Nunito', sans-serif;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: 99px;
  white-space: nowrap;
}

.plan-icon {
  font-size: 2rem;
  margin-bottom: 12px;
}

.plan-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 4px;
}

.plan-card.popular .plan-name {
  color: var(--dark);
}

.plan-price {
  font-family: 'Nunito', sans-serif;
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  color: inherit;
}

.plan-card.popular .plan-price {
  color: var(--deep);
}

.plan-features {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.plan-features li {
  font-family: 'Nunito', sans-serif;
  font-size: 0.9rem;
  line-height: 1.4;
  padding-left: 20px;
  position: relative;
}

.plan-features li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--sky);
  font-weight: 700;
}

.plan-card.popular .plan-features li {
  color: var(--mid);
}

.plan-card.popular .plan-features li::before {
  color: var(--teal);
}

@media (max-width: 600px) {
  h2 {
    font-size: 1.8rem;
  }

  .plans {
    grid-template-columns: 1fr;
  }

  .plan-card.popular {
    transform: translateY(0);
  }
}
</style>
