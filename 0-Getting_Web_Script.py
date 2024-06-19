import requests
from bs4 import BeautifulSoup
import re

web_link = input("Web Link:")
response = requests.get(web_link)

soup = BeautifulSoup(response.text, 'lxml')
script_tag = soup.find('script', id='__NEXT_DATA__', type='application/json', crossorigin='anonymous')
script_contents = script_tag.text

pattern_3 = r'{"header":"公告",\s*"content":".*?"}'
excluded_content = re.findall(pattern_3, script_contents)
for exc in excluded_content:
    content_matches = [c for c in content_matches if c != exc.split('"content":"')[1][:-2]]
    print(content_matches)

# pattern_2 = r'"gid_str":\s*"(.*?)"'
# post_links_pre = re.findall(pattern_2, script_contents)
# link_format = "https://wwww.dongchedi.com/ugc/article"
# post_links = [f'{link_format}/{post_link}' for post_link in post_links_pre]
#
# print(post_links)