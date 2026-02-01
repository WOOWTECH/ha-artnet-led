# CF-1.3.9: Fixture Validation Tests

## Overview
Tests for fixture input validation in Config Flow

## Test Cases (4)

---

### CF-1.3.9a: Missing Fixture Name

**Description:** Verify error when fixture name is empty

**Preconditions:**
- In Fixture step

**Test Steps:**
1. Leave Name empty
2. Select Type: Dimmer
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Error: "Name required" or validation error

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.9b: Invalid Channel (Too Low)

**Description:** Verify error for channel below valid range

**Preconditions:**
- In Fixture step

**Test Steps:**
1. Enter Name: "Test"
2. Select Type: Dimmer
3. Enter Channel: 0
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Error: "Invalid channel" (must be 1-512)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.9c: Invalid Channel (Too High)

**Description:** Verify error for channel above valid range

**Preconditions:**
- In Fixture step

**Test Steps:**
1. Enter Name: "Test"
2. Select Type: Dimmer
3. Enter Channel: 513
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Error: "Invalid channel"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.9d: Done With No Fixtures

**Description:** Verify error when trying to finish without fixtures

**Preconditions:**
- In Fixture step
- No fixtures added yet

**Test Steps:**
1. Select Action: "Done - Review Configuration"
2. Click Submit

**Expected Result:** Error: "No fixtures configured" or similar

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
