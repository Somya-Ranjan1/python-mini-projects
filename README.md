# Python Mini Projects

A collection of Python projects built while learning backend development.

## Projects

### 1. Calculator
- Basic calculator with +, -, *, /, % operations
- Input validation using try/except
- Division by zero handling
- Loop to keep calculator running

### 2. Number Guessing Game
- Random number generation
- 5 attempts with high/low hints
- Input validation using try/except
- Tracks all guesse

### 3. Login System
- 3 attempt limit with lockout
- Separate validation for username and password
- Remaining attempts counter
- Account locked message

### 4. CLI Log Analyzer
- Collects log entries from user input
- Counts INFO, ERROR, WARNING occurrences
- Case-insensitive log matching
- Real-world DevOps concept

### 5. CLI Log Analyzer V2
A command-line based log analyzer with improved validation and structured output.

**Features:**
- Validates log input format (INFO, ERROR, WARNING)
- Uses dictionary-based counting for efficiency
- Displays percentage breakdown for each log level
- Handles edge cases using `.strip()` and input checks
- Provides clean and readable summary output

### 6. Port Status Checker
A CLI tool to identify common network ports and their services.

Features:
- Identifies ports like HTTP (80), HTTPS (443), SSH (22), FTP (21)
- Uses dictionary-based mapping for efficient lookup
- Continuous input using loop (interactive CLI tool)
- Input validation to prevent crashes
- Exit option for clean termination

Use Case:
Helps understand basic networking concepts and common service ports used in DevOps and backend systems.

### 7. JSON User Manager
A CLI tool to store user data in JSON format.

Features:
- Add users (name + email)
- Stores data in JSON file
- Demonstrates structured data handling

Use Case:
Useful for backend development and API data handling.

### 8. API Status Checker
A CLI tool to check the availability and response status of APIs.

Features:
- Sends HTTP requests to given URLs
- Displays response status codes (200, 404, etc.)
- Handles connection errors using try/except
- Continuous input with exit option

Use Case:
Useful for backend service testing, API monitoring, and DevOps health checks.

### 9. Multi API Health Checker
A CLI tool to monitor multiple APIs at once.

Features:
- Checks multiple API endpoints automatically
- Displays HTTP status codes
- Handles connection failures using try/except

Use Case:
Useful for DevOps monitoring and backend service health checks.

### 10. Environment Variable Checker

A CLI tool to read system environment variables.

Features:
- Retrieves environment variable values
- Handles missing variables
- Interactive CLI loop

	
### Skills Learned
- Python functions
- Error handling (try/except)
- Loops and conditionals
- f-strings
