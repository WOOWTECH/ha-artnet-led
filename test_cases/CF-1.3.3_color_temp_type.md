# CF-1.3.3: Color Temperature Fixture Type Tests

## Overview
Tests for Color Temperature (CCT/Tunable White) fixture type

## Test Cases (5)

---

### CF-1.3.3a: Add Color Temperature Fixture

**Description:** Add a color temperature fixture

**Preconditions:**
- Completed connection and universe steps
- In Fixture step

**Test Steps:**
1. Enter Name: "Test CCT"
2. Select Type: Color Temperature
3. Enter Channel: 1
4. Select Action: "Add Fixture"
5. Click Submit

**Expected Result:** Shows fixture_details with temperature fields (Min/Max Kelvin)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.3b: Color Temp with Valid Settings

**Description:** Complete color temp fixture with valid temperature range

**Preconditions:**
- Completed CF-1.3.3a

**Test Steps:**
1. Enter Min Temp: "2700K"
2. Enter Max Temp: "6500K"
3. Enter Channel Setup: "ch" (cool/hot)
4. Click Submit

**Expected Result:** Fixture added with 2 channels, temp range 2700K-6500K

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.3c: Invalid Min Temp Format

**Description:** Verify error for temperature without K suffix

**Preconditions:**
- Completed CF-1.3.3a (new fixture)

**Test Steps:**
1. Enter Min Temp: "2700" (missing K)
2. Enter Max Temp: "6500K"
3. Click Submit

**Expected Result:** Error: "Invalid temperature format" or similar

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.3d: Empty Min Temp

**Description:** Verify error when min temp is empty

**Preconditions:**
- Completed CF-1.3.3a (new fixture)

**Test Steps:**
1. Leave Min Temp empty
2. Enter Max Temp: "6500K"
3. Click Submit

**Expected Result:** Error: "Temperature required" or validation error

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.3.3e: Custom Channel Order

**Description:** Configure color temp with reversed channel order

**Preconditions:**
- Completed CF-1.3.3a (new fixture)

**Test Steps:**
1. Enter Min Temp: "2700K"
2. Enter Max Temp: "6500K"
3. Enter Channel Setup: "hc" (hot first, then cool)
4. Click Submit

**Expected Result:** Fixture added with reversed channel order

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
