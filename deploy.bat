@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo   [1/2] 同步笔记到 docs 目录...
echo ========================================
python sync.py
if errorlevel 1 goto error

echo.
echo ========================================
echo   [2/2] 构建并部署到 GitHub Pages...
echo ========================================
python -m mkdocs gh-deploy --force
if errorlevel 1 goto error

echo.
echo ========================================
echo   部署成功！网页地址：
echo   https://knkgjnrkh.github.io/blog/
echo   （首次部署后等 1-2 分钟再刷新）
echo ========================================
goto end

:error
echo.
echo !!! 出错了，请把上面的红字发给 Claude 排查 !!!

:end
pause
