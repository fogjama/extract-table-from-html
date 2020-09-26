set original_dir=%CD%
call %original_dir%\venv\Scripts\activate.bat

for /f "usebackq delims=| tokens=*" %%G in (`dir /b %original_dir%\samples\*.htm`) DO python main.py %%G

call %original_dir%\venv\Scripts\deactivate.bat
exit /B