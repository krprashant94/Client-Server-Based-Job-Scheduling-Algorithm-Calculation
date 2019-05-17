@echo off

cd Server

echo 1. Round Robin
echo 2. Greedy Algorithm (SJF)
echo 3. Min-Max Algorithm (SJF Primitive)
echo 4. Burt Force Algorithm (FCFS)
echo 5. LRTF Client (Python)
echo 6. Prority Sheduling Client (Python)
set /p choice= "Please Select one of the above options :"
if %choice% == 1 goto rr
if %choice% == 2 goto sjf
if %choice% == 3 goto sjfp
if %choice% == 4 goto fcfs
if %choice% == 5 goto lrtf
if %choice% == 6 goto ps
goto end

:rr
java RRServer
goto end

:sjf
java SJFServer
goto end


:sjfp
java SJFPServer
goto end


:fcfs
java GFGServer
goto end


:lrtf
cd..
python ./LRTF.py
goto end


:ps
cd ..
python ./prority_sheduling.py
goto end

:end