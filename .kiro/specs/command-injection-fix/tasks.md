# Implementation Plan

- [x] 1. Modify parameter parsing logic in _xterm_magic function
  - Update the parameter parsing loop to extract command parameter alongside height and port
  - Preserve command arguments instead of clearing parsed_args list
  - Handle command parameter with proper string parsing using shlex
  - _Requirements: 1.1, 1.2, 2.1_

- [ ] 2. Implement command argument processing
  - Add logic to process the command parameter and convert it to argument list
  - Handle empty/None command cases to maintain default shell behavior
  - Ensure proper escaping and argument separation for complex commands
  - _Requirements: 1.3, 2.2, 3.4_

- [ ] 3. Update manager.start() call with processed command arguments
  - Modify the call to manager.start() to pass the processed command arguments
  - Ensure backward compatibility when no command is provided
  - Test that the command arguments flow correctly through to the xterm process
  - _Requirements: 1.1, 3.1, 3.2_

- [ ] 4. Add error handling for command parsing
  - Implement graceful handling of malformed command syntax
  - Add fallback behavior for invalid commands
  - Ensure security by using safe parsing methods
  - _Requirements: 2.3, 2.2_

- [ ] 5. Create unit tests for parameter parsing
  - Write tests for extracting height, port, and command parameters
  - Test various command formats including quotes and special characters
  - Test backward compatibility with existing parameter usage
  - _Requirements: 1.2, 1.3, 3.3_

- [ ] 6. Create integration tests for full magic command execution
  - Test complete workflow from magic command to terminal execution
  - Verify that commands execute correctly in the spawned terminal
  - Test multiple parameter combinations work together
  - _Requirements: 1.1, 1.2, 3.3_

- [ ] 7. Validate backward compatibility
  - Test that existing usage patterns continue to work unchanged
  - Verify default behavior when no command parameter is provided
  - Ensure existing height and port parameters still function correctly
  - _Requirements: 3.1, 3.2, 3.4_