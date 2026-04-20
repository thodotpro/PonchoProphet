<!-- frontend/src/components/MessageBubble.vue -->
<!-- Renders a single message in the chat.
     Receives a message object with { role, text } where
     role is "user", "assistant", or "error". -->

<template>
  <div class="bubble-row" :class="message.role">
    <div class="bubble" :class="message.role">
      {{ message.text }}
    </div>
  </div>
</template>

<script setup>
defineProps({
  message: {
    type: Object,
    required: true
    // Expected shape: { role: 'user' | 'assistant' | 'error', text: String }
  }
})
</script>

<style scoped>
.bubble-row {
  display: flex;
  margin-bottom: 10px;
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

.bubble {
  max-width: 75%;
  padding: 10px 14px;
  border-radius: 16px;
  font-size: 14px;
  line-height: 1.5;
  white-space: pre-wrap; /* Preserves line breaks in the LLM response */
}

.bubble.user {
  background: #534AB7;
  color: #fff;
  border-bottom-right-radius: 4px;
}

.bubble.assistant {
  background: #fff;
  color: #1a1a1a;
  border: 1px solid #e0e0e0;
  border-bottom-left-radius: 4px;
}

.bubble.error {
  background: #fff0f0;
  color: #a32d2d;
  border: 1px solid #f09595;
  border-bottom-left-radius: 4px;
}
</style>