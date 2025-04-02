<template>
  <div class="text-white">
    <h1 class="text-4xl font-bold mb-8 text-center">Mon Compte</h1>

    <div class="max-w-2xl mx-auto">
      <!-- Photo de profil -->
      <div class="text-center mb-8">
        <div class="w-32 h-32 bg-gray-700 rounded-full mx-auto mb-4"></div>
        <button class="text-blue-400 hover:text-blue-300 transition-colors">
          Changer la photo
        </button>
      </div>

      <!-- Formulaire -->
      <div class="bg-gray-800 bg-opacity-50 backdrop-blur-sm rounded-lg p-6 space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Nom d'utilisateur</label>
          <input 
            type="text" 
            class="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500"
            placeholder="Votre nom d'utilisateur"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Email</label>
          <input 
            type="email" 
            class="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500"
            placeholder="votre@email.com"
          >
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-300 mb-2">Mot de passe</label>
          <input 
            type="password" 
            class="w-full bg-gray-700 border border-gray-600 rounded-lg px-4 py-2 text-white focus:outline-none focus:border-blue-500"
            placeholder="••••••••"
          >
        </div>

        <button class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg transition-colors">
          Sauvegarder les modifications
        </button>
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