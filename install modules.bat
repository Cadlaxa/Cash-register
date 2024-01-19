@echo off


:start
cls

cd \
cd \python%python_ver%\Scripts\
pip install pygame
pip install colorama
pip install tabulate
pip install qrcode
pip install opencv-python
pip install pyzbar

pause
exit