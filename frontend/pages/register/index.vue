<template>
  <div class="flex justify-center items-center min-h-[calc(100vh-5rem)]">
    <AuthRegisterForm @registerSuccess="handleRegisterSuccess" />
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default'
})

const handleRegisterSuccess = () => {
  // Rediriger après l'inscription réussie (à implémenter)
  console.log('Register success, redirecting...')
}
</script> 