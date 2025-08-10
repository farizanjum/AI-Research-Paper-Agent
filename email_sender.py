"""
Simple email sender for Research Digest Agent
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

from config import config

logger = logging.getLogger(__name__)

class EmailSender:
    """Simple email sender for digest emails"""
    
    def __init__(self):
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.email_user = config.EMAIL_USER
        self.email_password = config.EMAIL_PASSWORD
        self.recipient_email = config.RECIPIENT_EMAIL
    
    def test_email_connection(self) -> bool:
        """Test email configuration"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            server.quit()
            
            logger.info("Email connection test successful")
            return True
            
        except Exception as e:
            logger.error(f"Email connection test failed: {e}")
            return False
