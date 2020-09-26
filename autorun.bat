set original_dir=%CD%
call %original_dir%\venv\Scripts\activate.bat

python main.py "./samples/Job 29 BARKER & STONEHOUSE OPEN modified.htm"

call %original_dir%\venv\Scripts\deactivate.bat
exit /B