<script setup lang="ts">
import {onMounted} from "vue"
import {useUserStore} from "@/stores/user";
// import {RouterView} from 'vue-router'
//
// import {useRouter} from "vue-router"
// import {Ref, ref} from "vue";
//
// const router = useRouter()
//
// const title: Ref<string> = ref('')
//
// router.afterEach((to, from) => {
//   title.value = to.meta.title ?? ''
// })


const userStore = useUserStore()

// const userinfo = await getUserInfo()

onMounted(async () => userStore.refresh())

</script>

<template>
  <!--  <header class="m-4">-->
  <!--    <h1 class="text-center font-bold">Bookkeeper {{ title ? '- ' + title : '' }}</h1>-->
  <!--  </header>-->

  <main>
    <RouterView/>
  </main>
</template>
