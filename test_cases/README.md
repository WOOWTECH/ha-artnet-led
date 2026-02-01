# Art-Net LED Integration Test Cases

## Summary

**Total Test Cases: 96**

| Category | Count |
|----------|-------|
| Part 1: Config Flow Tests | 55 |
| Part 2: Options Flow Tests | 31 |
| Part 3: Entity Verification Tests | 5 |
| Part 4: Protocol-Specific Tests | 5 |

## Test Case Files

### Part 1: Config Flow (CF-*)
- `CF-1.1_connection_step.md` - Connection Step Tests (11 cases)
- `CF-1.2_universe_step.md` - Universe Step Tests (9 cases)
- `CF-1.3.1_binary_type.md` - Binary Fixture Tests (2 cases)
- `CF-1.3.2_dimmer_type.md` - Dimmer Fixture Tests (3 cases)
- `CF-1.3.3_color_temp_type.md` - Color Temperature Fixture Tests (5 cases)
- `CF-1.3.4_rgb_type.md` - RGB Fixture Tests (5 cases)
- `CF-1.3.5_rgbw_type.md` - RGBW Fixture Tests (3 cases)
- `CF-1.3.6_rgbww_type.md` - RGBWW Fixture Tests (3 cases)
- `CF-1.3.7_xy_type.md` - XY Color Space Fixture Tests (2 cases)
- `CF-1.3.8_fixed_type.md` - Fixed Output Fixture Tests (4 cases)
- `CF-1.3.9_validation.md` - Fixture Validation Tests (4 cases)
- `CF-1.4_review_step.md` - Review Step Tests (4 cases)

### Part 2: Options Flow (OF-*)
- `OF-2.1_options_menu.md` - Options Menu Tests (4 cases)
- `OF-2.2_connection_editing.md` - Connection Editing Tests (5 cases)
- `OF-2.3_universe_management.md` - Universe Management Tests (5 cases)
- `OF-2.4_universe_editing.md` - Universe Editing Tests (4 cases)
- `OF-2.5_fixture_management.md` - Fixture Management Tests (5 cases)
- `OF-2.6_fixture_adding.md` - Fixture Adding Tests (3 cases)
- `OF-2.7_fixture_editing.md` - Fixture Editing Tests (5 cases)

### Part 3: Entity Verification (EV-*)
- `EV-3_entity_verification.md` - Entity Verification Tests (5 cases)

### Part 4: Protocol-Specific (PS-*)
- `PS-4.1_artnet_direct.md` - Art-Net Direct Tests (2 cases)
- `PS-4.2_artnet_broadcast.md` - Art-Net Broadcast Tests (1 case)
- `PS-4.3_sacn.md` - sACN (E1.31) Tests (1 case)
- `PS-4.4_kinet.md` - KiNet Tests (1 case)

## Test Execution

Each test case file contains:
- Test ID
- Description
- Preconditions
- Test Steps
- Expected Results
- Status field for tracking

## Running Tests

1. Start Home Assistant: `/Users/alanlin/core/venv/bin/python3 -m homeassistant -c /Users/alanlin/core/config`
2. Access UI: `http://localhost:8123/config/integrations/integration/artnet_led`
3. Execute test cases in order
4. Record results in each test case file
