# Run Your Google Drive Locally on a Raspberry Pi

## Instructions

### 1. Install Python and Flask

Make sure Python is installed, then install Flask:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install flask
```

### 2. Clone the Repository

```bash
git clone https://github.com/Haifishbro209/local_cloud.git
cd local_cloud
```

### 3. Run the Application

```bash
python3 app.py
```

### 4. Access the Web Interface

After running the script, check the output. You will see something like:

```
 * Running on http://127.0.0.1:7000
 * Running on http://192.168.178.122:7000
```

- `http://127.0.0.1:7000`: Accessible **only** on the Raspberry Pi itself  
- `http://192.168.178.122:7000`: Accessible from **all devices in your local network**

> **Note**: Your IP address may differ — adjust accordingly.

---

## ⚠️ Disclaimer

This tool is **not secure** and should **only** be used within your **local network**.  
Do **not** expose it to the internet.

---

## Autostart on Boot (Optional)

To automatically start the app on boot:

1. Open the crontab editor:

```bash
crontab -e
```

2. Add this line at the end:

```bash
@reboot python3 /home/pi/local_cloud/app.py &
```

> Adjust the path if your project is in a different folder.

This ensures the app starts automatically every time the Raspberry Pi boots.
