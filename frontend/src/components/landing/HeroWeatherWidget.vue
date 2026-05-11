<template>
  <div class="weather-widget" :class="{ 'is-loading': state === 'loading' }">
    <template v-if="state === 'loading'">
      <span class="skeleton skeleton-emoji" aria-hidden="true"></span>
      <div class="widget-text">
        <div class="skeleton skeleton-temp" aria-hidden="true"></div>
        <div class="skeleton skeleton-outfit" aria-hidden="true"></div>
      </div>
      <span class="sr-only">Loading current weather…</span>
    </template>
    <template v-else>
      <span class="emoji" aria-hidden="true">{{ emoji }}</span>
      <div class="widget-text">
        <div class="temp">{{ temp }}</div>
        <div class="outfit">{{ outfit }}</div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { v4 as uuidv4 } from 'uuid'

const state = ref('loading') // 'loading' | 'resolved' | 'fallback'
const temp = ref('')
const outfit = ref('')
const emoji = ref('🌦️')

const FALLBACK = {
  temp: '18°C',
  outfit: 'Light Jacket Day',
  emoji: '☀️',
}

function pickEmoji(summary) {
  const s = (summary || '').toLowerCase()
  if (/(sun|clear)/.test(s)) return '☀️'
  if (/(rain|drizzle|shower|storm)/.test(s)) return '🌧️'
  if (/(snow|cold|freez)/.test(s)) return '❄️'
  if (/cloud/.test(s)) return '☁️'
  return '🌦️'
}

function extractTemp(summary) {
  const match = (summary || '').match(/(-?\d+(?:\.\d+)?)\s*°/)
  if (!match) return null
  // Round to int for display, keep °C.
  const value = Math.round(parseFloat(match[1]))
  return `${value}°C`
}

function shortOutfit(answer) {
  if (!answer) return null
  const trimmed = answer.trim()
  // Prefer first sentence (ending in . ! or ?).
  const sentenceMatch = trimmed.match(/^[^.!?]{3,}[.!?]/)
  let candidate = sentenceMatch ? sentenceMatch[0] : trimmed
  candidate = candidate.replace(/\s+/g, ' ').trim()
  if (candidate.length > 40) {
    candidate = candidate.slice(0, 37).trimEnd() + '…'
  }
  return candidate || null
}

function applyFallback() {
  temp.value = FALLBACK.temp
  outfit.value = FALLBACK.outfit
  emoji.value = FALLBACK.emoji
  state.value = 'fallback'
}

onMounted(async () => {
  const sessionId = uuidv4()
  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: sessionId,
        location: 'Graz',
        message: null,
      }),
      signal: AbortSignal.timeout(5000),
    })
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    const data = await response.json()

    const parsedTemp = extractTemp(data.weather_summary)
    const parsedOutfit = shortOutfit(data.answer)

    if (!parsedTemp || !parsedOutfit) {
      applyFallback()
      return
    }

    temp.value = parsedTemp
    outfit.value = parsedOutfit
    emoji.value = pickEmoji(data.weather_summary)
    state.value = 'resolved'
  } catch (err) {
    applyFallback()
  }
})
</script>

<style scoped>
.weather-widget {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: rgba(255, 255, 255, 0.18);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 16px;
  padding: 14px 22px;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  min-width: 240px;
  min-height: 64px;
}

.emoji {
  font-size: 36px;
  line-height: 1;
}

.widget-text {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 2px;
}

.temp {
  font-size: 32px;
  font-weight: 900;
  color: #ffffff;
  line-height: 1.05;
}

.outfit {
  font-size: 13px;
  color: var(--sun);
  font-weight: 800;
  letter-spacing: 0.2px;
}

/* ── Skeleton / loading state ── */
.skeleton {
  background: rgba(255, 255, 255, 0.25);
  border-radius: 8px;
  animation: pulse 1.4s ease-in-out infinite;
}

.skeleton-emoji {
  width: 36px;
  height: 36px;
  border-radius: 50%;
}

.skeleton-temp {
  width: 80px;
  height: 26px;
  margin-bottom: 4px;
}

.skeleton-outfit {
  width: 140px;
  height: 12px;
}

@keyframes pulse {
  0%, 100% { opacity: 0.55; }
  50%      { opacity: 1; }
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>
