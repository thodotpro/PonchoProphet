<!-- frontend/src/components/ChatWindow.vue -->

<template>
  <div class="chat-window">

    <div class="chat-header">
      <h1>Poncho Prophet</h1>
      <p>Ask about the weather, get outfit advice</p>
    </div>

    <StatusBadge :agent="currentAgent" :loading="isLoading" />

    <div class="messages" ref="messageList">
      <div v-if="messages.length === 0" class="empty-state">
        Type a location and hit Send to get started
      </div>
      <MessageBubble
        v-for="(msg, i) in messages"
        :key="i"
        :message="msg"
      />
      <div v-if="isLoading" class="typing-indicator">
        <span></span><span></span><span></span>
      </div>
    </div>

    <div v-if="weatherSummary" class="weather-bar">
      <span class="weather-text">{{ weatherSummary }}</span>
      <span v-if="lastCacheHit" class="cache-badge">cached</span>
    </div>

    <div class="input-area">
      <input
        v-model="locationInput"
        placeholder="Location (e.g. Vienna, Austria)"
        class="location-input"
        :disabled="isLoading"
      />
      <input
        v-model="messageInput"
        placeholder="Describe your style — casual, smart, love layers… (optional)"
        class="message-input"
        :disabled="isLoading"
        @keydown.enter="sendMessage"
      />
      <button @click="sendMessage" :disabled="isLoading || !locationInput">
        {{ isLoading ? '...' : 'Send' }}
      </button>
    </div>

  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { v4 as uuidv4 } from 'uuid'
import MessageBubble from './MessageBubble.vue'
import StatusBadge from './StatusBadge.vue'

const sessionId = uuidv4()
const messages = ref([])
const locationInput = ref('')
const messageInput = ref('')
const isLoading = ref(false)
const currentAgent = ref(null)
const weatherSummary = ref('')
const lastCacheHit = ref(false)
const messageList = ref(null)

async function sendMessage() {
  if (!locationInput.value || isLoading.value) return

  messages.value.push({
    role: 'user',
    text: `${locationInput.value} — ${messageInput.value}`,
  })

  isLoading.value = true
  currentAgent.value = 'supervisor'

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: sessionId,
        location: locationInput.value,
        message: messageInput.value || null,
      }),
    })
    if (!response.ok) {
      const err = await response.json().catch(() => ({ detail: response.statusText }))
      throw new Error(err.detail || `Server error: ${response.status}`)
    }
    const data = await response.json()

    messages.value.push({ role: 'assistant', text: data.answer })
    weatherSummary.value = data.weather_summary
    lastCacheHit.value = data.cache_hit
    currentAgent.value = null
    messageInput.value = ''

  } catch (err) {
    messages.value.push({ role: 'error', text: `Something went wrong: ${err.message}` })
  } finally {
    isLoading.value = false
    await nextTick()
    if (messageList.value) {
      messageList.value.scrollTop = messageList.value.scrollHeight
    }
  }
}
</script>

<style scoped>
.chat-window {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #ffffff;
  border-left: 1px solid #e8e8e8;
  border-right: 1px solid #e8e8e8;
}

/* ── Header ── */
.chat-header {
  padding: 20px 24px 16px;
  border-bottom: 1px solid #f0f0f0;
  background: #ffffff;
}

.chat-header h1 {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 2px;
}

.chat-header p {
  font-size: 13px;
  color: #888;
}

/* ── Status badge sits just below the header ── */
.status-badge-wrap {
  padding: 8px 24px 0;
}

/* ── Message list ── */
.messages {
  flex: 1;          /* takes up all remaining vertical space */
  overflow-y: auto;
  padding: 20px 24px;
  display: flex;
  flex-direction: column;
}

.empty-state {
  margin: auto;
  color: #bbb;
  font-size: 14px;
  text-align: center;
}

/* ── Typing indicator (three bouncing dots) ── */
.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 10px 14px;
  background: #f5f5f5;
  border-radius: 16px;
  border-bottom-left-radius: 4px;
  width: fit-content;
  margin-top: 4px;
}

.typing-indicator span {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #aaa;
  animation: bounce 1.2s ease-in-out infinite;
}

.typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
.typing-indicator span:nth-child(3) { animation-delay: 0.4s; }

@keyframes bounce {
  0%, 80%, 100% { transform: translateY(0); }
  40%           { transform: translateY(-6px); }
}

/* ── Weather summary bar ── */
.weather-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 24px;
  background: #f9f9f9;
  border-top: 1px solid #f0f0f0;
  font-size: 13px;
  color: #555;
}

.cache-badge {
  background: #e1f5ee;
  color: #085041;
  font-size: 11px;
  font-weight: 500;
  padding: 2px 8px;
  border-radius: 20px;
}

/* ── Input area ── */
.input-area {
  display: flex;
  gap: 8px;
  padding: 16px 24px;
  border-top: 1px solid #f0f0f0;
  background: #ffffff;
}

.location-input {
  width: 180px;
  flex-shrink: 0;
  padding: 10px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.15s;
}

.message-input {
  flex: 1;
  padding: 10px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.15s;
}

.location-input:focus,
.message-input:focus {
  border-color: #534AB7;
}

button {
  padding: 10px 20px;
  background: #534AB7;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.15s;
  white-space: nowrap;
}

button:hover:not(:disabled) {
  background: #3C3489;
}

button:disabled {
  background: #c0bce8;
  cursor: not-allowed;
}
</style>