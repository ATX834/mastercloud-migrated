<script setup lang="ts">
import { useRoute } from 'vue-router';

const { $api } = useNuxtApp()
onMounted(async () => {
    const route = useRoute();
    const sessionId = route.query.session_id as string;

    await $api.get(`/auth/finalize?session_id=${sessionId}`);
    navigateTo('/profile');
})
</script>
