# AI Research Digest Agent

A simple, reliable research digest agent that automatically fetches recent AI research papers and delivers clean email summaries to your inbox.

<img width="1425" height="711" alt="image" src="https://github.com/user-attachments/assets/3b10c560-ab0f-49e8-b80f-15448bcc5e92" />


## ✅ Features

- **arXiv Paper Fetching** - Fetches recent AI/ML/NLP papers from arXiv
- **Email Delivery** - Sends HTML-formatted digest emails via SMTP  
- **Smart Filtering** - Filters papers by categories and keywords
- **Database Tracking** - Saves digest records to SQLite
- **Clean Logging** - Proper error handling and progress tracking
- **Easy CLI** - Simple command-line interface

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install feedparser python-dotenv
```

### 2. Configure Email
Create a `.env` file:
```env
EMAIL_USER=your.email@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@example.com
```

### 3. Test Configuration
```bash
python main.py --test-config
```

### 4. Run Digest
```bash
# Preview papers (dry run)
python main.py --dry-run

# Generate digest without sending email
python main.py --no-email

# Full run: generate and send email
python main.py
```

## 📊 What You Get

- **18-20 recent papers** from the last 7 days
- **AI, ML, NLP categories** (cs.AI, cs.LG, cs.CL)
- **Keyword filtering** removes irrelevant papers
- **Clean HTML emails** with paper summaries, authors, and links
- **Database tracking** of all generated digests

## 📁 Files

- `main.py` - Main application
- `fetchers.py` - arXiv paper fetching
- `config.py` - Configuration management
- `email_sender.py` - SMTP email sending
- `.env` - Your email credentials
- `papers.db` - SQLite database

## 🛠️ Usage Examples

```bash
# Test everything is working
python main.py --test-config

# Preview what papers would be included  
python main.py --dry-run

# Generate digest without sending email
python main.py --no-email

# Full automated digest
python main.py
```

## ⚙️ Configuration

The agent fetches papers from these categories by default:
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning  
- `cs.CL` - Computational Linguistics

And filters using these keywords:
- transformer, llm, large language model
- vision transformer, diffusion, reinforcement learning
- computer vision, nlp, multimodal
- embedding, attention, neural network

You can modify these in `config.py` if needed.

## 🔧 Automation

To run daily, you can set up a scheduled task (Windows) or cron job (Linux/Mac):

**Windows Task Scheduler:**
```
python C:\path\to\your\research-digest-agent\main.py
```

**Linux/Mac Cron (daily at 7 AM):**
```bash
0 7 * * * cd /path/to/research-digest-agent && python main.py
```

---

**Simple. Reliable. Focused on what works.** 🎯

