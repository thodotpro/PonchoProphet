<template>
  <router-view />
  <BottomCTA v-if="route.path === '/'" />
</template>

<script setup>
import { useRoute } from 'vue-router'
import BottomCTA from './components/landing/BottomCTA.vue'

const route = useRoute()
</script>
