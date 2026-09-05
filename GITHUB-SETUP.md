# Putting this on GitHub (and why it makes handoff trivial)

The whole project is packaged in the **`repo/`** folder, already committed as a git repository.

---

## Why GitHub solves the handoff problem

Instead of explaining the project to a new AI and uploading a pile of files, you paste **one line**:

> Read https://github.com/YOURNAME/photo-style-prompts — start with AGENT.md, then help me with ___

Most AI assistants can read a public GitHub repo directly. `AGENT.md` briefs them on the rules,
the lessons already learned, and what's done. Nothing gets lost, and you never re-explain.

---

## Upload it (easiest way — no command line)

1. Go to **github.com** → **New repository**
2. Name it `photo-style-prompts`, set it **Public**, don't add a README (there's one already)
3. On the next screen click **uploading an existing file**
4. Download `repo/` from this workspace, then drag **everything inside it** into the browser
5. Click **Commit changes**

Done. Your URL is `https://github.com/YOURNAME/photo-style-prompts`

> **Note:** the folder contains your two photos in `photos/` and your reference images in `refs/`.
> If you'd rather not have those public, delete those two folders before uploading, or make the
> repository **Private** instead. Everything still works — the prompts just won't have example
> photos attached.

## Or with the command line

```bash
cd repo
git remote add origin https://github.com/YOURNAME/photo-style-prompts.git
git branch -M main
git push -u origin main
```

---

## Viewing the picker online (optional, 30 seconds)

GitHub can host `style-picker.html` as a real webpage you can open on your phone:

1. In your repo go to **Settings → Pages**
2. Under *Source* pick **Deploy from a branch**, branch **main**, folder **/ (root)**, click Save
3. Wait about a minute, then open:
   `https://YOURNAME.github.io/photo-style-prompts/style-picker.html`

Now your style library is a bookmark, always with you.

---

## Working with a new AI from then on

**Starting a session:**
> Read https://github.com/YOURNAME/photo-style-prompts — start with AGENT.md. I want to test the
> Blue Painterly style on a new photo I'm attaching.

**Ending a session:**
> Give me the updated `styles.json` and `ig-effects-recreated.md` so I can commit them.

Then upload those two files back to GitHub (drag-and-drop works). That's the whole loop — the repo
stays the memory, and every assistant picks up exactly where the last one stopped.

---

## If an AI can't open the link

Some tools can't browse the web. In that case just attach these four files:

1. `AGENT.md`
2. `prompts/styles.json`
3. one photo
4. one image from `examples/` as the quality bar
