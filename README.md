# Googleplay-crawler
## It's just named baidu at the beginning, but it works for google in the latest version.
This crawler is based on scrapy framework. Get the apps information and  store them as dictionary in jSON FILE.
We got 5800k apps info thougn this program.

The items are as follows.
```
    url = scrapy.Field()
    app_id = scrapy.Field()
    Author = scrapy.Field()
    category = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    Updated = scrapy.Field()
    Size = scrapy.Field()
    installs = scrapy.Field()
    CurrentVersion = scrapy.Field()
    RequiresAndroid = scrapy.Field()
    ContentRating = scrapy.Field()
    developer_email = scrapy.Field()
```

Sample dictionary:

```
    {"Author": "Barokah Studio", "category": "Books & Reference", "app_id": "com.suratpendek.suratsuratpendek.alquran", "score": "4.7", "reviews": "3,875 total", "installs": "100,000+", "developer_email": "barokahstudio@yahoo.com", "url": "https://play.google.com/store/apps/details?id=com.suratpendek.suratsuratpendek.alquran&hl=en_US", "Size": "38M", "Updated": "July 21, 2020", "CurrentVersion": "3.0", "RequiresAndroid": "4.1 and up", "ContentRating": "Everyone"}
    
{"Author": "Onion search engine", "category": "Books & Reference", "app_id": "com.onionsearchengine.onionsearchengine", "score": "4.0", "reviews": "2,251 total", "installs": "500,000+", "developer_email": "info@onionsearchengine.com", "url": "https://play.google.com/store/apps/details?id=com.onionsearchengine.onionsearchengine&hl=en_US", "Size": "4.7M", "Updated": "July 21, 2020", "CurrentVersion": "2.3.5", "RequiresAndroid": "4.1 and up", "ContentRating": "Everyone"}

{"Author": "Hinovel", "category": "Books & Reference", "app_id": "com.aynovel.vixs", "score": "4.2", "reviews": "30,171 total", "installs": "1,000,000+", "developer_email": "support@hinovel.com", "url": "https://play.google.com/store/apps/details?id=com.aynovel.vixs&hl=en_US", "Size": "9.0M", "Updated": "July 23, 2020", "CurrentVersion": "3.0.3", "RequiresAndroid": "4.4 and up", "ContentRating": "Everyone"}
```
