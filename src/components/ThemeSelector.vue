<template>
  <div class="relative" v-bind="$attrs">
    <span class="sr-only">Theme</span>
    <button
      @click="isOpen = !isOpen"
      class="flex h-6 w-6 items-center justify-center rounded-lg shadow-md ring-1 shadow-black/5 ring-black/5 dark:bg-slate-700 dark:ring-white/5 dark:ring-inset"
      aria-label="Theme"
    >
      <LightIcon
        :class="clsx(
          'h-4 w-4 dark:hidden',
          theme === 'system' ? 'fill-slate-400' : 'fill-sky-400'
        )"
      />
      <DarkIcon
        :class="clsx(
          'hidden h-4 w-4 dark:block',
          theme === 'system' ? 'fill-slate-400' : 'fill-sky-400'
        )"
      />
    </button>

    <Transition
      enter-active-class="transition duration-100 ease-out"
      enter-from-class="opacity-0 scale-95"
      enter-to-class="opacity-100 scale-100"
      leave-active-class="transition duration-75 ease-in"
      leave-from-class="opacity-100 scale-100"
      leave-to-class="opacity-0 scale-95"
    >
      <ul
        v-if="isOpen"
        @click.outside="() => isOpen = false"
        class="absolute top-full left-1/2 mt-3 w-36 -translate-x-1/2 space-y-1 rounded-xl bg-white p-3 text-sm font-medium shadow-md ring-1 shadow-black/5 ring-black/5 dark:bg-slate-800 dark:ring-white/5"
      >
        <li
          v-for="themeOption in themes"
          :key="themeOption.value"
          @click="selectTheme(themeOption.value)"
          :class="clsx(
            'flex cursor-pointer items-center rounded-[0.625rem] p-1 select-none',
            theme === themeOption.value && 'text-sky-500',
            theme !== themeOption.value && 'text-slate-700 dark:text-slate-400',
            'hover:text-slate-900 hover:bg-slate-100 dark:hover:text-white dark:hover:bg-slate-900/40'
          )"
        >
          <div class="rounded-md bg-white p-1 shadow-sm ring-1 ring-slate-900/5 dark:bg-slate-700 dark:ring-white/5 dark:ring-inset">
            <component
              :is="themeOption.icon"
              :class="clsx(
                'h-4 w-4',
                theme === themeOption.value
                  ? 'fill-sky-400 dark:fill-sky-400'
                  : 'fill-slate-400'
              )"
            />
          </div>
          <div class="ml-3">{{ themeOption.name }}</div>
        </li>
      </ul>
    </Transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import clsx from 'clsx'
import { useTheme } from '@/composables/useTheme'
import LightIcon from './icons/LightIcon.vue'
import DarkIcon from './icons/DarkIcon.vue'
import SystemIcon from './icons/SystemIcon.vue'

const { theme, setTheme } = useTheme()
const isOpen = ref(false)

const themes = [
  { name: 'Luminos', value: 'light', icon: LightIcon },
  { name: 'Întunecat', value: 'dark', icon: DarkIcon },
  { name: 'Sistem', value: 'system', icon: SystemIcon },
]

const selectTheme = (value) => {
  setTheme(value)
  isOpen.value = false
}
</script>
