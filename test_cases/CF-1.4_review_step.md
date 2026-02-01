# CF-1.4: Review Step Tests

## Overview
Tests for the final review step of Config Flow (`async_step_review`)

## Test Cases (4)

---

### CF-1.4.1: Review Summary Correct

**Description:** Verify review summary shows all configuration details

**Preconditions:**
- Completed all previous steps with:
  - 1 universe configured
  - 2 fixtures configured

**Test Steps:**
1. Reach Review step
2. Examine the configuration summary displayed

**Expected Result:** Summary shows:
- Host/Protocol details
- Universe(s) configured
- All fixtures with names, types, channels

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.4.2: Go Back to Edit

**Description:** Return to fixture step to make changes

**Preconditions:**
- In Review step

**Test Steps:**
1. Select Action: "Go Back to Edit"
2. Click Submit

**Expected Result:** Returns to fixture step with all data preserved

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.4.3: Create Integration

**Description:** Successfully create the integration

**Preconditions:**
- In Review step
- All configuration valid

**Test Steps:**
1. Select Action: "Create Integration"
2. Click Submit

**Expected Result:**
- Integration entry created successfully
- Shows success message
- Entity appears in Home Assistant

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.4.4: Duplicate Entry Check

**Description:** Verify error when creating duplicate integration

**Preconditions:**
- Integration already exists for same host:port

**Test Steps:**
1. Start new config flow with same host:port
2. Complete all steps to Review
3. Click "Create Integration"

**Expected Result:** Error: "Already configured" or similar

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
