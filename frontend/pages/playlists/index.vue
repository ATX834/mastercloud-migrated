<template>
  <div class="text-white">
    <h1 class="text-4xl font-bold mb-8 text-center">Ma Playlist</h1>

    <!-- En-tête de la playlist -->
    <div class="bg-gray-800 bg-opacity-50 backdrop-blur-sm rounded-lg p-6 mb-8">
      <div class="flex items-center gap-6">
        <div class="w-48 h-48 bg-gray-700 rounded-lg"></div>
        <div>
          <h2 class="text-2xl font-bold mb-2">Ma Playlist Personnelle</h2>
          <p class="text-gray-400">12 titres • 45 minutes</p>
        </div>
      </div>
    </div>

    <!-- Liste des morceaux -->
    <div class="space-y-2">
      <div v-for="i in 5" :key="i" class="bg-gray-800 bg-opacity-50 backdrop-blur-sm rounded-lg p-4 flex items-center gap-4 hover:bg-opacity-70 transition-all">
        <div class="w-12 h-12 bg-gray-700 rounded"></div>
        <div class="flex-grow">
          <h3 class="font-semibold">Titre de la musique {{ i }}</h3>
          <p class="text-gray-400 text-sm">Artiste {{ i }}</p>
        </div>
        <div class="text-gray-400">3:45</div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default',
  auth: true
})
</script> 