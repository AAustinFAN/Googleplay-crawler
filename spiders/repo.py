# # -*- coding: utf-8 -*-
# import os
# import scrapy
#
#
# class RepoSpider(scrapy.Spider):
#     name = 'repo'
#     allowed_domains = ['github.com']
#     path = r"C:\Users\18135\Desktop"
#     files = os.listdir(path)
#     start_urls = []
#     for file in files:
#         if not os.path.isdir(file):
#             f = open(path + "/" + file, encoding='UTF-8');
#             lines = f.readlines()
#             for line in lines:
#                 if line.startswith("SourceCode:"):
#                     print(line)
#                     line = line.replace("\n", "")
#                     link = line.split(":")[-1].strip()
#                     if "github" in link or "gitlab" in link:
#                         print(link)
#                         str = "http:"
#                         str = str + link
#                         start_urls.append(str)  # 每个文件的文本存到list中
#     print(start_urls)
#     print(len(start_urls))
#
#     def parse(self, response):
#         print('=' * 40)
#         # content = response.xpath(
#         #           "//*[text()[contains(.,'https://git')]]/text()"
#         # ).extract()[-1]
#         # print(content)
#         pass
