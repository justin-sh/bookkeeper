<template>

  <header class="p-2 sticky top-0 bg-stone-200 relative flex flex-row z-50">
    <div class="flex-none">
      <button @click.stop="back" class="px-4">&lt;</button>
    </div>
    <h1 class="text-center font-bold inline-block flex-1">Add Expenses</h1>
  </header>

  <div class="flex flex-col divide-y">
    <RowItem>
      <label class="content-center">
        Date
      </label>
      <vue-date-picker :ui="{input:'text-right dp_input_imp'}" v-model="exp.date"
                       :enable-time-picker="false" :clearable="false"
                       format="yyyy/MM/dd"
                       position="right"
                       auto-apply hide-input-icon/>
    </RowItem>
    <RowItem @click="goListSelect('account')" class="cursor-pointer">
      <label class="content-center">From the account</label>
      <label class="content-center pr-2 cursor-pointer"><span class="me-2">{{ exp.account.name }}</span> > </label>
    </RowItem>
    <RowItem @click="goListSelect('category')" class="cursor-pointer">
      <label class="content-center">Category</label>
      <label class="content-center pr-2 cursor-pointer"><span class="me-2">{{ exp.category.name }}</span> > </label>
    </RowItem>
    <RowItem @click="goListSelect('subcategory')" class="cursor-pointer">
      <label class="content-center">Subcategory</label>
      <label class="content-center pr-2 cursor-pointer"><span class="me-2">{{ exp.subcategory.name }}</span> > </label>
    </RowItem>
    <RowItem>
      <label class="content-center">Amount</label>
      <!--      <div>-->
      <input type="number" placeholder="0.00" step="0.01" v-model="exp.amount" class="w-full text-center ms-4">
      <!--      </div>-->
    </RowItem>
    <RowItem @click="goListSelect('currency')" class="cursor-pointer">
      <label class="content-center">Currency</label>
      <label class="content-center pr-2 cursor-pointer"><span class="me-2">{{ exp.currency.name }}</span> > </label>
    </RowItem>
    <!--    <RowItem>-->
    <!--      <label class="content-center">Quantity</label>-->
    <!--    </RowItem>-->

    <RowItem>
      <div class="text-left w-full content-center">
        <div>Note</div>
        <textarea class="w-full" placeholder="Enter text" v-model="exp.note">
        </textarea>
      </div>
    </RowItem>

    <button class="bg-amber-500	" @click.prevent="save">Save and continue</button>
  </div>

</template>

<script setup lang="ts">
import {onMounted, ref} from "vue";
import {onBeforeRouteLeave, useRoute, useRouter} from "vue-router";
import Cache from "@/utils/cache";
import {type Expense, createExpense, getOptions, getAccounts} from "@/api";

import RowItem from "../components/Row.vue"


const expNew = {
  date: new Date,
  account: {id: 0, name: ''},
  category: {id: 0, name: ''},
  subcategory: {id: 0, name: ''},
  amount: 0,
  currency: {id: 0, name: ''},
  qty: 1,
  note: ''
}
const exp = ref<Expense>(expNew)
// console.log(d.value)

const router = useRouter()
const route = useRoute()

function back() {
  router.back()
}

function goListSelect(type: string) {
  if ('subcategory' == type) {
    router.push({name: 'list-select', params: {type}, query: {'parent': exp.value.category.id}})
    return
  }
  router.push({name: 'list-select', params: {type}})
}

async function save() {
  // const result = (await createExpense(exp.value)).data
  // console.log(result)
  // console.log(exp.value.date)
  await createExpense(exp.value)

  router.back()
  // console.log(toZonedTime(exp.value.date, "Asia/Bangkok").toTimeString()) //Australia/Adelaide
}

onBeforeRouteLeave((to, from) => {
  // console.log(from.result)
  // console.log(from.path + '->' + (to.name as string))
  // console.log()

  if (to.name?.toString() === 'list-select') {
    // console.log("===== save cache")
    Cache.save("expnew", exp.value)
  } else {
    Cache.remove("expnew")
  }
})

onMounted(() => {
  // console.log("meta")
  // console.log(route.meta.result)
  // console.log("meta")
  const selectResult = route.meta.result
  const expCache = Cache.get("expnew") || {}
  // if (!expCache) {
  // exp.value[selectResult.type] = selectResult.name;
  if (selectResult && selectResult.id !== 0) {
    expCache[selectResult.type] = selectResult
  }
  // }
  // console.log("restore from cache")
  // console.log(expCache)
  exp.value = {...exp.value, ...expCache}
})
</script>

<style>
.dp__main {
  width: auto;
}

.dp__input {
  border: none !important;
}
</style>