// middleware/auth.global.ts
import { defineNuxtRouteMiddleware, navigateTo, useState } from '#imports';

export default defineNuxtRouteMiddleware((to, from) => {
  const authToken = useState<string | null>('authToken');
  const isAuthRequired = to.meta.auth;

  if (isAuthRequired && !authToken.value) {
    console.log('Middleware: Route requires auth and user is not authenticated.');
    return navigateTo(`/login?redirect=${encodeURIComponent(to.fullPath)}`, { replace: true });
  }

  // Si l'utilisateur est authentifié et essaie d'accéder à une page OÙ l'authentification N'EST PAS requise
  if (authToken.value && !isAuthRequired && to.path !== '/auth/callback') {
    console.log('Middleware: Authenticated user accessing a non-protected guest route (excluding callback), redirecting to /playlists.');
    return navigateTo('/playlists', { replace: true });
  }
});