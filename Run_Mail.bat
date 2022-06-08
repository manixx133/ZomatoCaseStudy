@echo off
python C:\zomato\script\mail.py %1 %*
timeout 5 >nul
exit
