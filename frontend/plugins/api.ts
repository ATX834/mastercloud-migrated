// plugins/api.ts
import type { FetchOptions } from 'ofetch';

export default defineNuxtPlugin(() => {
    const config = useRuntimeConfig();

    const baseURL = config.public.apiBaseUrl as string;

    const fetchOptions: FetchOptions = {
        baseURL,
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
        }
    };

    return {
        provide: {
            api: {
                get: <T = any>(url: string, opts: FetchOptions = {}): Promise<T> =>
                    $fetch<T>(url, { ...fetchOptions, ...opts, method: 'GET' }),

                post: <T = any>(url: string, body?: any, opts: FetchOptions = {}): Promise<T> =>
                    $fetch<T>(url, { ...fetchOptions, ...opts, method: 'POST', body }),

                put: <T = any>(url: string, body?: any, opts: FetchOptions = {}): Promise<T> =>
                    $fetch<T>(url, { ...fetchOptions, ...opts, method: 'PUT', body }),

                delete: <T = any>(url: string, opts: FetchOptions = {}): Promise<T> =>
                    $fetch<T>(url, { ...fetchOptions, ...opts, method: 'DELETE' })
            }
        }
    };
});