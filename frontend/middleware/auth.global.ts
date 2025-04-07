import { defineNuxtRouteMiddleware, navigateTo } from '#imports';
import { useUserStore } from '~/store/user';

export default defineNuxtRouteMiddleware(async (to, _from) => {
  const store = useUserStore();

  const {isLoggedIn} = storeToRefs(store);
  if (!to.meta.auth) return;

  if (isLoggedIn.value) return;

  await store.fetchUserProfile();

  if (!isLoggedIn.value) {
    return navigateTo(`/login?redirect=${encodeURIComponent(to.fullPath)}`, { replace: true });
  }
});