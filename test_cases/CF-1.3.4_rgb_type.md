# CF-1.3.4: RGB Fixture Type Tests

## Overview
Tests for RGB fixture type in Config Flow Fixture Step

## Test Cases (5)

---

### CF-1.3.4a: Add RGB Fixture

**Description:** Add an RGB fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test RGB"
2. Select Type: RGB
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.4b: RGB Default Channel Order

**Description:** Complete RGB with default rgb order

**Preconditions:**
- Completed CF-1.3.4a

**Test Steps:**
1. In fixture_details step
2. Channel Setup shows default "rgb"
3. Click Submit

**Expected Result:** Fixture added with 3 channels (R-G-B order)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.4c: RGB Custom Order (BGR)

**Description:** Configure RGB with BGR channel order

**Preconditions:**
- Completed CF-1.3.4a (new fixture)

**Test Steps:**
1. Enter Channel Setup: "bgr"
2. Click Submit

**Expected Result:** Fixture added with B-G-R channel order

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.4d: RGB with Dimmer Channel

**Description:** Configure RGB with additional dimmer channel

**Preconditions:**
- Completed CF-1.3.4a (new fixture)

**Test Steps:**
1. Enter Channel Setup: "drgb" (dimmer + RGB)
2. Click Submit

**Expected Result:** Fixture added with 4 channels (D-R-G-B)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.4e: RGB 16-bit Channels

**Description:** Configure RGB with 16-bit resolution

**Preconditions:**
- Completed CF-1.3.4a (new fixture)

**Test Steps:**
1. Enter Channel Setup: "RGB" (uppercase = 16-bit)
2. Click Submit

**Expected Result:** Fixture added with 6 channels (2 per color, 16-bit)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
