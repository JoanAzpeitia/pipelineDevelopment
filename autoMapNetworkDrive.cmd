@echo off

:Start
timeout /t 5 /nobreak >NUL

if exist Z:\NUL goto End
net use Z: \\ip number\serverName\desiredFolder /user:admin password 

if ERRORLEVEL 1 goto Start
:End