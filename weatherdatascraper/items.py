import scrapy


class CurrentWeatherItem(scrapy.Item):
    # Current Weather Data
    source = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    zipcode = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    sl_height = scrapy.Field()
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
    sl_pressure = scrapy.Field()
    humidity = scrapy.Field()
    hum_daily_max = scrapy.Field()
    hum_daily_min = scrapy.Field()
    snow_depth = scrapy.Field()
    precipitation = scrapy.Field()


