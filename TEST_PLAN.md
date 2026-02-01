# Art-Net LED Integration Test Plan

## Overview
This test plan covers comprehensive testing of the Config Flow and Options Flow for the Art-Net LED Home Assistant integration.

## Test Environment
- Home Assistant Core: Development environment at `/Users/alanlin/core`
- Integration Location: `/Users/alanlin/core/custom_components/artnet_led/`
- URL: `http://localhost:8123/config/integrations/integration/artnet_led`

---

## Part 1: Config Flow Tests

### 1.1 Connection Step (Step 1: `async_step_user`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.1.1 | Valid Art-Net connection | Host: `192.168.1.100`, Protocol: Art-Net Direct, Port: (default) | Proceeds to Universe step | |
| CF-1.1.2 | Valid sACN connection | Host: `192.168.1.100`, Protocol: sACN (E1.31), Port: 5568 | Proceeds to Universe step | |
| CF-1.1.3 | Valid KiNet connection | Host: `192.168.1.100`, Protocol: KiNet PDS, Port: 6038 | Proceeds to Universe step | |
| CF-1.1.4 | Valid Art-Net Broadcast | Host: `192.168.1.255`, Protocol: Art-Net Broadcast | Proceeds to Universe step | |
| CF-1.1.5 | Invalid IP format | Host: `invalid.ip`, Protocol: Art-Net Direct | Error: "Invalid IPv4 address" | |
| CF-1.1.6 | Invalid port (too low) | Host: `192.168.1.100`, Port: 0 | Error: "Invalid port" | |
| CF-1.1.7 | Invalid port (too high) | Host: `192.168.1.100`, Port: 70000 | Error: "Invalid port" | |
| CF-1.1.8 | Custom FPS | Host: `192.168.1.100`, Max FPS: 60 | Proceeds to Universe step | |
| CF-1.1.9 | Custom Refresh | Host: `192.168.1.100`, Refresh Every: 5.0 | Proceeds to Universe step | |
| CF-1.1.10 | With host override | Host: `192.168.1.100`, Host Override: `192.168.1.200` | Proceeds to Universe step | |
| CF-1.1.11 | Invalid host override | Host: `192.168.1.100`, Host Override: `invalid` | Error on host_override field | |

### 1.2 Universe Step (Step 2: `async_step_universe`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.2.1 | Add single universe | Universe: 1, Action: "Add Universe" | Universe added, form refreshes | |
| CF-1.2.2 | Add multiple universes | Universe: 1, then 2, then 3 | All universes shown in placeholder | |
| CF-1.2.3 | Skip to fixtures (auto-create) | No universes added, Action: "Continue to Fixtures" | Universe 1 auto-created | |
| CF-1.2.4 | Skip to fixtures (with universes) | Add Universe 1, Action: "Continue to Fixtures" | Proceeds to Fixture step | |
| CF-1.2.5 | Duplicate universe | Add Universe 1 twice | Error: "Duplicate universe" | |
| CF-1.2.6 | Invalid universe (too low) | Universe: 0 | Error: "Invalid universe" | |
| CF-1.2.7 | Invalid universe (too high) | Universe: 65536 | Error: "Invalid universe" | |
| CF-1.2.8 | With output correction | Universe: 1, Output Correction: "sRGB" | Universe added with correction | |
| CF-1.2.9 | Send partial universe | Universe: 1, Send Partial: checked | Universe added with partial flag | |

### 1.3 Fixture Step (Step 3: `async_step_fixture`)

#### 1.3.1 Binary Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.1a | Add binary fixture | Name: "Test Binary", Type: Binary, Channel: 1 | Shows fixture_details step | |
| CF-1.3.1b | Binary details | Channel Setup: (default empty) | Fixture added | |

#### 1.3.2 Dimmer Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.2a | Add dimmer fixture | Name: "Test Dimmer", Type: Dimmer, Channel: 1 | Shows fixture_details step | |
| CF-1.3.2b | Dimmer details | Channel Setup: "d" (default) | Fixture added | |
| CF-1.3.2c | Dimmer custom channel | Channel Setup: "D" (16-bit) | Fixture added with 16-bit | |

#### 1.3.3 Color Temperature Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.3a | Add color temp fixture | Name: "Test CCT", Type: Color Temperature, Channel: 1 | Shows fixture_details with temp fields | |
| CF-1.3.3b | Color temp details | Min Temp: "2700K", Max Temp: "6500K", Channel Setup: "ch" | Fixture added | |
| CF-1.3.3c | Invalid min temp format | Min Temp: "2700" (no K) | Error: "Invalid temperature format" | |
| CF-1.3.3d | Empty min temp | Min Temp: "" | Error: "Temperature required" | |
| CF-1.3.3e | Custom channel order | Channel Setup: "hc" (reversed) | Fixture added with custom order | |

#### 1.3.4 RGB Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.4a | Add RGB fixture | Name: "Test RGB", Type: RGB, Channel: 1 | Shows fixture_details step | |
| CF-1.3.4b | RGB details default | Channel Setup: "rgb" (default) | Fixture added | |
| CF-1.3.4c | RGB custom order | Channel Setup: "bgr" | Fixture added with BGR order | |
| CF-1.3.4d | RGB with dimmer | Channel Setup: "drgb" | Fixture added with 4 channels | |
| CF-1.3.4e | RGB 16-bit channels | Channel Setup: "RGB" | Fixture added with 16-bit | |

#### 1.3.5 RGBW Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.5a | Add RGBW fixture | Name: "Test RGBW", Type: RGBW, Channel: 1 | Shows fixture_details step | |
| CF-1.3.5b | RGBW details default | Channel Setup: "rgbw" (default) | Fixture added | |
| CF-1.3.5c | RGBW custom order | Channel Setup: "wrgb" | Fixture added with WRGB order | |

#### 1.3.6 RGBWW Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.6a | Add RGBWW fixture | Name: "Test RGBWW", Type: RGBWW, Channel: 1 | Shows fixture_details with temp fields | |
| CF-1.3.6b | RGBWW details | Min: "2700K", Max: "6500K", Setup: "rgbch" | Fixture added | |
| CF-1.3.6c | RGBWW custom | Min: "3000K", Max: "5600K", Setup: "drgbch" | Fixture added with dimmer | |

#### 1.3.7 XY Color Space Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.7a | Add XY fixture | Name: "Test XY", Type: XY Color Space, Channel: 1 | Shows fixture_details step | |
| CF-1.3.7b | XY details default | Channel Setup: "dxy" (default) | Fixture added | |

#### 1.3.8 Fixed Output Type

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.8a | Add fixed fixture | Name: "Test Fixed", Type: Fixed Output, Channel: 1 | Shows fixture_details with channel count | |
| CF-1.3.8b | Fixed 3 channels | Channel Count: 3 | Fixture added with 3 channels | |
| CF-1.3.8c | Fixed invalid count | Channel Count: 0 | Error: "Invalid channel count" | |
| CF-1.3.8d | Fixed max channels | Channel Count: 512 | Fixture added with 512 channels | |

#### 1.3.9 Fixture Validation

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.3.9a | Missing fixture name | Name: "", Type: Dimmer | Error: "Name required" | |
| CF-1.3.9b | Invalid channel (too low) | Channel: 0 | Error: "Invalid channel" | |
| CF-1.3.9c | Invalid channel (too high) | Channel: 513 | Error: "Invalid channel" | |
| CF-1.3.9d | Done with no fixtures | Action: "Done - Review" (no fixtures) | Error: "No fixtures" | |

### 1.4 Review Step (Step 4: `async_step_review`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| CF-1.4.1 | Review summary correct | Add 1 universe, 2 fixtures | Summary shows all details | |
| CF-1.4.2 | Go back to edit | Action: "Go Back to Edit" | Returns to fixture step | |
| CF-1.4.3 | Create integration | Action: "Create Integration" | Entry created successfully | |
| CF-1.4.4 | Duplicate entry check | Create same host:port twice | Error: "Already configured" | |

---

## Part 2: Options Flow Tests

### 2.1 Options Menu (`async_step_init`)

| Test ID | Test Case | Action | Expected Result | Status |
|---------|-----------|--------|-----------------|--------|
| OF-2.1.1 | Open options menu | Click CONFIGURE on entry | Shows 3 options | |
| OF-2.1.2 | Select connection | "Edit Connection Settings" | Opens connection editor | |
| OF-2.1.3 | Select universes | "Edit Universes" | Opens universe manager | |
| OF-2.1.4 | Select fixtures | "Edit Fixtures" | Opens fixture manager | |

### 2.2 Connection Editing (`async_step_connection`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| OF-2.2.1 | View existing connection | Open connection editor | Pre-filled with current values | |
| OF-2.2.2 | Change host | Host: `192.168.1.200` | Saved, integration reloads | |
| OF-2.2.3 | Change protocol | Protocol: sACN | Saved, port updates | |
| OF-2.2.4 | Invalid host | Host: `invalid` | Error: "Invalid host" | |
| OF-2.2.5 | Change FPS | Max FPS: 30 | Saved successfully | |

### 2.3 Universe Management (`async_step_universe`)

| Test ID | Test Case | Action | Expected Result | Status |
|---------|-----------|--------|-----------------|--------|
| OF-2.3.1 | List universes | Open universe manager | Shows all configured universes | |
| OF-2.3.2 | Add new universe | "Add New Universe" | Opens universe edit form | |
| OF-2.3.3 | Edit universe | "Edit Universe X" | Opens form with current values | |
| OF-2.3.4 | Delete universe | "Delete Universe X" | Universe and fixtures removed | |
| OF-2.3.5 | Back to menu | "Back to Menu" | Returns to options menu | |

### 2.4 Universe Editing (`async_step_universe_edit`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| OF-2.4.1 | Add universe 2 | Universe: 2 | Universe 2 created | |
| OF-2.4.2 | Change universe number | Universe 1 -> 5 | Fixtures moved to universe 5 | |
| OF-2.4.3 | Change output correction | sRGB -> Linear | Universe updated | |
| OF-2.4.4 | Toggle partial universe | Enabled/Disabled | Universe updated | |

### 2.5 Fixture Management (`async_step_fixture`)

| Test ID | Test Case | Action | Expected Result | Status |
|---------|-----------|--------|-----------------|--------|
| OF-2.5.1 | List fixtures | Open fixture manager | Shows all fixtures with details | |
| OF-2.5.2 | Add new fixture | "Add New Fixture" | Opens fixture add form | |
| OF-2.5.3 | Edit fixture | "Edit: Fixture Name" | Opens form with current values | |
| OF-2.5.4 | Delete fixture | "Delete: Fixture Name" | Fixture removed | |
| OF-2.5.5 | Back to menu | "Back to Menu" | Returns to options menu | |

### 2.6 Fixture Adding (`async_step_fixture_add`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| OF-2.6.1 | Add dimmer | Name: "New Dimmer", Type: Dimmer, Ch: 10 | Fixture added | |
| OF-2.6.2 | Add to different universe | Universe: 2 | Fixture in universe 2 | |
| OF-2.6.3 | Missing name | Name: "" | Error: "Name required" | |

### 2.7 Fixture Editing (`async_step_fixture_edit`)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| OF-2.7.1 | View existing fixture | Open edit for fixture | Pre-filled with current values | |
| OF-2.7.2 | Change name | Name: "Renamed Fixture" | Fixture updated | |
| OF-2.7.3 | Change channel | Channel: 20 | Fixture updated | |
| OF-2.7.4 | Change universe | Universe: 2 | Fixture moved to universe 2 | |
| OF-2.7.5 | Change type | Dimmer -> RGB | Type changed (channel setup updates) | |

---

## Part 3: Entity Verification Tests

| Test ID | Test Case | Steps | Expected Result | Status |
|---------|-----------|-------|-----------------|--------|
| EV-3.1 | Entity appears after config | Create integration with 1 fixture | Light entity appears in dashboard | |
| EV-3.2 | Multiple entities | Create with 3 fixtures | 3 light entities appear | |
| EV-3.3 | Entity name matches | Create fixture "Living Room" | Entity named "Living Room" | |
| EV-3.4 | Entity reload after edit | Edit fixture via options | Entity updates | |
| EV-3.5 | Entity removed after delete | Delete fixture via options | Entity disappears | |

---

## Part 4: Protocol-Specific Tests

### 4.1 Art-Net Direct (UDP 6454)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| PS-4.1.1 | Default port | Protocol: Art-Net Direct, Port: empty | Uses port 6454 | |
| PS-4.1.2 | Custom port | Protocol: Art-Net Direct, Port: 6455 | Uses port 6455 | |

### 4.2 Art-Net Broadcast

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| PS-4.2.1 | Broadcast address | Host: `192.168.1.255` | Accepted | |

### 4.3 sACN (E1.31)

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| PS-4.3.1 | Default port | Protocol: sACN, Port: empty | Uses port 5568 | |

### 4.4 KiNet

| Test ID | Test Case | Input Values | Expected Result | Status |
|---------|-----------|--------------|-----------------|--------|
| PS-4.4.1 | Default port | Protocol: KiNet PDS, Port: empty | Uses port 6038 | |

---

## Test Execution Log

### Session: [DATE]

| Test ID | Tester | Result | Notes/Screenshot |
|---------|--------|--------|------------------|
| | | | |

---

## Channel Setup Code Reference

| Code | Meaning | Bit Depth |
|------|---------|-----------|
| `d` | Dimmer | 8-bit |
| `D` | Dimmer | 16-bit |
| `r` | Red | 8-bit |
| `R` | Red | 16-bit |
| `g` | Green | 8-bit |
| `G` | Green | 16-bit |
| `b` | Blue | 8-bit |
| `B` | Blue | 16-bit |
| `w` | White | 8-bit |
| `W` | White | 16-bit |
| `c` | Cool White | 8-bit |
| `C` | Cool White | 16-bit |
| `h` | Hot/Warm White | 8-bit |
| `H` | Hot/Warm White | 16-bit |
| `x` | CIE X | 8-bit |
| `X` | CIE X | 16-bit |
| `y` | CIE Y | 8-bit |
| `Y` | CIE Y | 16-bit |

---

## Notes

- All tests should be run with browser automation for reproducibility
- Screenshots should be captured at key steps
- Test with both valid and invalid inputs to verify error handling
- Entity verification requires checking the Home Assistant dashboard after integration setup
