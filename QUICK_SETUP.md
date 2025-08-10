# 🚀 QUICK SETUP - Autonomous Daily Email Digest

## 5-Minute GitHub Actions Setup (100% FREE!)

### Step 1: Create GitHub Repository

**Option A - Using GitHub Desktop (Easiest):**
1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in to your GitHub account
3. Click "Publish repository" 
4. Name: `research-digest-agent`
5. Make it **Public** (required for free Actions)
6. Click "Publish"

**Option B - Using Command Line:**
```bash
# Install GitHub CLI first
winget install GitHub.cli

# Then run:
gh auth login
gh repo create research-digest-agent --public --push --source .
```

### Step 2: Add Email Secrets
1. Go to your new repo on GitHub.com
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add these 3 secrets:

| Secret Name | Secret Value |
|-------------|--------------|
| `EMAIL_USER` | `your.email@gmail.com` |
| `EMAIL_PASSWORD` | `your_gmail_app_password` |
| `RECIPIENT_EMAIL` | `recipient@example.com` |

### Step 3: Enable GitHub Actions
1. Go to **Actions** tab in your repo
2. Click **"I understand my workflows"** 
3. Enable workflows

### Step 4: Test It! 
1. Go to **Actions** → **Daily AI Research Digest**
2. Click **Run workflow** → **Run workflow**
3. Check your email in a few minutes! 📧

## ✅ You're Done!

Your digest will now run **automatically every day at 7:00 AM UTC**

### Want to change the time?
Edit `.github/workflows/daily-digest.yml`:
```yaml
schedule:
  # 7 AM UTC = 12:30 PM IST (India)
  - cron: '0 7 * * *'
  
  # 1:30 AM UTC = 7:00 AM IST (India)  
  - cron: '30 1 * * *'
```

### Want to change frequency?
```yaml
# Only weekdays at 7 AM
- cron: '0 7 * * 1-5'

# Twice daily (morning and evening)
- cron: '0 7,19 * * *'
```

## 🎯 Benefits of GitHub Actions:
- ✅ **Completely FREE** (2000 minutes/month)
- ✅ **Always runs** - no computer needed
- ✅ **Cloud reliable**
- ✅ **Easy to modify**
- ✅ **Professional deployment**

---

**That's it! You'll get fresh AI research papers in your inbox every day! 🤖📚**
