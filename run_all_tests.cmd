@echo off
cd SRC
:start
python -m unittest
pause
cls
goto :start
