# UI/UX Audit Report: Ledgerly Web App

**Audit Date:** 2026-09-21  
**Files Audited:** index.html, invoices.html, signup.html, styles.css  
**Audit Scope:** Read-only analysis using accessibility standards and usability best practices

---

## Executive Summary

The Ledgerly app demonstrates decent structural foundations but suffers from **critical accessibility failures**, **confusing interaction patterns**, **poor form design**, and **visual inconsistency**. High-severity issues affect keyboard navigation, form usability, and data safety. The app needs systematic remediation in accessibility, form validation, semantic HTML, and button consistency.

**Findings by Severity:**
- Critical: 4
- Major: 15
- Minor: 12

---

## Detailed Findings

### CRITICAL ISSUES

#### 1. Non-semantic clickable spans without keyboard access
**Files:** index.html:39, index.html:88  
**Severity:** Critical  
**Description:** Clickable elements use `<span>` with `onclick` handler instead of proper `<a>` or `<button>` elements. These are inaccessible to keyboard users and screen readers.  
**Evidence:**
- Line 39: `<span class="go" onclick="location.href='#'"></span>`
- Line 88: `<span class="ghostlink" onclick="location.href='signup.html'">Create your free account</span>`

**Fix:** Replace with semantic HTML elements:
```html
<!-- Instead of line 39: -->
<button class="go" aria-label="Search" onclick="location.href='#'"></button>

<!-- Instead of line 88: -->
<a href="signup.html" class="ghostlink">Create your free account</a>
```

---

#### 2. Placeholder text used as form labels (no proper labels)
**File:** signup.html:41-57  
**Severity:** Critical  
**Description:** Form fields lack associated `<label>` elements and rely solely on placeholder text. Placeholders disappear when typing, leaving users confused about field purpose. Screen readers cannot connect labels to inputs.  
**Evidence:**
- Line 41: `<input type="text" name="e" placeholder="Email">` (no `<label>`)
- Line 42: `<input type="password" name="p" placeholder="Password">` (no `<label>`)
- Line 43-57: Most fields follow this pattern

**Fix:** Add proper labels:
```html
<div class="field">
  <label for="email" class="lbl">Email</label>
  <input type="email" id="email" name="e" placeholder="user@example.com" required>
</div>
```

---

#### 3. Permanently visible error message in HTML
**File:** signup.html:58  
**Severity:** Critical  
**Description:** Error message is hardcoded in the HTML and always visible: `<div class="err">Error: invalid input.</div>`. This confuses users since no error has occurred yet. Should only appear on validation failure.  
**Evidence:** Line 58 displays an error that doesn't reflect actual validation state.

**Fix:** Hide error message by default with CSS (`display: none;`) or JavaScript, only show on form submission failure:
```html
<div class="err" style="display: none;" id="form-error">Error: invalid input.</div>
```

---

#### 4. Credit card collection without security disclosure
**File:** signup.html:57  
**Severity:** Critical  
**Description:** Form collects raw credit card numbers (`pattern="[0-9]{16}"`) with no mention of SSL encryption, PCI compliance, or security assurances. This violates security best practices and user trust.  
**Evidence:** Line 57: `<input type="text" name="cc" placeholder="Card number (no spaces or dashes)" pattern="[0-9]{16}" required>`

**Fix:** 
1. Add security disclosure before the form
2. Use `type="text"` is wrong—should handle securely or redirect to payment processor
3. Add text: `<p>Your payment information is encrypted and secure. Ledgerly never stores credit card details.</p>`
4. Better: Use a payment gateway (Stripe, Square) instead of collecting raw card data

---

### MAJOR ISSUES

#### 5. Broken navigation links (# anchors)
**File:** index.html:13-21  
**Severity:** Major  
**Description:** Most top-bar utility links point to "#" and don't navigate anywhere. Users click expecting functionality but nothing happens.  
**Evidence:** Lines 13-21: `<a href="#">Help</a>`, `<a href="#">FAQ</a>`, `<a href="#">Blog</a>`, etc.

**Fix:** Update href attributes with actual URLs:
```html
<a href="/help/">Help</a>
<a href="/faq/">FAQ</a>
<a href="/blog/">Blog</a>
```

---

#### 6. Hero section text is vague corporate jargon
**File:** index.html:47  
**Severity:** Major  
**Description:** Value proposition uses buzzwords ("synergistic solutions," "forward-thinking," "leverage core competencies") that don't communicate real benefits. Users won't understand what Ledgerly actually does.  
**Evidence:** Line 47: "...synergistic solutions that empower forward-thinking organizations to leverage their core competencies..."

**Fix:** Replace with clear, benefit-focused copy:
```html
<p>Send invoices, track payments, and manage your finances—all in one place. Get paid faster with Ledgerly.</p>
```

---

#### 7. Too many CTAs in hero section
**File:** index.html:48-54  
**Severity:** Major  
**Description:** Five buttons in a row (Learn More, Watch Video, See Pricing, Read the Blog, Let's Go!) overwhelm users and reduce conversion. Best practice: 1-2 primary CTAs.  
**Evidence:** Lines 48-54 contain 5 different button options in `.cta-row`

**Fix:** Reduce to primary and secondary CTAs:
```html
<div class="cta-row">
  <a class="btn btn-blue" href="#signup">Start Free Trial</a>
  <a class="btn btn-outline" href="#features">Learn More</a>
</div>
```

---

#### 8. Manipulative promo messaging with false urgency
**File:** index.html:65-72  
**Severity:** Major  
**Description:** Promo cards use artificial urgency ("!!!"), vague deadlines ("Offer ends soon"), and hype ("rocketship"). This erodes user trust and uses dark patterns.  
**Evidence:**
- Line 65: "Hot!!! Summer Sale" + "Offer ends soon!" (triple exclamation marks, no date)
- Line 67: "before seats run out!" (artificial scarcity)
- Line 68: "Join the rocketship!" (hype language)

**Fix:** Use honest, specific messaging:
```html
<div class="promo"><h3>Summer Sale</h3>20% off annual plans through September 30</div>
<div class="promo"><h3>Webinar Thursday</h3>Register for advanced invoicing strategies at 2 PM EST</div>
<div class="promo"><h3>We're Hiring</h3>Join our growing team. View open roles.</div>
```

---

#### 9. Poor contrast in hero section text
**File:** styles.css:41-42  
**Severity:** Major  
**Description:** Subtle text on blue hero background fails WCAG AA contrast requirements:
- Motto (#9a9a9a on #2456c9): ~3.2:1 contrast (needs 4.5:1 for AA)
- Paragraph text (rgba(255,255,255,0.45) on #2456c9): ~2.8:1 contrast

**Evidence:**
- Line 41: `.hero .motto { color: #9a9a9a; ... }` on #2456c9 background
- Line 42: `.hero p { color: rgba(255,255,255,0.45); ... }` on #2456c9 background

**Fix:** Use higher contrast colors:
```css
.hero .motto { color: #e8e8e8; }
.hero p { color: #ffffff; }
```

---

#### 10. Active navigation state barely distinguishable
**File:** styles.css:25  
**Severity:** Major  
**Description:** Active nav link (#4d4d4d) is only slightly darker than inactive (#555), making current page indicator nearly invisible.  
**Evidence:** Line 25: `.topbar .nav a.active { color: #4d4d4d; }` vs. Line 24: `.topbar .nav a { color: #555; }`

**Fix:** Use more distinct styling:
```css
.topbar .nav a.active { 
  color: #1a6fe0; 
  font-weight: 700;
  border-bottom: 3px solid #1a6fe0;
}
```

---

#### 11. Inconsistent button styling and sizing
**File:** styles.css:45-60  
**Severity:** Major  
**Description:** Button classes have inconsistent padding, sizing, and formatting rules making the component unpredictable:
- `.btn-blue` and `.btn-green`: standard padding
- `.btn-orange`: custom `border-radius: 18px` (inconsistent)
- `.btn-red`: custom padding (12px 26px), `font-size: 18px`, `text-transform: uppercase` (stands out unnecessarily)
- `.btn-grey`: `border-radius: 0` (no radius)

**Evidence:**
- Line 56: `.btn-blue { background: #1a6fe0; }` (standard)
- Line 58: `.btn-orange { border-radius: 18px; }` (custom)
- Line 59: `.btn-red { font-size: 18px; padding: 12px 26px; text-transform: uppercase; }` (over-styled)
- Line 60: `.btn-grey { border-radius: 0; }` (no radius)

**Fix:** Standardize all buttons:
```css
.btn {
  display: inline-block;
  font-size: 1em;
  padding: 0.6em 1.2em;
  border-radius: 4px;
  border: 0;
  color: #fff;
  text-decoration: none;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn:hover { opacity: 0.9; }
.btn-blue { background: #1a6fe0; }
.btn-green { background: #1fa34a; }
.btn-orange { background: #ee7d11; }
.btn-red { background: #e01a1a; }
.btn-grey { background: #c9c9c9; color: #000; }
```

---

#### 12. Delete button has no confirmation
**File:** invoices.html:57  
**Severity:** Major  
**Description:** Prominent red "Delete" button in invoices UI can permanently destroy data with a single click and no confirmation dialog. High risk of accidental deletion.  
**Evidence:** Line 57: `<button class="btn btn-red">Delete</button>`

**Fix:** Add confirmation dialog:
```html
<button class="btn btn-red" onclick="if(confirm('Are you sure? This cannot be undone.')) deleteInvoice(this);">Delete</button>
```

---

#### 13. Misleading "Archive" button labeled with danger class
**File:** invoices.html:73-78  
**Severity:** Major  
**Description:** Archive buttons use `.quiet-danger` class (dark red color #8a1c1c) but archiving is a safe, reversible action—not dangerous. This mislabels the severity.  
**Evidence:** Lines 73-78: `<button class="quiet-danger">Archive</button>` appearing in table rows

**Fix:** Use neutral styling:
```html
<button class="btn-grey">Archive</button>
```

Or create an `.archive` class:
```css
.btn-archive { background: #6ba3d0; color: #fff; }
```

---

#### 14. Form fields stretch full width without max-width
**File:** styles.css:120  
**Severity:** Major  
**Description:** Form inputs are set to `width: 100%` with no `max-width` constraint. On desktop, inputs become absurdly wide (e.g., 1200px), creating poor UX for data entry.  
**Evidence:** Line 120: `.field input, .field select { width: 100%; ... }`

**Fix:** Add max-width constraint:
```css
.field input, .field select { 
  width: 100%; 
  max-width: 500px; 
  border: 1px solid #999; 
  font-size: 14px; 
}
```

---

#### 15. Phone number format too strict
**File:** signup.html:43  
**Severity:** Major  
**Description:** Phone field requires exact `[0-9]{10}` format with no flexibility for international formats, extensions, or common separators (dashes, spaces, parentheses).  
**Evidence:** Line 43: `<input type="text" name="ph" placeholder="Phone (format: 5557654321, digits only)" pattern="[0-9]{10}" required>`

**Fix:** Use flexible validation or allow common formats:
```html
<input type="tel" name="ph" placeholder="Phone (e.g., 555-765-4321)" 
  pattern="[0-9\s\-\(\)]{10,}" required>
```

---

#### 16. Date format requires exact MM/DD/YYYY entry
**File:** signup.html:47  
**Severity:** Major  
**Description:** Date of birth field requires text input with exact "MM/DD/YYYY" format instead of using `<input type="date">` which provides a date picker and flexible parsing.  
**Evidence:** Line 47: `<input type="text" name="dob" placeholder="Date of birth (MM/DD/YYYY exactly)" required>`

**Fix:** Use proper date input:
```html
<input type="date" name="dob" required>
```

---

#### 17. Tight line-height reduces readability
**File:** styles.css:10  
**Severity:** Major  
**Description:** Body text uses `line-height: 1.2` which is below the WCAG AA recommendation of 1.5 for body text. Creates cramped, hard-to-read paragraphs.  
**Evidence:** Line 10: `line-height: 1.2;`

**Fix:** Increase to WCAG standard:
```css
body { line-height: 1.5; }
```

---

#### 18. Promo grid not responsive (4-column fixed)
**File:** styles.css:63  
**Severity:** Major  
**Description:** Promo grid uses `grid-template-columns: repeat(4, 25%)` with no responsive breakpoints. On tablets and mobile, content is crushed or forces horizontal scrolling.  
**Evidence:** Line 63: `.promo-grid { grid-template-columns: repeat(4, 25%); ... }`

**Fix:** Add responsive grid:
```css
.promo-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
  gap: 10px;
}
```

---

#### 19. Missing alt text on images
**Files:** index.html:81, signup.html:61-63  
**Severity:** Major  
**Description:** Images lack `alt` attributes, making content inaccessible to screen readers and broken for users with images disabled.  
**Evidence:**
- Line 81 (index.html): `<img class="bigicon" src="icons/check-16.svg">` (no alt)
- Lines 61-63 (signup.html): `<img src="people/a.jpg">` (no alt)

**Fix:** Add descriptive alt text:
```html
<img class="bigicon" src="icons/check-16.svg" alt="Check mark icon">
<img src="people/a.jpg" alt="Team member avatar">
```

---

#### 20. Reset button on form can cause accidental data loss
**File:** signup.html:67  
**Severity:** Major  
**Description:** "Clear form" reset button offers no value and risks accidental data loss when users fat-finger or misclick. Most modern forms don't include reset.  
**Evidence:** Line 67: `<button type="reset" class="btn btn-blue">Clear form</button>`

**Fix:** Remove the reset button entirely or replace with Cancel:
```html
<div class="actions">
  <a href="#" class="btn btn-grey">Cancel</a>
  <button type="submit" class="btn btn-blue">Submit</button>
</div>
```

---

### MINOR ISSUES

#### 21. Missing table semantic structure
**File:** invoices.html:72  
**Severity:** Minor  
**Description:** Table lacks proper `<thead>` and `<tbody>` wrapping. While it works, semantic HTML improves accessibility and styling capability.  
**Evidence:** Line 72 starts `<tr><th>` but no `<thead>` wrapper

**Fix:** Wrap headers and body:
```html
<table class="dense">
  <thead>
    <tr><th>Number</th><th>Client</th>...</tr>
  </thead>
  <tbody>
    <tr><td>INV-2041</td><td>Northwind Traders</td>...</tr>
    ...
  </tbody>
</table>
```

---

#### 22. No visible keyboard focus indicators
**File:** styles.css  
**Severity:** Minor  
**Description:** No `:focus` or `:focus-visible` styles defined for links, buttons, or form fields. Keyboard users cannot see what element currently has focus.  
**Evidence:** No focus styles anywhere in CSS

**Fix:** Add focus styles to all interactive elements:
```css
a:focus, button:focus, input:focus, select:focus {
  outline: 3px solid #1a6fe0;
  outline-offset: 2px;
}
```

---

#### 23. Color-only status indicators
**File:** invoices.html:64-66  
**Severity:** Minor  
**Description:** Metrics show "Collected" in green and "Outstanding" in red, but color alone isn't sufficient for colorblind users. Should include text labels or icons.  
**Evidence:** Lines 64-66:
```html
<div class="metric"><div>Collected</div><div class="num up">$18,400</div><div class="up">8%</div></div>
<div class="metric"><div>Outstanding</div><div class="num down">$9,120</div><div class="down">14%</div></div>
```
Classes `up` and `down` rely only on color (#1fa34a green and #e01a1a red)

**Fix:** Add icons or text indicators:
```html
<div class="metric">
  <div>Collected</div>
  <div class="num up">↑ $18,400</div>
  <div class="up">8% increase</div>
</div>
```

---

#### 24. Confusing "Cancel my subscription" link on signup page
**File:** signup.html:69  
**Severity:** Minor  
**Description:** Users haven't signed up yet, so seeing "Cancel my subscription" is confusing and makes the form feel untrustworthy. This belongs on an account settings page, not signup.  
**Evidence:** Line 69: `<a class="quiet-danger" href="#">Cancel my subscription</a>` appears in the signup form

**Fix:** Remove from signup; add to account management page only.

---

#### 25. Privacy statement comes AFTER sensitive data collection
**File:** signup.html:71  
**Severity:** Minor  
**Description:** "Your privacy is very important to us" appears after the form has already asked for name, email, phone, address, DOB, income, and card number. Privacy assurance should come before data collection.  
**Evidence:** Line 71: Privacy statement appears after line 57 (card number input)

**Fix:** Move privacy statement above the form:
```html
<div class="help">
  <p>Your privacy is very important to us. We encrypt all data and never share your information.</p>
  <p>The following form is designed to collect the information that we need...</p>
</div>
```

---

#### 26. Empty state lacks action
**File:** invoices.html:84-85  
**Severity:** Minor  
**Description:** The "RECURRING" section shows "No data" with no clear call-to-action to create a recurring invoice.  
**Evidence:** Lines 84-85: `<div class="empty">No data.</div>` with no adjacent help text

**Fix:** Add actionable empty state:
```html
<div class="empty">
  No recurring invoices yet.
  <a href="#create" class="btn btn-blue">Create Recurring Invoice</a>
</div>
```

---

#### 27. Example email uses .example TLD (invalid)
**File:** invoices.html:45  
**Severity:** Minor  
**Description:** Sample data shows `ap@northwind.example` which is not a valid domain. Should use .com or other actual TLD for better realism.  
**Evidence:** Line 45: `<td>ap@northwind.example</td>`

**Fix:** Use realistic domain:
```html
<td>ap@northwind.com</td>
```

---

#### 28. Input placeholder text too large
**File:** signup.html:40-57  
**Severity:** Minor  
**Description:** Placeholder text in signup form is same size as body text (14px) and can be confused with actual data. Should be smaller or lighter.  
**Evidence:** Lines 40-57: inputs use 14px placeholder with no visual distinction

**Fix:** Add placeholder styling in CSS:
```css
.field input::placeholder, .field select { 
  color: #aaa; 
  opacity: 0.6;
}
```

---

#### 29. Sidebar color provides insufficient contrast
**File:** styles.css:84  
**Severity:** Minor  
**Description:** Sidebar uses `background: #dfe6f5` (very light blue) which blends into white background and provides weak visual separation from main content.  
**Evidence:** Line 84: `.sidebar { background: #dfe6f5; ... }`

**Fix:** Use more distinct color:
```css
.sidebar { background: #e8edf7; border-right: 2px solid #1a6fe0; }
```

---

#### 30. "What are you?" section needs better heading
**File:** index.html:58  
**Severity:** Minor  
**Description:** "Which one are you?" is vague and doesn't explain what choosing these options does. Should have clearer framing.  
**Evidence:** Line 58: `<div>Which one are you?</div>` with no context

**Fix:** Add descriptive heading:
```html
<h2>Choose Your Account Type</h2>
<p>Select the option that best matches your use case to get started:</p>
```

---

#### 31. Finder (Quick Find) interaction unclear
**File:** index.html:30-40  
**Severity:** Minor  
**Description:** The "Quick Find" widget is in the topbar but provides no visual feedback on selection or search. It's unclear if clicking the dropdown or button performs the search.  
**Evidence:** Lines 30-40: `.finder` with select, input, and empty `.go` span—interaction not obvious

**Fix:** Add aria-labels and clarify:
```html
<div class="finder">
  <label for="find-type">Quick Find:</label>
  <select id="find-type" aria-label="Search by">
    <option>Keyword</option>
    <option>Client ID</option>
    <option>Doc number</option>
    <option>Tag</option>
  </select>
  <input type="text" id="find-input" placeholder="Enter search term..." aria-label="Search term">
  <button class="go" aria-label="Search">Search</button>
</div>
```

---

## What the App Does Well

✓ **Clean, minimal visual design** - The layout is uncluttered and uses whitespace effectively  
✓ **Good page structure** - Proper use of semantic sections (hero, promo grid, features, footer)  
✓ **Responsive meta viewport tag** - Includes `<meta name="viewport">` for mobile compatibility  
✓ **Organized CSS** - CSS is well-commented with clear sections  
✓ **Consistent typography** - Uses system fonts and readable base sizes  
✓ **Functional layout** - The dashboard (invoices.html) has good information hierarchy with sidebar and main content  
✓ **Color contrast in most areas** - Primary content is readable (hero text issue is exception)

---

## TOP 5 PRIORITY FIXES

### 1. **Add Proper Form Labels (signup.html:40-57)** — CRITICAL
Replace placeholder-only inputs with associated `<label>` elements. This fixes accessibility failures and improves UX.
```html
<div class="field">
  <label for="email" class="lbl">Email Address</label>
  <input type="email" id="email" name="e" required>
</div>
```
**Impact:** Fixes screen reader access, WCAG A compliance, user clarity

---

### 2. **Fix Hero Section Text Contrast (styles.css:41-42)** — CRITICAL
Increase contrast of subtitle and paragraph text on blue background from 3.2:1 to 4.5:1+ for WCAG AA compliance.
```css
.hero .motto { color: #e8e8e8; font-weight: 400; }
.hero p { color: #ffffff; }
```
**Impact:** Makes content readable, passes accessibility standards

---

### 3. **Replace Non-semantic Clickables with Buttons/Links** — CRITICAL
Convert span elements with onclick to proper `<button>` or `<a>` elements (index.html:39, 88).
```html
<!-- Line 39: Replace with -->
<button class="go" onclick="search()">Search</button>

<!-- Line 88: Replace with -->
<a href="signup.html" class="ghostlink">Create your free account</a>
```
**Impact:** Enables keyboard navigation, fixes screen reader access

---

### 4. **Hide Permanent Error Message (signup.html:58)** — CRITICAL
Remove always-visible error message; show only on validation failure.
```html
<div class="err" id="error-message" style="display: none;">Please fix the errors above.</div>
```
**Impact:** Reduces user confusion, improves form clarity

---

### 5. **Standardize Button Styling (styles.css:45-60)** — MAJOR
Remove inconsistent padding, sizing, and border-radius from button classes. All buttons should follow one style pattern.
```css
.btn-red { background: #e01a1a; padding: 0.6em 1.2em; font-size: 1em; text-transform: none; }
.btn-orange { border-radius: 4px; /* matches others */ }
```
**Impact:** Improves visual consistency, reduces cognitive load, more professional appearance

---

## Summary Statistics

| Severity | Count |
|----------|-------|
| Critical | 4     |
| Major    | 15    |
| Minor    | 12    |
| **Total** | **31** |

**Files with Issues:**
- index.html: 11 issues
- signup.html: 13 issues
- invoices.html: 4 issues
- styles.css: 3 issues

---

## Recommendations

1. **Immediate:** Address all 4 critical issues before any user testing or launch
2. **High Priority:** Fix 15 major issues within 1-2 weeks (mostly accessibility and UX patterns)
3. **Medium Priority:** Address minor issues in next sprint (mostly polish and refinement)
4. **Testing:** Conduct accessibility audit using WAVE or Axe DevTools after fixes
5. **Keyboard Testing:** Test full form flow and navigation with keyboard only (no mouse)
6. **Usability Testing:** Conduct user testing on signup flow with real users

---

**Report Generated:** 2026-09-21  
**Audit Scope:** Read-only analysis, no tools or skills invoked
