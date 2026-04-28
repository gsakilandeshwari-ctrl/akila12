# TODO - Fix & Update EquiMind AI

## Issues Found
1. `public/app.js` is heavily corrupted with duplicated, broken code
2. WhatsApp popup only works for Banking, needs to work for HR and Healthcare too
3. "Open with WhatsApp" real WhatsApp Web link missing from notifications
4. Some features may not be running due to broken JS

## Plan
1. **Rewrite `public/app.js`** completely with clean, working code
   - All existing features preserved
   - WhatsApp popup auto-shows after analysis for ALL 3 industries
   - Add `openRealWhatsApp()` function for real WhatsApp Web links
   - Add "Open in WhatsApp" buttons to notification banners
   - Fix all broken functions

2. **Update `public/index.html`** if needed for new WhatsApp buttons

3. **Update `public/style.css`** for new WhatsApp action buttons

4. **Restart server** and test

5. **Provide preview link**

## Implementation Steps
- [ ] Rewrite app.js with clean code
- [ ] Add openRealWhatsApp() function
- [ ] Add WhatsApp popup triggers for HR and Healthcare
- [ ] Add "Open WhatsApp" buttons in HTML
- [ ] Restart server
- [ ] Test preview
