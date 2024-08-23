
@echo off

for /f "tokens=1-2 delims= " %%a in ('echo %time%') do set currentTime=%%a%%b
title Command shell window opened at %currentTime%


rem Set the title to the command prompt window
rem title Command shell window to Open a wifi menu 


python wifi_menu.py

PAUSE
