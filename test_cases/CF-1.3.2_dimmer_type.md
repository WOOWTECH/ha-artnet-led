# CF-1.3.2: Dimmer Fixture Type Tests

## Overview
Tests for Dimmer fixture type in Config Flow Fixture Step

## Test Cases (3)

---

### CF-1.3.2a: Add Dimmer Fixture

**Description:** Add a dimmer fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test Dimmer"
2. Select Type: Dimmer
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.2b: Dimmer Default Channel Setup

**Description:** Complete dimmer with default 8-bit setup

**Preconditions:**
- Completed CF-1.3.2a

**Test Steps:**
1. In fixture_details step
2. Channel Setup shows default "d" (8-bit dimmer)
3. Click Submit

**Expected Result:** Fixture added with 1 DMX channel (8-bit)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.2c: Dimmer 16-bit Channel

**Description:** Configure dimmer with 16-bit resolution

**Preconditions:**
- Completed CF-1.3.2a (new fixture)

**Test Steps:**
1. In fixture_details step
2. Enter Channel Setup: "D" (16-bit dimmer)
3. Click Submit

**Expected Result:** Fixture added with 2 DMX channels (16-bit)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
