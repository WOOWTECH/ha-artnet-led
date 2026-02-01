# OF-2.1: Options Menu Tests

## Overview
Tests for the Options Flow main menu (`async_step_init`)

## Test Cases (4)

---

### OF-2.1.1: Open Options Menu

**Description:** Access the options menu from integration entry

**Preconditions:**
- Art-Net LED integration entry exists

**Test Steps:**
1. Navigate to Settings > Devices & Services
2. Find Art-Net LED integration
3. Click "CONFIGURE" on the entry

**Expected Result:** Options dialog opens showing 3 options:
- Edit Connection Settings
- Edit Universes
- Edit Fixtures

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.1.2: Select Connection Editor

**Description:** Navigate to connection settings editor

**Preconditions:**
- Options menu open

**Test Steps:**
1. Select "Edit Connection Settings"
2. Click Submit

**Expected Result:** Opens connection editor step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.1.3: Select Universe Manager

**Description:** Navigate to universe management

**Preconditions:**
- Options menu open

**Test Steps:**
1. Select "Edit Universes"
2. Click Submit

**Expected Result:** Opens universe manager step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.1.4: Select Fixture Manager

**Description:** Navigate to fixture management

**Preconditions:**
- Options menu open

**Test Steps:**
1. Select "Edit Fixtures"
2. Click Submit

**Expected Result:** Opens fixture manager step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
