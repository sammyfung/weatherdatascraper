from scrapy.crawler import CrawlerProcess
from weatherdatascraper.spiders.HKORegionalWeather import HKORegionalWeatherSpider


def test_hko_regional_weather_spider():
    process = CrawlerProcess()
    process.crawl(HKORegionalWeatherSpider)
    process.start()
