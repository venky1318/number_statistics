# Number Statistics — Test Cases

## Testing Objective

To verify that the program correctly separates even and odd integers, identifies the largest and smallest numbers, and handles invalid input.

## Test Cases

| Test ID | Input | Expected Result |
|---|---|---|
| TC01 | `[12, 7, 18, 5, 0, -3, 22, 9]` | Even: `[12, 18, 0, 22]`; odd: `[7, 5, -3, 9]` |
| TC02 | `[2, 4, 6]` | All numbers even |
| TC03 | `[1, 3, 5]` | All numbers odd |
| TC04 | `[-4, -3, 0, 7]` | Even: `[-4, 0]`; odd: `[-3, 7]` |
| TC05 | `[5]` | Largest and smallest are both 5 |
| TC06 | `[8, 8, 8]` | All numbers even; largest and smallest are 8 |
| TC07 | `[]` | Display an empty-list error |
| TC08 | `[2, 3.5, 4]` | Reject non-integer input |
| TC09 | `[2, "five", 4]` | Reject non-integer input |
| TC10 | `[0]` | Even list is `[0]`; odd list is empty |

## Test Execution Record

Run each test by temporarily changing the `numbers` list in the program. Record the actual result and mark each test as Pass or Fail.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC10 | Record after execution | Pending |

## Testing Conclusion

Testing should confirm that the program classifies integers correctly and identifies the maximum and minimum values. Empty lists and invalid values should produce clear error messages.

Only mark a test as passed after verifying its actual output.
