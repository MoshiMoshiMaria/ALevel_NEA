@echo off
TITLE Hail from Chancellor Gowron, Qo'nos
cls
SET /A baseNumber=%RANDOM% * 100 / 32768 + 1
echo Survey Station %baseNumber% has detected an Omega Particle forming in the alpha quadrant.
set /p=Hit enter to continue...
cls
echo You must find and destroy the particle before the Federation or Romulan dogs seize it and destroy our glorius empire.
set /p=Hit enter to continue...
cls
echo Qapla'
set /p=Hit enter to continue...
cls
exit
