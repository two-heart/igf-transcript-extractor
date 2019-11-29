import subprocess

from bs4 import BeautifulSoup
import re

base = "https://intgovforum.org/"

url = base + "multilingual/igf-2019-transcripts"
html_page = subprocess.Popen(["wget", "-qO-", "https://intgovforum.org/multilingual/igf-2019-transcripts"],
                             stdout=subprocess.PIPE).communicate()[0]
soup = BeautifulSoup(html_page, "html.parser")

output = ""

for link in soup.findAll('a', attrs={'href': re.compile("^/multilingual/content/igf-2019-%E2%80%93")}):
    transcript_html = subprocess.Popen(["wget", "-qO-", base + link.get("href")],
                                       stdout=subprocess.PIPE).communicate()[0]
    inner_html = BeautifulSoup(transcript_html, "html.parser").findAll('div', {'class': 'WordSection1'})
    if inner_html:
        output += "^^new transcript^^" + link.get("href") + "^^" + "\n"
        output += inner_html[0].text + "\n"
text_file = open("allTranscripts.txt", "w")
text_file.write(output)
text_file.close()
