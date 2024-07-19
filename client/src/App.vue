<script setup lang="ts">
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

</script>

<template>
<!--  <header class="m-4">-->
<!--    <h1 class="text-center font-bold">Bookkeeper {{ title ? '- ' + title : '' }}</h1>-->
<!--  </header>-->

  <main>
    <RouterView/>
  </main>
</template>
