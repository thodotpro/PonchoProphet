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
import { ref, nextTick, onMounted } from 'vue'
import { v4 as uuidv4 } from 'uuid'
import MessageBubble from './MessageBubble.vue'
import StatusBadge from './StatusBadge.vue'

// Optional pre-fill props (used by the wizard's Step 3 hand-off).
// When omitted, the chat behaves exactly as before: empty inputs,
// user types manually and clicks Send.
const props = defineProps({
  initialLocation: { type: String, default: '' },
  initialStyle: { type: String, default: '' },
  autoSubmit: { type: Boolean, default: false },
})

const sessionId = uuidv4()
const messages = ref([])
const locationInput = ref('')
const messageInput = ref('')
const isLoading = ref(false)
const currentAgent = ref(null)
const weatherSummary = ref('')
const lastCacheHit = ref(false)
const messageList = ref(null)

onMounted(async () => {
  // Pre-fill inputs from wizard answers if provided.
  if (props.initialLocation) locationInput.value = props.initialLocation
  if (props.initialStyle) messageInput.value = props.initialStyle

  // Auto-submit the first message when arriving from a completed wizard.
  if (
    props.autoSubmit &&
    props.initialLocation &&
    props.initialLocation.trim() !== '' &&
    props.initialStyle &&
    props.initialStyle.trim() !== ''
  ) {
    await nextTick()
    sendMessage()
  }
})

async function sendMessage() {
  if (!locationInput.value || isLoading.value) return

  messages.value.push({
    role: 'user',
    text: `${locationInput.value} - ${messageInput.value}`,
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

    // Attach weather_summary to the assistant message so MessageBubble
    // can pick the right PonchoChar mood (sunny/rainy/cold/thinking).
    messages.value.push({
      role: 'assistant',
      text: data.answer,
      weatherSummary: data.weather_summary,
    })
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
  border-left: 1px solid var(--light);
  border-right: 1px solid var(--light);
  font-family: 'Nunito', sans-serif;
}

/* ── Header ── */
.chat-header {
  padding: 22px 24px 18px;
  border-bottom: 1px solid var(--light);
  background: linear-gradient(160deg, var(--cloud) 0%, var(--mint) 100%);
}

.chat-header h1 {
  font-family: 'Playfair Display', serif;
  font-size: 24px;
  font-weight: 700;
  color: var(--deep);
  margin-bottom: 2px;
  letter-spacing: -0.3px;
}

.chat-header p {
  font-size: 13px;
  color: var(--mid);
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
  background: #ffffff;
}

.empty-state {
  margin: auto;
  color: var(--mid);
  font-size: 14px;
  text-align: center;
}

/* ── Typing indicator (three bouncing dots) ── */
.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 10px 14px;
  background: var(--cloud);
  border-radius: 16px;
  border-bottom-left-radius: 4px;
  width: fit-content;
  margin-top: 4px;
}

.typing-indicator span {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--teal);
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
  padding: 10px 24px;
  background: var(--cloud);
  border-top: 1px solid var(--light);
  font-size: 13px;
  font-weight: 500;
  color: var(--mid);
}

.cache-badge {
  background: var(--teal);
  color: #ffffff;
  font-size: 11px;
  font-weight: 600;
  padding: 2px 10px;
  border-radius: 9999px;
  letter-spacing: 0.3px;
  text-transform: uppercase;
}

/* ── Input area ── */
.input-area {
  display: flex;
  gap: 8px;
  padding: 16px 24px;
  border-top: 1px solid var(--light);
  background: #ffffff;
}

.location-input,
.message-input {
  font-family: 'Nunito', sans-serif;
  padding: 10px 14px;
  border: 1px solid var(--light);
  border-radius: 12px;
  font-size: 13px;
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
  background: #ffffff;
  color: var(--dark);
}

.location-input {
  width: 180px;
  flex-shrink: 0;
}

.message-input {
  flex: 1;
}

.location-input:focus,
.message-input:focus {
  border-color: var(--deep);
  box-shadow: 0 0 0 3px rgba(2, 119, 189, 0.18);
}

button {
  font-family: 'Nunito', sans-serif;
  padding: 10px 22px;
  background: var(--deep);
  color: #ffffff;
  border: none;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.15s, transform 0.05s;
  white-space: nowrap;
  letter-spacing: 0.2px;
}

button:hover:not(:disabled) {
  background: #01579b; /* slightly darker than --deep (#0277bd) */
}

button:active:not(:disabled) {
  transform: translateY(1px);
}

button:disabled {
  background: var(--light);
  color: var(--mid);
  cursor: not-allowed;
}
</style>
