<template>
  <div class="p-8">
    <h1 class="text-2xl mb-4">Traitement de l'authentification...</h1>
    <p v-if="message">{{ message }}</p>
    <p v-if="error" class="text-red-500">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useState, definePageMeta } from '#imports';

const message = ref('Veuillez patienter...');
const error = ref<string | null>(null);
const authToken = useState<string | null>('authToken'); // Utilise le même état global que LoginForm

const router = useRouter();
const route = useRoute();

onMounted(() => {
  // Essayer de récupérer le token depuis le fragment d'URL (#)
  // ou potentiellement des query params (?) selon comment le backend redirige
  let token = null;
  if (route.hash && route.hash.startsWith('#token=')) {
    token = route.hash.substring(7); // Enlever '#token='
  } else if (route.query.token) {
    token = route.query.token;
  }

  if (token) {
    message.value = 'Authentification réussie ! Redirection...';
    authToken.value = token;
    // Rediriger vers la page principale ou le tableau de bord après un court délai
    setTimeout(() => {
      router.push('/my-playlist'); // Ou la page de destination souhaitée
    }, 1500);
  } else {
    error.value = 'Token non trouvé après redirection. Impossible de finaliser la connexion.';
    message.value = 'Échec de l\'authentification.';
    // Optionnel : rediriger vers la page de login après un délai
     setTimeout(() => {
       router.push('/login');
     }, 3000);
  }
});

definePageMeta({
  layout: 'default' // Ou un autre layout si nécessaire
});
</script> 