# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import  json
#
# class BaiducrawlerPipeline:
#
#     def __init__(self):
#         pass
#
#     def open_spider(self, spider):
#         print("爬虫开始了")
#         self.fp = open("data.json", "w", encoding="utf-8")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + "\n")
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print("爬虫结束了")

# from scrapy.exporters import JsonItemExporter  #比较耗内存
# class BaiducrawlerPipeline:
#
#     def __init__(self):
#         self.fp = open("data.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#
#     def open_spider(self, spider):
#         print("爬虫开始了")
#
#
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了")


# from scrapy.exporters import JsonLinesItemExporter
# # 存储到硬盘 坏处是每一个字典是一行，整个文件不是一个满足json格式的文件 好处是 每次处理数据的时候就直接
# # 存储到了硬盘，比较安全
#
from scrapy.exporters import JsonLinesItemExporter


class BaiducrawlerPipeline:

    def __init__(self):
        self.fp = open("data.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print("爬虫开始了")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print("存了")
        return item

    def close_spider(self, spider):
        self.fp.close()
        print("爬虫结束了")
