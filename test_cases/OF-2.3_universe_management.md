# OF-2.3: Universe Management Tests

## Overview
Tests for universe management via Options Flow (`async_step_universe`)

## Test Cases (5)

---

### OF-2.3.1: List Universes

**Description:** View all configured universes

**Preconditions:**
- Integration has universes configured
- In options menu

**Test Steps:**
1. Select "Edit Universes"
2. Click Submit

**Expected Result:** Shows list of all configured universes with numbers

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.3.2: Add New Universe

**Description:** Add a new universe to existing configuration

**Preconditions:**
- In universe manager

**Test Steps:**
1. Select "Add New Universe"
2. Click Submit
3. Enter Universe: 2
4. Click Submit

**Expected Result:** Universe 2 created, returns to universe list

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.3.3: Edit Universe

**Description:** Edit an existing universe's settings

**Preconditions:**
- In universe manager
- Universe 1 exists

**Test Steps:**
1. Select "Edit Universe 1"
2. Click Submit

**Expected Result:** Opens form with current universe settings

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.3.4: Delete Universe

**Description:** Remove a universe and its fixtures

**Preconditions:**
- In universe manager
- Universe exists with fixtures

**Test Steps:**
1. Select "Delete Universe X"
2. Click Submit
3. Confirm deletion

**Expected Result:**
- Universe removed
- All fixtures in that universe removed
- Related entities removed

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.3.5: Back to Menu

**Description:** Return to options menu

**Preconditions:**
- In universe manager

**Test Steps:**
1. Select "Back to Menu"
2. Click Submit

**Expected Result:** Returns to main options menu

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
