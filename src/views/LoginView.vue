<template>
  <div class="row">
    <div class="col-12 col-md-8 col-lg-5 offset-md-2 offset-lg-3">
      <div class="card border-0 shadow-sm">
        <div class="card-body p-4">
          <h1 class="h3 mb-3">Login</h1>

          <div v-if="route.query.denied === '1'" class="alert alert-warning">
            Access denied. Please log in to continue.
          </div>

          <p class="text-muted">
            Demo credentials: <strong>student / fit5032</strong>. This is for
            Lab demonstration only and must not be used in production.
          </p>

          <form @submit.prevent="submitLogin" novalidate>
            <div class="mb-3">
              <label for="login-username" class="form-label">Username</label>
              <input
                id="login-username"
                type="text"
                class="form-control"
                :class="{ 'is-invalid': errors.username }"
                v-model="credentials.username"
                @input="errors.username = null"
              />
              <div v-if="errors.username" class="text-danger mt-1">
                {{ errors.username }}
              </div>
            </div>

            <div class="mb-3">
              <label for="login-password" class="form-label">Password</label>
              <input
                id="login-password"
                type="password"
                class="form-control"
                :class="{ 'is-invalid': errors.password }"
                v-model="credentials.password"
                @input="errors.password = null"
              />
              <div v-if="errors.password" class="text-danger mt-1">
                {{ errors.password }}
              </div>
            </div>

            <div v-if="loginError" class="text-danger mb-3">
              {{ loginError }}
            </div>

            <button type="submit" class="btn btn-primary w-100">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { login } from '../auth'

const route = useRoute()
const router = useRouter()

const credentials = reactive({
  username: '',
  password: ''
})

const errors = reactive({
  username: null,
  password: null
})

const loginError = ref('')

const validateLoginForm = () => {
  errors.username = credentials.username.trim() ? null : 'Username is required.'
  errors.password = credentials.password ? null : 'Password is required.'

  return !errors.username && !errors.password
}

const submitLogin = () => {
  loginError.value = ''

  if (!validateLoginForm()) return

  if (credentials.username.trim() !== 'student' || credentials.password !== 'fit5032') {
    loginError.value = 'Invalid username or password.'
    return
  }

  login()
  router.push(route.query.redirect?.toString() || '/about')
}
</script>
