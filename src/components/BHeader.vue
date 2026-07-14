<template>
  <header class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
    <div class="container">
      <router-link class="navbar-brand fw-semibold" to="/">
        NoMash Library
      </router-link>

      <nav>
        <ul class="navbar-nav flex-row gap-2 align-items-center">
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/">
              Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/about">
              About
            </router-link>
          </li>
          <li v-if="!isAuthenticated" class="nav-item">
            <router-link class="nav-link" active-class="active" to="/login">
              Login
            </router-link>
          </li>
          <li v-else class="nav-item">
            <button class="btn btn-outline-light btn-sm" @click="handleLogout">
              Logout
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { isAuthenticated, logout } from '../auth'

const router = useRouter()

const handleLogout = () => {
  logout()
  router.push('/login')
}
</script>
