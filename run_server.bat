@echo off

cd Server

echo 1. Round Robin
echo 2. SJF
set /p choice= "Please Select one of the above options :"
if %choice% == 1 goto rr
if %choice% == 2 goto sjf
goto end

:rr
java RRServer
goto end

:sjf
java SJFServer
goto end

:end