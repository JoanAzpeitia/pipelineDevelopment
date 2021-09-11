####running a pipeline under Windows OS sometimes gives errors at mapping network ip's, using this cmd we managed to automate this process at machine startup and avoid the issue####

@echo off

:Start
timeout /t 5 /nobreak >NUL

if exist Z:\NUL goto End
net use Z: \\ip number\serverName\desiredFolder /user:admin password 

if ERRORLEVEL 1 goto Start
:End
