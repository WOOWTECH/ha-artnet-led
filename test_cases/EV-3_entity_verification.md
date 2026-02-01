# EV-3: Entity Verification Tests

## Overview
Tests for verifying entities are correctly created and managed

## Test Cases (5)

---

### EV-3.1: Entity Appears After Config

**Description:** Verify entity is created after completing config flow

**Preconditions:**
- No existing integration

**Test Steps:**
1. Complete full config flow with 1 fixture
2. Navigate to Developer Tools > States
3. Search for the entity

**Expected Result:**
- Light entity appears in states
- Entity has correct state (off by default)
- Entity has correct attributes

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### EV-3.2: Multiple Entities

**Description:** Verify multiple entities created for multiple fixtures

**Preconditions:**
- No existing integration

**Test Steps:**
1. Complete config flow with 3 fixtures
2. Navigate to Developer Tools > States
3. Search for all entities

**Expected Result:** 3 separate light entities appear

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### EV-3.3: Entity Name Matches Fixture

**Description:** Verify entity friendly name matches fixture name

**Preconditions:**
- None

**Test Steps:**
1. Create fixture named "Living Room"
2. Complete config flow
3. Check entity properties

**Expected Result:** Entity has friendly_name "Living Room"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### EV-3.4: Entity Reload After Edit

**Description:** Verify entity updates after editing via options flow

**Preconditions:**
- Integration exists with fixture

**Test Steps:**
1. Edit fixture name via options flow
2. Check entity after reload

**Expected Result:** Entity friendly name updates to new name

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### EV-3.5: Entity Removed After Delete

**Description:** Verify entity is removed when fixture is deleted

**Preconditions:**
- Integration exists with fixture

**Test Steps:**
1. Note existing entity
2. Delete fixture via options flow
3. Check Developer Tools > States

**Expected Result:** Entity no longer exists

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
