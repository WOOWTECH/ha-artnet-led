# PS-4.1: Art-Net Direct Protocol Tests

## Overview
Tests for Art-Net Direct (unicast UDP port 6454) protocol

## Test Cases (2)

---

### PS-4.1.1: Default Port

**Description:** Verify default port is used when not specified

**Preconditions:**
- None

**Test Steps:**
1. Start config flow
2. Enter Host: `192.168.1.100`
3. Select Protocol: Art-Net Direct
4. Leave Port empty/default
5. Complete flow

**Expected Result:** Integration uses port 6454 (Art-Net standard)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### PS-4.1.2: Custom Port

**Description:** Verify custom port can be specified

**Preconditions:**
- None

**Test Steps:**
1. Start config flow
2. Enter Host: `192.168.1.100`
3. Select Protocol: Art-Net Direct
4. Enter Port: 6455
5. Complete flow

**Expected Result:** Integration uses port 6455

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
