@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo 同步笔记...
python sync.py
if errorlevel 1 goto error

echo.
echo 启动本地预览，浏览器打开 http://127.0.0.1:8000
echo 按 Ctrl+C 停止预览
python -m mkdocs serve
goto end

:error
echo 出错了，请把上面的信息发给 Claude
pause

:end
