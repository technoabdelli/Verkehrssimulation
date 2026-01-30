@echo off
setlocal enabledelayedexpansion
set "SCRIPT_DIR=%~dp0"

set "ARGS_FOLDER=%SCRIPT_DIR%Eingabedatei"

for %%f in ("%ARGS_FOLDER%\.txt") do ( 
	echo Wird bearbeitet: %%f
    start /wait python "%SCRIPT_DIR%main.py" "%%f"
    echo Wurde fertig bearbeitet: %%f
    echo.
)

echo Die fertige Datei finden Sie in dem Ordner "Lösungen"
pause