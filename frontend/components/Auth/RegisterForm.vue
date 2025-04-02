<template>
  <div class="max-w-lg w-full bg-gray-900 bg-opacity-85 backdrop-blur-lg rounded-xl p-10 shadow-2xl border border-gray-700/50">
    <h2 class="text-4xl font-bold text-white mb-8 text-center">Inscription</h2>
    
    <!-- Affichage des erreurs -->
    <div v-if="errorMessage" class="bg-red-900 border border-red-700 text-red-100 px-4 py-3 rounded relative mb-4" role="alert">
      <strong class="font-bold">Erreur!</strong>
      <span class="block sm:inline"> {{ errorMessage }}</span>
    </div>
    <!-- Affichage succès -->
    <div v-if="successMessage" class="bg-green-900 border border-green-700 text-green-100 px-4 py-3 rounded relative mb-4" role="alert">
      <strong class="font-bold">Succès!</strong>
      <span class="block sm:inline"> {{ successMessage }}</span>
    </div>

    <form @submit.prevent="handleRegister" class="space-y-5">
      <div>
        <label for="username" class="block text-sm font-semibold text-gray-300 mb-2">Nom d'utilisateur</label>
        <input 
          id="username"
          v-model="username"
          type="text" 
          class="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
          placeholder="Choisissez un nom d'utilisateur"
          required
        >
      </div>

      <div>
        <label for="email" class="block text-sm font-semibold text-gray-300 mb-2">Email</label>
        <input 
          id="email"
          v-model="email"
          type="email" 
          class="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
          placeholder="votre@email.com"
          required
        >
      </div>

      <div>
        <label for="password" class="block text-sm font-semibold text-gray-300 mb-2">Mot de passe</label>
        <input 
          id="password"
          v-model="password"
          type="password" 
          class="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
          placeholder="••••••••"
          required
        >
      </div>

      <div>
        <label for="confirmPassword" class="block text-sm font-semibold text-gray-300 mb-2">Confirmer le mot de passe</label>
        <input 
          id="confirmPassword"
          v-model="confirmPassword"
          type="password" 
          class="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
          placeholder="••••••••"
          required
        >
      </div>

      <div class="flex items-center pt-1">
        <input 
          id="acceptTerms"
          type="checkbox" 
          v-model="acceptTerms"
          class="rounded border-gray-600 text-blue-500 focus:ring-blue-500 focus:ring-offset-gray-900"
          required
        >
        <label for="acceptTerms" class="ml-2 text-sm text-gray-300">
          J'accepte les <a href="#" class="font-medium text-blue-400 hover:text-blue-300 transition-colors">conditions d&#39;utilisation</a>
        </label>
      </div>

      <button 
        type="submit"
        :disabled="isLoading"
        class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg transition-colors font-semibold text-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-900 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {{ isLoading ? 'Inscription...' : 'S\'inscrire' }}
      </button>
    </form>

    <!-- Séparateur -->
    <div class="my-8 flex items-center">
      <div class="flex-grow border-t border-gray-700"></div>
      <span class="mx-4 text-gray-400 text-sm font-medium">Ou s'inscrire avec</span>
      <div class="flex-grow border-t border-gray-700"></div>
    </div>

    <!-- Bouton OAuth -->
    <div class="text-center">
      <button @click="handleGoogleLogin" class="w-full flex items-center justify-center py-3 px-4 bg-gray-800 hover:bg-gray-700 rounded-lg transition-colors border border-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:ring-offset-2 focus:ring-offset-gray-900">
        <svg class="w-5 h-5 mr-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"/><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"/><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"/><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.574l6.19,5.238C39.71,35.981,44,30.607,44,24C44,22.659,43.862,21.35,43.611,20.083z"/></svg>
        <span class="text-white font-medium">S'inscrire avec Google</span>
      </button>
    </div>

    <div class="mt-8 text-center">
      <p class="text-gray-400">
        Déjà un compte ? 
        <NuxtLink to="/login" class="font-semibold text-blue-400 hover:text-blue-300 transition-colors">
          Se connecter
        </NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const username = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const acceptTerms = ref(false)
const isLoading = ref(false)
const errorMessage = ref<string | null>(null)
const successMessage = ref<string | null>(null)

const emit = defineEmits(['registerSuccess'])
const router = useRouter()

const config = useRuntimeConfig()
// Assurez-vous que cette variable est définie dans votre config Nuxt (public runtime config)
const apiUrlBase = config.public.apiUrl ? `${config.public.apiUrl}/auth` : 'http://localhost:8000/api/v1/auth';

// --- Inscription Locale --- 
const handleRegister = async () => {
  errorMessage.value = null // Réinitialiser les messages
  successMessage.value = null
  isLoading.value = true

  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Les mots de passe ne correspondent pas.'
    isLoading.value = false
    return
  }
  if (!acceptTerms.value) {
    errorMessage.value = 'Vous devez accepter les conditions d\'utilisation.'
    isLoading.value = false
    return
  }

  try {
    const response = await $fetch(`${apiUrlBase}/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: {
        username: username.value,
        email: email.value,
        password: password.value
      }
    })

    // Si $fetch réussit (pas d'erreur 4xx/5xx), l'inscription est ok
    successMessage.value = 'Inscription réussie ! Vous allez être redirigé...'
    console.log('Register success:', response)
    emit('registerSuccess') // Émettre l'événement pour la page parente

    // Optionnel: rediriger vers le login ou le tableau de bord après un délai
    setTimeout(() => {
      router.push('/login') // Ou une autre page après succès
    }, 2000)

  } catch (error: any) {
    console.error('Erreur inscription:', error);
    let detail = 'Une erreur inconnue est survenue.';
    if (error.response && error.response._data && error.response._data.detail) {
        // Erreur venant de $fetch avec détail FastAPI
        detail = error.response._data.detail;
    } else if (error.data && error.data.detail) {
        // Autre structure d'erreur potentielle
        detail = error.data.detail;
    } else if (error.message) {
        // Erreur JavaScript générique
        detail = error.message;
    }
    errorMessage.value = `Échec de l'inscription: ${detail}`;
  } finally {
    isLoading.value = false
  }
}

// --- Connexion Google --- 
const handleGoogleLogin = () => {
  errorMessage.value = null // Réinitialiser les messages
  successMessage.value = null
  // Rediriger vers l'endpoint de login Google du backend
  window.location.href = `${apiUrlBase}/google/login`;
}
</script> 