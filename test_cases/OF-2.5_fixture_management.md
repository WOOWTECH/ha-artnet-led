# OF-2.5: Fixture Management Tests

## Overview
Tests for fixture management via Options Flow (`async_step_fixture`)

## Test Cases (5)

---

### OF-2.5.1: List Fixtures

**Description:** View all configured fixtures

**Preconditions:**
- Integration has fixtures configured
- In options menu

**Test Steps:**
1. Select "Edit Fixtures"
2. Click Submit

**Expected Result:** Shows list of all fixtures with:
- Fixture names
- Types
- Channels
- Universe assignment

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.5.2: Add New Fixture

**Description:** Add a new fixture via options flow

**Preconditions:**
- In fixture manager

**Test Steps:**
1. Select "Add New Fixture"
2. Click Submit

**Expected Result:** Opens fixture add form

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.5.3: Edit Fixture

**Description:** Edit an existing fixture's settings

**Preconditions:**
- In fixture manager
- Fixtures exist

**Test Steps:**
1. Select "Edit: [Fixture Name]"
2. Click Submit

**Expected Result:** Opens form with current fixture settings

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.5.4: Delete Fixture

**Description:** Remove a fixture from configuration

**Preconditions:**
- In fixture manager
- Fixture exists

**Test Steps:**
1. Select "Delete: [Fixture Name]"
2. Click Submit
3. Confirm deletion

**Expected Result:**
- Fixture removed from configuration
- Related entity removed from Home Assistant

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.5.5: Back to Menu

**Description:** Return to options menu

**Preconditions:**
- In fixture manager

**Test Steps:**
1. Select "Back to Menu"
2. Click Submit

**Expected Result:** Returns to main options menu

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
