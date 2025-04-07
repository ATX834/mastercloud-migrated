<template>
  <div class="text-center text-white">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-6xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-500">
        Bienvenue sur MasterCloud Remaster
      </h1>
      <p class="text-2xl mb-8 text-gray-200">Votre plateforme de streaming musical</p>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
        <div class="bg-gray-800 bg-opacity-50 backdrop-blur-sm p-6 rounded-lg border border-gray-700 hover:border-blue-500 transition-colors">
          <h3 class="text-xl font-semibold mb-3">Découvrez</h3>
          <p class="text-gray-300">Découvrez notre vaste collection de musique</p>
        </div>
        
        <div class="bg-gray-800 bg-opacity-50 backdrop-blur-sm p-6 rounded-lg border border-gray-700 hover:border-blue-500 transition-colors">
          <h3 class="text-xl font-semibold mb-3">Créez</h3>
          <p class="text-gray-300">Créez vos propres playlists personnalisées</p>
        </div>
        
        <div class="bg-gray-800 bg-opacity-50 backdrop-blur-sm p-6 rounded-lg border border-gray-700 hover:border-blue-500 transition-colors">
          <h3 class="text-xl font-semibold mb-3">Partagez</h3>
          <p class="text-gray-300">Partagez votre musique avec vos amis</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default'
})
</script> 