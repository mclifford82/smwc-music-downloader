# Download SMWC Music
# by Martin Clifford

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

header = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
  'AppleWebKit/537.11 (KHTML, like Gecko) '
  'Chrome/23.0.1271.64 Safari/537.11',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive'
}

page_num = 1
base_url = f"https://www.smwcentral.net/?p=section&s=smwmusic&u=0&g=0&o=date&d=desc&n={page_num}"

page = urlopen(Request(base_url, headers=header))
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

all_rows = soup.find_all("tr")
for x in all_rows[:5]:
  print(x)

#links = soup.find_all("a")
#all_links = [f'{base_url}/{target.string.lower()}' for target in links]

# <a href="//dl.smwcentral.net/31967/Brain%20Lord%20-%20Site%20of%20Civilization.zip">Download</a>
# r'//dl.smwcentral.net/(\d+)/(.*.zip)'