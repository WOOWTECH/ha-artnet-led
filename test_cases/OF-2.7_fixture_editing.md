# OF-2.7: Fixture Editing Tests

## Overview
Tests for editing fixtures via Options Flow (`async_step_fixture_edit`)

## Test Cases (5)

---

### OF-2.7.1: View Existing Fixture

**Description:** Verify existing settings are pre-populated

**Preconditions:**
- Fixture exists
- In fixture edit form for that fixture

**Test Steps:**
1. Select "Edit: [Fixture Name]" from fixture manager
2. Examine pre-filled values

**Expected Result:** All fields show current fixture values

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.7.2: Change Fixture Name

**Description:** Rename an existing fixture

**Preconditions:**
- In fixture edit form

**Test Steps:**
1. Change Name to "Renamed Fixture"
2. Click Submit

**Expected Result:**
- Fixture renamed
- Entity friendly name updates

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.7.3: Change Channel

**Description:** Move fixture to different DMX channel

**Preconditions:**
- In fixture edit form

**Test Steps:**
1. Change Channel from current to 20
2. Click Submit

**Expected Result:** Fixture now outputs on channel 20

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.7.4: Change Universe

**Description:** Move fixture to different universe

**Preconditions:**
- In fixture edit form
- Multiple universes exist

**Test Steps:**
1. Change Universe from 1 to 2
2. Click Submit

**Expected Result:** Fixture moved to Universe 2

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.7.5: Change Fixture Type

**Description:** Change fixture type (e.g., Dimmer to RGB)

**Preconditions:**
- In fixture edit form
- Fixture is currently Dimmer type

**Test Steps:**
1. Change Type from Dimmer to RGB
2. Click Submit

**Expected Result:**
- Type changed
- Channel setup updates to RGB default
- Entity capabilities update

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
