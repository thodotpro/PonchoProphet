// frontend/vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://backend:8000',
        rewrite: (path) => path.replace(/^\/api/, ''),
      }
    }
  }
})




     // '/api': {
   //     target: process.env.VITE_API_URL || 'http://localhost:8000',
 //       rewrite: (path) => path.replace(/^\/api/, ''),
//      }
