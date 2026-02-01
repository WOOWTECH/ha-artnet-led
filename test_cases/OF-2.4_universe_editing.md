# OF-2.4: Universe Editing Tests

## Overview
Tests for editing individual universe settings (`async_step_universe_edit`)

## Test Cases (4)

---

### OF-2.4.1: Add Universe 2

**Description:** Create a new universe with specific number

**Preconditions:**
- In universe edit form (adding new)

**Test Steps:**
1. Enter Universe: 2
2. Click Submit

**Expected Result:** Universe 2 created successfully

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.4.2: Change Universe Number

**Description:** Renumber an existing universe

**Preconditions:**
- In universe edit form for Universe 1
- Universe 1 has fixtures

**Test Steps:**
1. Change Universe from 1 to 5
2. Click Submit

**Expected Result:**
- Universe renumbered to 5
- All fixtures moved to universe 5
- Entities continue working

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.4.3: Change Output Correction

**Description:** Update universe output correction

**Preconditions:**
- In universe edit form
- Currently set to "sRGB"

**Test Steps:**
1. Change Output Correction to "Linear"
2. Click Submit

**Expected Result:** Universe updated with linear correction

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.4.4: Toggle Partial Universe

**Description:** Enable/disable partial universe sending

**Preconditions:**
- In universe edit form

**Test Steps:**
1. Toggle "Send Partial Universe" checkbox
2. Click Submit

**Expected Result:** Universe updated with new partial setting

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
