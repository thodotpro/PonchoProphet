<!-- frontend/src/components/StatusBadge.vue -->
<!-- Shows which agent is currently active while the graph is running.
     Hidden when loading is false.
     This is the "visual flair" component — it makes the multi-agent
     system visible to the user, which is important for a learning project. -->

<template>
  <div v-if="loading" class="status-badge">
    <span class="dot"></span>
    {{ label }}
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  agent: {
    type: String,
    default: null,
    // Expected values: 'supervisor', 'cache_agent',
    //                  'weather_agent', 'outfit_agent'
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

// Maps the internal agent name from the backend to a human-readable label.
// When the backend sends active_agent: "cache_agent", the user sees
// "Checking weather cache..." — making the agent graph legible.
const label = computed(() => {
  const labels = {
    supervisor: 'Supervisor is routing...',
    cache_agent: 'Checking weather cache...',
    weather_agent: 'Fetching live weather...',
    outfit_agent: 'Generating outfit recommendation...',
  }
  return labels[props.agent] ?? 'Thinking...'
})
</script>

<style scoped>
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background: var(--deep);
  color: #ffffff;
  border-radius: 9999px; /* Full-pill, brochure style */
  font-family: 'Nunito', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.2px;
  width: fit-content;
  margin: 0 0 10px 0;
  box-shadow: 0 2px 6px rgba(2, 119, 189, 0.2);
}

.dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--sun);
  /* Pulse animation so it's obvious something is happening */
  animation: pulse 1.2s ease-in-out infinite;
}

@keyframes pulse {
  0%,
  100% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.4;
    transform: scale(0.8);
  }
}
</style>
