@echo off


:start
cls

cd \
cd \python%python_ver%\Scripts\
py -3.11 -m pip install pygame
py -3.11 -m pip install colorama
py -3.11 -m pip install tabulate
py -3.11 -m pip install qrcode
py -3.11 -m pip install opencv-python
py -3.11 -m pip install pyzbar

pause
exit