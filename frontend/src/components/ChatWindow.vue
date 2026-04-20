<!-- frontend/src/components/ChatWindow.vue -->
<!-- Dev B owns the entire frontend directory -->

<template>
  <div class="chat-window">
    <!-- Status badge: shows which agent is currently thinking -->
    <StatusBadge :agent="currentAgent" :loading="isLoading" />

    <!-- Message history -->
    <div class="messages" ref="messageList">
      <MessageBubble
        v-for="(msg, i) in messages"
        :key="i"
        :message="msg"
      />
      <!-- Typing indicator while waiting for the agent graph -->
      <div v-if="isLoading" class="typing-indicator">
        <span></span><span></span><span></span>
      </div>
    </div>

    <!-- Weather summary bar — shown after first successful response -->
    <div v-if="weatherSummary" class="weather-bar">
      {{ weatherSummary }}
      <span v-if="lastCacheHit" class="cache-badge">cached</span>
    </div>

    <!-- Input area -->
    <div class="input-area">
      <input
        v-model="locationInput"
        placeholder="Location (e.g. Vienna, Austria)"
        class="location-input"
        :disabled="isLoading"
      />
      <input
        v-model="messageInput"
        placeholder="Ask about the weather..."
        class="message-input"
        :disabled="isLoading"
        @keydown.enter="sendMessage"
      />
      <button @click="sendMessage" :disabled="isLoading || !locationInput">
        Send
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { v4 as uuidv4 } from 'uuid'
import MessageBubble from './MessageBubble.vue'
import StatusBadge from './StatusBadge.vue'

// session_id is stable for the lifetime of this page load.
// Refresh the page to start a new conversation (new Redis checkpoint).
// 🎓 LEARNING COMPLEXITY: A real app would persist this to localStorage.
const sessionId = uuidv4()

const messages = ref([])
const locationInput = ref('')
const messageInput = ref("What should I wear today?")
const isLoading = ref(false)
const currentAgent = ref(null)
const weatherSummary = ref('')
const lastCacheHit = ref(false)
const messageList = ref(null)

async function sendMessage() {
  if (!locationInput.value || isLoading.value) return

  const userMessage = {
    role: 'user',
    text: `${locationInput.value} — ${messageInput.value}`,
  }
  messages.value.push(userMessage)
  isLoading.value = true
  currentAgent.value = 'supervisor'  // Show activity immediately

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: sessionId,
        location: locationInput.value,
        message: messageInput.value,
      }),
    })

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`)
    }

    const data = await response.json()

    messages.value.push({
      role: 'assistant',
      text: data.answer,
    })

    weatherSummary.value = data.weather_summary
    lastCacheHit.value = data.cache_hit
    currentAgent.value = null
    messageInput.value = ''

  } catch (err) {
    messages.value.push({
      role: 'error',
      text: `Something went wrong: ${err.message}`,
    })
  } finally {
    isLoading.value = false
    // Scroll to bottom after render
    await nextTick()
    if (messageList.value) {
      messageList.value.scrollTop = messageList.value.scrollHeight
    }
  }
}
</script>