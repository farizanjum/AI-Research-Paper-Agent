# 🚀 Deployment Guide - Autonomous Daily Research Digest

Deploy your Research Digest Agent to run automatically every day at your preferred time!

## 🕐 Option 1: Windows Task Scheduler (Local)

**Best for**: Running on your Windows PC/laptop that stays on

### Quick Setup:
1. **Run as Administrator** (Right-click PowerShell/CMD → "Run as administrator")
2. Double-click `setup_windows_scheduler.bat`
3. Done! ✅

### Manual Setup:
```bash
# Create task for daily 7 AM execution
schtasks /create /tn "ResearchDigestAgent" /tr "python C:\Users\Fariz\research-digest-agent\main.py" /sc daily /st 07:00

# Change time to 9:30 AM
schtasks /change /tn "ResearchDigestAgent" /st 09:30

# Delete task
schtasks /delete /tn "ResearchDigestAgent" /f
```

**Pros**: Free, simple, runs locally  
**Cons**: Requires your computer to be on

---

## ☁️ Option 2: GitHub Actions (FREE Cloud)

**Best for**: Free cloud automation, no server needed

### Setup Steps:

1. **Create GitHub Repository**:
   ```bash
   cd C:\Users\Fariz\research-digest-agent
   git init
   git add .
   git commit -m "Initial commit"
   gh repo create research-digest-agent --public --push
   ```

2. **Add Secrets** (GitHub repo → Settings → Secrets):
   - `EMAIL_USER`: farizanjum2018@gmail.com
   - `EMAIL_PASSWORD`: your app password
   - `RECIPIENT_EMAIL`: works.farizanjum@gmail.com

3. **Push the workflow** (already created in `.github/workflows/daily-digest.yml`)

4. **Enable Actions**: Go to Actions tab in your GitHub repo → Enable workflows

**Pros**: Completely free, cloud-based, no maintenance  
**Cons**: 2000 minutes/month limit (plenty for daily emails)

---

## 🌐 Option 3: VPS/Cloud Server (Advanced)

**Best for**: Full control, professional deployment

### Cloud Provider Options:

#### A) **DigitalOcean** ($6/month)
```bash
# Create droplet, SSH in, then:
git clone https://github.com/yourusername/research-digest-agent.git
cd research-digest-agent
chmod +x deploy_cloud.sh
./deploy_cloud.sh
```

#### B) **AWS EC2 Free Tier**
```bash
# Launch t2.micro instance, SSH in:
sudo apt update
git clone your-repo
cd research-digest-agent
bash deploy_cloud.sh
```

#### C) **Google Cloud Platform** (Free $300 credit)
```bash
# Create VM instance, then same steps as above
```

**Pros**: Full control, always running, professional  
**Cons**: Costs $5-10/month

---

## 🎯 Recommended Approach

### For You: **GitHub Actions** (Option 2)

**Why?**
- ✅ **Completely FREE**
- ✅ **No server maintenance**
- ✅ **Cloud-based reliability**
- ✅ **Easy to modify schedule**
- ✅ **Automatic backups via Git**

### Setup GitHub Actions (5 minutes):

1. **Install GitHub CLI** (if not installed):
   ```bash
   winget install GitHub.cli
   ```

2. **Create repo and deploy**:
   ```bash
   cd C:\Users\Fariz\research-digest-agent
   
   # Initialize git
   git init
   git add .
   git commit -m "Research digest agent ready for deployment"
   
   # Create GitHub repo
   gh auth login
   gh repo create research-digest-agent --public --push --source .
   ```

3. **Add secrets** on GitHub:
   - Go to: `https://github.com/yourusername/research-digest-agent/settings/secrets/actions`
   - Add:
     - `EMAIL_USER` = `farizanjum2018@gmail.com`
     - `EMAIL_PASSWORD` = `shff rnha ustw qxvu`
     - `RECIPIENT_EMAIL` = `works.farizanjum@gmail.com`

4. **Enable workflow**:
   - Go to Actions tab → Enable workflows
   - It will run daily at 7:00 AM UTC (adjust timezone in `.github/workflows/daily-digest.yml`)

---

## ⚙️ Customizing Schedule

### Change Time:
Edit `.github/workflows/daily-digest.yml`:
```yaml
schedule:
  # 7 AM UTC = 12:30 PM IST, 2:30 AM EST, etc.
  - cron: '0 7 * * *'
  
  # 9:30 AM UTC (change to your preferred time)
  - cron: '30 9 * * *'
```

### Change Frequency:
```yaml
# Every Monday at 9 AM
- cron: '0 9 * * 1'

# Twice daily (9 AM and 6 PM)
- cron: '0 9,18 * * *'

# Only weekdays
- cron: '0 7 * * 1-5'
```

---

## 🔍 Monitoring & Troubleshooting

### GitHub Actions:
- **Check runs**: Go to Actions tab in your repo
- **View logs**: Click on any workflow run
- **Manual trigger**: Actions → Daily AI Research Digest → Run workflow

### Windows Task Scheduler:
- **Check status**: Task Scheduler → Task Scheduler Library → ResearchDigestAgent
- **View history**: Right-click task → View history
- **Test run**: Right-click task → Run

### VPS/Cloud:
```bash
# Check service status
sudo systemctl status research-digest.timer

# View logs
sudo journalctl -u research-digest.service -f

# Manual test run
sudo systemctl start research-digest.service
```

---

## 🎉 You're All Set!

Choose your deployment method and enjoy automated daily AI research digests! 

**Need help?** The system will:
- ✅ Fetch latest AI papers daily
- ✅ Send beautiful HTML emails to works.farizanjum@gmail.com
- ✅ Skip weekends if no new papers
- ✅ Log all activity for monitoring
