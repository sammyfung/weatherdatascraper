import scrapy


class GeneralWeatherItem(scrapy.Item):
    # General Weather Data
    type = scrapy.Field()
    provider = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    zipcode = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    sea_level_height = scrapy.Field()
    timezone = scrapy.Field()
    scraping_time = scrapy.Field()
    local_time = scrapy.Field()
    utc_time = scrapy.Field()
    temperature = scrapy.Field()
    temp_unit = scrapy.Field()
    temp_daily_max = scrapy.Field()
    temp_daily_min = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_speed = scrapy.Field()
    wind_speed_unit = scrapy.Field()
    max_gust = scrapy.Field()
    sea_level_pressure = scrapy.Field()
    humidity = scrapy.Field()
    humidity_daily_max = scrapy.Field()
    humidity_daily_min = scrapy.Field()
    snow_depth = scrapy.Field()
    precipitation = scrapy.Field()


