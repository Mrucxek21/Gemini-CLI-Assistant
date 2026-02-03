<div align="center">

# 🧠 Gemini CLI Assistant
### Your AI Terminal Companion

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch_Linux-Compatible-1793d1?style=for-the-badge&logo=arch-linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

<p align="center">
  A lightweight, lightning-fast terminal client for Google's Gemini AI.<br>
  Built for Linux power users who refuse to leave the console.
</p>

</div>

---

## ⚡ Why use this?

* **🚀 Zero Lag:** No browser overhead. Runs instantly in your terminal.
* **🛡️ Smart Handling:** Auto-detects API limits (429) and handles model versioning (404).
* **🔒 Secure:** Keeps your API keys safe in `.env` (never uploaded to Git).
* **🐧 Linux Native:** Tested on Arch Linux / CachyOS with Wayland support.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Mrucxek21/Gemini-CLI-Assistant.git
cd Gemini-CLI-Assistant
```
 ### 2. Set up Environment
Arch Linux / CachyOS (Recommended):
```bash
# Install pip
sudo pacman -S python-pip
# Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate.fish
```
### Debian / Ubuntu:
```bash
sudo apt install python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### ⚙️ Configuration
## 1.Get your Free API Key from Google AI Studio.
## 2.Create a .env file in the project folder:
```bash
cp .env.example .env
nano .env
```
## 3.Paste your key inside the file:
```bash
GEMINI_API_KEY=PASTE_YOUR_API_KEY_HERE
```

### 🚀 Usage
## 💬 Ask a Question
```bash
python ask.py "Write a bash script to update Arch Linux mirrors"
```
## 🔍 Check Available Models
Not sure which model works? Run the diagnostic tool to see all models on your account:
```bash
python check_models.py
```
## 🔧 Change AI Model
Edit ask.py to switch between different versions of Gemini:
```bash 
# Inside ask.py - line 24
response = client.models.generate_content(
    model="gemini-flash-lite-latest", # <--- Change model name here
    contents=prompt
)
```
### ⚠️ Troubleshooting
429 RESOURCE_EXHAUSTED	Free tier limit reached.	Wait 60 seconds or switch to a "Lite" model.
404 NOT_FOUND	Wrong model name in code.	Run check_models.py and update the name in ask.py.
ModuleNotFoundErrorVirtual environment not active.Run source venv/bin/activate.fish again.
