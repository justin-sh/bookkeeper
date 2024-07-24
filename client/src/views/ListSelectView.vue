<template>

  <header class="p-2 sticky top-0 bg-stone-200 relative flex flex-row z-50">
    <!--    <div class="flex-none">-->
    <!--      <button @click.stop="back" class="px-4">&lt;</button>-->
    <!--    </div>-->
    <h1 class="text-center font-bold inline-block flex-1">Select {{ route.params.type }}</h1>
  </header>

  <div class="flex flex-col divide-y">
    <RowItem v-for="d in data" :key="d.name" @click="select" class="cursor-pointer">
      <label class="content-center">{{ d.name }}</label>
      <label class="content-center pr-2"> {{ d.val }} </label>
    </RowItem>
  </div>

</template>

<script setup lang="ts">
import {onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";

import RowItem from "../components/Row.vue"

// defineProps(['type'])
const emit = defineEmits<{
  (e: 'itemSelect', value: { name: string, val: string }): void
}>()

const data = ref([])

const router = useRouter()
const route = useRoute()

function getTypeListData() {
  const type = route.params.type

  data.value = [{name: 'Cash', val: 'cash'}, {name: 'Anz', val: 'anz'}]
}

function select(d) {
  emit('itemSelect', d)
  router.back()
}

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