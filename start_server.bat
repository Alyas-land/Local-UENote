@echo off
echo Starting flask server ...
echo ====================================
echo Activating venv ...
echo [.] 
timeout /t 1 /nobreak >nul
echo [..]
timeout /t 1 /nobreak >nul
call venv\Scripts\activate

:: Check exisiting app.py file
if exist app.py (
    echo app.py founded.
	echo Starting server ...
	echo [.] 
	timeout /t 1 /nobreak >nul
	echo [..]
	timeout /t 1 /nobreak >nul
	
	:: Start the Flask server in background and open Chrome
	start "" python app.py
	timeout /t 3 /nobreak >nul
	start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8080/
	echo Server started in background, Chrome opened.
) else (
	echo [Error]:
    echo app.py not founded!
)

pause
