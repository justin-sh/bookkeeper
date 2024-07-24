<template>
  <header class="p-2 sticky top-0 bg-stone-200 relative">
    <h1 class="text-center font-bold inline-block">Bookkeeper Login </h1>
  </header>

  <div class="flex flex-row justify-center">
    <form @submit.prevent="submit" class="w-auto">
      <div class="flex flex-row mt-3 items-center">
        <div class="w-1/3">
          <label for="email" class="">Username:</label>
        </div>
        <div class="w-2/3">
          <input name="email" id="email"
                 class="w-full rounded-md border-0 py-1.5 pl-3 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                 v-model="form.name"/>
        </div>
      </div>
      <div class="flex flex-row mt-3 items-center">
        <div class="w-1/3">
          <label for="password" class="">Password:</label>
        </div>
        <div class="w-2/3">
          <input type="password" id="password" name="password"
                 class="w-full rounded-md border-0 py-1.5 pl-3 pr-5 text-gray-900 ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                 v-model="form.passwd"/>
        </div>
      </div>
      <div class="flex flex-row justify-center mt-3 text-center bg-red-300">
        <p v-if="error" id="error" class="font-bold text-black">Username or Password is incorrect</p>
      </div>
      <div class="flex flex-row justify-center mt-3">
        <div class="">
          <button type="submit"
                  class="flex w-full justify-center rounded-md bg-blue-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            Submit
          </button>

          <RouterLink to="/register" class="inline-block">
            <span class="block">Register</span>
          </RouterLink>
        </div>
      </div>
    </form>
  </div>
</template>

<script lang="ts" setup>

import {useUserStore} from "@/stores/user";
import {type LoginForm} from "@/api";
import {reactive, ref} from "vue";

const error = ref(false)

const user = useUserStore()

const form: LoginForm = reactive({name: '', passwd: '', showError:false})

const submit = async () => {
  error.value = false
  // console.log(JSON.stringify(form))
  const succeed = await user.login(form)

  if (succeed) {
    location.href = '/'
  }else{
    error.value = true
  }
}

</script>
