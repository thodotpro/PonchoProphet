<!-- frontend/src/components/MessageBubble.vue -->
<!-- Renders a single message in the chat.
     Receives a message object with { role, text, weatherSummary? } where
     role is "user", "assistant", or "error". Assistant messages render a
     <PonchoChar> avatar on the left whose mood is derived from the
     associated weather_summary via weatherToMood. -->

<template>
  <div class="bubble-row" :class="message.role">
    <div v-if="message.role === 'assistant'" class="avatar">
      <PonchoChar :mood="mood" :size="56" aria-label="Poncho avatar" />
    </div>
    <div class="bubble" :class="message.role">
      {{ message.text }}
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import PonchoChar from './shared/PonchoChar.vue'
import { weatherToMood } from '../composables/weatherToMood.js'

const props = defineProps({
  message: {
    type: Object,
    required: true,
    // Expected shape: { role: 'user' | 'assistant' | 'error',
    //                   text: String,
    //                   weatherSummary?: String }
  },
})

// Derive the avatar mood from the message's associated weather summary.
// Missing/undefined weatherSummary falls through to 'thinking'.
const mood = computed(() => weatherToMood(props.message.weatherSummary))
</script>

<style scoped>
.bubble-row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  margin-bottom: 14px;
}

/* User messages sit on the right */
.bubble-row.user {
  justify-content: flex-end;
}

/* Assistant and error messages sit on the left */
.bubble-row.assistant,
.bubble-row.error {
  justify-content: flex-start;
}

.avatar {
  flex-shrink: 0;
  /* Negative bottom margin nudges the character a touch below the bubble
     baseline so its feet "stand" on the bubble row. */
  margin-bottom: -4px;
}

.bubble {
  max-width: 70%;
  padding: 12px 16px;
  border-radius: 18px;
  font-family: 'Nunito', sans-serif;
  font-size: 14px;
  line-height: 1.55;
  white-space: pre-wrap; /* Preserves line breaks in the LLM response */
  box-shadow: 0 2px 6px rgba(2, 119, 189, 0.08);
}

.bubble.user {
  background: var(--deep);
  color: #ffffff;
  border-bottom-right-radius: 6px;
}

.bubble.assistant {
  background: var(--mint);
  color: var(--dark);
  border: 1px solid var(--light);
  border-bottom-left-radius: 6px;
}

.bubble.error {
  background: #fff0f0;
  color: #a32d2d;
  border: 1px solid #f09595;
  border-bottom-left-radius: 6px;
}
</style>
