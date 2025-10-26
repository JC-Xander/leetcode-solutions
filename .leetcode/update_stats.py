#!/usr/bin/env python3
"""
LeetCode Stats Updater
Updates the README.md file with current LeetCode statistics
"""

import re
import requests
from pathlib import Path

# Configuration
USERNAME = "jc-xander"
API_URL = f"https://leetcode-stats-api.herokuapp.com/{USERNAME}"
README_PATH = Path(__file__).parent.parent / "README.md"

def fetch_leetcode_stats():
    """Fetch LeetCode statistics from the API"""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stats: {e}")
        return None

def create_progress_bar(solved, total, length=20):
    """Create a text-based progress bar"""
    if total == 0:
        percentage = 0
    else:
        percentage = (solved / total) * 100
    
    filled = int((percentage / 100) * length)
    bar = "█" * filled + "░" * (length - filled)
    return f"{bar}  {percentage:.1f}%"

def update_readme(stats):
    """Update README.md with new statistics"""
    if not README_PATH.exists():
        print(f"README.md not found at {README_PATH}")
        return False
    
    # Extract statistics
    easy_solved = stats.get("easySolved", 0)
    medium_solved = stats.get("mediumSolved", 0)
    hard_solved = stats.get("hardSolved", 0)
    total_solved = stats.get("totalSolved", 0)
    total_questions = stats.get("totalQuestions", 3000)
    acceptance_rate = stats.get("acceptanceRate", 0)
    
    # Read current README
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update badges
    content = re.sub(
        r'Problems%20Solved-\d+',
        f'Problems%20Solved-{total_solved}',
        content
    )
    content = re.sub(
        r'Easy-\d+',
        f'Easy-{easy_solved}',
        content
    )
    content = re.sub(
        r'Medium-\d+',
        f'Medium-{medium_solved}',
        content
    )
    content = re.sub(
        r'Hard-\d+',
        f'Hard-{hard_solved}',
        content
    )
    
    # Update statistics section
    stats_pattern = r'```text\nTotal Solved.*?\n```'
    stats_text = f"""```text
Total Solved    : {total_solved}/{total_questions}+
Easy            : {easy_solved}
Medium          : {medium_solved}
Hard            : {hard_solved}
Acceptance Rate : {acceptance_rate:.1f}%
```"""
    content = re.sub(stats_pattern, stats_text, content, flags=re.DOTALL)
    
    # Update progress bars
    progress_pattern = r'```text\nEasy.*?Hard.*?\n```'
    progress_text = f"""```text
Easy    {create_progress_bar(easy_solved, 800)}
Medium  {create_progress_bar(medium_solved, 1700)}
Hard    {create_progress_bar(hard_solved, 700)}
```"""
    content = re.sub(progress_pattern, progress_text, content, flags=re.DOTALL)
    
    # Write updated content
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ README.md updated successfully!")
    print(f"📊 Total Solved: {total_solved}")
    print(f"   Easy: {easy_solved} | Medium: {medium_solved} | Hard: {hard_solved}")
    return True

def main():
    """Main function"""
    print(f"🔄 Fetching LeetCode stats for {USERNAME}...")
    
    stats = fetch_leetcode_stats()
    if stats is None:
        print("❌ Failed to fetch statistics")
        return 1
    
    print(f"✅ Stats fetched successfully!")
    
    if update_readme(stats):
        return 0
    else:
        return 1

if __name__ == "__main__":
    exit(main())
