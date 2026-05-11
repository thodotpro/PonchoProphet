// frontend/src/composables/weatherToMood.js
//
// Pure function that maps a backend `weather_summary` string (e.g.
// "Sunny, 22°C", "Rainy, 8°C", "Snowy, -3°C") onto one of the four
// moods supported by <PonchoChar> for the chat avatar.
//
// Returns: 'sunny' | 'rainy' | 'cold' | 'thinking'
//
// Explicit weather keywords win over the temperature heuristic — e.g.
// "Sunny, 4°C" stays 'sunny' rather than being downgraded to 'cold'.

const SUNNY_KEYWORDS = ['sun', 'clear']
const RAINY_KEYWORDS = ['rain', 'drizzle', 'shower', 'storm', 'thunder']
const COLD_KEYWORDS = ['snow', 'sleet', 'cold', 'freez', 'ice']

const COLD_TEMP_THRESHOLD = 5

export function weatherToMood(weatherSummary) {
  if (!weatherSummary || typeof weatherSummary !== 'string') {
    return 'thinking'
  }

  const text = weatherSummary.toLowerCase()

  // Explicit weather keywords take precedence over the temperature heuristic.
  if (SUNNY_KEYWORDS.some((kw) => text.includes(kw))) {
    return 'sunny'
  }
  if (RAINY_KEYWORDS.some((kw) => text.includes(kw))) {
    return 'rainy'
  }
  if (COLD_KEYWORDS.some((kw) => text.includes(kw))) {
    return 'cold'
  }

  // Fall back to a temperature heuristic: any number followed by a degree
  // sign (e.g. "4°C", "-3 °", "12°") classifies as cold when <= 5.
  const tempMatch = text.match(/(-?\d+(?:\.\d+)?)\s*°/)
  if (tempMatch) {
    const temp = parseFloat(tempMatch[1])
    if (!Number.isNaN(temp) && temp <= COLD_TEMP_THRESHOLD) {
      return 'cold'
    }
  }

  return 'thinking'
}

export default weatherToMood
