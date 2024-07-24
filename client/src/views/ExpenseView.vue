<template>


  <header class="p-2 sticky top-0 bg-stone-200 relative z-50">
    <h1 class="text-center font-bold inline-block">Bookkeeper Expenses </h1>
    <button class="button font-bold text-2xl absolute right-5" @click.stop="addNew()"> + </button>
  </header>

  <div v-for="exp in data" class="p-2 divide-y">
    <div class="flex flex-row justify-between w-full">
      <div class="text-left">
        <font-awesome-icon icon="fa-solid fa-angle-up" size="xs"/>
        {{ exp.date }}
      </div>
      <div class="text-right">{{ exp.totalAmt }}</div>
    </div>
    <div v-for="d in exp.details" class="bg-white">
      <div class="flex flex-row  justify-between">
        <span class="text-left">{{ d.accType }}</span>
        <span class="text-right">{{ d.amt }}</span>
      </div>
      <div class="flex flex-row">
        <span class="w-4/5 text-left">{{ d.cat }}</span>
        <span class="w-1/5 text-right">{{ d.qty + d.unit }}</span>
      </div>
      <div>
        {{ d.note || '&nbsp;' }}
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import {ref} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useRouter} from "vue-router";

const router = useRouter()

const tData = [
  {
    date: '16/07/2024',
    totalAmt: 30000,
    details: [
      {accType: 'Cash', amt: 7.9, cat: 'Food', subCat: 'Convenience Food', qty: 1, unit: 'pack', note: ''},
      {accType: 'Cash', amt: 4, cat: 'Food', subCat: '', qty: 2, unit: 'bottle', note: ''}
    ]
  },
  {
    date: '15/07/2024',
    totalAmt: 3,
    details: [
      {accType: 'Cash', amt: 7.9, cat: 'Food', subCat: 'Convenience Food', qty: 1, unit: 'pack', note: ''},
    ]
  },
  {
    date: '14/07/2024',
    totalAmt: 3,
    details: [
      {accType: 'Cash', amt: 7.9, cat: 'Food', subCat: 'Convenience Food', qty: 1, unit: 'pack', note: ''},
      {accType: 'Cash', amt: 4, cat: 'Food', subCat: '', qty: 2, unit: 'bottle', note: ''}
    ]
  }
]
const data = ref(tData)

function addNew(){
  router.push("/expenses/new")
}

</script>
