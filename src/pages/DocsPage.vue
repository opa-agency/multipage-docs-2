<template>
  <div class="min-w-0 max-w-2xl flex-auto px-4 py-16 lg:max-w-none lg:pr-0 lg:pl-8 xl:px-16">
    <article>
      <header class="mb-9 space-y-1">
        <p class="font-display text-sm font-medium text-sky-500">
          Documentation
        </p>
        <h1 class="font-display text-3xl tracking-tight text-slate-900 dark:text-white">
          {{ pageTitle }}
        </h1>
      </header>
      <MarkdownRenderer v-if="pageContent" :content="pageContent" />
    </article>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import MarkdownRenderer from '../components/MarkdownRenderer.vue'
import { docsContent } from '../data/docsContent'

const props = defineProps({
  slug: {
    type: String,
    required: true
  }
})

const pageTitle = computed(() => {
  const doc = docsContent[props.slug]
  return doc ? doc.title : props.slug
    .split('-')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
})

const pageContent = computed(() => {
  const doc = docsContent[props.slug]
  return doc ? doc.content : ''
})
</script>
