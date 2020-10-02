cd /d "%~dp0"
set run_dir=%CD%
call %run_dir%\venv\Scripts\activate.bat

"%run_dir%\venv\Scripts\python.exe" drop-file.py %*

call %run_dir%\venv\Scripts\deactivate.bat
exit /B
