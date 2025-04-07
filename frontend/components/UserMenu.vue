<template>
  <div class="relative">
    <button 
      @click="isOpen = !isOpen"
      class="flex items-center space-x-3 text-white hover:text-gray-300 transition-colors"
    >
      <div class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center">
        {{ userInitials }}
      </div>
      <span class="hidden md:block">{{ username }}</span>
      <svg 
        class="w-4 h-4" 
        :class="{ 'transform rotate-180': isOpen }"
        fill="none" 
        stroke="currentColor" 
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <div 
      v-if="isOpen"
      class="absolute right-0 mt-2 w-48 bg-gray-900 bg-opacity-95 backdrop-blur-sm rounded-lg shadow-xl py-2 z-50"
    >
      <NuxtLink 
        to="/profile" 
        class="block px-4 py-2 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors"
        @click="isOpen = false"
      >
        Mon Profil
      </NuxtLink>
      <NuxtLink 
        to="/playlists" 
        class="block px-4 py-2 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors"
        @click="isOpen = false"
      >
        Ma Playlist
      </NuxtLink>
      <button 
        @click="handleLogout"
        class="w-full text-left px-4 py-2 text-red-400 hover:bg-gray-800 hover:text-red-300 transition-colors"
      >
        Se déconnecter
      </button>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '~/store/user'
const isOpen = ref(false)

const store = useUserStore()
const { logout } = store

const username = ref('John Doe')
const userInitials = computed(() => {
  return username.value
    .split(' ')
    .map(n => n[0])
    .join('')
    .toUpperCase()
})

async function handleLogout() {
  isOpen.value = false
  await logout()
}
</script> 