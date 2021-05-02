rem turn off echo
@echo off

rem set TouchDesigner build numbers
set TOUCHVERSION=2021.12380

rem set our project file target
set TOEFILE="dev-env.toe"

rem set the rest of our paths for executables
set TOUCHDIR=%PROGRAMFILES%\Derivative\TouchDesigner.
set TOUCHEXE=\bin\TouchDesigner.exe

rem combine our elements so we have a single path to our TouchDesigner.exe 
set TOUCHPATH="%TOUCHDIR%%TOUCHVERSION%%TOUCHEXE%"

rem start our project file with the target TD installation
start "" %TOUCHPATH% %TOEFILE%