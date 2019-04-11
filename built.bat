@echo off

echo Removing Previous Build

RMDIR /S /Q "Server"
RMDIR /S /Q "Client"
md Client
md Server

echo Bulding Client
javac Client.java -d Client

echo Bulding Server
javac SJF.java
javac RR.java -d Server
javac SJF.java -d Server
javac RRServer.java -d Server
javac SJFServer.java -d Server

echo Cleaning...
del Process.class
del SJF.class