# Test Result: OF-2.5.1 - Delete Fixture

## Test Information
- **Test ID:** OF-2.5.1
- **Test Name:** Delete Fixture via Options Flow
- **Category:** Options Flow > Fixture Management > Delete
- **Executed By:** Automated Test
- **Execution Date:** 2026-02-01
- **Status:** ⚠️ BUG FOUND (Same root cause as OF-2.4.5)

## Test Objective
Verify that deleting a fixture via Options Flow removes the fixture.

## Test Steps Executed

### Step 1: Navigate to Manage Fixtures
- **Path:** CONFIGURE → Edit Fixtures → Manage Fixtures
- **Initial state:** "1 fixture(s) configured"
- **Fixture:** Test LED Strip (Dimmer, Ch: 1)
- **Screenshot:** `OF-2.5.1_delete_fixture_selected.png`

### Step 2: Select Delete Fixture
- **Action:** Select "Delete: Test LED Strip"
- **Click:** SUBMIT button

### Step 3: Verify Immediate Result
- **Dialog shows:** "0 fixture(s) configured"
- **Options:** Only "Add New Fixture" and "Back to Menu"
- **Screenshot:** `OF-2.5.1_fixture_deleted.png`

### Step 4: Reload Integration
- **Action:** Menu → Reload
- **Result:** "The integration was reloaded"

### Step 5: Check Fixture Status After Reload
- **Action:** Navigate back to Manage Fixtures
- **Result:** Shows "1 fixture(s) configured" again
- **Fixture returned:** Test LED Strip (Dimmer, Ch: 1)
- **Screenshot:** `OF-2.5.2_delete_not_persisted.png`

## Expected Result
- Fixture should be permanently deleted
- After reload, fixture should remain deleted

## Actual Result
⚠️ **BUG:** Delete does not persist:
- Delete appears to work in the current session
- After integration reload, fixture returns
- Same root cause as OF-2.4.5 (fixture add not persisted)

## Root Cause
Options Flow is not calling `async_update_entry()` to save changes to config entry.

## Impact
- **Severity:** High/Critical
- **User Impact:** Users cannot delete fixtures via Options Flow
- **Same root cause as:** OF-2.4.5 (fixture persistence bug)

## Screenshots
- `OF-2.5.1_delete_fixture_selected.png` - Delete option selected
- `OF-2.5.1_fixture_deleted.png` - After delete (0 fixtures)
- `OF-2.5.2_delete_not_persisted.png` - After reload (fixture returned)

