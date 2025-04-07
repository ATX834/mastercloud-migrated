<template>
  <div class="text-white px-4 py-12">
    <h1 class="text-4xl font-bold mb-10 text-center">Mon Compte</h1>

    <div class="max-w-xl mx-auto bg-gray-800 rounded-2xl shadow-lg p-8 space-y-6">

      <!-- Infos utilisateur -->
      <div class="space-y-2 text-center">
        <img
          src="https://avatars.githubusercontent.com/u/9919?s=200&v=4"
          alt="Avatar"
          class="w-24 h-24 rounded-full mx-auto shadow"
        />
        <p class="text-xl font-semibold">John Doe</p>
        <p class="text-gray-400">john.doe@example.com</p>
      </div>

      <hr class="border-gray-700">

      <!-- Comptes liés -->
      <div class="space-y-4">
        <p class="text-lg font-medium text-gray-300">Comptes liés</p>

        <button
          class="w-full flex items-center justify-center gap-3 bg-red-600 hover:bg-red-700 py-2 rounded-lg transition-colors font-medium"
        >
          <Icon name="mdi:youtube" class="text-xl" />
          Lier mon compte YouTube
        </button>

        <button
          class="w-full flex items-center justify-center gap-3 bg-green-600 hover:bg-green-700 py-2 rounded-lg transition-colors font-medium"
        >
          <Icon name="mdi:spotify" class="text-xl" />
          Lier mon compte Spotify
        </button>
      </div>

      <hr class="border-gray-700">

      <!-- Déconnexion -->
      <button
        class="w-full text-red-400 hover:text-red-300 text-sm mt-4 underline"
        @click="handleLogout"
      >
        Se déconnecter
      </button>
    </div>
  </div>
</template>

<script setup>
import {useUserStore} from "~/store/user"

definePageMeta({
  layout: 'default',
  auth: true
});

const store = useUserStore()
const { logout } = store;

async function handleLogout() {
  await logout()
  console.log("Déconnexion...")
}
</script>
