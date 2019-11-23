@echo off
TITLE Hail from Admiral Ross, Starfleet HQ
cls
SET /A baseNumber=%RANDOM% * 100 / 32768 + 1
echo Starbase %baseNumber%'s sensors picked up evidence of an Omega Particle forming within the alpha quadrant.
set /p=Hit enter to continue...
cls
echo Starfleet has tasked you with finding and destryoing the particle before it falls into the wrong hands.
set /p=Hit enter to continue...
cls
echo A chain reaction of molecules would rupture subspace in the entire quadrant. It is paramount you succeed.
set /p=Hit enter to continue...
cls
echo You are authorised to destroy any militant ships that stand in your way.
set /p=Hit enter to continue...
cls
echo Goodluck, Captain
set /p=Hit enter to continue...
cls
exit
