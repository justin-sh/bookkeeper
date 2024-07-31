<template>

  <header class="p-2 sticky top-0 bg-stone-200 relative z-50">
    <h1 class="text-center font-bold inline-block">Bookkeeper Expenses </h1>
    <button class="button font-bold text-2xl absolute right-5" @click.stop="addNew()"> +</button>
  </header>

  <div v-for="k in data.keys()" class="p-2 divide-y">
    <div class="flex flex-row justify-between w-full">
      <div class="text-left">
        <font-awesome-icon icon="fa-solid fa-angle-up" size="xs"/>
        {{ k }}
      </div>
      <div class="text-right">${{ data.get(k).totalAmt }}</div>
    </div>
    <div v-for="d in data.get(k).details" v-bind:key="d.id" class="bg-white">
      <div class="flex flex-row  justify-between">
        <span class="text-left">{{ accounts[d.account_id] }}</span>
        <span class="text-right">${{ d.amount }}</span>
      </div>
      <div class="flex flex-row">
        <span class="w-4/5 text-left">{{ op_items[d.cat_id] }}
          {{ (d.subcat_id ? '/' + op_items[d.subcat_id] : '') }}
        </span>
        <span class="w-1/5 text-right">{{  }}</span>
      </div>
      <div class="flex justify-start">
        {{ d.note || '&nbsp;' }}
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import {onMounted, ref} from "vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useRouter} from "vue-router";
import {getAccounts, getAllOptions, getExpenses} from "@/api";
import {formatInTimeZone} from "date-fns-tz";

const router = useRouter()

const localTZ = Intl.DateTimeFormat().resolvedOptions().timeZone

const data = ref<Map<string, any>>(new Map<string, any>())

let accounts = {}
let op_items = {}

function addNew() {
  router.push("/expenses/new")
}

onMounted(async () => {
  (await getAccounts()).data.forEach(x => accounts[x.id] = x.name);
  (await getAllOptions()).data.forEach(x => op_items[x.id] = x.name);

  const result = (await getExpenses()).data

  result.forEach(d => {
    const key = formatInTimeZone(d.date, localTZ, "yyyy/MM/dd") as string

    if (data.value.has(key)) {
      const s = data.value.get(key)
      s.totalAmt += d.amount
      s.details.push(d)
    } else {
      data.value.set(key, {totalAmt: d.amount, 'details': [d]})
    }
  })
})

</script>
