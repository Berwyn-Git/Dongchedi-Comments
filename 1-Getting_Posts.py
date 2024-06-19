import requests
from bs4 import BeautifulSoup
import re
import csv


def scrape_and_save_content(url):
    page_number = 1
    while True:
        # 构建当前页的URL
        current_url = f'{url}/{page_number}' if page_number > 1 else url

        # 发送GET请求获取网页内容
        response = requests.get(current_url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 使用Beautiful Soup解析HTML
            soup = BeautifulSoup(response.text, 'lxml')

            # 找到指定的<script>标签
            script_tag = soup.find('script', id='__NEXT_DATA__', type='application/json', crossorigin='anonymous')

            if script_tag:
                # 提取该标签下的文本内容
                script_contents = script_tag.text

                # 翻页处理
                if page_number == page_number_web + 1:
                    print("已到达最后一页")
                    break
                else:
                    # 使用正则表达式查找包含 "content": 的部分
                    pattern_1 = r'"content":\s*"(.*?)"'
                    content_matches = re.findall(pattern_1, script_contents)
                    # 使用正则表达式查找对应评论的连接
                    pattern_2 = r'"gid_str":\s*"(.*?)"'
                    post_links_pre = re.findall(pattern_2, script_contents)
                    link_format = "https://wwww.dongchedi.com/ugc/article"
                    post_links = [f'{link_format}/{post_link}' for post_link in post_links_pre]

                    # 打开 CSV 文件以追加内容
                    with open('Result.csv', 'a', newline='', encoding='utf-8') as csvfile:
                        csv_writer = csv.writer(csvfile)

                        # 写入每个 content
                        for content, post_link in zip(content_matches, post_links):
                            csv_writer.writerow([content, post_link])

                    print(f"已爬取并写入第{page_number}页的内容")

                page_number += 1

            else:
                print("未找到指定的<script>标签")
                break
        else:
            print(f"请求失败，状态码: {response.status_code}")
            break


if __name__ == '__main__':
    input_url = input("请输入要爬取的网页URL：")
    page_number_web = int(input("请输入网页的最大页数："))
    scrape_and_save_content(input_url)