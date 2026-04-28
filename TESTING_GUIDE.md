# Client Portal - Testing & Demo Guide

## 🎯 Quick Demo Walkthrough

### Step 1: Launch Application
1. Open terminal in project directory
2. Run: `node server.js`
3. Navigate to: `http://localhost:3000`

### Step 2: Access Client Portal

**From Landing Page:**
1. Click **"Client Portal"** button in top navigation (next to Admin Login)
2. Or click **"Client Portal"** in hero section button area

### Step 3: Login as Client (Demo Mode)

**Option A: Existing Client Login**
- Name: `Ravi Kumar`
- Phone: `+91-98765-43210`
- Type: `Bank Loan Request`
- Click **"Login to Portal →"**

**Option B: New Client Signup**
- Click **"Create one"** link at bottom
- Fill signup form
- Click **"Create Account →"**

### Step 4: Explore Dashboard

#### **Overview Tab (Default)**
✅ What you'll see:
- Welcome message personalized with client name
- Status card showing:
  - 3 Total Requests
  - 1 Approved
  - 1 Pending
  - 1 Rejected
- Approval Messages section with real-time status
- Quick action buttons

#### **My Requests Tab**
✅ What you'll see:
- Table with sample requests:
  - #REQ-2025-001: Bank Loan - ✓ Approved
  - #REQ-2025-002: HR Application - ⏳ Pending
  - #REQ-2025-003: Healthcare - ✗ Rejected
- Each has View button

#### **New Request Tab**
✅ Try submitting a request:

**Bank Loan Request:**
1. Select "Bank Loan Request" from Request Type
2. Fill form:
   - Loan Purpose: "Personal Loan"
   - Loan Amount: "500000"
   - Loan Duration: "60" months
   - Monthly Income: "50000"
   - Credit Score: "750"
   - Employment Type: "Salaried"
3. Click "✓ Submit Request"
4. See success toast: "Request submitted successfully!"
5. Auto-redirect to My Requests page

**HR Application:**
1. Select "HR Application"
2. Fill form:
   - Position: "Software Engineer"
   - Experience: "5" years
   - Salary: "800000"
   - Education: "Master's Degree"
   - Cover Letter: Your text
3. Submit and see confirmation

**Healthcare Request:**
1. Select "Healthcare Request"
2. Fill form:
   - Service: "General Consultation"
   - Age: "30"
   - Blood Type: "O+"
   - Symptoms: Your text
   - Severity: "Low"
3. Submit and see notification

#### **Messages Tab**
✅ Placeholder for admin communication
- Shows "No messages yet"
- Will display admin responses when integrated

#### **FAQ Tab**
✅ Common questions displayed
- Approval timeline
- Request modification
- Rejection handling
- Support info

#### **Contact Us Tab**
✅ Support information
- Phone: +91-1800-EQUIMIND
- Email: support@equimindai.com
- WhatsApp: +91-98765-43210
- Support hours: 9 AM - 6 PM
- Message submission form

## 📋 Testing Checklist

### Authentication
- [ ] Client Portal button visible on landing page
- [ ] Client login modal opens correctly
- [ ] Signup modal opens from login page
- [ ] Can switch between login/signup modes
- [ ] Login with valid data loads dashboard
- [ ] Logout returns to landing page

### Dashboard Overview
- [ ] Client name displays correctly
- [ ] Status card shows correct stats
- [ ] Approval messages display with proper formatting
- [ ] Color coding works (green/amber/red)
- [ ] Quick action buttons navigate correctly
- [ ] Topbar shows current page title

### Navigation
- [ ] Sidebar items highlight when active
- [ ] Can navigate between all pages
- [ ] Active tab shows visual indicator
- [ ] Topbar title updates with page selection
- [ ] All page transitions are smooth

### My Requests Page
- [ ] Table displays sample requests
- [ ] Status pills show correct colors
- [ ] View buttons are clickable
- [ ] All request data is visible

### New Request Form
- [ ] Request type dropdown works
- [ ] Form fields change based on type
- [ ] Bank form shows correct fields
- [ ] HR form shows correct fields
- [ ] Healthcare form shows correct fields
- [ ] Required fields are marked
- [ ] Submit button works
- [ ] Success toast appears
- [ ] Form resets after submission
- [ ] New request appears in My Requests

### Validation
- [ ] Cannot submit without selecting type
- [ ] Cannot submit incomplete forms
- [ ] Error messages appear for missing fields
- [ ] Phone number validation (if implemented)

### UI/UX
- [ ] Colors match design system
- [ ] Responsive on desktop (1920x1080)
- [ ] Responsive on tablet (768px)
- [ ] Responsive on mobile (375px)
- [ ] No layout breaks
- [ ] Smooth animations
- [ ] Buttons have hover effects
- [ ] Icons display correctly

### Notifications
- [ ] Login success toast appears
- [ ] Request submission toast appears
- [ ] Logout toast appears
- [ ] Error toasts on validation failures

### Data Flow
- [ ] Client requests are tracked
- [ ] Request IDs increment correctly
- [ ] Status shows "pending" for new requests
- [ ] Date stamps are accurate
- [ ] Request data persists (until page reload)

## 🚀 Browser Testing

### Recommended Browsers:
- ✅ Google Chrome (Latest)
- ✅ Mozilla Firefox (Latest)
- ✅ Microsoft Edge (Latest)
- ✅ Safari (macOS)

### Test Scenarios:

**Scenario 1: Complete Bank Loan Request**
1. Login as client
2. Navigate to "New Request"
3. Select "Bank Loan Request"
4. Fill all fields with realistic data
5. Submit request
6. Verify in "My Requests" page
7. Check status shows "Pending"

**Scenario 2: HR Application**
1. Submit HR job application
2. Verify correct form appears
3. Submit with valid data
4. Check success message

**Scenario 3: Healthcare Request**
1. Submit healthcare request
2. Verify all health-related fields
3. Submit with emergency severity
4. See confirmation toast

**Scenario 4: Navigation Flow**
1. Login
2. Visit all pages in sidebar
3. Use topbar search placeholder (visual test)
4. Logout and return to landing

**Scenario 5: Mobile Responsiveness**
1. Open in Chrome DevTools mobile view
2. Test tablet view (768px)
3. Test phone view (375px)
4. Verify no layout breaks
5. Check sidebar responsiveness

## 🐛 Known Behaviors

### Current Implementation:
- ✓ Data stored in JavaScript memory (CLIENT object)
- ✓ Data resets on page refresh
- ✓ No backend persistence (to be added)
- ✓ Mock approval messages shown
- ✓ Sample request history included
- ✓ Real-time notifications via toast
- ✓ Form validation on submit

### Future Enhancements:
- [ ] Database integration
- [ ] Real authentication with OTP
- [ ] Admin approval workflow
- [ ] WhatsApp notifications
- [ ] Email notifications
- [ ] Document upload
- [ ] File attachment support
- [ ] Request amendments
- [ ] Payment gateway
- [ ] Chat system with admin

## 📊 Sample Test Data

**Login Credentials (Demo):**
```
Name: Ravi Kumar
Phone: +91-98765-43210
Type: Bank Loan Request
```

**Signup Test:**
```
Name: [Any name]
Phone: [Any phone number]
Type: [Select any]
```

**Bank Loan Test:**
```
Loan Purpose: Personal Loan
Amount: ₹5,00,000
Duration: 60 months
Income: ₹50,000
Credit Score: 750
Employment: Salaried
```

**HR Application Test:**
```
Position: Software Engineer
Experience: 5 years
Salary: ₹8,00,000
Education: Master's Degree
Cover Letter: [Any text]
```

**Healthcare Test:**
```
Service: General Consultation
Age: 30
Blood Type: O+
Symptoms: [Any text]
Severity: Medium
```

## ✅ Quality Assurance Checklist

- [ ] All forms validate properly
- [ ] Success/error messages appear
- [ ] Navigation is intuitive
- [ ] Design is consistent
- [ ] Mobile is responsive
- [ ] Performance is good
- [ ] No console errors
- [ ] All buttons functional
- [ ] All links working
- [ ] Logout works properly

---

## Need Help?

For issues or questions:
1. Check browser console (F12 → Console tab)
2. Look for error messages in toast notifications
3. Verify all required fields are filled
4. Try clearing browser cache and reloading
5. Test in different browser for compatibility

**Happy testing! 🎉**
