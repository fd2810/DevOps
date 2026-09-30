# Practical 4: Creating and Managing a Virtual Machine

## Aim
a. Set up a Virtual Machine using VMware (Ubuntu)  
b. Configure networking (IP, ports, network modes)  
c. Deploy a Flask application manually on the VM

## Software Required
- VMware Workstation
- Ubuntu VM (already installed)
- Python 3 + Flask
- Terminal / Web Browser

---

## Part (a): Set Up Virtual Machine

### Step 1: Start the VM
1. Open VMware Workstation
2. Select your Ubuntu Virtual Machine
3. Click **Power On**
4. Login with your username and password

### Step 2: Update Ubuntu
```bash
sudo apt update
sudo apt upgrade -y
```

### Step 3: Verify Python
```bash
python3 --version
```

If not installed:
```bash
sudo apt install python3 python3-pip -y
```

### Step 4: Install Flask
```bash
pip3 install flask
pip3 show flask
```

**Result (a):** Ubuntu VM is ready with Python and Flask.

---

## Part (b): Configure Networking

### Step 1: Check IP Address
```bash
ip addr
# or
hostname -I
```

Example output: `192.168.43.128`

### Step 2: Understand Network Modes in VMware

| Mode     | Description |
|----------|-------------|
| NAT      | Shares host internet (recommended for beginners) |
| Bridged  | Gets its own IP on the same network as host |
| Host-only | Only host ↔ VM communication |

To change mode:
1. Shut down VM
2. VM → Settings → Network Adapter
3. Choose **NAT** (or Bridged if required)

### Step 3: Test Internet
```bash
ping google.com
```

### Step 4: Check Listening Ports
```bash
sudo ss -tuln
# or
netstat -tuln
```

### Step 5: Allow Flask Port (if firewall is on)
```bash
sudo ufw allow 5000
sudo ufw status
```

**Result (b):** Network configured, IP verified, port 5000 available.

---

## Part (c): Deploy Flask App Manually on VM

### Step 1: Create project folder
```bash
mkdir FlaskApp
cd FlaskApp
```

### Step 2: Create `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask running on Virtual Machine!"

@app.route('/about')
def about():
    return "Deployed successfully on Ubuntu VM"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

> `host='0.0.0.0'` is important so the app is accessible from outside the VM.

### Step 3: Run the application
```bash
python3 app.py
```

### Step 4: Access from browser
- Inside VM: http://127.0.0.1:5000
- From host machine: http://<VM-IP>:5000  
  Example: http://192.168.43.128:5000

---

## What to Show Teacher
1. VM running in VMware
2. `hostname -I` output (IP address)
3. Flask app running
4. Browser showing the Flask page from host machine
