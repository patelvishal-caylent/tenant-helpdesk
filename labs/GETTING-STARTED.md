# Getting Started — Read This Before Your First Lab

*One-time orientation, not a lab itself. Covers opening a terminal, starting Claude Code, and switching branches — step by step, assuming none of it yet.*

You already took the "Claude Code in Action" async course, so you know roughly what Claude Code is. This guide is the literal, mechanical part: exactly what to click, type, and expect to see, on your own laptop, right now. Read it once, all the way through, before you open your assigned lab card.

A **repo** (short for "repository") is just the project's folder of files — in this case, a small practice app. You'll be working inside it for every lab.

## 1. Before you start: three things that need to be true

1. **A terminal is open.** A terminal is a text-only window where you type instead of clicking icons. Don't have one open? Skip to Section 2 — it shows you exactly how, on Mac and on Windows.
2. **This repo is already cloned onto your computer.** "Cloned" means a full copy of the project already exists as a folder on your machine. This should have happened during setup, before today. If you can't find that folder, or aren't sure it happened, tell your facilitator now — don't guess, and don't try to fix this mid-lab.
3. **Claude Code is installed, and you're logged in.** Claude Code is the tool you'll type your requests into. To check it's installed: open a terminal (Section 2) and type `claude --version`, then press Enter. Seeing a version number means it's installed. Whether you're logged in becomes obvious the moment you actually start it — Section 4 shows you exactly what "ready" looks like versus "not logged in yet."

If any of these three isn't true and the fix isn't obvious below, say so out loud right now. Don't wait.

## 2. What is a terminal, and how do you open one?

A **terminal** (also called "command line," "console," or "shell" — all the same thing) is a window where you talk to your computer by typing text instead of clicking icons. You type a line of text called a **command**, press **Enter** (some Mac keyboards label this key **Return** — it's the same key), and the computer runs it and prints its response as more text. Type, Enter, read, repeat. That's the whole model.

**On a Mac:**
1. Press **Cmd (⌘) + Space** together. This opens "Spotlight," a search box, in the middle of your screen.
2. Type `Terminal`.
3. An app called **Terminal** appears in the results, with a dark, rectangular icon. Press **Enter**, or click it.
4. A window opens with some text and a blinking cursor next to a `%` or `$` symbol. That blinking cursor means it's ready for you to type.

**On Windows:**
1. Click the **Start** button (the Windows logo, bottom-left of your screen), or press the **Windows key**.
2. Type `Windows Terminal` (use this if it shows up) or `PowerShell` (also fine).
3. A matching app appears in the results. Press **Enter**, or click it.
4. A window opens with some text and a blinking cursor next to a `>` symbol. Same idea — ready for you to type.

Everything else in this guide works the same in either app, once it's open.

## 3. Getting into the right folder (`cd`)

**`cd`** stands for "change directory." A **directory** is just another word for a folder. Typing `cd` followed by a folder's location tells the terminal "go inside that folder" — the same result as double-clicking a folder icon, just typed instead of clicked. A **path** is that folder's location written as text — like a mailing address, but for files on your computer.

1. Open your normal file browser (Finder on Mac, File Explorer on Windows) and find this project's folder — it's likely named `advancedmd-workshop-demo-app`. Can't find it? Ask your facilitator before continuing.
2. In your terminal, type `cd` followed by one space. Don't press Enter yet.
3. Drag that folder from Finder/File Explorer and drop it directly onto the terminal window. The full path types itself in after your `cd ` — this avoids typos entirely. (If dragging doesn't work in your setup, ask your facilitator for the exact path to type instead.)
4. Press **Enter**.
5. Confirm you're in the right place: type `ls` and press Enter (this works in Mac Terminal and in Windows Terminal/PowerShell). You should see a list of names including `README.md`, `app.py`, and a folder called `labs`. See something else, or an error? You're in the wrong folder — go back to step 1.

You'll do this once per terminal window you open. Stay in this folder for everything that follows.

## 4. Starting Claude Code (and stopping it)

1. Confirm you're inside the repo folder in your terminal (Section 3) — Claude Code needs to start from inside it every time.
2. Type `claude` (just that word, lowercase) and press **Enter**.
3. **"Ready" looks like this:** a short welcome screen, then a box near the bottom of the window with a blinking cursor, waiting for you to type. Seeing that box means you're ready — skip ahead to Section 5.
4. **"Not logged in" looks like this:** instead of that box, a message about logging in — maybe a link or a short code, meant to be used in a web browser. Follow whatever it says on screen, then type `claude` again once you're done.

**Stopping Claude Code.** Some labs ask you to quit Claude Code and start it again — that's how it picks up a new or changed file, like a `CLAUDE.md` you just created. Here's how:
1. Hold the **Control** key and press **C** at the same time (on Mac, this is the **Control** key specifically, not **Cmd**). This combination is called "**Ctrl-C**" — it's the universal way to stop a running program in a terminal.
2. You'll land back at the plain terminal itself — the blinking cursor next to `%`, `$`, or `>` from Section 2, with no box.
3. To start Claude Code again: type `claude` and press **Enter** — exactly like step 2 above.

## 5. What a "prompt" is

A **prompt** is the request you type into that waiting box from Section 4 — plain English, the way you'd ask a coworker. Not code. No special format. No punctuation rules to learn.

Here's the part that isn't magic: when you press Enter, Claude actually opens and reads the real files sitting in the folder you started it in (the same folder from Section 3) — the same files you could open yourself in a text editor. It isn't guessing from some general memory of "apps like this." It's reading this specific repo's real files, live, right now, and answering based on what's actually written in them.

Example: if you type `Read schema.sql and tell me what tables exist`, Claude opens the real file named `schema.sql` in this folder, reads what's actually in it, and answers from that — not from a guess.

To send a prompt: type your sentence, then press **Enter**.

## 6. Reading what Claude does: diffs, questions, and permission prompts

After you send a prompt, you'll see one or more of these three things:

1. **A diff.** When Claude wants to change a file, it can show a "diff" — a before/after view of just the lines that change. Lines it wants to remove appear with a `-` in front (often red). Lines it wants to add appear with a `+` in front (often green). Nothing else about the file is shown — just the changed lines, like a track-changes view.
2. **A plain question.** Sometimes Claude just asks you something first, in plain English — for example, "Should I also update the tests?" Answer it the same way you'd answer a coworker: a normal sentence, then Enter.
3. **A permission prompt.** Before Claude writes a file or runs a command that changes something, it stops and asks first. It looks something like this (exact wording varies by version):
   ```
   Do you want to make this edit to schema.sql?
   ❯ 1. Yes
     2. Yes, and don't ask again this session
     3. No
   ```
   - **This is normal.** It happens constantly, in every lab. It is not a sign anything went wrong.
   - To answer: use the arrow keys to highlight your choice and press **Enter**, or type the number next to your choice and press **Enter**.
   - For every lab in this workshop, answering **Yes** (or "Allow") is expected and safe. Don't hesitate on these — the prompt exists so you get a look before anything happens, not as an obstacle to clear.

## 7. Branches: what they are, and the exact commands you'll type

**git** is the tool that keeps track of every saved version of this project. A **branch** is one saved, complete copy of the whole project, frozen at a specific point in time. Switching to a different branch is like being handed a different starting kit for a different exercise — not editing the same kit you already had open. Nothing you did on one branch shows up on another unless you deliberately carried it over.

This is why every lab's "Step 0" starts with a branch switch: it puts you on that lab's own starting kit, with exactly the files that lab needs, and none of the leftovers from the last one.

Every lab's Step 0 gives you two commands, typed into the terminal (not into Claude Code's prompt box). They look like this — this exact example is from Lab 1; your lab card will give you the exact names for that lab:

```
git fetch origin
git checkout -b lab-l1-work origin/lab-l1-start
```

1. **`git fetch origin`** — "origin" is the name for the shared project all of this lives in. This command checks in with it and downloads any branches you don't already have, without touching any of your own files yet. Think of it as syncing before you grab anything.
2. **`git checkout -b lab-l1-work origin/lab-l1-start`** — this creates a brand-new branch on your computer (`-b` means "make a new one"), names it `lab-l1-work` (your own copy, for this lab), and fills it with the exact starting content from `lab-l1-start` (that lab's official starting kit). The moment this finishes, your files change to match that starting point.

A few practical notes:
- The names after `-b` and after `origin/` are different for every lab. Always use the exact names printed on that lab's own Step 0 — not the example above.
- If Claude Code was already running from an earlier lab, stop it (**Ctrl-C**, Section 4) and start it again (`claude`) after switching branches. It needs a fresh start to see the new branch's files — it doesn't notice on its own.

## 8. Is the app running? (and the one command to start it)

This repo includes a small practice website — a fake customer-support tool, used only for these labs. Everyone just calls it "the app." It runs only on your own computer; nobody else can see or reach it. It lives at the address `http://localhost:5050`. **"localhost"** just means "this computer, right here" — not the real internet.

**To check if it's running:**
1. Open a normal web browser (Chrome, Safari, Edge — whichever you have).
2. Type or paste `http://localhost:5050/` into the address bar and press Enter.
3. **Running:** you see a real page — a dashboard with tenant names and numbers.
4. **Not running:** you see a browser error like "can't connect" or "refused to connect," or the page never loads.

**The one command to start it, if it isn't running:**
1. Open a second terminal window or tab — you need the app and Claude Code running at the same time, in two separate places. (Mac Terminal: **Cmd+T** for a new tab. Windows Terminal: **Ctrl+Shift+T**.)
2. In that new terminal, navigate into the repo folder again (Section 3 — `cd`, then drag-and-drop).
3. Type `python app.py` and press **Enter**.
4. Look for a line mentioning `5050` and the word "Running." Leave this terminal open and alone afterward — closing it, or pressing Ctrl-C in it, stops the app.
5. Go back to your browser and reload `http://localhost:5050/`.

Prefer not to juggle a second terminal yourself? You can also just ask Claude Code: "run python app.py for me" — same effect, one less window to manage.

Something else on screen instead — an error, nothing happening? That's exactly what Section 9 is for. Say so immediately.

## 9. Stuck vs. on track — and what to do about it

**Signs you're on track:**
- Claude's response roughly matches the shape of the "You should see" example on your lab card — not word-for-word, just the same kind of answer.
- Commands run and return you to a normal prompt, with no red error text.
- You roughly understand why the last thing happened.

**Signs you're stuck:**
- The same error shows up again, after you've already tried the obvious fix once.
- You don't understand what's on the screen, and reading it twice didn't help.
- More than a minute or two has passed without anything changing.
- What's on screen looks nothing like your lab card's "You should see" example, and you don't know why.

**What to do the moment you're stuck:**
1. Say so immediately — out loud in the room, or in chat if you're remote. Don't sit with it quietly, and don't try to power through alone.
2. Check your lab card's own "If you get stuck" table first — most common issues are already answered there, listed by exact symptom.
3. Not listed, or the fix doesn't work? Ask your facilitator or TA directly. Unblocking you fast is their job in this room. Asking early is normal and expected — it is not falling behind.

## 10. Your ready-to-start checklist

Before you open your assigned lab card, confirm every line below is true:

- [ ] A terminal window is open (Section 2).
- [ ] I ran `cd` into the repo folder, and `ls` shows `README.md`, `app.py`, and `labs/` (Section 3).
- [ ] I typed `claude` and see the waiting input box — not a login message (Section 4).
- [ ] I know how to stop Claude Code (**Ctrl-C**) and start it again (`claude`) (Section 4).
- [ ] I understand a permission prompt is normal, and answering "Yes" is expected (Section 6).
- [ ] I know my lab's exact branch commands will be printed on that lab's own Step 0 — nothing to memorize now (Section 7).
- [ ] I checked `http://localhost:5050/`, and either see the app, or know the one command to start it (`python app.py`) (Section 8).
- [ ] I know exactly what to do the moment I'm stuck: say so immediately (Section 9).

All checked? Open your assigned lab card and start at Step 0.
