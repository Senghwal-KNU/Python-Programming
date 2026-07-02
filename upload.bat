@echo off
git add .
git commit -m "%date% upload"
git push origin main
pause