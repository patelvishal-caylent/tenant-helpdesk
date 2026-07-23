# Pre-Work — Set This Up Before the Workshop

Do this **before** the day of the workshop, on your own laptop. It takes about 15-20
minutes. If anything below fails or you get stuck, contact your facilitator ahead of
time — don't wait until the room.

You need four things installed, plus one account created, plus this repo on your
laptop:

1. **Python 3** (runs the practice app)
2. **Git** (gets the repo, and switches branches during labs)
3. **Claude Code** (the tool you'll actually use in the labs)
4. **A Claude.ai account on a paid plan** — Pro, Max, or a Claude for Teams seat.
   A free Claude.ai account will not work with Claude Code.
5. **This repo, cloned onto your laptop**

- [macOS](#macos)
- [Windows](#windows)
- [Get the repo onto your laptop](#get-the-repo-onto-your-laptop)
- [Verify the app runs](#verify-the-app-runs)
- [Ready-to-go checklist](#ready-to-go-checklist)

Pick your OS below and follow it top to bottom.

---

## macOS

### 1. Check what you already have

Open **Terminal** (Cmd+Space, type `Terminal`, press Enter), then run:

```bash
python3 --version
git --version
```

- If `python3 --version` prints something like `Python 3.11.x` or higher, you're set —
  skip to step 3.
- If `git --version` prompts you to install "Command Line Developer Tools," accept —
  that installs Git. Skip to step 3 once it finishes.
- If either command says "command not found," continue to step 2.

### 2. Install Homebrew, then Python and Git

[Homebrew](https://brew.sh) is a package manager for Mac — the standard way to install
command-line tools. Install it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow any on-screen instructions it prints (it may ask you to run one or two more
commands to add Homebrew to your PATH — copy/paste exactly what it shows you). Then:

```bash
brew install python git
```

Confirm both installed:

```bash
python3 --version
git --version
```

### 3. Install Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Confirm it installed:

```bash
claude --version
```

### 4. Log in

```bash
claude
```

This opens a browser tab to sign in. Sign in with your Claude.ai account (Pro, Max, or
Teams — see the account requirement above). Approve the login, return to the terminal —
you should land in Claude Code's prompt box. Type `/exit` or press **Ctrl-C** to close it
for now; you don't need it running yet.

---

## Windows

### 1. Check what you already have

Open **PowerShell** (Start menu, type `PowerShell`, press Enter), then run:

```powershell
python3 --version
git --version
```

- If `python3 --version` prints something like `Python 3.11.x` or higher, skip to step 3.
- If `git --version` prints a version, skip to step 3.
- If either says it's not recognized as a command, continue to step 2.

### 2. Install Python and Git

- **Python:** download the installer from [python.org/downloads](https://www.python.org/downloads/).
  Run it, and on the first install screen **check the box "Add python.exe to PATH"**
  before clicking Install — this is the step people miss.
- **Git:** download the installer from [git-scm.com/downloads/win](https://git-scm.com/downloads/win).
  Run it and accept the defaults on every screen.

Close and reopen PowerShell, then confirm both:

```powershell
python3 --version
git --version
```

### 3. Install Claude Code

```powershell
irm https://claude.ai/install.ps1 | iex
```

Confirm it installed:

```powershell
claude --version
```

### 4. Log in

```powershell
claude
```

This opens a browser tab to sign in. Sign in with your Claude.ai account (Pro, Max, or
Teams — see the account requirement above). Approve the login, return to the terminal —
you should land in Claude Code's prompt box. Type `/exit` or press **Ctrl-C** to close it
for now; you don't need it running yet.

---

## Get the repo onto your laptop

From a terminal, outside any other project folder:

```bash
git clone https://github.com/patelvishal-caylent/tenant-helpdesk.git
cd tenant-helpdesk
```

This has to be a real `git clone`, not a zip download — the labs work by switching
branches (`git fetch`, `git checkout`), which only works with the full repo history.

## Verify the app runs

From inside the repo folder:

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
python app.py
```

Then open `http://localhost:5050/` in a browser. Seeing a dashboard with tenant names
means everything works. Stop the app with **Ctrl-C** in that terminal — you don't need
to leave it running until the workshop itself.

## Ready-to-go checklist

- [ ] `python3 --version` shows 3.9 or higher
- [ ] `git --version` shows a version
- [ ] `claude --version` shows a version
- [ ] I have a Claude.ai Pro, Max, or Teams account (not free) and logged in successfully once
- [ ] The repo is cloned on my laptop, and `python app.py` + `http://localhost:5050/` showed a working dashboard

All checked? You're done — see you at the workshop. Read `labs/GETTING-STARTED.md`
first thing on the day, before your assigned lab card.
