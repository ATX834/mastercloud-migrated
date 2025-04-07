import { defineStore } from 'pinia';
import { useNuxtApp } from '#app';
import { ref, computed } from 'vue';

interface UserProfile {
    id: number;
    email: string;
}

export const useUserStore = defineStore('user', () => {
    const userProfile = ref<UserProfile | null>(null)
    const isLoggedIn = computed(() => !!userProfile.value)


    async function fetchUserProfile() {
        if (userProfile.value) return;
        const { $api } = useNuxtApp();
        try {
            const response = await $api.get('/auth/me');
            userProfile.value = response.user;
        } catch (error) {
            console.error('Error fetching user profile:', error);
            userProfile.value = null;
        }
    }

    async function logout() {
        userProfile.value = null;
        const { $api } = useNuxtApp();
        await $api.get('/auth/logout');
        navigateTo('/login');
    }

    return {
        userProfile,
        isLoggedIn,
        fetchUserProfile,
        logout
    };
});