
@echo off


for /f "tokens=1-2 delims= " %%a in ('echo %time%') do set currentTime=%%a%%b

rem Set the title to the command prompt window.
title Command shell window to Open Wifi and auto-close it. Opened at %currentTime%


python Wifi_Modem_control.py

PAUSE
