[![ci](https://github.com/sammyfung/weatherdatascraper/actions/workflows/weatherdatascraper.yml/badge.svg)](https://github.com/sammyfung/weatherdatascraper/actions/workflows/weatherdatascraper.yml)
[![codecov](https://codecov.io/gh/sammyfung/weatherdatascraper/graph/badge.svg?token=FTBHLM0LEZ)](https://codecov.io/gh/sammyfung/weatherdatascraper)

# Weather Data Scraper

Weather Data Scraper is an open source project aimed to collect global weather data.

## Quickstart

```
$ pip install -r requirements.txt
$ cd weatherdatascraper
$ scrapy crawl HKORegionalWeather
```

## An Example of Current Weather Data in JSON format

```
{
 'city': 'Wong Chuk Hang',
 'country': 'HK',
 'humidity': 68,
 'latitude': 22.24777778,
 'local_time': '2024-05-29T17:00:00+08:00',
 'longitude': 114.17361111,
 'max_gust': 31,
 'provider': 'HKO',
 'scraping_time': '2024-05-29T09:12:13.375557+00:00',
 'sea_level_height': 5,
 'state': 'HK',
 'temp_daily_max': 27.4,
 'temp_daily_min': 24.7,
 'temp_unit': 'C',
 'temperature': 26.8,
 'timezone': 'GMT+8',
 'utc_time': '2024-05-29T09:00:00+00:00',
 'wind_direction': 'E',
 'wind_speed': 16,
 'wind_speed_unit': 'kmh'
}
```

## Contribution

You can read CONTRIBUTING.md to see how you can make contribution, and you can sponsor this project on GitHub.
