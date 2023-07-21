echo "[+] Setting up the packages for termui..."
echo "[!] Make sure to have internet access."
pkg update -y
pkg upgrade -y
pkg install python3 -y
pip install colorama
chmod +x termui.py
cp termui.py $PREFIX/bin/termui
echo "[+] Setup finished."
echo "[+] You can now run termui by typing termui on your terminal."