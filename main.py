import subprocess

from bs4 import BeautifulSoup
import re

base = "https://intgovforum.org/"

url = base + "multilingual/igf-2020-transcripts"
html_page = subprocess.Popen(["wget", "-qO-", "https://intgovforum.org/multilingual/igf-2020-transcripts"],
                             stdout=subprocess.PIPE).communicate()[0]
soup = BeautifulSoup(html_page, "html.parser")

output = ""

for link in soup.findAll('a', attrs={'href': re.compile("^/multilingual/content/igf-2020")}):
    print(link)
    transcript_html = subprocess.Popen(["wget", "-qO-", base + link.get("href")],
                                       stdout=subprocess.PIPE).communicate()[0]
    inner_html = BeautifulSoup(transcript_html, "html.parser").findAll('div', {'class': 'WordSection1'})
    if inner_html:
        output += "^^new transcript^^" + link.get("href") + "^^" + "\n"
        text = inner_html[0].text
        output += text + "\n"
text_file = open("2020.txt", "w")
text_file.write(output)
text_file.close()
