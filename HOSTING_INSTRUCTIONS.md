# Hosting Guide — Simple steps

This file explains two easy ways to host your static site: (A) Vercel — recommended, and (B) GitHub Pages (useful if you want the site under a different GitHub account). Follow the steps exactly.

Prerequisites
- You have Git installed and basic comfort with the terminal.
- A GitHub account (and a second GitHub account if you want to push under a different account).
- (Optional for Vercel CLI) Node.js / npm installed.

Quick checklist before you push
1. Pick the GitHub account that will own the repository (the "hosting" account).
2. Decide the repository name (e.g. `pharma-site`).
3. Replace `https://YOUR_DOMAIN.com` placeholders in files (if you know the domain).

Option A — Deploy to Vercel (recommended)

1. Create a repository on GitHub under the target GitHub account

   - On GitHub (in the chosen account) click **New repository** and create `pharma-site` (public or private).

2. Push your local site to that repository

   Open a terminal in the project folder and run:

   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/OTHER_USERNAME/pharma-site.git
   git push -u origin main
   ```

   Replace `OTHER_USERNAME` and `pharma-site` with the actual account and repo name.

3. Deploy on Vercel (web method)

   - Go to https://vercel.com and sign up / log in.
   - Click "New Project" → Import from GitHub → select the `pharma-site` repo you just pushed.
   - For root directory, leave empty (site is at repository root). Vercel will detect a static site.
   - Click Deploy. When finished you get a live URL like `https://pharma-site.vercel.app`.

   OR use Vercel CLI (alternative):

   ```bash
   npm i -g vercel
   vercel login
   vercel --prod
   ```

4. After deploy

- Set a custom domain in the Vercel dashboard if you have one (add domain, follow DNS steps).
- Update `vercel.json` or site files if you need redirects/rewrite rules.
- Replace placeholder social links and canonical URL with your real domain.

Option B — Host via GitHub Pages under a different GitHub account

1. Create the repository on the other GitHub account (same as step A.1).

2. Push code to that repo (same as step A.2). Example if pushing from your current local repo:

   ```bash
   git remote add origin https://github.com/OTHER_USERNAME/pharma-site.git
   git push -u origin main
   ```

3. Enable GitHub Pages

   - On GitHub, open the repo → Settings → Pages.
   - Under "Build and deployment" choose **Branch: main** and folder **/ (root)**, then Save.
   - GitHub will provide a URL like `https://OTHER_USERNAME.github.io/pharma-site/` within a minute.

4. Notes for GitHub Pages

- If your site uses relative paths correctly (most files here do), it should work. If links use `../` from nested pages, verify pages load correctly.
- For a custom domain, configure DNS and add a `CNAME` in repo settings or a `CNAME` file in project root containing your domain.

Common tips & troubleshooting

- If images or CSS fail to load: check paths (absolute vs relative). Try opening a product page directly in the browser to confirm asset paths.
- If a page 404s on GH Pages: ensure case-sensitive filenames match exactly and that the repo push succeeded.
- If links still show `YOUR_DOMAIN` placeholders, search and replace before pushing.
- To change the GitHub remote later: `git remote set-url origin https://github.com/NEW_USER/REPO.git`

Verify the live site

1. Open the deployed URL (Vercel URL or `https://OTHER_USERNAME.github.io/pharma-site/`).
2. Click a few pages, check images, click the contact form and test `tel:` and `mailto:` links.
3. Use the Lighthouse panel in Chrome DevTools for a quick performance/accessibility check.

Want me to do it for you?
- I can: create the GitHub repo, push the code to the different account (you'll need to provide that account's access or create the repo and invite me), and trigger a Vercel deploy. Tell me which account name to use and whether you prefer Vercel or GitHub Pages.

That's it — this is the minimal, copy-paste friendly guide to get your static site live. Good luck! 🚀
