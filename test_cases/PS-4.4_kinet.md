# PS-4.4: KiNet Protocol Tests

## Overview
Tests for KiNet PDS protocol

## Test Cases (1)

---

### PS-4.4.1: Default Port

**Description:** Verify default KiNet port is used

**Preconditions:**
- None

**Test Steps:**
1. Start config flow
2. Enter Host: `192.168.1.100`
3. Select Protocol: KiNet PDS
4. Leave Port empty/default
5. Complete flow

**Expected Result:** Integration uses port 6038 (KiNet standard)

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
