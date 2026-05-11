// Wizard state machine for the /demo route.
// Module-level refs make a singleton: every component that calls useWizard()
// reads/writes the same reactive state during a single mount.

import { ref } from 'vue'

const STORAGE_KEY = 'poncho:wizard'

// Hydrate from localStorage once at module load.
function loadPersisted() {
  if (typeof window === 'undefined' || !window.localStorage) {
    return { location: '', style: '' }
  }
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY)
    if (!raw) return { location: '', style: '' }
    const parsed = JSON.parse(raw)
    return {
      location: typeof parsed.location === 'string' ? parsed.location : '',
      style: typeof parsed.style === 'string' ? parsed.style : '',
    }
  } catch {
    return { location: '', style: '' }
  }
}

const persisted = loadPersisted()

const currentStep = ref(1)
const location = ref(persisted.location)
const style = ref(persisted.style)

function advance() {
  if (currentStep.value === 1) {
    if (location.value.trim() === '') return
    currentStep.value = 2
    return
  }
  if (currentStep.value === 2) {
    if (style.value === '') return
    currentStep.value = 3
    return
  }
  // Step 3 is terminal — no-op.
}

function back() {
  if (currentStep.value > 1) {
    currentStep.value = currentStep.value - 1
  }
}

function skip() {
  currentStep.value = 3
}

function complete() {
  if (typeof window === 'undefined' || !window.localStorage) return
  try {
    window.localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({ location: location.value, style: style.value })
    )
  } catch {
    // Storage may be unavailable (private mode, quota); silently ignore.
  }
}

function reset() {
  location.value = ''
  style.value = ''
  currentStep.value = 1
  if (typeof window !== 'undefined' && window.localStorage) {
    try {
      window.localStorage.removeItem(STORAGE_KEY)
    } catch {
      // ignore
    }
  }
}

export function useWizard() {
  return {
    currentStep,
    location,
    style,
    advance,
    back,
    skip,
    complete,
    reset,
  }
}
