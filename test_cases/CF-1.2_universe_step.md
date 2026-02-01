# CF-1.2: Universe Step Tests

## Overview
Tests for the second step of Config Flow: Universe Setup (`async_step_universe`)

## Test Cases (9)

---

### CF-1.2.1: Add Single Universe

**Description:** Add a single universe to the configuration

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. In Universe step, enter Universe: 1
2. Select Action: "Add Universe"
3. Click Submit

**Expected Result:** Universe added, form refreshes showing universe in list

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.2: Add Multiple Universes

**Description:** Add multiple universes sequentially

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. Add Universe 1, click Submit
2. Add Universe 2, click Submit
3. Add Universe 3, click Submit

**Expected Result:** All universes shown in placeholder text (e.g., "1, 2, 3")

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.3: Skip to Fixtures (Auto-Create)

**Description:** Continue without adding universes - auto-create universe 1

**Preconditions:**
- Completed connection step successfully
- No universes added yet

**Test Steps:**
1. In Universe step with no universes added
2. Select Action: "Continue to Fixtures"
3. Click Submit

**Expected Result:** Universe 1 auto-created, proceeds to Fixture step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.4: Skip to Fixtures (With Universes)

**Description:** Continue to fixtures after adding universes

**Preconditions:**
- Completed connection step successfully
- At least one universe added

**Test Steps:**
1. Add Universe 1
2. Select Action: "Continue to Fixtures"
3. Click Submit

**Expected Result:** Proceeds to Fixture step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.5: Duplicate Universe Error

**Description:** Verify error when adding duplicate universe

**Preconditions:**
- Completed connection step successfully
- Universe 1 already added

**Test Steps:**
1. Add Universe 1 (first time - success)
2. Try to add Universe 1 again
3. Click Submit

**Expected Result:** Error: "Duplicate universe" or similar

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.6: Invalid Universe (Too Low)

**Description:** Verify error for universe number below valid range

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. Enter Universe: 0
2. Select Action: "Add Universe"
3. Click Submit

**Expected Result:** Error: "Invalid universe" (must be 1-65535)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.7: Invalid Universe (Too High)

**Description:** Verify error for universe number above valid range

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. Enter Universe: 65536
2. Select Action: "Add Universe"
3. Click Submit

**Expected Result:** Error: "Invalid universe"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.8: With Output Correction

**Description:** Add universe with specific output correction

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. Enter Universe: 1
2. Set Output Correction: "sRGB"
3. Select Action: "Add Universe"
4. Click Submit

**Expected Result:** Universe added with sRGB correction

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.2.9: Send Partial Universe

**Description:** Add universe with partial universe flag

**Preconditions:**
- Completed connection step successfully

**Test Steps:**
1. Enter Universe: 1
2. Enable "Send Partial Universe" checkbox
3. Select Action: "Add Universe"
4. Click Submit

**Expected Result:** Universe added with partial flag enabled

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
