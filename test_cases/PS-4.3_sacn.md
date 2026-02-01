# PS-4.3: sACN (E1.31) Protocol Tests

## Overview
Tests for sACN/E1.31 protocol

## Test Cases (1)

---

### PS-4.3.1: Default Port

**Description:** Verify default sACN port is used

**Preconditions:**
- None

**Test Steps:**
1. Start config flow
2. Enter Host: `192.168.1.100`
3. Select Protocol: sACN (E1.31)
4. Leave Port empty/default
5. Complete flow

**Expected Result:** Integration uses port 5568 (sACN standard)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
