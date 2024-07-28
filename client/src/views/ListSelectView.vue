<template>

  <header class="p-2 sticky top-0 bg-stone-200 relative flex flex-row z-50">
    <!--    <div class="flex-none">-->
    <!--      <button @click.stop="back" class="px-4">&lt;</button>-->
    <!--    </div>-->
    <h1 class="text-center font-bold inline-block flex-1">Select {{ route.params.type }}</h1>
  </header>

  <div class="flex flex-col divide-y">
    <RowItem v-for="d in data" :key="d.id" @click="select(d)" class="cursor-pointer">
      <label class="content-center">{{ d.name }}</label>
    </RowItem>
  </div>

</template>

<script setup lang="ts">
import {onMounted, reactive, ref} from "vue";
import {onBeforeRouteLeave, useRoute, useRouter} from "vue-router";

import RowItem from "@/components/Row.vue"
import {getOptions} from "@/api";

// defineProps(['type'])
const emit = defineEmits<{
  (e: 'itemSelect', value: { name: string, id: number }): void
}>()

const data = ref<Record<'id' | 'name', any>[]>([])

const router = useRouter()
const route = useRoute()

const result = {type: route.params.type, name: "", id: 0}

async function getTypeListData() {
  const type = route.params.type as string
  const parent = (route.query.parent || '') as string

  data.value = (await getOptions(type, parent)).data
}

function select(d) {
  result.name = d.name
  result.id = d.id
  // emit('itemSelect', d)
  router.back()
}

onBeforeRouteLeave((to, from) => {
  console.log(result)
  console.log(from.path + '->' + to.path)
  console.log()
  to.meta.result = result
})

onMounted(async () => getTypeListData())

</script>

<style>
.dp__main {
  width: auto;
}

.dp__input {
  border: none !important;
}
</style>