```markdown
# 🚀 Gemini CLI Assistant

A lightweight, Python-based terminal client for Google's Gemini AI. Designed for Linux power users who want quick AI answers directly in their console without opening a browser.

## ✨ Features

* **Fast & Light:** Runs entirely in the terminal.
* **Smart Error Handling:** Automatically detects quota limits (Error 429) and model configuration errors (Error 404).
* **Secure:** Uses `.env` file configuration to keep your API keys safe.
* **Model Diagnoser:** Includes a script to list all Gemini models available to your account.

---

## 🛠️ Installation

### Prerequisites
* Python 3.10 or newer
* A free Google AI Studio API Key

### Step 1: Clone the repository

```bash
git clone [https://github.com/Mrucxek21/Gemini-CLI-Assistant.git](https://github.com/Mrucxek21/Gemini-CLI-Assistant.git)
cd gemini-cli

```

### Step 2: Set up Virtual Environment

**🟢 Arch Linux (CachyOS, Manjaro, EndeavourOS)**

```bash
# 1. Install pip if missing
sudo pacman -S python-pip

# 2. Create virtual environment
python -m venv venv

# 3. Activate it (Fish Shell)
source venv/bin/activate.fish
# OR if you use Bash/Zsh:
# source venv/bin/activate

```

**🔴 Debian / Ubuntu / Linux Mint**

```bash
# 1. Install venv package
sudo apt update && sudo apt install python3-venv python3-pip

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

```

### Step 3: Install Dependencies

Once your environment is active (you should see `(venv)` in your terminal), install the required libraries:

```bash
pip install -r requirements.txt

```

---

## ⚙️ Configuration

1. **Get your API Key:**
Go to [Google AI Studio](https://aistudio.google.com/) and create a free API Key.
2. **Set up the environment file:**
Create a file named `.env` in the project folder and paste your key inside.
```bash
# Create the file
nano .env

```


**Inside `.env` file:**
```env
GEMINI_API_KEY=PASTE_YOUR_API_KEY_HERE

```


*(Save with `Ctrl+O`, `Enter`, then Exit with `Ctrl+X`)*

---

## 🚀 Usage

### Ask a question

To send a prompt to Gemini, simply run `ask.py` followed by your question:

```bash
python ask.py "Write a simple Python script to list files in a directory"

```

### Check available models

If you are getting "Model not found" errors, run this script to see which models your API key has access to:

```bash
python check_models.py

```

### Change the Model

You can edit `ask.py` to change the model version (e.g., if you want to use a newer or faster version):

```python
# Inside ask.py
response = client.models.generate_content(
    model="gemini-flash-lite-latest", # <--- Change this line
    contents=prompt
)

```

---

## ⚠️ Troubleshooting

* **Error 429 (Resource Exhausted):**
This means you hit the free tier limit. Wait for a minute and try again, or switch to a "Lite" model in the code.
* **Error 404 (Not Found):**
The model name in `ask.py` is incorrect or deprecated. Run `python check_models.py` to see the valid names and update your code.

---

## 📜 License

MIT License

```

```