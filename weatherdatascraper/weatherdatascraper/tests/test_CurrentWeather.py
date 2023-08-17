from scrapy.crawler import CrawlerProcess
from weatherdatascraper.spiders.CurrentWeatherHKO import CurrentWeatherHKOSpider


def test_current_weather_hko():
    process = CrawlerProcess()
    process.crawl(CurrentWeatherHKOSpider)
    process.start()
