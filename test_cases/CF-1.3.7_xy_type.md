# CF-1.3.7: XY Color Space Fixture Type Tests

## Overview
Tests for XY Color Space (CIE 1931) fixture type

## Test Cases (2)

---

### CF-1.3.7a: Add XY Color Space Fixture

**Description:** Add an XY color space fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test XY"
2. Select Type: XY Color Space
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.7b: XY Default Settings

**Description:** Complete XY fixture with default settings

**Preconditions:**
- Completed CF-1.3.7a

**Test Steps:**
1. In fixture_details step
2. Channel Setup shows default "dxy" (dimmer + X + Y)
3. Click Submit

**Expected Result:** Fixture added with 3 channels (D-X-Y)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
