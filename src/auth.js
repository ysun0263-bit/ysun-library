import { ref } from 'vue'

const storageKey = 'ysun-library-authenticated'

const readStoredAuth = () => {
  if (typeof window === 'undefined') return false

  return window.localStorage.getItem(storageKey) === 'true'
}

export const isAuthenticated = ref(readStoredAuth())

export const login = () => {
  isAuthenticated.value = true

  if (typeof window !== 'undefined') {
    window.localStorage.setItem(storageKey, 'true')
  }
}

export const logout = () => {
  isAuthenticated.value = false

  if (typeof window !== 'undefined') {
    window.localStorage.removeItem(storageKey)
  }
}
