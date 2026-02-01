# CF-1.1: Connection Step Tests

## Overview
Tests for the first step of Config Flow: Connection Settings (`async_step_user`)

## Test Cases (11)

---

### CF-1.1.1: Valid Art-Net Direct Connection

**Description:** Create integration with valid Art-Net Direct settings

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Settings > Devices & Services
2. Click "Add Integration"
3. Search for "Art-Net LED"
4. Enter: Host: `192.168.1.100`, Protocol: Art-Net Direct, Port: (default 6454)
5. Click Submit

**Expected Result:** Proceeds to Universe step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.2: Valid sACN Connection

**Description:** Create integration with sACN (E1.31) protocol

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Protocol: sACN (E1.31), Port: 5568
3. Click Submit

**Expected Result:** Proceeds to Universe step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.3: Valid KiNet Connection

**Description:** Create integration with KiNet PDS protocol

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Protocol: KiNet PDS, Port: 6038
3. Click Submit

**Expected Result:** Proceeds to Universe step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.4: Valid Art-Net Broadcast

**Description:** Create integration with broadcast address

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.255`, Protocol: Art-Net Broadcast
3. Click Submit

**Expected Result:** Proceeds to Universe step

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.5: Invalid IP Format

**Description:** Verify error handling for invalid IP address

**Preconditions:**
- None

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `invalid.ip`, Protocol: Art-Net Direct
3. Click Submit

**Expected Result:** Error message: "Invalid IPv4 address"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.6: Invalid Port (Too Low)

**Description:** Verify error handling for port below valid range

**Preconditions:**
- None

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Port: 0
3. Click Submit

**Expected Result:** Error message: "Invalid port"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.7: Invalid Port (Too High)

**Description:** Verify error handling for port above valid range

**Preconditions:**
- None

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Port: 70000
3. Click Submit

**Expected Result:** Error message: "Invalid port"

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.8: Custom FPS Setting

**Description:** Create integration with custom Max FPS value

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Max FPS: 60
3. Click Submit

**Expected Result:** Proceeds to Universe step with FPS=60 saved

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.9: Custom Refresh Interval

**Description:** Create integration with custom refresh interval

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Refresh Every: 5.0
3. Click Submit

**Expected Result:** Proceeds to Universe step with refresh=5.0 saved

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.10: With Host Override

**Description:** Create integration with host override for network translation

**Preconditions:**
- No existing artnet_led integration for this host

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Host Override: `192.168.1.200`
3. Click Submit

**Expected Result:** Proceeds to Universe step with override saved

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**

---

### CF-1.1.11: Invalid Host Override

**Description:** Verify error handling for invalid host override

**Preconditions:**
- None

**Test Steps:**
1. Navigate to Add Integration > Art-Net LED
2. Enter: Host: `192.168.1.100`, Host Override: `invalid`
3. Click Submit

**Expected Result:** Error on host_override field

**Status:** [ ] Pass [ ] Fail [ ] Blocked

**Notes:**
