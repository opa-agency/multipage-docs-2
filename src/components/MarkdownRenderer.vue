<script setup>
import { computed } from 'vue'
import MarkdownIt from 'markdown-it'
import Prism from 'prismjs'
import 'prismjs/components/prism-javascript'
import 'prismjs/components/prism-typescript'
import 'prismjs/components/prism-jsx'
import 'prismjs/components/prism-bash'
import 'prismjs/components/prism-json'

const props = defineProps({
  content: {
    type: String,
    required: true
  }
})

const md = new MarkdownIt({
  highlight: (code, lang) => {
    if (lang && Prism.languages[lang]) {
      try {
        return `<pre class="language-${lang}"><code class="language-${lang}">${Prism.highlight(
          code,
          Prism.languages[lang],
          lang
        )}</code></pre>`
      } catch (e) {
        return `<pre><code>${code}</code></pre>`
      }
    }
    return `<pre><code>${code}</code></pre>`
  }
})

const html = computed(() => {
  return md.render(props.content)
})
</script>

<template>
  <div class="prose prose-slate dark:prose-invert max-w-none" v-html="html"></div>
</template>
