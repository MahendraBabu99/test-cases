Project: Piston-Subprocess Code Runner
A Python-based utility to execute and test code snippets across multiple languages using the Piston API. This project demonstrates how to manage local file operations and environment preparation using Python’s built-in automation while offloading execution to a remote sandboxed environment.

🛠 Features
Remote Execution: Uses the Piston API to run code in 70+ languages without needing local compilers or runtimes.

Subprocess Management: Automates local file handling, metadata checks, and cleanup tasks using the Python subprocess module.

Automated Testing: Compares remote execution results against local expected output files to validate code correctness.

Error Analysis: Captures standard error and exit codes from the API to provide detailed debugging reports.

🚀 Getting Started
Prerequisites
Python 3.8+

Piston API Key: Required for high-volume requests or private instances.

Requests Library: Necessary for handling HTTP communication with the Piston engine.

Installation
Clone the repository to your local machine.

Navigate to the project directory.

Set your Piston API Key as an environment variable to keep it secure from the source code.

📂 Project Structure
runner.py: The core script that integrates subprocess calls with API requests.

test_cases/: A directory containing paired input and output text files for validation.

snippets/: A storage folder for the code files (e.g., Python, C++, Java) that need to be tested.

💻 How It Works
1. Local Pre-processing
The script uses the subprocess module to check if the target source files exist and to retrieve file details before sending them to the cloud. This ensures no empty or corrupted files are processed.

2. API Interaction
The Python script reads the content of a local file and packages it into a JSON payload. This payload is sent to the Piston API endpoint along with the specified programming language and version.

3. Automated Validation
Once the API returns the result, the script compares the "stdout" (the program's output) against a corresponding "expected" file in the test_cases folder. It then generates a pass or fail status based on the match.

🧪 Running the Suite
To trigger the full automated testing suite, execute the main runner script via the terminal. The script will iterate through all files in the snippets folder, communicate with the Piston API, and print a summary report of all successful and failed test cases.

🛡 Security
While the code execution happens in a remote sandbox, this project follows best practices for local security:

No Shell Execution: Subprocess commands are called using list arguments to prevent shell injection attacks.

Environment Isolation: API keys are managed through environment variables rather than hardcoded strings.
