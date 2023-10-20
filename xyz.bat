@echo off
::script file path - c:\myprojects\xyz.py
::script filename if batch runs in same directory - xyz.py
set myscrpt="csv_to_excel.py"

::Log file path
set pylog="myscriptlog.log"

::Python Path
::pushd C:\Python27

::script output to log
echo ----------log-start---------- >>%pylog%
python %myscrpt%>>%pylog%
echo ----------log-end---------- >>%pylog%


::Display log output in prompt
type %pylog%
pause>nul
exit