# CF-1.3.6: RGBWW Fixture Type Tests

## Overview
Tests for RGBWW (RGB + Color Temperature) fixture type

## Test Cases (3)

---

### CF-1.3.6a: Add RGBWW Fixture

**Description:** Add an RGBWW fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test RGBWW"
2. Select Type: RGBWW
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details with temperature fields

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.6b: RGBWW with Default Settings

**Description:** Complete RGBWW with typical settings

**Preconditions:**
- Completed CF-1.3.6a

**Test Steps:**
1. Enter Min Temp: "2700K"
2. Enter Max Temp: "6500K"
3. Enter Channel Setup: "rgbch" (RGB + cool + hot)
4. Click Submit

**Expected Result:** Fixture added with 5 channels

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.6c: RGBWW with Dimmer

**Description:** Configure RGBWW with additional dimmer channel

**Preconditions:**
- Completed CF-1.3.6a (new fixture)

**Test Steps:**
1. Enter Min Temp: "3000K"
2. Enter Max Temp: "5600K"
3. Enter Channel Setup: "drgbch" (dimmer + RGB + cool + hot)
4. Click Submit

**Expected Result:** Fixture added with 6 channels

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
