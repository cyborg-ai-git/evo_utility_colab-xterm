# Design Document

## Overview

The command injection fix involves modifying the `%xterm` magic command parser in `colabxterm/notebook.py` to properly handle the `command` parameter. The current implementation clears all parsed arguments after extracting `height` and `port`, which prevents command arguments from being passed to the underlying xterm process.

## Architecture

The fix will modify the argument parsing flow in the `_xterm_magic` function:

1. **Current Flow**: Parse all arguments → Extract height/port → Clear arguments → Start xterm with empty command list
2. **New Flow**: Parse all arguments → Extract height/port → Extract command → Start xterm with command arguments

The change is isolated to the `notebook.py` file and maintains backward compatibility with existing usage patterns.

## Components and Interfaces

### Modified Components

#### `_xterm_magic` function in `colabxterm/notebook.py`
- **Input**: Magic command line arguments (e.g., `height=1000 port=10002 command="ls -l"`)
- **Processing**: Parse parameters while preserving command arguments
- **Output**: Properly formatted command list for the xterm process

### Parameter Parsing Logic

The function will handle three types of parameters:
1. **height**: Integer value for terminal height
2. **port**: Integer value for server port  
3. **command**: String value for the command to execute

### Command Format Support

The design supports multiple command formats:
- Simple commands: `command="ls"`
- Commands with arguments: `command="ls -l"`
- Commands with pipes: `command="ps aux | grep python"`
- Commands with quotes: `command="echo 'hello world'"`

## Data Models

### Parameter Structure
```python
{
    'height': int,      # Terminal height (default: 800)
    'port': int,        # Server port (default: 10000)  
    'command': str      # Command to execute (default: None)
}
```

### Command Processing
- Commands will be parsed using `shlex.split()` to handle proper escaping
- Empty or None commands will result in default shell behavior
- Commands will be passed as a list to maintain argument separation

## Error Handling

### Invalid Command Scenarios
1. **Malformed command syntax**: Log warning and fall back to default shell
2. **Command execution failure**: Let the underlying shell handle the error naturally
3. **Parameter parsing errors**: Continue with default values for invalid parameters

### Security Considerations
- Use `shlex.split()` for safe command parsing
- No additional shell escaping needed as commands are passed directly to `PtyProcess.spawn()`
- Maintain existing security model of the underlying terminal

## Testing Strategy

### Unit Tests
1. **Parameter parsing tests**:
   - Test extraction of height, port, and command parameters
   - Test handling of various command formats
   - Test backward compatibility with existing parameter formats

2. **Command processing tests**:
   - Test simple commands
   - Test commands with arguments and special characters
   - Test empty/None command handling

3. **Integration tests**:
   - Test full magic command execution with various parameter combinations
   - Test that existing functionality remains unchanged

### Manual Testing Scenarios
1. `%xterm command="ls -l"` - Simple command execution
2. `%xterm height=1000 port=10002 command="ps aux"` - Multiple parameters
3. `%xterm height=500 command="echo 'test with quotes'"` - Commands with quotes
4. `%xterm` - Ensure existing behavior unchanged
5. `%xterm height=800` - Ensure partial parameter usage works

## Implementation Details

### Code Changes Required

1. **Modify argument parsing loop** to extract command parameter
2. **Preserve command arguments** instead of clearing parsed_args
3. **Handle command parameter** alongside existing height/port logic
4. **Pass processed command** to manager.start()

### Backward Compatibility

- All existing usage patterns continue to work unchanged
- New command parameter is optional
- Default behavior (no command) remains identical to current implementation
- Existing parameter parsing for height and port is preserved