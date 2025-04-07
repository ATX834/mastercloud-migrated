<template>
  <div class="min-h-screen relative">
      <div class="fixed inset-0 z-0">
      <div class="absolute inset-0 bg-black"></div>
    </div>

    <!-- Navbar fixe -->
    <nav class="fixed top-0 left-0 right-0 z-50 bg-black bg-opacity-90 backdrop-blur-md border-b border-gray-800">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center h-20">
          <!-- Logo -->
          <NuxtLink to="/" class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-r from-blue-400 to-purple-500 rounded-lg"></div>
            <span class="text-white text-2xl font-bold">MasterCloud Remaster</span>
          </NuxtLink>

          <!-- Menu utilisateur -->
          <div class="flex items-center space-x-4">
            <UserMenu v-if="isLoggedIn" />
            <template v-else>
              <NuxtLink to="/login" class="text-gray-300 hover:text-white transition-colors font-medium">
                Connexion
              </NuxtLink>
              <NuxtLink to="/register"
                class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors font-medium">
                Inscription
              </NuxtLink>
            </template>

            <!-- Menu mobile -->
            <button class="md:hidden text-white">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>

    <!-- Contenu principal -->
    <div class="relative z-10 pt-20">
      <main class="container mx-auto px-4 py-8">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/store/user'
import UserMenu from '~/components/UserMenu.vue'
import { storeToRefs } from 'pinia'

const store = useUserStore()
const { isLoggedIn } = storeToRefs(store)


</script>

<style>
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.1);
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.3);
}
</style>