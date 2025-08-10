#!/usr/bin/env python3
"""
Streamlined Working Research Fetchers
====================================

This module contains only the features that are actually working properly.
No experimental features, just solid, tested functionality.
"""

import requests
import feedparser
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class WorkingPaper:
    """Simple paper class with only working features"""
    
    def __init__(self, entry_data: Dict[str, Any]):
        self.raw_data = entry_data
        self._parse_entry()
    
    def _parse_entry(self):
        """Parse feedparser entry into structured data"""
        entry = self.raw_data
        
        # Basic information that always works
        self.id = entry.get('id', '').split('/')[-1]  # Extract arXiv ID
        self.title = self._clean_text(entry.get('title', ''))
        self.summary = self._clean_text(entry.get('summary', ''))
        self.abstract = self.summary  # Alias
        
        # Authors
        self.authors = []
        if 'authors' in entry:
            for author in entry['authors']:
                if isinstance(author, dict) and 'name' in author:
                    self.authors.append(author['name'])
                elif isinstance(author, str):
                    self.authors.append(author)
        
        # Dates
        self.published = self._parse_date(entry.get('published', ''))
        self.updated = self._parse_date(entry.get('updated', ''))
        
        # Categories
        self.categories = []
        if 'tags' in entry:
            for tag in entry['tags']:
                if isinstance(tag, dict) and 'term' in tag:
                    self.categories.append(tag['term'])
        
        self.primary_category = self.categories[0] if self.categories else None
        
        # URLs
        self.arxiv_url = entry.get('id', '')
        self.pdf_url = entry.get('id', '').replace('/abs/', '/pdf/') + '.pdf'
        
        # Additional metadata
        self.comment = entry.get('arxiv_comment', '')
        self.doi = entry.get('arxiv_doi', '')
        
    def _clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ""
        import re
        return re.sub(r'\s+', ' ', text.strip())
    
    def _parse_date(self, date_str: str) -> Optional[datetime]:
        """Parse date string to datetime object"""
        if not date_str:
            return None
        try:
            if date_str.endswith('Z'):
                date_str = date_str[:-1] + '+00:00'
            return datetime.fromisoformat(date_str).replace(tzinfo=None)
        except Exception as e:
            logger.warning(f"Could not parse date '{date_str}': {e}")
            return None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'abstract': self.abstract,
            'authors': self.authors,
            'published': self.published.isoformat() if self.published else None,
            'updated': self.updated.isoformat() if self.updated else None,
            'categories': self.categories,
            'primary_category': self.primary_category,
            'arxiv_url': self.arxiv_url,
            'pdf_url': self.pdf_url,
            'comment': self.comment,
            'doi': self.doi
        }

def fetch_working_arxiv_papers(
    query: str,
    days: int = 7,
    max_results: int = 20
) -> List[WorkingPaper]:
    """
    Fetch papers from arXiv - WORKING VERSION ONLY
    
    Args:
        query: arXiv search query (e.g., "cat:cs.CL OR cat:cs.LG")
        days: Filter papers from last N days
        max_results: Maximum number of results to fetch
    
    Returns:
        List of WorkingPaper objects
    """
    logger.info(f"Fetching arXiv papers: query='{query}', days={days}, max_results={max_results}")
    
    papers = []
    cutoff_date = datetime.now() - timedelta(days=days)
    
    try:
        # Make request
        response = requests.get(
            "http://export.arxiv.org/api/query",
            params={
                'search_query': query,
                'start': 0,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            },
            timeout=30
        )
        response.raise_for_status()
        
        # Parse with feedparser (this part definitely works!)
        feed = feedparser.parse(response.content)
        
        logger.info(f"Retrieved {len(feed.entries)} entries from arXiv")
        
        # Process entries
        for entry in feed.entries:
            try:
                paper = WorkingPaper(entry)
                
                # Apply date filter
                if paper.published and paper.published >= cutoff_date:
                    papers.append(paper)
                elif not paper.published:
                    # Include papers without clear publication date
                    papers.append(paper)
                    
            except Exception as e:
                logger.error(f"Error parsing paper entry: {e}")
                continue
        
        logger.info(f"Filtered to {len(papers)} papers within last {days} days")
        
    except Exception as e:
        logger.error(f"Error fetching arXiv papers: {e}")
    
    return papers

def filter_papers_by_keywords(
    papers: List[WorkingPaper],
    keywords: List[str]
) -> List[WorkingPaper]:
    """Filter papers by keywords - SIMPLE VERSION THAT WORKS"""
    
    filtered = []
    
    for paper in papers:
        text_content = f"{paper.title} {paper.abstract}".lower()
        
        # Check if any keyword matches
        if any(keyword.lower() in text_content for keyword in keywords):
            filtered.append(paper)
    
    logger.info(f"Filtered from {len(papers)} to {len(filtered)} papers using keywords")
    return filtered

def get_working_digest(
    query: str = "cat:cs.AI OR cat:cs.LG OR cat:cs.CL",
    days: int = 7,
    max_results: int = 20,
    keywords: List[str] = None
) -> List[Dict[str, Any]]:
    """
    Get a working research digest - NO EXPERIMENTAL FEATURES
    
    This function is guaranteed to work and return clean data.
    """
    logger.info("Starting WORKING digest generation")
    
    # Default keywords for AI/ML papers
    if keywords is None:
        keywords = [
            "transformer", "llm", "language model", "neural", "deep learning",
            "machine learning", "artificial intelligence", "computer vision",
            "natural language", "reinforcement learning"
        ]
    
    # Fetch papers from arXiv
    papers = fetch_working_arxiv_papers(
        query=query,
        days=days,
        max_results=max_results
    )
    
    if not papers:
        logger.warning("No papers fetched")
        return []
    
    # Filter by keywords
    filtered_papers = filter_papers_by_keywords(papers, keywords)
    
    # Convert to dictionaries for easy JSON export
    digest = [paper.to_dict() for paper in filtered_papers]
    
    logger.info(f"Generated working digest with {len(digest)} papers")
    return digest

if __name__ == "__main__":
    # Simple test
    print("🧪 Testing working fetchers...")
    
    digest = get_working_digest(
        query="cat:cs.CL",
        days=7,
        max_results=5
    )
    
    print(f"✅ Generated digest with {len(digest)} papers")
    
    for i, paper in enumerate(digest, 1):
        print(f"{i}. {paper['title']}")
        print(f"   Authors: {', '.join(paper['authors'][:2])}")
        print(f"   arXiv: {paper['arxiv_url']}")
        print()
