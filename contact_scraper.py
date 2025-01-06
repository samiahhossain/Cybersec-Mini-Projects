from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re

# User input
given_url = input("Enter URL: ")
urls = deque([given_url])
limit = int(input("How many sites do you want to search through? "))

# Initializing
count = 0
scraped_urls = set()
emails = set()
phone_numbers = set()

try:
    while len(urls):
        # Searching until specified limit
        if count == limit:
            break
        count += 1
        
        url = urls.popleft()
        scraped_urls.add(url)

        # Breaking down URL
        parts = urllib.parse.urlsplit(url)
        base_url = '{0.scheme}://{0.netloc}'.format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url     # Determine 'directory' portion of link

        # Going into site
        print('[%d] Searching %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        
        # Collect text matching the regex (emails)
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(new_emails)

        # Collect text matching the regex (phone numbers)
        new_numbers = set(re.findall(r"\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}", response.text, re.I))
        phone_numbers.update(new_numbers)

        # Allow for HTML/XML parsing
        soup = BeautifulSoup(response.text, features="lxml")

        # Get more links to search through from HTML/XML code
        for anchor in soup.find_all("a"):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            # Complete for full link
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scraped_urls:
                # Add to URL list
                urls.append(link)
except KeyboardInterrupt:
    print('Closing!')

# Display emails
for mail in emails:
    print(mail)

# Display phone numbers
for number in phone_numbers:
    print(number)

print(f"Found {len(emails)} emails.")
print(f"Found {len(phone_numbers)} phone numbers.")