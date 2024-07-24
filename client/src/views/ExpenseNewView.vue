<template>

  <header class="p-2 sticky top-0 bg-stone-200 relative flex flex-row z-50">
    <div class="flex-none"><button @click.stop="back" class="px-4">&lt;</button></div>
    <h1 class="text-center font-bold inline-block flex-1">Add Expenses</h1>
  </header>

  <div class="flex flex-col divide-y">
    <RowItem>
      <label class="content-center">
        Date
      </label>
      <vue-date-picker :ui="{input:'text-right dp_input_imp'}" v-model="d"
                       :enable-time-picker="false" :clearable="false"
                       position="right"
                       auto-apply hide-input-icon/>
    </RowItem>
    <RowItem>
      <label class="content-center">From the account</label>
      <label class="content-center pr-2"> > </label>
    </RowItem>
    <RowItem>
      <label class="content-center">Category</label>
      <label class="content-center pr-2"> > </label>
    </RowItem>
    <RowItem>
      <label class="content-center">Subcategory</label>
      <label class="content-center pr-2"> > </label>
    </RowItem>
    <RowItem>
      <input type="number" placeholder="0.00" class="w-full text-center">
    </RowItem>
    <RowItem>
      <label class="content-center">Currency</label>
      <label class="content-center pr-2"> > </label>
    </RowItem>
    <RowItem>
      <label class="content-center">Quantity</label>
    </RowItem>

    <RowItem>
      <div class="text-left w-full content-center">
        <div>Note</div>
        <input class="w-full" placeholder="Enter text">
      </div>
    </RowItem>

    <button class="bg-amber-500	">Save and continue</button>
  </div>

</template>

<script setup lang="ts">
import {ref} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useRouter} from "vue-router";

import RowItem from "../components/Row.vue"

const d = ref(new Date())
console.log(d.value)

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
]
const data = ref(tData)


function back(){
  router.back()
}
</script>

<style>
.dp__main{
  width: auto;
}

.dp__input{
  border: none !important;
}
</style>