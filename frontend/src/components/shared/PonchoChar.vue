<template>
  <svg v-if="mood === 'happy'" :width="size" :height="size * (165/110)" viewBox="0 0 110 165" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <path d="M28 52 C20 56 16 70 16 88 C16 104 19 116 23 120 C27 118 30 106 30 90 C30 74 32 60 36 54 Z" fill="#2C1810"/>
    <path d="M82 52 C90 56 94 70 94 88 C94 104 91 116 87 120 C83 118 80 106 80 90 C80 74 78 60 74 54 Z" fill="#2C1810"/>
    <ellipse cx="55" cy="48" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 54 Q55 34 83 54 Q74 46 55 44 Q36 46 27 54 Z" fill="#3D2314"/>
    <path d="M55 36 Q56 46 55 56" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="70" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="84" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="67" r="5" fill="#5D3A1A"/><circle cx="43" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="65" r="1.4" fill="white"/>
    <circle cx="67" cy="67" r="5" fill="#5D3A1A"/><circle cx="67" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="65" r="1.4" fill="white"/>
    <path d="M36 62 Q43 58 50 62" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M60 62 Q67 58 74 62" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <line x1="37" y1="61" x2="35" y2="58" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="59" x2="40" y2="56" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="59" x2="60" y2="56" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="65" y1="58" x2="64" y2="55" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="59" x2="70" y2="56" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="75" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="76" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="76" r="1.5" fill="#D4906A"/>
    <path d="M44 83 Q55 95 66 83" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.12)" stroke-linecap="round"/>
    <path d="M47 84 Q55 92 63 84" fill="white" opacity="0.6"/>
    <ellipse cx="33" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="97" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="24" y="108" width="62" height="55" rx="11" fill="#D4A843"/>
    <polygon points="55,110 46,127 55,122" fill="#B8902E"/>
    <polygon points="55,110 64,127 55,122" fill="#B8902E"/>
    <rect x="24" y="137" width="62" height="7" rx="3" fill="#B8902E"/>
    <rect x="47" y="133" width="16" height="15" rx="2" fill="#8B6914"/>
    <rect x="8"  y="110" width="18" height="11" rx="5.5" fill="#D4A843"/>
    <rect x="84" y="110" width="18" height="11" rx="5.5" fill="#D4A843"/>
    <ellipse cx="9"  cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <ellipse cx="101" cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'worried'" :width="size" :height="size * (165/110)" viewBox="0 0 110 165" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <line x1="10" y1="4"  x2="7"  y2="17" stroke="#4fc3f7" stroke-width="1.6" stroke-linecap="round" opacity="0.75"/>
    <line x1="26" y1="2"  x2="23" y2="15" stroke="#4fc3f7" stroke-width="1.6" stroke-linecap="round" opacity="0.65"/>
    <line x1="84" y1="5"  x2="81" y2="18" stroke="#4fc3f7" stroke-width="1.6" stroke-linecap="round" opacity="0.7"/>
    <line x1="100" y1="3" x2="97" y2="16" stroke="#4fc3f7" stroke-width="1.6" stroke-linecap="round" opacity="0.6"/>
    <line x1="55" y1="1"  x2="52" y2="14" stroke="#4fc3f7" stroke-width="1.2" stroke-linecap="round" opacity="0.5"/>
    <path d="M28 52 C20 56 16 70 16 88 C16 104 19 116 23 120 C27 118 30 106 30 90 C30 74 32 60 36 54 Z" fill="#2C1810"/>
    <path d="M82 52 C90 56 94 70 94 88 C94 104 91 116 87 120 C83 118 80 106 80 90 C80 74 78 60 74 54 Z" fill="#2C1810"/>
    <ellipse cx="21" cy="122" rx="3" ry="5" fill="#4fc3f7" opacity="0.5"/>
    <ellipse cx="89" cy="120" rx="3" ry="5" fill="#4fc3f7" opacity="0.45"/>
    <ellipse cx="55" cy="48" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 54 Q55 34 83 54 Q74 46 55 44 Q36 46 27 54 Z" fill="#3D2314"/>
    <path d="M55 36 Q56 46 55 56" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="70" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="84" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="68" r="5" fill="#5D3A1A"/><circle cx="43" cy="68" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="66" r="1.4" fill="white"/>
    <circle cx="67" cy="68" r="5" fill="#5D3A1A"/><circle cx="67" cy="68" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="66" r="1.4" fill="white"/>
    <path d="M36 59 Q43 64 50 60" stroke="#2C1810" stroke-width="2.6" fill="none" stroke-linecap="round"/>
    <path d="M60 60 Q67 64 74 59" stroke="#2C1810" stroke-width="2.6" fill="none" stroke-linecap="round"/>
    <line x1="37" y1="62" x2="35" y2="59" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="61" x2="40" y2="58" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="60" x2="60" y2="57" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="60" x2="70" y2="57" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="75" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="76" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="76" r="1.5" fill="#D4906A"/>
    <path d="M44 87 Q55 80 66 87" stroke="#C06240" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="82" cy="64" rx="3.5" ry="4.5" fill="#4fc3f7" opacity="0.8"/>
    <path d="M82 59 L80 63 L84 63 Z" fill="#4fc3f7" opacity="0.8"/>
    <ellipse cx="33" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="97" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="30" y="108" width="50" height="55" rx="11" fill="#EF9A9A"/>
    <rect x="10" y="110" width="22" height="11" rx="5.5" fill="#EF9A9A"/>
    <rect x="78" y="110" width="22" height="11" rx="5.5" fill="#EF9A9A"/>
    <ellipse cx="10"  cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <ellipse cx="100" cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'excited'" :width="size" :height="size * (165/110)" viewBox="0 0 110 165" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <text x="2"  y="18" font-size="12">✨</text>
    <text x="88" y="15" font-size="11">⭐</text>
    <text x="90" y="34" font-size="9">✨</text>
    <path d="M28 52 C20 56 16 70 16 88 C16 104 19 116 23 120 C27 118 30 106 30 90 C30 74 32 60 36 54 Z" fill="#2C1810"/>
    <path d="M82 52 C90 56 94 70 94 88 C94 104 91 116 87 120 C83 118 80 106 80 90 C80 74 78 60 74 54 Z" fill="#2C1810"/>
    <ellipse cx="55" cy="48" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 54 Q55 34 83 54 Q74 46 55 44 Q36 46 27 54 Z" fill="#3D2314"/>
    <path d="M55 36 Q56 46 55 56" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="70" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="84" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="66" rx="8.5" ry="8.5" fill="white"/>
    <ellipse cx="67" cy="66" rx="8.5" ry="8.5" fill="white"/>
    <circle cx="43" cy="66" r="6" fill="#5D3A1A"/><circle cx="43" cy="66" r="3.2" fill="#1A0F0A"/>
    <circle cx="67" cy="66" r="6" fill="#5D3A1A"/><circle cx="67" cy="66" r="3.2" fill="#1A0F0A"/>
    <circle cx="45" cy="63" r="2" fill="white"/><circle cx="69" cy="63" r="2" fill="white"/>
    <circle cx="46" cy="65" r="0.9" fill="white"/><circle cx="70" cy="65" r="0.9" fill="white"/>
    <path d="M35 57 Q43 53 51 57" stroke="#2C1810" stroke-width="2.3" fill="none" stroke-linecap="round"/>
    <path d="M59 57 Q67 53 75 57" stroke="#2C1810" stroke-width="2.3" fill="none" stroke-linecap="round"/>
    <line x1="36" y1="59" x2="34" y2="56" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="40" y1="57" x2="39" y2="54" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="60" y1="57" x2="59" y2="54" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="57" x2="70" y2="54" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="75" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="76" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="76" r="1.5" fill="#D4906A"/>
    <path d="M41 82 Q55 98 69 82" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.16)" stroke-linecap="round"/>
    <path d="M44 83 Q55 95 66 83" fill="white" opacity="0.7"/>
    <ellipse cx="33" cy="76" rx="8" ry="5" fill="rgba(230,100,70,0.28)"/>
    <ellipse cx="77" cy="76" rx="8" ry="5" fill="rgba(230,100,70,0.28)"/>
    <rect x="48" y="97" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="28" y="108" width="54" height="55" rx="11" fill="#80DEEA"/>
    <polygon points="55,110 46,126 55,121" fill="#4DD0E1"/>
    <polygon points="55,110 64,126 55,121" fill="#4DD0E1"/>
    <rect x="4"  y="96" width="26" height="11" rx="5.5" fill="#80DEEA" transform="rotate(-42,17,101)"/>
    <rect x="80" y="96" width="26" height="11" rx="5.5" fill="#80DEEA" transform="rotate(42,93,101)"/>
    <ellipse cx="7"  cy="88" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <ellipse cx="103" cy="88" rx="6.5" ry="7.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'thinking'" :width="size" :height="size * (165/110)" viewBox="0 0 110 165" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <circle cx="86" cy="48" r="2.2" fill="rgba(255,255,255,0.22)"/>
    <circle cx="91" cy="39" r="3.5" fill="rgba(255,255,255,0.18)"/>
    <circle cx="96" cy="28" r="6"   fill="rgba(255,255,255,0.15)"/>
    <text x="92" y="32" text-anchor="middle" font-size="7" fill="rgba(255,255,255,0.45)">?</text>
    <path d="M28 52 C20 56 16 70 16 88 C16 104 19 116 23 120 C27 118 30 106 30 90 C30 74 32 60 36 54 Z" fill="#2C1810"/>
    <path d="M82 52 C90 56 94 70 94 88 C94 104 91 116 87 120 C83 118 80 106 80 90 C80 74 78 60 74 54 Z" fill="#2C1810"/>
    <ellipse cx="55" cy="48" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 54 Q55 34 83 54 Q74 46 55 44 Q36 46 27 54 Z" fill="#3D2314"/>
    <path d="M55 36 Q56 46 55 56" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="70" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="84" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="45" cy="67" r="5" fill="#5D3A1A"/><circle cx="45" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="47" cy="65" r="1.4" fill="white"/>
    <circle cx="69" cy="67" r="5" fill="#5D3A1A"/><circle cx="69" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="71" cy="65" r="1.4" fill="white"/>
    <path d="M36 59 Q43 55 50 59" stroke="#2C1810" stroke-width="2.3" fill="none" stroke-linecap="round"/>
    <path d="M60 62 Q67 60 74 62" stroke="#2C1810" stroke-width="2"   fill="none" stroke-linecap="round"/>
    <line x1="37" y1="61" x2="35" y2="58" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="59" x2="40" y2="56" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="61" x2="60" y2="58" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="61" x2="70" y2="58" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="75" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="76" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="76" r="1.5" fill="#D4906A"/>
    <path d="M46 84 Q55 90 64 84" stroke="#C06240" stroke-width="2" fill="none" stroke-linecap="round"/>
    <ellipse cx="33" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="97" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="30" y="108" width="50" height="55" rx="11" fill="#B0BEC5"/>
    <polygon points="55,110 46,125 55,120" fill="#90A4AE"/>
    <polygon points="55,110 64,125 55,120" fill="#90A4AE"/>
    <rect x="10" y="110" width="22" height="11" rx="5.5" fill="#B0BEC5"/>
    <ellipse cx="10" cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <rect x="78" y="104" width="11" height="24" rx="5.5" fill="#B0BEC5" transform="rotate(-18,83,116)"/>
    <ellipse cx="84" cy="95" rx="7.5" ry="6.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'sunny'" :width="size" :height="size * (185/110)" viewBox="0 0 110 185" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <circle cx="90" cy="18" r="12" fill="#FFCA28" opacity="0.9"/>
    <line x1="90" y1="2"  x2="90" y2="6"  stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="90" y1="30" x2="90" y2="34" stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="74" y1="18" x2="78" y2="18" stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="102" y1="18" x2="106" y2="18" stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="78" y1="7"  x2="80" y2="9"  stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="98" y1="27" x2="100" y2="30" stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="100" y1="7"  x2="98"  y2="9"  stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <line x1="78"  y1="30" x2="80"  y2="27" stroke="#FFCA28" stroke-width="2" stroke-linecap="round"/>
    <rect x="32" y="55" width="46" height="8" rx="4" fill="#1A2E3B" opacity="0.88"/>
    <rect x="32" y="55" width="20" height="8" rx="4" fill="#1A2E3B"/>
    <rect x="58" y="55" width="20" height="8" rx="4" fill="#1A2E3B"/>
    <rect x="52" y="57" width="6"  height="4" rx="1" fill="#2C4A60"/>
    <path d="M28 66 C20 70 16 84 16 102 C16 118 19 130 23 134 C27 132 30 120 30 104 C30 88 32 74 36 68 Z" fill="#2C1810"/>
    <path d="M82 66 C90 70 94 84 94 102 C94 118 91 130 87 134 C83 132 80 120 80 104 C80 88 78 74 74 68 Z" fill="#2C1810"/>
    <ellipse cx="55" cy="62" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 68 Q55 48 83 68 Q74 60 55 58 Q36 60 27 68 Z" fill="#3D2314"/>
    <path d="M55 50 Q56 60 55 70" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="84" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="86" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="86" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="86" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="86" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="98" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="80" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="80" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="81" r="5" fill="#5D3A1A"/><circle cx="43" cy="81" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="79" r="1.4" fill="white"/>
    <circle cx="67" cy="81" r="5" fill="#5D3A1A"/><circle cx="67" cy="81" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="79" r="1.4" fill="white"/>
    <path d="M36 76 Q43 72 50 76" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M60 76 Q67 72 74 76" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <line x1="37" y1="75" x2="35" y2="72" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="73" x2="40" y2="70" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="73" x2="60" y2="70" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="73" x2="70" y2="70" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="89" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="90" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="90" r="1.5" fill="#D4906A"/>
    <path d="M44 97 Q55 109 66 97" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.12)" stroke-linecap="round"/>
    <path d="M47 98 Q55 107 63 98" fill="white" opacity="0.6"/>
    <ellipse cx="33" cy="90" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="90" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="111" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <path d="M30 124 L42 120 L55 122 L68 120 L80 124 L76 182 L34 182 Z" fill="#FF8A65"/>
    <path d="M42 120 L55 122 L68 120 L64 133 L55 135 L46 133 Z" fill="#FF7043"/>
    <rect x="42" y="120" width="7" height="15" rx="3.5" fill="#FF7043"/>
    <rect x="61" y="120" width="7" height="15" rx="3.5" fill="#FF7043"/>
    <rect x="6"  y="124" width="26" height="10" rx="5" fill="#F5C9A0"/>
    <rect x="78" y="124" width="26" height="10" rx="5" fill="#F5C9A0"/>
    <ellipse cx="5"  cy="137" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <rect x="80" y="132" width="20" height="16" rx="5" fill="#FFCA28"/>
    <rect x="80" y="129" width="20" height="6"  rx="3" fill="#F9A825"/>
    <line x1="90" y1="129" x2="90" y2="123" stroke="#F9A825" stroke-width="2"/>
  </svg>

  <svg v-else-if="mood === 'rainy'" :width="size" :height="size * (185/110)" viewBox="0 0 110 185" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <line x1="10" y1="4"  x2="7"  y2="17" stroke="#4fc3f7" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>
    <line x1="26" y1="2"  x2="23" y2="15" stroke="#4fc3f7" stroke-width="1.5" stroke-linecap="round" opacity="0.65"/>
    <line x1="44" y1="5"  x2="41" y2="18" stroke="#4fc3f7" stroke-width="1.5" stroke-linecap="round" opacity="0.5"/>
    <line x1="76" y1="3"  x2="73" y2="16" stroke="#4fc3f7" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>
    <line x1="94" y1="6"  x2="91" y2="19" stroke="#4fc3f7" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>
    <path d="M18 58 Q55 32 92 58" fill="#E53935" stroke="#C62828" stroke-width="1.5"/>
    <path d="M18 58 Q36 50 55 58" fill="#EF5350"/>
    <path d="M55 58 Q74 50 92 58" fill="#EF5350"/>
    <line x1="55" y1="58" x2="55" y2="108" stroke="#5D4037" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M55 108 Q55 116 49 116" stroke="#5D4037" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M28 74 C20 78 16 92 16 110 C16 126 19 138 23 142 C27 140 30 128 30 112 C30 96 32 82 36 76 Z" fill="#2C1810"/>
    <path d="M82 74 C90 78 94 92 94 110 C94 126 91 138 87 142 C83 140 80 128 80 112 C80 96 78 82 74 76 Z" fill="#2C1810"/>
    <ellipse cx="21" cy="144" rx="3" ry="5.5" fill="#4fc3f7" opacity="0.48"/>
    <ellipse cx="89" cy="142" rx="3" ry="5.5" fill="#4fc3f7" opacity="0.44"/>
    <ellipse cx="55" cy="70" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 76 Q55 56 83 76 Q74 68 55 66 Q36 68 27 76 Z" fill="#3D2314"/>
    <path d="M55 58 Q56 68 55 78" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="92" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="94" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="94" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="94" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="94" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="106" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="88" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="88" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="89" r="5" fill="#5D3A1A"/><circle cx="43" cy="89" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="87" r="1.4" fill="white"/>
    <circle cx="67" cy="89" r="5" fill="#5D3A1A"/><circle cx="67" cy="89" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="87" r="1.4" fill="white"/>
    <path d="M36 84 Q43 80 50 84" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M60 84 Q67 80 74 84" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <line x1="37" y1="83" x2="35" y2="80" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="81" x2="40" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="81" x2="60" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="81" x2="70" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="97" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="98" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="98" r="1.5" fill="#D4906A"/>
    <path d="M44 105 Q55 117 66 105" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.12)" stroke-linecap="round"/>
    <path d="M47 106 Q55 115 63 106" fill="white" opacity="0.6"/>
    <ellipse cx="33" cy="98" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="98" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="119" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="24" y="130" width="62" height="53" rx="11" fill="#FDD835"/>
    <polygon points="55,132 46,148 55,143" fill="#F9A825"/>
    <polygon points="55,132 64,148 55,143" fill="#F9A825"/>
    <rect x="24" y="158" width="62" height="7" rx="3" fill="#F9A825"/>
    <rect x="6"  y="132" width="20" height="11" rx="5.5" fill="#FDD835"/>
    <rect x="84" y="132" width="20" height="11" rx="5.5" fill="#FDD835"/>
    <ellipse cx="6"  cy="145" rx="6.5" ry="7.5" fill="#F5C9A0"/>
    <ellipse cx="104" cy="145" rx="6.5" ry="7.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'waving'" :width="size" :height="size * (165/110)" viewBox="0 0 110 165" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <path d="M28 52 C20 56 16 70 16 88 C16 104 19 116 23 120 C27 118 30 106 30 90 C30 74 32 60 36 54 Z" fill="#2C1810"/>
    <path d="M82 52 C90 56 94 70 94 88 C94 104 91 116 87 120 C83 118 80 106 80 90 C80 74 78 60 74 54 Z" fill="#2C1810"/>
    <ellipse cx="55" cy="48" rx="28" ry="16" fill="#2C1810"/>
    <path d="M27 54 Q55 34 83 54 Q74 46 55 44 Q36 46 27 54 Z" fill="#3D2314"/>
    <path d="M55 36 Q56 46 55 56" stroke="#4A2D1A" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="70" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="72" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="72" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="43" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="66" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="67" r="5" fill="#5D3A1A"/><circle cx="43" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="65" r="1.4" fill="white"/>
    <circle cx="67" cy="67" r="5" fill="#5D3A1A"/><circle cx="67" cy="67" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="65" r="1.4" fill="white"/>
    <path d="M36 62 Q43 58 50 62" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M60 62 Q67 58 74 62" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <ellipse cx="55" cy="75" rx="3" ry="2" fill="#E8A878"/>
    <path d="M44 83 Q55 95 66 83" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.12)" stroke-linecap="round"/>
    <ellipse cx="33" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="76" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="48" y="97" width="14" height="13" rx="4" fill="#F5C9A0"/>
    <rect x="30" y="108" width="50" height="40" rx="11" fill="#4fc3f7"/>
    <rect x="4" y="98" width="26" height="11" rx="5.5" fill="#4fc3f7" transform="rotate(-40,17,103)"/>
    <ellipse cx="6" cy="90" rx="7" ry="8" fill="#F5C9A0"/>
    <rect x="80" y="110" width="22" height="11" rx="5.5" fill="#4fc3f7"/>
    <ellipse cx="103" cy="123" rx="6.5" ry="7.5" fill="#F5C9A0"/>
  </svg>

  <svg v-else-if="mood === 'cold'" :width="size" :height="size * (185/110)" viewBox="0 0 110 185" xmlns="http://www.w3.org/2000/svg" :aria-label="ariaLabel" role="img">
    <text x="4"  y="18" font-size="11" fill="#90CAF9" opacity="0.8">❄</text>
    <text x="88" y="14" font-size="9"  fill="#90CAF9" opacity="0.6">❄</text>
    <text x="74" y="28" font-size="8"  fill="#90CAF9" opacity="0.5">❄</text>
    <path d="M28 74 C20 78 16 92 16 110 C16 126 19 138 23 142 C27 140 30 128 30 112 C30 96 32 82 36 76 Z" fill="#2C1810"/>
    <path d="M82 74 C90 78 94 92 94 110 C94 126 91 138 87 142 C83 140 80 128 80 112 C80 96 78 82 74 76 Z" fill="#2C1810"/>
    <rect x="26" y="62" width="58" height="30" rx="12" fill="#EF5350"/>
    <rect x="22" y="78" width="66" height="11" rx="5" fill="#C62828"/>
    <circle cx="55" cy="57" r="9"  fill="#EF5350"/>
    <circle cx="55" cy="53" r="6.5" fill="#FFCDD2"/>
    <ellipse cx="55" cy="92" rx="27" ry="29" fill="#F5C9A0"/>
    <ellipse cx="27" cy="94" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="27" cy="94" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="83" cy="94" rx="5" ry="7" fill="#F5C9A0"/><ellipse cx="83" cy="94" rx="3" ry="5" fill="#E8A878"/>
    <ellipse cx="55" cy="106" rx="17" ry="7" fill="#E8A878" opacity="0.28"/>
    <ellipse cx="43" cy="88" rx="7.5" ry="7.5" fill="white"/>
    <ellipse cx="67" cy="88" rx="7.5" ry="7.5" fill="white"/>
    <circle cx="43" cy="89" r="5" fill="#5D3A1A"/><circle cx="43" cy="89" r="2.8" fill="#1A0F0A"/><circle cx="45" cy="87" r="1.4" fill="white"/>
    <circle cx="67" cy="89" r="5" fill="#5D3A1A"/><circle cx="67" cy="89" r="2.8" fill="#1A0F0A"/><circle cx="69" cy="87" r="1.4" fill="white"/>
    <path d="M36 84 Q43 80 50 84" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <path d="M60 84 Q67 80 74 84" stroke="#2C1810" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <line x1="37" y1="83" x2="35" y2="80" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="41" y1="81" x2="40" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="81" x2="60" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="70" y1="81" x2="70" y2="78" stroke="#2C1810" stroke-width="1.2" stroke-linecap="round"/>
    <ellipse cx="55" cy="97" rx="3" ry="2" fill="#E8A878"/>
    <circle cx="52.5" cy="98" r="1.5" fill="#D4906A"/><circle cx="57.5" cy="98" r="1.5" fill="#D4906A"/>
    <path d="M44 105 Q55 117 66 105" stroke="#C06240" stroke-width="2.5" fill="rgba(200,90,70,0.12)" stroke-linecap="round"/>
    <path d="M47 106 Q55 115 63 106" fill="white" opacity="0.6"/>
    <ellipse cx="33" cy="98" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <ellipse cx="77" cy="98" rx="7" ry="4.5" fill="rgba(230,100,70,0.22)"/>
    <rect x="36" y="117" width="38" height="15" rx="7.5" fill="#FFCA28"/>
    <rect x="36" y="117" width="38" height="6"  rx="3"   fill="#F9A825"/>
    <rect x="36" y="123" width="13" height="22" rx="6"   fill="#FFCA28"/>
    <rect x="22" y="130" width="66" height="53" rx="13" fill="#5C6BC0"/>
    <polygon points="55,132 45,149 55,144" fill="#3F51B5"/>
    <polygon points="55,132 65,149 55,144" fill="#3F51B5"/>
    <ellipse cx="55" cy="131" rx="22" ry="6.5" fill="#ECEFF1"/>
    <circle cx="55" cy="144" r="2.8" fill="#3F51B5"/>
    <circle cx="55" cy="154" r="2.8" fill="#3F51B5"/>
    <circle cx="55" cy="164" r="2.8" fill="#3F51B5"/>
    <rect x="4"  y="130" width="20" height="16" rx="8" fill="#5C6BC0"/>
    <rect x="86" y="130" width="20" height="16" rx="8" fill="#5C6BC0"/>
    <ellipse cx="6"  cy="149" rx="7.5" ry="8.5" fill="#EF5350"/>
    <ellipse cx="104" cy="149" rx="7.5" ry="8.5" fill="#EF5350"/>
  </svg>
</template>

<script setup>
defineProps({
  mood: {
    type: String,
    default: null,
    validator: (v) =>
      v == null ||
      ['happy', 'worried', 'excited', 'thinking', 'sunny', 'rainy', 'cold', 'waving'].includes(v),
  },
  size: {
    type: Number,
    default: 110,
  },
  ariaLabel: {
    type: String,
    default: 'Poncho character',
  },
})
</script>
