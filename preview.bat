@echo off
cd /d "%~dp0"

echo [1/2] Syncing notes to docs...
python sync.py
if errorlevel 1 goto error

echo.
echo [2/2] Starting local preview at http://127.0.0.1:8000
echo Press Ctrl+C to stop.
python -m mkdocs serve
goto end

:error
echo.
echo !!! ERROR - please send the messages above to Claude !!!
pause

:end
