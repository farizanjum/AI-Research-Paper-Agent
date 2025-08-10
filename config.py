"""
Configuration settings for Research Digest Agent
"""
import os
from dataclasses import dataclass
from typing import List, Optional
from datetime import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@dataclass
class Config:
    # Data Sources
    HUGGINGFACE_API_BASE = "https://huggingface.co/api"
    ARXIV_API_BASE = "http://export.arxiv.org/api"
    
    # Keywords and domains of interest
    KEYWORDS: List[str] = None
    DOMAINS: List[str] = None
    
    # Number of papers to fetch daily
    MAX_PAPERS_PER_DAY: int = 10
    
    # Email settings
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    EMAIL_USER: Optional[str] = None
    EMAIL_PASSWORD: Optional[str] = None
    RECIPIENT_EMAIL: Optional[str] = None
    
    # LLM settings
    GEMINI_API_KEY: Optional[str] = None
    
    # Scheduling
    DELIVERY_TIME: time = time(7, 0)  # 7:00 AM
    
    # Database
    DATABASE_PATH: str = "papers.db"
    
    def __post_init__(self):
        # Load from environment variables
        self.EMAIL_USER = os.getenv('EMAIL_USER', self.EMAIL_USER)
        self.EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', self.EMAIL_PASSWORD)
        self.RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', self.RECIPIENT_EMAIL)
        self.GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', self.GEMINI_API_KEY)
        
        # Default keywords and domains if not specified
        if self.KEYWORDS is None:
            self.KEYWORDS = [
                "transformer", "llm", "large language model", "vision transformer",
                "diffusion", "reinforcement learning", "computer vision", "nlp",
                "multimodal", "embedding", "attention", "neural network"
            ]
        
        if self.DOMAINS is None:
            self.DOMAINS = [
                "cs.AI", "cs.LG", "cs.CV", "cs.CL", "cs.NE", "stat.ML"
            ]

# Global config instance
config = Config()
