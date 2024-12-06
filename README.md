# HSTS Checker

## Project Overview

**HSTS Checker** is a simple tool to check if a website supports **HTTP Strict Transport Security (HSTS)**. HSTS is an important security feature that forces web browsers to communicate only over HTTPS, preventing man-in-the-middle (MITM) attacks like SSL stripping. This tool checks if the HSTS header is present and verifies its validity for websites.


## Tools and Libraries Used

- **Requests**: A simple and elegant HTTP library for Python to send HTTP requests.
- **Pyfiglet**: To display ASCII art banners in the terminal.
  
## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/selychan/hsts-header-check.git
   cd hsts_checker
   python hsts_checker.py

