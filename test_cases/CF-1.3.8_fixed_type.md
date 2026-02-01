# CF-1.3.8: Fixed Output Fixture Type Tests

## Overview
Tests for Fixed Output fixture type (constant DMX values)

## Test Cases (4)

---

### CF-1.3.8a: Add Fixed Output Fixture

**Description:** Add a fixed output fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test Fixed"
2. Select Type: Fixed Output
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details with channel count field

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.8b: Fixed 3 Channels

**Description:** Configure fixed output with 3 channels

**Preconditions:**
- Completed CF-1.3.8a

**Test Steps:**
1. Enter Channel Count: 3
2. Click Submit

**Expected Result:** Fixture added with 3 fixed channels

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.8c: Fixed Invalid Count (Zero)

**Description:** Verify error for zero channel count

**Preconditions:**
- Completed CF-1.3.8a (new fixture)

**Test Steps:**
1. Enter Channel Count: 0
2. Click Submit

**Expected Result:** Error: "Invalid channel count"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.8d: Fixed Maximum Channels

**Description:** Configure fixed output with maximum channels

**Preconditions:**
- Completed CF-1.3.8a (new fixture)

**Test Steps:**
1. Enter Channel Count: 512
2. Click Submit

**Expected Result:** Fixture added with 512 channels

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
