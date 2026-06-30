<template>
  <main class="container">
    <h1>📚 Working with JSON Arrays</h1>

    <p>
      Our <code>authors.json</code> contains an array of author objects.
      Our <code>bookstores.json</code> contains bookstore information.
    </p>

    <section>
      <h2>Activity 1: Import JSON files</h2>
      <p>
        Imported <code>authors.json</code> and <code>bookstores.json</code>
        into this Vue component.
      </p>
    </section>

    <section>
      <h2>Activity 2: Get Authors Born After 1850</h2>
      <p>Computed property: <code>modernAuthors</code></p>

      <ul>
        <li
          v-for="author in modernAuthors"
          :key="author.id"
          :class="{ highlight: isGeorgeOrwell(author) }"
          :style="getAuthorStyle(author)"
        >
          {{ author.name }} ({{ author.birthYear }})
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 3: Get All Famous Works</h2>
      <p>Computed property: <code>allFamousWorks</code></p>

      <ul>
        <li v-for="work in allFamousWorks" :key="work">
          {{ work }}
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 4: Search Author by Name</h2>
      <p>Search result for George Orwell:</p>

      <div
        v-if="authorByName"
        class="card"
        :class="{ highlight: isGeorgeOrwell(authorByName) }"
        :style="getAuthorStyle(authorByName)"
      >
        {{ authorByName.name }} was born in {{ authorByName.birthYear }}.
      </div>
    </section>

    <section>
      <h2>Activity 5: Search Author by ID</h2>
      <p>Search result for author ID 1:</p>

      <div v-if="authorById" class="card">
        {{ authorById.name }} was born in {{ authorById.birthYear }}.
      </div>
    </section>

    <section>
      <h2>Activity 6: Iterating through Arrays</h2>
      <p>Author names and birth years:</p>

      <ul>
        <li
          v-for="author in authors"
          :key="author.id"
          :class="{ highlight: isGeorgeOrwell(author) }"
          :style="getAuthorStyle(author)"
          :title="`Author ID: ${author.id}`"
        >
          {{ author.name }} ({{ author.birthYear }})
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 7: Filtering Arrays</h2>
      <p>Authors born after 1850:</p>

      <ul>
        <li
          v-for="author in modernAuthors"
          :key="author.id"
          :class="{ highlight: isGeorgeOrwell(author) }"
          :style="getAuthorStyle(author)"
        >
          {{ author.name }} ({{ author.birthYear }})
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 8: Mapping Arrays</h2>
      <p>Famous works:</p>

      <ul>
        <li v-for="work in allFamousWorks" :key="work">
          {{ work }}
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 9: Bookstore Overview</h2>

      <div class="card">
        <p><strong>Name:</strong> {{ bookstores.name }}</p>
        <p><strong>Total stores:</strong> {{ bookstores.totalStores }}</p>
      </div>
    </section>

    <section>
      <h2>Activity 10: Countries</h2>
      <p>Countries in <code>bookstores.json</code>:</p>

      <ul>
        <li v-for="country in bookstoreCountries" :key="country">
          {{ country }}
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 11: Store Types</h2>
      <p>Physical and online store numbers:</p>

      <ul>
        <li v-for="[type, count] in storeTypeEntries" :key="type">
          {{ type }}: {{ count }}
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 12: Top Sellers and Opening Hours</h2>

      <h3>Top Sellers</h3>
      <ul>
        <li
          v-for="book in topSellers"
          :key="book"
          :class="{ bestseller: book === '1984' }"
          :title="`Top seller: ${book}`"
        >
          {{ book }}
        </li>
      </ul>

      <h3>Opening Hours</h3>
      <ul>
        <li v-for="[dayType, hours] in openingHourEntries" :key="dayType">
          {{ dayType }}: {{ hours.open }} - {{ hours.close }}
        </li>
      </ul>
    </section>

    <section>
      <h2>Activity 13: v-if & v-else</h2>
      <p>Toggle visibility based on a condition.</p>

      <button @click="showMessage = !showMessage">
        Toggle Message
      </button>

      <p v-if="showMessage" class="message success">
        ✨ You're a Vue superstar! ✨
      </p>

      <p v-else class="message">
        Click the button to see a message.
      </p>
    </section>
  </main>
</template>

<script setup>
import { computed, ref } from 'vue'
import authors from '../assets/json/authors.json'
import bookstores from '../assets/json/bookstores.json'

const showMessage = ref(false)

const modernAuthors = computed(() =>
  authors.filter((author) => author.birthYear > 1850)
)

const allFamousWorks = computed(() =>
  authors.flatMap((author) =>
    author.famousWorks.map((work) => work.title)
  )
)

const authorByName = computed(() =>
  authors.find((author) => author.name === 'George Orwell')
)

const authorById = computed(() =>
  authors.find((author) => author.id === 1)
)

const bookstoreCountries = computed(() => bookstores.countries ?? [])

const topSellers = computed(() => bookstores.topSellers ?? [])

const storeTypeEntries = computed(() =>
  Object.entries(bookstores.storeTypes ?? {})
)

const openingHourEntries = computed(() =>
  Object.entries(bookstores.openingHours ?? {})
)

const isGeorgeOrwell = (author) => {
  return author.name === 'George Orwell'
}

const getAuthorStyle = (author) => {
  if (author.name === 'George Orwell') {
    return {
      borderLeft: '6px solid #42b883',
      fontWeight: 'bold'
    }
  }

  return {}
}
</script>

<style scoped>
.container {
  max-width: 850px;
  margin: 0 auto;
  padding: 24px;
  font-family: Arial, sans-serif;
}

section {
  margin-top: 32px;
}

ul {
  padding-left: 0;
}

li {
  list-style: none;
  background-color: #f1f1f1;
  margin: 8px 0;
  padding: 14px;
  border-radius: 4px;
}

.card {
  background-color: #f1f1f1;
  margin: 8px 0;
  padding: 14px;
  border-radius: 4px;
}

.highlight {
  background-color: #e8fff3;
  color: #1b5e20;
}

.bestseller {
  background-color: #fff8dc;
  font-weight: bold;
}

.message {
  margin-top: 16px;
  padding: 16px;
  border-radius: 4px;
  background-color: #f1f1f1;
}

.success {
  background-color: #e8fff3;
  border: 1px solid #42b883;
  color: #1b5e20;
}
</style>