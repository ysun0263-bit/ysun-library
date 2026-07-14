# FIT5032 Assessed Lab 5 Submission Checklist

Student Name: Yilian Sun  
Student Email: ysun0263@student.monash.edu

## Submission PDF Order

Use the following order when assembling the final Moodle PDF:

1. Cover page: FIT5032 Assessed Lab 5, Yilian Sun, ysun0263@student.monash.edu.
2. Task 5.1 - Password Confirmation Validation.
3. Task 5.1 - Vue DevTools.
4. Task 5.2 - `src/router/index.js`.
5. Task 5.2 - `src/App.vue`.
6. Task 5.2 - `src/views/HomeView.vue`.
7. Screenshot of Home page on localhost.
8. Screenshot of About page on localhost.
9. Custom routing screenshots:
   - Unauthenticated About redirect.
   - Login page with access denied message.
   - Authenticated About page.
   - Logout result.
   - Access Denied page.

## Generated Screenshots

The following real browser screenshots were generated in `submission/screenshots/`:

- `01-password-mismatch.png`
- `03-home-page.png`
- `04-about-page.png`
- `05-unauthenticated-about-redirect.png`
- `06-login-page.png`
- `07-authenticated-about.png`
- `08-logout.png`
- `09-access-denied.png`

## Manual Screenshot Still Required

`02-vue-devtools.png` still needs to be captured manually because the in-app browser could not open a populated Vue DevTools panel. Do not use the blank attempted DevTools image.

Manual steps:

1. Run `npm run dev`.
2. Open `http://127.0.0.1:5173/` in Chrome.
3. Open Chrome Developer Tools.
4. Open the Vue tab.
5. Select or expand `HomeView`.
6. Expand `formData`.
7. Make sure `username`, `password`, `confirmPassword`, `gender`, `resident`, `reason`, and `suburb` are visible.
8. Capture the browser form and Vue DevTools Components panel as `submission/screenshots/02-vue-devtools.png`.

## Final PDF Status

The final PDF was not generated automatically because the required Vue DevTools screenshot is incomplete. After capturing `02-vue-devtools.png`, assemble the PDF using the order above.
