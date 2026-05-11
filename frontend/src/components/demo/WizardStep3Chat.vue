<template>
  <section class="step">
    <div class="step-header">
      <PonchoChar mood="happy" :size="72" />
      <h2 class="heading">Here's your outfit</h2>
    </div>

    <div class="chat-wrap">
      <ChatWindow
        :initialLocation="location"
        :initialStyle="style"
        :autoSubmit="true"
      />
    </div>
  </section>
</template>

<script setup>
import PonchoChar from '../shared/PonchoChar.vue'
import ChatWindow from '../ChatWindow.vue'
import { useWizard } from '../../composables/useWizard.js'

const { location, style } = useWizard()
</script>

<style scoped>
.step {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 24px 0;
}
.step-header {
  display: flex;
  align-items: center;
  gap: 16px;
}
.heading {
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  font-weight: 700;
  color: var(--deep);
  margin: 0;
}
.chat-wrap {
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 40px rgba(2, 119, 189, 0.15);
  height: 520px;
  display: flex;
  flex-direction: column;
}
.chat-wrap :deep(.chat-window) {
  height: 100%;
}
</style>
