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
git clone [https://github.com/Mrucxek21/Gemini-CLI-Assistant.git](https://github.com/Mrucxek21/Gemini-CLI-Assistant.git)
cd Gemini-CLI-Assistant
2. Set up EnvironmentArch Linux / CachyOS (Recommended):Fragment kodu# Install pip
sudo pacman -S python-pip

# Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate.fish
Debian / Ubuntu:Bashsudo apt install python3-venv python3-pip
python3 -m venv venv
source venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
⚙️ ConfigurationGet your Free API Key from Google AI Studio.Create a .env file in the project folder:Bashcp .env.example .env
nano .env
Paste your key inside the file:Fragment koduGEMINI_API_KEY=AIzaSy...YourKeyHere
🚀 Usage💬 Ask a QuestionBashpython ask.py "Write a bash script to update Arch Linux mirrors"
🔍 Check Available ModelsNot sure which model works? Run the diagnostic tool:Bashpython check_models.py
🔧 Change AI ModelEdit ask.py to switch between speed (Flash) and power (Pro):Python# Inside ask.py
response = client.models.generate_content(
    model="gemini-flash-lite-latest", # <--- Change this line
    contents=prompt
)
⚠️ TroubleshootingErrorCauseSolution429 RESOURCE_EXHAUSTEDFree tier limit reached.Wait 60 seconds or switch to a "Lite" model.404 NOT_FOUNDWrong model name.Run check_models.py to see valid model names.ModuleNotFoundErrorVenv not active.Run source venv/bin/activate.fish again.
