echo "Installing required packages"
pip install -r requirements.txt
echo "Copying service"
cp ./alarm.service /etc/systemd/system/alarm.service
echo "Staring service"
systemctl enable alarm.service
systemctl daemon-reload
systemctl start alarm.service
echo "Generating serial"
python serial.py
