# CF-1.3.5: RGBW Fixture Type Tests

## Overview
Tests for RGBW fixture type in Config Flow Fixture Step

## Test Cases (3)

---

### CF-1.3.5a: Add RGBW Fixture

**Description:** Add an RGBW fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test RGBW"
2. Select Type: RGBW
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.5b: RGBW Default Channel Order

**Description:** Complete RGBW with default rgbw order

**Preconditions:**
- Completed CF-1.3.5a

**Test Steps:**
1. In fixture_details step
2. Channel Setup shows default "rgbw"
3. Click Submit

**Expected Result:** Fixture added with 4 channels (R-G-B-W order)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.5c: RGBW Custom Order (WRGB)

**Description:** Configure RGBW with white-first channel order

**Preconditions:**
- Completed CF-1.3.5a (new fixture)

**Test Steps:**
1. Enter Channel Setup: "wrgb"
2. Click Submit

**Expected Result:** Fixture added with W-R-G-B channel order

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
