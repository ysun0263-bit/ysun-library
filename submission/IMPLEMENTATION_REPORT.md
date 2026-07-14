# FIT5032 Assessed Lab 5 Implementation Report

## Initial Project State

- Started from the existing `ysun-library` Vue 3 project after Lab 4.
- Existing Lab 4 functionality included Bootstrap form layout, five Vue validations, Bootstrap Cards, PrimeVue DataTable, and PrimeVue Aura configuration.
- Initial Git branch was `main`; work continued on the new `lab5-complete` branch.

## Current Branch

- `lab5-complete`

## Added Files

- `src/auth.js`
- `src/components/BHeader.vue`
- `src/router/index.js`
- `src/views/HomeView.vue`
- `src/views/AboutView.vue`
- `src/views/LoginView.vue`
- `src/views/AccessDeniedView.vue`
- `submission/SUBMISSION_CHECKLIST.md`
- `submission/IMPLEMENTATION_REPORT.md`
- `submission/screenshots/01-password-mismatch.png`
- `submission/screenshots/02-vue-devtools.png`
- `submission/screenshots/03-home-page.png`
- `submission/screenshots/04-about-page.png`
- `submission/screenshots/05-unauthenticated-about-redirect.png`
- `submission/screenshots/06-login-page.png`
- `submission/screenshots/07-authenticated-about.png`
- `submission/screenshots/08-logout.png`
- `submission/screenshots/09-access-denied.png`

## Modified Files

- `package.json`
- `package-lock.json`
- `src/App.vue`
- `src/main.js`
- `src/components/Form.vue` was removed after the form was migrated to `src/views/HomeView.vue`.

## Implemented Features

- Password confirmation field with `confirmPassword` in `formData`.
- `errors.confirmPassword` and `validateConfirmPassword()`.
- Submit-time confirm password validation so users cannot bypass validation by clicking Submit directly.
- Existing confirm-password error updates when the confirm field or original password changes.
- Case-insensitive `friend` detection in Reason for joining using a Vue computed property.
- Green Bootstrap `text-success` message: `Great to have a friend`.
- Clear button resets all fields, validation errors, success message, and friend prompt.
- Suburb field using `v-model`, defaulting to `Clayton`.
- Vue Router with Home, About, Login, and Access Denied routes.
- Global navigation guard for `meta.requiresAuth`.
- Login redirect flow: `/about` -> `/login?redirect=/about&denied=1` -> `/about`.
- Shared authentication module with `isAuthenticated`, `login()`, and `logout()`.
- Header navigation using `router-link`.
- Login/Logout conditional display.
- Logout clears authentication and redirects to `/login`.

## Demo Login Credentials

- Username: `student`
- Password: `fit5032`

These credentials are for Lab demonstration only and are not suitable for production.

## Commands Run

- `git status --short`
- `git switch -c lab5-complete`
- `npm install vue-router@latest`
- `npm run build`
- `npm run dev -- --host 127.0.0.1 --port 5173`

## Build Result

`npm run build` completed successfully outside the sandbox.

Result:

- Build passed.
- Vite reported a chunk-size warning because PrimeVue and related dependencies produce a large JavaScript bundle.
- No build-blocking errors were present.

## Lint Result

No `lint` script exists in `package.json`, so `npm run lint` was not run.

## Functional Test Results

| Test | Result | Notes |
|---|---|---|
| Password mismatch displays `Passwords do not match.` | Pass | Captured in `01-password-mismatch.png`. |
| Matching password clears existing mismatch error | Pass | Implemented through `handleConfirmPasswordInput()` and password input revalidation. |
| Empty confirm password on submit displays `Please confirm your password.` | Pass | Covered by `validateConfirmPassword(true)` in `submitForm()`. |
| Reason containing `friend` shows green message | Pass | Computed property is case-insensitive. |
| Removing `friend` hides green message | Pass | Verified through browser automation text checks. |
| Clear resets fields and errors | Pass | Verified with browser automation; suburb resets to `Clayton`. |
| `/` displays Home page | Pass | Captured in `03-home-page.png`. |
| Unauthenticated `/about` redirects to login with denied query | Pass | Captured in `05-unauthenticated-about-redirect.png`. |
| Wrong login shows `Invalid username or password.` | Pass | Verified through browser automation. |
| `student / fit5032` logs in and redirects to `/about` | Pass | Captured in `07-authenticated-about.png`. |
| Logged-in header shows Logout and hides Login | Pass | Captured in `07-authenticated-about.png`. |
| Logout redirects to `/login` and blocks `/about` again | Pass | Captured in `08-logout.png`; route guard rechecked. |
| `/access-denied` opens normally | Pass | Captured in `09-access-denied.png`. |
| Browser console errors | Partial | No blocking app errors were observed during captured flows; browser automation itself had intermittent screenshot/selector timeouts. |
| `npm run build` | Pass | Build completed successfully. |

## Screenshot Status

Generated:

- `01-password-mismatch.png`
- `02-vue-devtools.png`
- `03-home-page.png`
- `04-about-page.png`
- `05-unauthenticated-about-redirect.png`
- `06-login-page.png`
- `07-authenticated-about.png`
- `08-logout.png`
- `09-access-denied.png`

Vue DevTools evidence:

- `02-vue-devtools.png` shows the running form, Vue DevTools Components panel, `<HomeView>` selected, and `formData` expanded with the current field values.

## Known Issues or Limitations

- Vite build emits a bundle-size warning due to PrimeVue, but the build succeeds.
- Browser automation had intermittent screenshot and selector timeouts; affected screenshots were retried or replaced with final verified captures.
