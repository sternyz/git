# Browser History Extraction Tool

This repository contains a Python script to extract browser history from Chrome/Edge SQLite database files and export the data to CSV format for analysis.

## 📋 Prerequisites

### Required Software
- **Windows 11** (or Windows 10)
- **Python 3.7 or higher** - [Download from python.org](https://python.org/downloads/)
- **VS Code** - [Download from code.visualstudio.com](https://code.visualstudio.com/)
- **VS Code Python Extension** - Install from VS Code Extensions marketplace

## 🚀 Setup Instructions

### Step 1: Install Python
1. Go to [python.org/downloads](https://python.org/downloads/)
2. Download the latest Python 3.x version for Windows
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Verify installation by opening Command Prompt and typing: `python --version`

### Step 2: Install VS Code Python Extension
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Python"
4. Install the official Python extension by Microsoft
5. Restart VS Code if prompted

### Step 3: Clone/Download the Repository
1. Clone this repository: `git clone https://github.com/sternyz/git.git`
2. Or download the ZIP file from GitHub and extract it
3. Open the folder in VS Code: `File > Open Folder`

## 🔧 Configuration

### Update Browser History Path
Before running the script, you need to update the database path in `scripts/history.py`:

**For Chrome:**
```python
conn = sqlite3.connect(r"C:\Users\[Username]\AppData\Local\Google\Chrome\User Data\Default\History")
```

**For Edge:**
```python
conn = sqlite3.connect(r"C:\Users\[Username]\AppData\Local\Microsoft\Edge\User Data\Default\History")
```

**Replace `[Username]` with the actual Windows username.**

### Finding the Correct Path
1. Open File Explorer
2. Navigate to: `C:\Users\[Username]\AppData\Local\`
3. Look for either:
   - `Google\Chrome\User Data\Default\History` (Chrome)
   - `Microsoft\Edge\User Data\Default\History` (Edge)

## 🏃‍♂️ Running the Script

### Method 1: Run from VS Code (Recommended)
1. Open `scripts/history.py` in VS Code
2. Press `F5` or click the "Run" button (▶️)
3. The script will execute and show output in the terminal
4. Check for the generated `Chrome_history.csv` file

### Method 2: Run from Terminal
1. Open VS Code terminal (Ctrl+`)
2. Navigate to the script directory: `cd scripts`
3. Run: `python history.py`

### Method 3: Run from Command Prompt
1. Open Command Prompt
2. Navigate to the repository folder
3. Run: `python scripts/history.py`

## 📊 Output

The script generates:
- **Console output**: Shows each history entry as it's processed
- **CSV file**: `Chrome_history.csv` with columns:
  - Timestamp (YYYY-MM-DD HH:MM:SS)
  - URL
  - Title
  - Visit Count

## 🔍 Troubleshooting

### Common Issues

**"Python is not recognized"**
- Python is not installed or not in PATH
- Reinstall Python and check "Add to PATH"

**"No module named 'sqlite3'"**
- This is a built-in module, shouldn't occur with standard Python installation

**"Database file not found"**
- Check the path in the script
- Ensure the browser is closed (database may be locked)
- Verify the username in the path

**"Permission denied"**
- Run VS Code as Administrator
- Check file permissions on the history database

### Browser Database Locked
If you get a database error, the browser might be running:
1. Close all Chrome/Edge windows
2. Check Task Manager for any remaining browser processes
3. End those processes if found
4. Try running the script again

## 📝 Customization

### Modify Output Format
Edit the CSV writing section in the script to change:
- Column headers
- Date/time format
- Additional data fields

### Add Error Handling
The script includes basic error handling, but you can add more specific checks for your environment.

## 🛡️ Security Notes

- This script reads browser history data
- Ensure proper permissions and authorization before use
- The script only reads data, it doesn't modify browser history
- Generated CSV files should be handled according to your organization's data policies

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify Python installation: `python --version`
3. Check VS Code Python extension is installed
4. Ensure the browser history path is correct

## 📄 License

This tool is provided for legitimate forensic analysis and data migration purposes only. 