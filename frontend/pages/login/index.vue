<template>
  <div class="flex justify-center items-center min-h-[calc(100vh-5rem)]">
    <AuthLoginForm @loginSuccess="handleLoginSuccess" />
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default'
})

const handleLoginSuccess = () => {
  console.log('Login success, redirecting...')
}
</script> 