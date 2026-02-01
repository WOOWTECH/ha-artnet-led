# CF-1.3.1: Binary Fixture Type Tests

## Overview
Tests for Binary fixture type in Config Flow Fixture Step

## Test Cases (2)

---

### CF-1.3.1a: Add Binary Fixture

**Description:** Add a binary (on/off) fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test Binary"
2. Select Type: Binary
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details step for advanced configuration

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.1b: Binary Fixture Details

**Description:** Complete binary fixture with default settings

**Preconditions:**
- Completed CF-1.3.1a

**Test Steps:**
1. In fixture_details step
2. Leave Channel Setup empty (default)
3. Click Submit

**Expected Result:** Fixture added successfully, returns to fixture list

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
