[![ci](https://github.com/opsoc/weatherdatascraper/actions/workflows/ci-weather-data-scraper.yml/badge.svg)](https://github.com/opsoc/weatherdatascraper/actions/workflows/ci-weather-data-scraper.yml)
[![codecov](https://codecov.io/gh/opsoc/weatherdatascraper/branch/main/graph/badge.svg?token=6RKB2AWHIG)](https://codecov.io/gh/opsoc/weatherdatascraper)

# Global Weather Data Scraper

Weather Data Scraper is an open source project aimed to collect global weather data.

## Quickstart

```
$ pip install -r requirements.txt
$ scrapy crawl CurrentWeatherHKO
```

## An Example of Current Weather Data in JSON format

```
{
    "scraping_time": "2023-04-25T15:06:13.967261+00:00", 
    "local_time": "2023-04-25T22:50:00+08:00",
    "utc_time": "2023-04-25T14:50:00+00:00",
    "city": "Hong Kong Observatory", 
    "source": "HKO", 
    "country": "HK", 
    "state": "HK", 
    "timezone": "HKT", 
    "temp_unit": "C", 
    "wind_speed_unit": "kmh", 
    "latitude": 22.30195171, 
    "longitude": 114.17427393, 
    "sl_height": 32, 
    "temperature": 20.9, 
    "humidity": 86, 
    "temp_daily_max": 23.7, 
    "temp_daily_min": 20.9, 
    "sl_pressure": 1015.1
},
```

## Contribution

You can read CONTRIBUTING.md to see how you can make contribution, and you can sponsor this project on GitHub.