@echo off
title Launching MediMate-AI Jupyter Notebook...
color 0A
echo =====================================================================
echo    MEDIMATE-AI : LAUNCHING JUPYTER NOTEBOOK FOR MACHINE LEARNING
echo    Student: PRAKASHRAJ A.V & SRIEE AMOGHAA M
echo    Guide: Dr. S. Aruna MCA., Ph.D. - Sona College of Technology
echo =====================================================================
echo.
echo Opening MediMate_AI_Model_Training.ipynb in your default web browser...
echo.
cd /d "%~dp0"
python -m notebook MediMate_AI_Model_Training.ipynb
pause
