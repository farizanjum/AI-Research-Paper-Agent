#!/usr/bin/env python3
"""
SIMPLE Research Digest Agent - WORKING VERSION ONLY
===================================================

This version includes ONLY features that work properly:
- arXiv paper fetching (using feedparser)
- Email sending (working SMTP)
- Basic paper filtering
- Clean JSON output

NO experimental features, NO complex enrichment, just what works!
"""

import logging
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any
import argparse
import sys

from config import config
from email_sender import EmailSender
from fetchers import get_working_digest

# Configure logging with UTF-8 encoding for Windows compatibility
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('digest_agent.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Fix Windows console encoding for emojis
import sys
if sys.platform.startswith('win'):
    import os
    os.system('chcp 65001 >nul 2>&1')  # Set console to UTF-8

logger = logging.getLogger(__name__)

class SimpleDigestAgent:
    """SIMPLIFIED digest agent with only working features"""
    
    def __init__(self):
        self.email_sender = EmailSender()
        self.db_path = config.DATABASE_PATH
        self._init_database()
    
    def _init_database(self):
        """Initialize simple database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS simple_digests (
                    date TEXT PRIMARY KEY,
                    papers_count INTEGER,
                    papers_json TEXT,
                    sent_successfully BOOLEAN
                )
            ''')
            
            conn.commit()
            conn.close()
            logger.info("Database initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            raise
    
    def generate_simple_digest(self) -> Dict[str, Any]:
        """Generate a simple digest using only working features"""
        logger.info("🚀 Starting SIMPLE digest generation...")
        
        # Use working fetcher
        papers = get_working_digest(
            query="cat:cs.AI OR cat:cs.LG OR cat:cs.CL",
            days=7,  # Use 7 days to ensure we get papers
            max_results=20
        )
        
        if not papers:
            logger.warning("No papers found")
            return None
        
        # Create simple digest structure
        digest = {
            'date': datetime.now().isoformat(),
            'papers_count': len(papers),
            'papers': papers,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        logger.info(f"✅ Generated simple digest with {len(papers)} papers")
        return digest
    
    def create_simple_email_content(self, digest: Dict[str, Any]) -> str:
        """Create simple HTML email content"""
        
        date_str = datetime.now().strftime('%B %d, %Y')
        papers = digest['papers']
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Research Digest - {date_str}</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
                .header {{ text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; margin-bottom: 30px; }}
                .paper {{ border-left: 4px solid #007bff; margin-bottom: 25px; padding-left: 15px; }}
                .paper-title {{ font-size: 18px; font-weight: bold; color: #333; margin-bottom: 8px; }}
                .paper-meta {{ color: #666; font-size: 14px; margin-bottom: 10px; }}
                .paper-abstract {{ margin-bottom: 10px; }}
                .paper-links {{ margin-top: 10px; }}
                .paper-links a {{ color: #007bff; text-decoration: none; margin-right: 15px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🤖 AI Research Digest</h1>
                <p>{date_str} • {len(papers)} papers</p>
            </div>
        """
        
        for i, paper in enumerate(papers, 1):
            authors = ", ".join(paper['authors'][:3])
            if len(paper['authors']) > 3:
                authors += " et al."
            
            html += f"""
            <div class="paper">
                <div class="paper-title">{i}. {paper['title']}</div>
                <div class="paper-meta">
                    👥 {authors} • 📅 {paper['published'][:10] if paper['published'] else 'Unknown'}
                </div>
                <div class="paper-abstract">
                    {paper['abstract'][:300]}{"..." if len(paper['abstract']) > 300 else ""}
                </div>
                <div class="paper-links">
                    <a href="{paper['arxiv_url']}">📄 arXiv Paper</a>
                    <a href="{paper['pdf_url']}">📄 PDF</a>
                </div>
            </div>
            """
        
        html += """
            <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid #ccc; color: #666;">
                <p>Generated by Simple Research Digest Agent</p>
                <p>Happy researching! 🎓</p>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def send_simple_digest(self, digest: Dict[str, Any]) -> bool:
        """Send simple digest email"""
        try:
            html_content = self.create_simple_email_content(digest)
            
            # Create email
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"AI Research Digest - {datetime.now().strftime('%B %d, %Y')}"
            msg['From'] = config.EMAIL_USER
            msg['To'] = config.RECIPIENT_EMAIL
            
            html_part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(html_part)
            
            # Send
            import smtplib
            server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
            server.starttls()
            server.login(config.EMAIL_USER, config.EMAIL_PASSWORD)
            
            text = msg.as_string()
            server.sendmail(config.EMAIL_USER, config.RECIPIENT_EMAIL, text)
            server.quit()
            
            logger.info("✅ Simple digest email sent successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error sending email: {e}")
            return False
    
    def save_digest_record(self, digest: Dict[str, Any], sent_successfully: bool):
        """Save digest to database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO simple_digests 
                (date, papers_count, papers_json, sent_successfully)
                VALUES (?, ?, ?, ?)
            ''', (
                datetime.now().strftime('%Y-%m-%d'),
                digest['papers_count'],
                json.dumps(digest['papers']),
                sent_successfully
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            logger.error(f"Error saving digest record: {e}")
    
    def run_simple_digest(self, dry_run: bool = False, send_email: bool = True) -> bool:
        """Run the SIMPLE digest pipeline"""
        try:
            logger.info("=" * 50)
            logger.info("🚀 STARTING SIMPLE DIGEST GENERATION")
            logger.info("=" * 50)
            
            # Generate digest
            digest = self.generate_simple_digest()
            
            if not digest:
                logger.info("No digest generated. Exiting.")
                return False
            
            # Print summary
            logger.info(f"📊 DIGEST SUMMARY:")
            logger.info(f"  📅 Date: {digest['date'][:10]}")
            logger.info(f"  📄 Papers: {digest['papers_count']}")
            
            for i, paper in enumerate(digest['papers'][:5], 1):  # Show first 5
                logger.info(f"    {i}. {paper['title'][:60]}...")
            
            if digest['papers_count'] > 5:
                logger.info(f"    ... and {digest['papers_count'] - 5} more papers")
            
            if dry_run:
                logger.info("🔍 DRY RUN MODE - Not sending email or saving to database")
                return True
            
            # Send email
            sent_successfully = False
            if send_email:
                logger.info("📧 Sending digest email...")
                sent_successfully = self.send_simple_digest(digest)
            else:
                logger.info("📧 Email sending skipped (--no-email option)")
            
            # Save record (always save, regardless of email option)
            self.save_digest_record(digest, sent_successfully)
            
            logger.info("=" * 50)
            logger.info("✅ SIMPLE DIGEST COMPLETED SUCCESSFULLY")
            logger.info("=" * 50)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Fatal error in simple digest: {e}")
            return False
    
    def test_configuration(self) -> bool:
        """Test simple configuration"""
        logger.info("🧪 Testing SIMPLE configuration...")
        
        issues = []
        
        # Test email
        if not all([config.EMAIL_USER, config.EMAIL_PASSWORD, config.RECIPIENT_EMAIL]):
            issues.append("Email configuration incomplete")
        else:
            if not self.email_sender.test_email_connection():
                issues.append("Email connection failed")
        
        # Test database
        try:
            conn = sqlite3.connect(self.db_path)
            conn.close()
        except Exception as e:
            issues.append(f"Database connection failed: {e}")
        
        if issues:
            logger.error("❌ Configuration issues found:")
            for issue in issues:
                logger.error(f"  - {issue}")
            return False
        else:
            logger.info("✅ All SIMPLE configuration tests passed")
            return True

def main():
    """Main entry point for SIMPLE digest agent"""
    parser = argparse.ArgumentParser(description='SIMPLE Research Digest Agent')
    parser.add_argument('--dry-run', action='store_true',
                       help='Run without sending emails or saving to database')
    parser.add_argument('--no-email', action='store_true',
                       help='Generate digest but do not send email')
    parser.add_argument('--test-config', action='store_true',
                       help='Test configuration and exit')
    
    args = parser.parse_args()
    
    # Create simple agent
    try:
        agent = SimpleDigestAgent()
    except Exception as e:
        logger.error(f"❌ Failed to initialize SIMPLE agent: {e}")
        return 1
    
    # Test configuration if requested
    if args.test_config:
        if agent.test_configuration():
            return 0
        else:
            return 1
    
    # Run simple digest
    success = agent.run_simple_digest(
        dry_run=args.dry_run,
        send_email=not args.no_email
    )
    
    return 0 if success else 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
