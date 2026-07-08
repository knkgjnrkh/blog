@echo off
cd /d "%~dp0"

echo ========================================
echo   [1/3] Syncing notes to docs folder...
echo ========================================
python sync.py
if errorlevel 1 goto error

echo.
echo ========================================
echo   [2/3] Backing up source to main branch...
echo ========================================
git add -A
git commit -m "update notes %date% %time%"
git push origin main

echo.
echo ========================================
echo   [3/3] Building and deploying to GitHub Pages...
echo ========================================
python -m mkdocs gh-deploy --force
if errorlevel 1 goto error

echo.
echo ========================================
echo   Deploy success! Site URL:
echo   https://knkgjnrkh.github.io/blog/
echo   (Wait 1-2 minutes then refresh)
echo ========================================
goto end

:error
echo.
echo !!! Error occurred. Please send the messages above to Claude. !!!

:end
pause
