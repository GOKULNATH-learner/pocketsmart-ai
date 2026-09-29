@echo off
echo ========================================================
echo PocketSmart AI - Git Repository Setup Helper
echo ========================================================
echo.

WHERE git >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo [!] Git command not found in current PATH.
    echo [!] Please install Git from https://git-scm.com/downloads
    echo [!] After installing, run this script again or run:
    echo     git init
    echo     git add .
    echo     git commit -m "Initial commit: PocketSmart AI"
    pause
    exit /b 1
)

echo [+] Initializing Git repository...
git init
git add .
git commit -m "Initial commit: PocketSmart AI full-stack application"
echo.
echo [+] Git repository initialized successfully!
echo [+] Next steps:
echo     1. Create a repository on GitHub (e.g. pocketsmart-ai)
echo     2. Run: git remote add origin https://github.com/YOUR_USERNAME/pocketsmart-ai.git
echo     3. Run: git push -u origin main
echo.
pause
