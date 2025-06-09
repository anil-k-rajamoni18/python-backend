from collections import Counter
import re

text = """
Python is great for data science. Python is also widely used in web development, scripting, and automation.
"""

# Clean and split text into words
words = re.findall(r'\w+', text.lower())

# Count word frequencies
word_counts = Counter(words)

# Get top 3 most common words
print("🔢 Most common words:", word_counts.most_common(5))