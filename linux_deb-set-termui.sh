echo "[+] Setting up the packages for termui..."
echo "[!] Make sure to have internet access."
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip
pip3 install colorama
chmod +x termui.py
sudo cp termui.py /usr/bin/termui
echo "[+] Setup finished."
echo "[+] You can now run termui by typing termui on your terminal."