# OF-2.6: Fixture Adding Tests

## Overview
Tests for adding fixtures via Options Flow (`async_step_fixture_add`)

## Test Cases (3)

---

### OF-2.6.1: Add Dimmer Fixture

**Description:** Add a new dimmer fixture via options

**Preconditions:**
- In fixture add form

**Test Steps:**
1. Enter Name: "New Dimmer"
2. Select Type: Dimmer
3. Enter Channel: 10
4. Select Universe: 1
5. Click Submit

**Expected Result:**
- Fixture added to configuration
- New entity appears in Home Assistant

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.6.2: Add to Different Universe

**Description:** Add fixture to a specific universe

**Preconditions:**
- In fixture add form
- Multiple universes exist

**Test Steps:**
1. Enter Name: "Universe 2 Light"
2. Select Type: RGB
3. Enter Channel: 1
4. Select Universe: 2
5. Click Submit

**Expected Result:** Fixture created in Universe 2

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.6.3: Missing Name Validation

**Description:** Verify error when name is empty

**Preconditions:**
- In fixture add form

**Test Steps:**
1. Leave Name empty
2. Fill other required fields
3. Click Submit

**Expected Result:** Error: "Name required"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
