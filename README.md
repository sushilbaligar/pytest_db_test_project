# PyTest DB Test Project
# Pytest project used to connect to local wordpress DB and validate DB data and validate APIs

## Prerequisites
1. **Install Python**:
   - Ensure you have Python installed on your machine. You can download the latest version from [python.org](https://www.python.org/).

2. **Install PyCharm**:
   - Download and install PyCharm from [JetBrains](https://www.jetbrains.com/pycharm/download/).

## Setup Instructions
1. **Clone the Repository**:
   - Open your terminal and clone the repository:
     ```bash
     git clone https://github.com/sushilbaligar/pytest_db_test_project.git
     cd pytest_db_test_project
     ```

2. **Create a Virtual Environment**:
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```

3. **Install Dependencies**:
   - Install the required dependencies from the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

## PyCharm Configuration
1. **Open the Project in PyCharm**:
   - Launch PyCharm and open the cloned project directory.

2. **Configure the Python Interpreter**:
   - Go to `File` -> `Settings` (or `PyCharm` -> `Preferences` on macOS).
   - Navigate to `Project: <Project Name>` -> `Python Interpreter`.
   - Select the virtual environment you created earlier (`venv`).

3. **Install pytest**:
   - Open the terminal within PyCharm (`Alt + F12`).
   - Ensure pytest is installed in the virtual environment:
     ```bash
     pip install pytest
     ```

4. **Enable pytest in PyCharm**:
   - Go to `File` -> `Settings` (or `PyCharm` -> `Preferences` on macOS).
   - Navigate to `Tools` -> `Python Integrated Tools`.
   - Under the `Testing` section, set the default test runner to `pytest`.

## Running Tests
1. **Run pytest in PyCharm**:
   - Open the terminal in PyCharm (`Alt + F12`).
   - Navigate to the directory containing your tests:
     ```bash
     cd tests
     ```
   - Run the tests using pytest:
     ```bash
     pytest
     ```

## Managing Git Remotes
1. **Delete Existing Remote**:
   - Open the terminal in PyCharm (`Alt + F12`) and run:
     ```bash
     git remote remove origin
     ```

2. **Add New Remote**:
   - Add your new remote repository:
     ```bash
     git remote add origin https://github.com/yourusername/new-repo.git
     ```

3. **Verify the Changes**:
   - Verify the new remote:
     ```bash
     git remote -v
     ```

## Handling Authentication Issues
1. **Using Personal Access Token**:
   - Generate a Personal Access Token (PAT) from [GitHub Settings](https://github.com/settings/tokens).
   - Use the token as your password when prompted.

2. **Configure Git to Use the Token**:
   - Set up the token globally:
     ```bash
     git remote set-url origin https://<YOUR-GITHUB-USERNAME>:<YOUR-TOKEN>@github.com/sushilbaligar/pytest_db_test_project.git
     ```

3. **Merge with Unrelated Histories**:
   - Allow unrelated histories:
     ```bash
     git pull origin master --allow-unrelated-histories
     ```

4. **Force Push (with caution)**:
   - Force push to overwrite remote history:
     ```bash
     git push -u origin master --force
     ```

Feel free to customize any part of this `README.md` to better fit your project. Let me know if you need any further modifications or assistance! 😊
