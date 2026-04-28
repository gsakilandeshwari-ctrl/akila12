# Client Portal - Admin Integration Guide

## 🔗 Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     EQUIMIND AI PLATFORM                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐      CLIENT REQUESTS FLOW      ┌────────────┐│
│  │              │                                │            ││
│  │  CLIENT      │  1. Submit Bank Request  →     │   BANK     ││
│  │  PORTAL      │  2. Submit HR Request    →     │   ADMIN    ││
│  │              │  3. Submit Healthcare    →     │   PANEL    ││
│  │              │                                │            ││
│  └──────────────┘                                └────────────┘│
│        ↕                                                ↕       │
│   (Phone Login)                            (View & Approve)   │
│                                                                 │
│  Sample Data: CLIENT.requests[]             Admin Workflow:   │
│  - REQ-2025-001 (Bank) ✓                    1. Show requests  │
│  - REQ-2025-002 (HR) ⏳                      2. Review details │
│  - REQ-2025-003 (Health) ✗                  3. Approve/Reject │
│                                             4. Send notification
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 🎯 Client Request Data Structure

### What Clients Submit:

```javascript
{
  id: "REQ-2025-001",
  type: "bank",  // 'bank' | 'hr' | 'healthcare'
  status: "pending",  // 'pending' | 'approved' | 'rejected'
  date: "Apr 27, 2025",
  
  // Bank-specific fields
  bankData: {
    loanPurpose: "Personal Loan",
    loanAmount: 500000,
    loanDuration: 60,
    monthlyIncome: 50000,
    creditScore: 750,
    employmentType: "Salaried"
  },
  
  // HR-specific fields
  hrData: {
    positionApplied: "Software Engineer",
    yearsExperience: 5,
    currentSalary: 800000,
    education: "Master's Degree",
    coverLetter: "..."
  },
  
  // Healthcare-specific fields
  healthcareData: {
    serviceRequired: "General Consultation",
    age: 30,
    bloodType: "O+",
    symptoms: "...",
    severityLevel: "Medium"
  },
  
  clientInfo: {
    name: "Ravi Kumar",
    phone: "+91-98765-43210"
  }
}
```

## 📍 Integration Points

### 1. Banking Admin Panel Integration

**Current Banking Module:**
- Located in: `panel-banking` (Admin Dashboard)
- Features: CSV upload, Rules setup, Analysis, Results

**How to Add Client Requests:**

**Option A: Add New "Client Requests" Section**
```html
<!-- In Banking Module -->
<div class="card">
  <div class="card-h">
    <div class="card-t">Client Loan Requests</div>
  </div>
  <div class="tbl-wrap">
    <table id="bank-client-requests">
      <thead>
        <tr>
          <th>Client Name</th>
          <th>Phone</th>
          <th>Loan Amount</th>
          <th>Purpose</th>
          <th>Credit Score</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody id="bank-client-req-body">
        <!-- Auto-populate from CLIENT.requests -->
      </tbody>
    </table>
  </div>
</div>
```

**Option B: Create Separate Tab**
```javascript
// Add to banking rules/analysis section
// Tabs: "Upload CSV" | "Client Requests" | "Analysis"

function loadBankClientRequests() {
  const bankRequests = CLIENT.requests.filter(r => r.type === 'bank');
  const tbody = document.getElementById('bank-client-req-body');
  
  bankRequests.forEach(req => {
    const row = tbody.insertRow();
    row.innerHTML = `
      <td>${req.clientInfo.name}</td>
      <td>${req.clientInfo.phone}</td>
      <td>₹${req.bankData.loanAmount}</td>
      <td>${req.bankData.loanPurpose}</td>
      <td>${req.bankData.creditScore}</td>
      <td><span class="pill pill-amber">⏳ ${req.status}</span></td>
      <td>
        <button onclick="reviewBankRequest('${req.id}')">Review</button>
      </td>
    `;
  });
}
```

### 2. HR Admin Panel Integration

**Current HR Module:**
- Located in: `panel-hr` (Admin Dashboard)
- Features: CSV upload, Candidate ranking, Results

**How to Add Client Requests:**

```javascript
function loadHRClientRequests() {
  const hrRequests = CLIENT.requests.filter(r => r.type === 'hr');
  const tbody = document.getElementById('hr-client-req-body');
  
  hrRequests.forEach(req => {
    const row = tbody.insertRow();
    row.innerHTML = `
      <td>${req.clientInfo.name}</td>
      <td>${req.clientInfo.phone}</td>
      <td>${req.hrData.positionApplied}</td>
      <td>${req.hrData.yearsExperience} years</td>
      <td>₹${req.hrData.currentSalary}</td>
      <td>${req.hrData.education}</td>
      <td><span class="pill pill-amber">⏳ ${req.status}</span></td>
      <td>
        <button onclick="reviewHRRequest('${req.id}')">Review</button>
      </td>
    `;
  });
}
```

### 3. Healthcare Admin Panel Integration

**Current Healthcare Module:**
- Located in: `panel-healthcare` (Admin Dashboard)
- Features: Patient data analysis, Triage engine, Doctor assignment

**How to Add Client Requests:**

```javascript
function loadHealthcareClientRequests() {
  const healthRequests = CLIENT.requests.filter(r => r.type === 'healthcare');
  const tbody = document.getElementById('health-client-req-body');
  
  healthRequests.forEach(req => {
    const row = tbody.insertRow();
    row.innerHTML = `
      <td>${req.clientInfo.name}</td>
      <td>${req.clientInfo.phone}</td>
      <td>${req.healthcareData.age}</td>
      <td>${req.healthcareData.bloodType}</td>
      <td>${req.healthcareData.serviceRequired}</td>
      <td><span class="pill pill-${getSeverityClass(req.healthcareData.severityLevel)}">
        ${req.healthcareData.severityLevel}
      </span></td>
      <td>
        <button onclick="reviewHealthRequest('${req.id}')">Review</button>
      </td>
    `;
  });
}

function getSeverityClass(severity) {
  if (severity === 'High') return 'red';
  if (severity === 'Medium') return 'amber';
  return 'green';
}
```

## 🔄 Request Workflow Implementation

### Step 1: Retrieve Client Requests

```javascript
// In admin panel, retrieve requests for specific type
function getClientRequestsByType(type) {
  return CLIENT.requests.filter(req => req.type === type);
}

// Or for specific client
function getClientRequests(clientPhone) {
  return CLIENT.requests.filter(req => req.clientInfo.phone === clientPhone);
}
```

### Step 2: Review Request Details

```javascript
function reviewBankRequest(requestId) {
  const request = CLIENT.requests.find(r => r.id === requestId);
  
  // Show details in modal or side panel
  console.log('Bank Request:', {
    client: request.clientInfo.name,
    phone: request.clientInfo.phone,
    loanAmount: request.bankData.loanAmount,
    purpose: request.bankData.loanPurpose,
    income: request.bankData.monthlyIncome,
    creditScore: request.bankData.creditScore,
    employment: request.bankData.employmentType
  });
  
  // Show review panel with Approve/Reject/Flag buttons
  showBankRequestReviewPanel(request);
}
```

### Step 3: Approve/Reject Request

```javascript
function approveBankRequest(requestId) {
  const request = CLIENT.requests.find(r => r.id === requestId);
  request.status = 'approved';
  
  // Send WhatsApp notification
  sendWhatsAppNotification(
    request.clientInfo.phone,
    `✅ Your loan request #${requestId} has been APPROVED! 
    Amount: ₹${request.bankData.loanAmount}
    Next steps will be sent to you shortly.`
  );
  
  // Update UI
  showToast('✅', `Request ${requestId} approved`, 'ok');
}

function rejectBankRequest(requestId, reason) {
  const request = CLIENT.requests.find(r => r.id === requestId);
  request.status = 'rejected';
  request.rejectionReason = reason;
  
  // Send WhatsApp notification
  sendWhatsAppNotification(
    request.clientInfo.phone,
    `❌ Your loan request #${requestId} was not approved.
    Reason: ${reason}
    You can submit a new application anytime.`
  );
  
  showToast('❌', `Request ${requestId} rejected`, 'error');
}
```

### Step 4: Send Notifications

```javascript
function sendWhatsAppNotification(phone, message) {
  // Integration with WhatsApp API or Twilio
  // Current mock in app.js
  
  console.log(`WhatsApp to ${phone}:`, message);
  
  // Production: Use actual WhatsApp/SMS gateway
  // Example with Twilio:
  // twilio.messages.create({
  //   body: message,
  //   from: '+1234567890',
  //   to: phone
  // })
}
```

## 📊 Admin Panel Request Table Template

### For Banking Admin:

```html
<div class="card">
  <div class="card-h">
    <div class="card-t">Pending Client Loan Requests</div>
    <button class="btn-sm" onclick="refreshClientRequests()">Refresh</button>
  </div>
  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Request ID</th>
          <th>Client Name</th>
          <th>Phone</th>
          <th>Loan Amount</th>
          <th>Purpose</th>
          <th>Credit Score</th>
          <th>Income</th>
          <th>Status</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody id="bank-client-requests-body">
        <!-- Auto-populate -->
      </tbody>
    </table>
  </div>
</div>

<div id="bank-review-panel" class="card" style="display:none;margin-top:2rem">
  <div class="card-h">
    <div class="card-t">Review Client Request</div>
  </div>
  <div class="card-body">
    <!-- Detailed review form here -->
    <div id="request-details"></div>
    <div style="display:flex;gap:1rem;margin-top:1.5rem">
      <button class="btn-p" onclick="approveBankRequestAction()">✓ Approve</button>
      <button class="btn-g" onclick="rejectBankRequestAction()">Flag for Review</button>
      <button class="btn-outline" onclick="closeBankReview()">Close</button>
    </div>
  </div>
</div>
```

## 🔌 JavaScript Integration

### Add to admin dashboard:

```javascript
// Initialize client request tracking
let PENDING_CLIENT_REQUESTS = {
  bank: [],
  hr: [],
  healthcare: []
};

// Load client requests when admin logs in
function loadAdminClientRequests() {
  PENDING_CLIENT_REQUESTS.bank = CLIENT.requests.filter(r => r.type === 'bank' && r.status === 'pending');
  PENDING_CLIENT_REQUESTS.hr = CLIENT.requests.filter(r => r.type === 'hr' && r.status === 'pending');
  PENDING_CLIENT_REQUESTS.healthcare = CLIENT.requests.filter(r => r.type === 'healthcare' && r.status === 'pending');
  
  // Update UI with counts
  document.getElementById('bank-pending-count').textContent = PENDING_CLIENT_REQUESTS.bank.length;
  document.getElementById('hr-pending-count').textContent = PENDING_CLIENT_REQUESTS.hr.length;
  document.getElementById('health-pending-count').textContent = PENDING_CLIENT_REQUESTS.healthcare.length;
}
```

## 📝 Request Review Process

### Admin Workflow:

1. **Login to Admin Dashboard**
   - View pending client requests count
   - See notifications for new requests

2. **Go to Respective Module**
   - Banking → View Client Loan Requests
   - HR → View Client Applications
   - Healthcare → View Client Requests

3. **Review Request Details**
   - Click on request to expand
   - See client information
   - Review all submitted data
   - Check fairness score (if applicable)

4. **Make Decision**
   - **Approve**: Process and send success notification
   - **Request More Info**: Ask for additional details
   - **Reject**: With reason and feedback
   - **Flag**: For manual review by supervisor

5. **Send Notification**
   - WhatsApp message to client
   - Email confirmation
   - In-app notification
   - Update request status

6. **Track History**
   - Log all decisions
   - Store timestamps
   - Keep audit trail
   - Track fairness metrics

## 🎨 UI Recommendations

### Admin Panel Enhancements:

1. **Request Badge on Sidebar**
   ```html
   <button class="sb-item mod-bank" onclick="showP('banking')">
     <span class="sb-icon">🏦</span>Banking
     <span class="sb-badge" id="bank-client-req-badge">3</span>
   </button>
   ```

2. **Quick Stats Card**
   ```html
   <div class="kpi">
     <div class="kpi-ic">📋</div>
     <div class="kpi-v" id="total-client-reqs">12</div>
     <div class="kpi-l">Client Requests</div>
   </div>
   ```

3. **Request Priority Indicator**
   ```html
   <div class="priority-badge" style="background:var(--red)">HIGH</div>
   <div class="priority-badge" style="background:var(--amber)">MEDIUM</div>
   <div class="priority-badge" style="background:var(--green)">LOW</div>
   ```

## 🔐 Security Considerations

When integrating with backend:

1. **Authentication**: Verify admin user before showing client data
2. **Authorization**: Only show requests for their organization
3. **Data Encryption**: Encrypt client phone numbers and sensitive data
4. **Audit Logging**: Log all admin actions on requests
5. **Rate Limiting**: Prevent abuse of request submission
6. **Data Validation**: Validate all client input data
7. **Privacy**: Comply with data protection regulations

## 🚀 Deployment Checklist

- [ ] Client request data structure defined
- [ ] Admin panel integration completed
- [ ] Approval/rejection workflow implemented
- [ ] WhatsApp notification system working
- [ ] Email notification system working
- [ ] Database persistence added
- [ ] Audit logging implemented
- [ ] User testing completed
- [ ] Performance testing done
- [ ] Security review completed

---

**Ready to integrate client requests into your admin panels!** 🎉

For technical questions, refer to the CLIENT object in app.js.
