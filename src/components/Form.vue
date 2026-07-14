<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-12 col-md-8 offset-md-2">
        <h1 class="text-center mb-4">User Information Form</h1>

        <form @submit.prevent="submitForm" novalidate>
          <div class="row mb-3">
            <div class="col-12 col-md-6 mb-3 mb-md-0">
              <label for="username" class="form-label">Username</label>
              <input
                type="text"
                class="form-control"
                :class="{ 'is-invalid': errors.username }"
                id="username"
                v-model="formData.username"
                @blur="validateName(true)"
                @input="validateName(false)"
              />
              <div v-if="errors.username" class="text-danger mt-1">
                {{ errors.username }}
              </div>
            </div>

            <div class="col-12 col-md-6">
              <label for="password" class="form-label">Password</label>
              <input
                type="password"
                class="form-control"
                :class="{ 'is-invalid': errors.password }"
                id="password"
                v-model="formData.password"
                @blur="validatePassword(true)"
                @input="validatePassword(false)"
              />
              <div v-if="errors.password" class="text-danger mt-1">
                {{ errors.password }}
              </div>
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-12 col-md-6 mb-3 mb-md-0">
              <label for="resident" class="form-label">
                Australian Resident?
              </label>
              <select
                class="form-select"
                :class="{ 'is-invalid': errors.resident }"
                id="resident"
                v-model="formData.resident"
                @blur="validateResident(true)"
                @change="validateResident(false)"
              >
                <option value="" disabled>Please select</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
              <div v-if="errors.resident" class="text-danger mt-1">
                {{ errors.resident }}
              </div>
            </div>

            <div class="col-12 col-md-6">
              <label for="gender" class="form-label">Gender</label>
              <select
                class="form-select"
                :class="{ 'is-invalid': errors.gender }"
                id="gender"
                v-model="formData.gender"
                @blur="validateGender(true)"
                @change="validateGender(false)"
              >
                <option value="" disabled>Please select</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>
              <div v-if="errors.gender" class="text-danger mt-1">
                {{ errors.gender }}
              </div>
            </div>
          </div>

          <div class="mb-3">
            <label for="reason" class="form-label">Reason for joining</label>
            <textarea
              class="form-control"
              :class="{ 'is-invalid': errors.reason }"
              id="reason"
              rows="3"
              v-model="formData.reason"
              @blur="validateReason(true)"
              @input="validateReason(false)"
            ></textarea>
            <div v-if="errors.reason" class="text-danger mt-1">
              {{ errors.reason }}
            </div>
          </div>

          <div class="text-center">
            <button type="submit" class="btn btn-primary me-2">Submit</button>
            <button type="button" class="btn btn-secondary" @click="clearForm">
              Clear
            </button>
          </div>
        </form>

        <div class="row mt-5" v-if="submittedCards.length">
          <div class="d-flex flex-wrap justify-content-start">
            <div
              v-for="(card, index) in submittedCards"
              :key="index"
              class="card m-2"
              style="width: 18rem;"
            >
              <div class="card-header">User Information</div>

              <ul class="list-group list-group-flush">
                <li class="list-group-item">Username: {{ card.username }}</li>
                <li class="list-group-item">Password: {{ card.password }}</li>
                <li class="list-group-item">
                  Australian Resident: {{ formatResident(card.resident) }}
                </li>
                <li class="list-group-item">Gender: {{ formatGender(card.gender) }}</li>
                <li class="list-group-item">Reason: {{ card.reason }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emptyForm = () => ({
  username: '',
  password: '',
  resident: '',
  reason: '',
  gender: ''
})

const formData = ref(emptyForm())

const errors = ref({
  username: null,
  password: null,
  resident: null,
  gender: null,
  reason: null
})

const submittedCards = ref([])

const formatResident = (value) => (value === 'yes' ? 'Yes' : 'No')

const formatGender = (value) => {
  const labels = {
    male: 'Male',
    female: 'Female',
    other: 'Other'
  }

  return labels[value] || ''
}

const validateName = (blur) => {
  const username = formData.value.username.trim()

  if (!username) {
    if (blur) errors.value.username = 'Username is required'
    return false
  }

  if (username.length < 3) {
    if (blur) errors.value.username = 'Username must be at least 3 characters'
    return false
  }

  errors.value.username = null
  return true
}

const validatePassword = (blur) => {
  const password = formData.value.password
  const hasUppercase = /[A-Z]/.test(password)
  const hasLowercase = /[a-z]/.test(password)
  const hasNumber = /\d/.test(password)
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password)

  if (password.length < 8) {
    if (blur) errors.value.password = 'Password must be at least 8 characters'
    return false
  }

  if (!hasUppercase) {
    if (blur) errors.value.password = 'Password must include an uppercase letter'
    return false
  }

  if (!hasLowercase) {
    if (blur) errors.value.password = 'Password must include a lowercase letter'
    return false
  }

  if (!hasNumber) {
    if (blur) errors.value.password = 'Password must include a number'
    return false
  }

  if (!hasSpecialChar) {
    if (blur) errors.value.password = 'Password must include a special character'
    return false
  }

  errors.value.password = null
  return true
}

const validateResident = (blur) => {
  if (!formData.value.resident) {
    if (blur) errors.value.resident = 'Please choose Yes or No'
    return false
  }

  errors.value.resident = null
  return true
}

const validateGender = (blur) => {
  if (!formData.value.gender) {
    if (blur) errors.value.gender = 'Please select a gender'
    return false
  }

  errors.value.gender = null
  return true
}

const validateReason = (blur) => {
  const reason = formData.value.reason.trim()

  if (!reason) {
    if (blur) errors.value.reason = 'Reason for joining is required'
    return false
  }

  if (reason.length < 10) {
    if (blur) errors.value.reason = 'Reason must be at least 10 characters'
    return false
  }

  if (reason.length > 200) {
    if (blur) errors.value.reason = 'Reason must be 200 characters or fewer'
    return false
  }

  errors.value.reason = null
  return true
}

const validateForm = () => {
  const checks = [
    validateName(true),
    validatePassword(true),
    validateResident(true),
    validateGender(true),
    validateReason(true)
  ]

  return checks.every(Boolean)
}

const submitForm = () => {
  if (!validateForm()) return

  submittedCards.value.push({
    username: formData.value.username.trim(),
    password: formData.value.password,
    resident: formData.value.resident,
    gender: formData.value.gender,
    reason: formData.value.reason.trim()
  })

  clearForm()
}

const clearForm = () => {
  formData.value = emptyForm()
  errors.value = {
    username: null,
    password: null,
    resident: null,
    gender: null,
    reason: null
  }
}
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: #275fda;
  color: white;
  padding: 10px;
  border-radius: 10px 10px 0 0;
}

.list-group-item {
  padding: 10px;
}
</style>
