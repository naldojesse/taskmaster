# Development Environment Setup Guide for TaskMaster AI

## Repository Structure

TaskMaster AI will use two repositories:
1. Public Repository (GitHub)
2. Private Repository (GitHub or GitLab)

### Public Repository Contents

The public repository should only contain:
- Source code
- Documentation (excluding sensitive information)
- Configuration files (excluding sensitive data)
- Test files (excluding sensitive test data)

### Private Repository Contents

The private repository will contain everything in the public repository, plus:
- Sensitive configuration files
- API keys and secrets
- Large data files
- Private documentation
- Any other sensitive or proprietary information

## Setting Up the Development Environment

1. **Install Required Software**
   - Python 3.8+
   - Git
   - Your preferred IDE (e.g., VS Code, PyCharm)

2. **Clone the Repositories**
   ```
   git clone https://github.com/your-username/taskmaster-ai-public.git
   git clone https://github.com/your-username/taskmaster-ai-private.git
   ```

3. **Set Up Virtual Environment**
   ```
   cd taskmaster-ai-public
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Configure Git**
   Set up your .gitignore file in the public repository to exclude sensitive files:

   ```
   # .gitignore
   *.env
   *_secret*
   private_config/
   large_data_files/
   ```

5. **Set Up Pre-Push Hook**
   Create a file named `.git/hooks/pre-push` in your public repository with the following content:

   ```bash
   #!/bin/bash

   # List of patterns for files/directories that shouldn't be in the public repo
   FORBIDDEN_PATTERNS=(
       "*.env"
       "*_secret*"
       "private_config/"
       "large_data_files/"
   )

   # Check if any forbidden files are staged for commit
   for pattern in "${FORBIDDEN_PATTERNS[@]}"; do
       if git diff --cached --name-only | grep -q "$pattern"; then
           echo "Error: Attempting to push forbidden files matching pattern: $pattern"
           echo "These files should not be included in the public repository."
           exit 1
       fi
   done

   # If we get here, no forbidden files were found
   exit 0
   ```

   Make the hook executable:
   ```
   chmod +x .git/hooks/pre-push
   ```

6. **Environment Variables**
   Store sensitive information like API keys in environment variables. Create a `.env` file in your private repository:

   ```
   # .env
   API_KEY=your_api_key_here
   DATABASE_URL=your_database_url_here
   ```

   Use a library like `python-dotenv` to load these variables in your code.

7. **Syncing Public and Private Repositories**
   Regularly sync changes from the public repository to the private repository:

   ```
   cd taskmaster-ai-private
   git remote add public https://github.com/your-username/taskmaster-ai-public.git
   git fetch public
   git merge public/main
   git push origin main
   ```

Remember to never commit sensitive information to the public repository. Always double-check your commits and pushes. The pre-push hook will help prevent accidental pushes of sensitive data, but it's not foolproof.

This setup ensures that you can work on the project locally with all the necessary files while maintaining a clean, public-facing repository.