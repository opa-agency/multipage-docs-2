import { ref, onMounted, watchEffect } from 'vue'

export function useTheme() {
  const theme = ref('system')
  const resolvedTheme = ref('light')

  const updateTheme = (newTheme) => {
    theme.value = newTheme
    localStorage.setItem('theme', newTheme)
    applyTheme(newTheme)
  }

  const applyTheme = (selectedTheme) => {
    const root = document.documentElement

    if (selectedTheme === 'dark') {
      root.classList.add('dark')
      resolvedTheme.value = 'dark'
    } else if (selectedTheme === 'light') {
      root.classList.remove('dark')
      resolvedTheme.value = 'light'
    } else {
      // system
      const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches
      if (isDark) {
        root.classList.add('dark')
        resolvedTheme.value = 'dark'
      } else {
        root.classList.remove('dark')
        resolvedTheme.value = 'light'
      }
    }
  }

  onMounted(() => {
    const savedTheme = localStorage.getItem('theme') || 'system'
    theme.value = savedTheme
    applyTheme(savedTheme)

    // Listen to system theme changes
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')
    const handleChange = () => {
      if (theme.value === 'system') {
        applyTheme('system')
      }
    }
    mediaQuery.addEventListener('change', handleChange)

    return () => {
      mediaQuery.removeEventListener('change', handleChange)
    }
  })

  watchEffect(() => {
    applyTheme(theme.value)
  })

  return {
    theme,
    resolvedTheme,
    setTheme: updateTheme
  }
}
