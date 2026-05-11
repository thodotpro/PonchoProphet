<!--
  Demo wizard root. Renders the correct step component based on
  useWizard().currentStep. The mood gallery from slice 02 is gone — wizard
  scaffolding (slice 08) lives here now.
-->
<template>
  <main class="demo-view">
    <header class="top-bar">
      <BackToHomeLink />
    </header>

    <div class="wizard-container">
      <WizardStep1Location v-if="currentStep === 1" />
      <WizardStep2Style    v-else-if="currentStep === 2" />
      <WizardStep3Chat     v-else />
    </div>
  </main>
</template>

<script setup>
import BackToHomeLink from '../components/demo/BackToHomeLink.vue'
import WizardStep1Location from '../components/demo/WizardStep1Location.vue'
import WizardStep2Style from '../components/demo/WizardStep2Style.vue'
import WizardStep3Chat from '../components/demo/WizardStep3Chat.vue'
import { useWizard } from '../composables/useWizard.js'

const { currentStep } = useWizard()
</script>

<style scoped>
.demo-view {
  min-height: 100vh;
  background:
    radial-gradient(circle at 12% 18%, rgba(77, 208, 225, 0.18), transparent 55%),
    radial-gradient(circle at 88% 82%, rgba(255, 138, 101, 0.14), transparent 55%),
    var(--cloud);
  padding: 20px 20px 60px;
  font-family: 'Nunito', sans-serif;
}
.top-bar {
  max-width: 1100px;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
}
.wizard-container {
  max-width: 720px;
  margin: 0 auto;
  padding: 24px 16px;
}

@media (max-width: 480px) {
  .demo-view {
    padding: 14px 12px 40px;
  }
  .wizard-container {
    padding: 12px 0;
  }
}
</style>
