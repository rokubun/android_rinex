rem 2019 LKB(c)
rem run module as standalone code
rem run it as -o OUTPUT FILE INPUT FILE
@ECHO OFF
setlocal

copy gnsslogger_to_rnx ..\gnsslogger_to_rnx.py
cd ..
python gnsslogger_to_rnx.py %1 %2 %3

del gnsslogger_to_rnx.py

endlocal
