# OF-2.2: Connection Editing Tests

## Overview
Tests for editing connection settings via Options Flow (`async_step_connection`)

## Test Cases (5)

---

### OF-2.2.1: View Existing Connection

**Description:** Verify existing settings are pre-populated

**Preconditions:**
- Integration configured with known settings
- In connection editor

**Test Steps:**
1. Open connection editor from options menu
2. Examine pre-filled values

**Expected Result:** All fields show current configuration values (host, port, protocol, etc.)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.2.2: Change Host Address

**Description:** Update the host IP address

**Preconditions:**
- In connection editor

**Test Steps:**
1. Change Host from `192.168.1.100` to `192.168.1.200`
2. Click Submit

**Expected Result:**
- Settings saved
- Integration reloads
- New host used for DMX output

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.2.3: Change Protocol

**Description:** Switch from Art-Net to sACN protocol

**Preconditions:**
- In connection editor
- Currently using Art-Net Direct

**Test Steps:**
1. Change Protocol to "sACN (E1.31)"
2. Click Submit

**Expected Result:**
- Settings saved
- Port may auto-update to 5568
- Integration reloads with new protocol

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.2.4: Invalid Host

**Description:** Verify validation for invalid host

**Preconditions:**
- In connection editor

**Test Steps:**
1. Change Host to "invalid"
2. Click Submit

**Expected Result:** Error: "Invalid host" or validation error

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### OF-2.2.5: Change FPS

**Description:** Update the maximum FPS setting

**Preconditions:**
- In connection editor

**Test Steps:**
1. Change Max FPS from 25 to 30
2. Click Submit

**Expected Result:** Settings saved successfully

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
