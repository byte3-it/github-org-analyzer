# GitHub Organization Analyzer

A Python tool to analyze GitHub organizations and extract author information from all repositories within an organization.

## Features

- Fetches all repositories from a specified GitHub organization
- Extracts commit author information (name and email) from each repository
- Handles pagination for large organizations and repositories
- Gracefully handles empty repositories and API errors
- Supports GitHub personal access tokens for authenticated requests

## Prerequisites

- Python 3.7 or higher
- GitHub personal access token (optional, but recommended for higher rate limits)

## Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd github-org-analyzer
```

### 2. Set Up Python Virtual Environment

#### Option A: Using venv (Recommended)

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Verify activation (you should see (venv) in your terminal prompt)
which python
```

#### Option B: Using virtualenv

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Make sure your virtual environment is activated
pip install -r requirements.txt
```

### 4. Configure GitHub Token (Optional but Recommended)

For better rate limits and access to private repositories, set your GitHub personal access token:

```bash
# Set as environment variable
export GITHUB_TOKEN=your_github_token_here

# Or add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
echo 'export GITHUB_TOKEN=your_github_token_here' >> ~/.zshrc
source ~/.zshrc
```

**Note:** If you don't set a token, the tool will work with unauthenticated requests but will have lower rate limits.

## Usage

1. **Activate your virtual environment** (if not already active):

   ```bash
   source venv/bin/activate
   ```

2. **Run the analyzer**:

   ```bash
   python main.py
   ```

3. **Enter the GitHub organization name** when prompted.

4. **View results** - the tool will display all repositories and their authors.

## Example Output

```
Enter GitHub organization name: example-org

Fetching repositories for organization 'example-org'...

Repository: project-a
  - John Doe <john.doe@example.com>
  - Jane Smith <jane.smith@example.com>

Repository: project-b
  - John Doe <john.doe@example.com>
  - Bob Wilson <bob.wilson@example.com>

Repository: empty-repo
  No authors found.
```

## Requirements

The project requires the following Python packages (see `requirements.txt`):

- `requests` - For making HTTP requests to GitHub API

## Rate Limiting

- **Without token**: 60 requests per hour
- **With token**: 5,000 requests per hour

For large organizations with many repositories, consider using a GitHub token to avoid rate limiting.
