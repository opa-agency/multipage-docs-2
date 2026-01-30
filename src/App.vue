<template>
  <div class="h-full antialiased font-sans">
    <div class="flex min-h-full bg-white dark:bg-slate-900">
      <Layout>
        <RouterView />
      </Layout>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import Layout from './components/Layout.vue'

onMounted(() => {
  // Apply saved theme on mount
  const savedTheme = localStorage.getItem('theme') || 'system'
  const root = document.documentElement
  
  if (savedTheme === 'dark') {
    root.classList.add('dark')
  } else if (savedTheme === 'light') {
    root.classList.remove('dark')
  } else {
    const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches
    if (isDark) {
      root.classList.add('dark')
    } else {
      root.classList.remove('dark')
    }
  }
})
</script>
