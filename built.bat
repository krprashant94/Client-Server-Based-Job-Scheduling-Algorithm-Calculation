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
javac SJFP.java
javac RR.java -d Server
javac SJF.java -d Server
javac GFG.java -d Server
javac SJFP.java -d Server
javac RRServer.java -d Server
javac SJFServer.java -d Server
javac GFGServer.java -d Server
javac SJFPServer.java -d Server

echo Cleaning...
del Process.class
del SJF.class
del SJFP.class