<template>
  <div>
    <button
      type="button"
      @click="isOpen = true"
      class="relative"
      aria-label="Open navigation"
    >
      <MenuIcon class="h-6 w-6 stroke-slate-500" />
    </button>

    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isOpen"
        @click="close"
        class="fixed inset-0 z-50 flex items-start overflow-y-auto bg-slate-900/50 pr-10 backdrop-blur-sm lg:hidden"
        aria-label="Navigation"
      >
        <div
          @click.stop
          class="min-h-full w-full max-w-xs bg-white px-4 pt-5 pb-12 sm:px-6 dark:bg-slate-900"
        >
          <div class="flex items-center">
            <button
              type="button"
              @click="close"
              aria-label="Close navigation"
            >
              <CloseIcon class="h-6 w-6 stroke-slate-500" />
            </button>
            <router-link to="/" class="ml-6" aria-label="Home page">
              <Logomark class="h-9 w-9" />
            </router-link>
          </div>
          <Navigation class="mt-5 px-1" :on-link-click="close" />
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Logomark from './Logomark.vue'
import Navigation from './Navigation.vue'
import MenuIcon from './icons/MenuIcon.vue'
import CloseIcon from './icons/CloseIcon.vue'

const isOpen = ref(false)
const route = useRoute()

const close = () => {
  isOpen.value = false
}

// Close on route change
watch(() => route.fullPath, () => {
  close()
})
</script>
