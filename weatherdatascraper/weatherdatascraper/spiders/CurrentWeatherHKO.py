# -*- coding: utf-8 -*-
# Web Scraping for Hong Kong Observatory 10-minute update regional weather data.
import scrapy
from scrapy.selector import Selector
import logging
from weatherdatascraper.items import CurrentWeatherItem
import re, pytz
from datetime import datetime


class CurrentWeatherHKOSpider(scrapy.Spider):
    name = "CurrentWeatherHKO"
    allowed_domains = ["weather.gov.hk"]
    start_urls = ["https://www.weather.gov.hk/wxinfo/ts/text_readings_c.htm"]

    SOURCE = "HKO"
    STATE = "HK"
    COUNTRY = "HK"
    TIMEZONE = "HKT"
    TEMPERATURE_UNIT = "C"
    WIND_SPEED_UNIT = "kmh"
    ZIP_CODE = ""

    # id, e_name, c_name, lat, lon, height
    stations = [
        ('hko', 'Hong Kong Observatory', '天文台', 22.30195171, 114.17427393, 32),
        ('kp', "King's Park", '京士柏', 22.31182454, 114.17289356, 65),
        ('hks', 'Wong Chuk Hang', '黃竹坑', 22.24777778, 114.17361111, 5),
        ('tkl', 'Ta Kwu Ling', '打鼓嶺', 22.52857256, 114.15658128, 15),
        ('lfs', 'Lau Fau Shan', '流浮山', 22.46892918, 113.98347614, 31),
        ('tpo', 'Tai Po', '大埔', 22.44605045, 114.17892305, 15),
        ('sha', 'Sha Tin', '沙田', 22.40251439, 114.20993048, 6),
        ('tun', 'Tuen Mun', '屯門', 22.3858791, 113.9641559, 28),
        ('jkb', 'Tseung Kwan O', '將軍澳', 22.31567794, 114.25563288, 38),
        ('skg', 'Sai Kung', '西貢', 22.37555556, 114.27444444, 4),
        ('cch', 'Cheung Chau', '長洲', 22.20123694, 114.02667351, 72),
        ('hka', 'Chek Lap Kok', '赤鱲角', 22.30939677, 113.92178895, 6),
        ('ty1', 'Tsing Yi', '青衣', 22.34414702, 114.109917, 8),
        ('sek', 'Shek Kong', '石崗', 22.43626486, 114.08469087, 16),
        ('twn', 'Tsuen Wan Ho Koon', '荃灣可觀', 22.38361111, 114.10777778, 142),
        ('tw', 'Tsuen Wan Shing Mun Valley', '荃灣城門谷', 22.37564208, 114.12665887, 35),
        ('hkp', 'Hong Kong Park', '香港公園', 22.2783144, 114.16201691, 26),
        ('skw', 'Shau Kei Wan', '筲箕灣', 22.28166667, 114.23611111, 53),
        ('klt', 'Kowloon City', '九龍城', 22.33512216, 114.18477853, 92),
        ('hpv', 'Happy Valley', '跑馬地', 22.27056652, 114.18347178, 5),
        ('wts', 'Wong Tai Sin', '黃大仙', 22.33938493, 114.20531575, 21),
        ('sty', 'Stanley', '赤柱', 22.21408207, 114.21852967, 31),
        ('ktg', 'Kwun Tong', '觀塘', 22.31861111, 114.22472222, 90),
        ('ssp', 'Sham Shui Po', '深水埗', 22.33583323, 114.13682629, 11),
        ('se1', 'Kai Tak Runway Park', '啟德跑道公園', 22.30492773, 114.21696254, 4),
        ('ksc', 'Kau Sai Chau', '滘西洲', 22.36940925, 114.31315951, 39),
        ('ngp', 'Ngong Ping', '昂坪', 22.25861111, 113.91277778, 593),
        ('pen', 'Peng Chau', '坪洲', 22.29117377, 114.04354504, 34),
        ('sc', 'Sha Chau', '沙洲', 22.34583333, 113.89111111, 31),
        ('sf', 'Star Ferry', '天星碼頭', 22.29301322, 114.16846444, 18),
        ('plc', 'Tai Mei Tuk', '大美督', 22.47523256, 114.23753518, 51),
        ('tpk', 'Tai Po Kau', '大埔滘', 22.44259977, 114.18402151, 11),
        ('tap', 'Tap Mun', '塔門', 22.47138889, 114.36055556, 15),
        ('tc', "Tate's Cairn", '大老山', 22.35797141, 114.21773918, 572),
        ('wgl', 'Waglan Island', '橫瀾島', 22.18222222, 114.30333333, 56),
        ('wlp', 'Wetland Park', '濕地公園', 22.46687063, 114.00866954, 4),
        ('ssh', 'Sheung Shui', '上水', 22.50191353, 114.11109377, 10),
        ('tyw', 'Pak Tam Chung', '北潭涌', 22.40280566, 114.32298884, 5),
        ('tms', 'Tai Mo Shan', '大帽山', 22.41053038, 114.12443485, 955),
        ('vp1', 'The Peak', '山頂', 22.26416667, 114.155, 406),
        ('ccb', 'Cheung Chau Beach', '長洲泳灘', 22.21091857, 114.0292504, 27),
        ('gi', 'Green Island', '青洲', 22.28502289, 114.11285643, 88),
        ('se', 'Kai Tak', '啟德', 22.3097122, 114.21331876, 3),
        ('tls', 'Tai Lung', '大隴', 22.48464102, 114.11720964, 21),
        ('cwb', 'Clear Water Bay', '清水灣', 22.26290979, 114.29918595, 66),
        ('cp1', 'Central Pier', '中環碼頭', 22.28888132, 114.15584695, 19),
        ('hss', 'Hong Kong Sea School', '香港航海學校', 22.2183973, 114.2141539, 22),
        ('lam', 'Lamma Island', '南丫島', 22.22623469, 114.10861764, 7),
        ('ylp', 'Yuen Long Park', '元朗公園', 22.44080875, 114.01821861, 8),
        ('br2', 'Beas River', '雙魚河', 22.49333333, 114.105, 11)
    ]
    # Lat, Lon, Height come from https://geodata.gov.hk/gs/view-dataset?uuid=8806a56e-6f68-4f3e-8320-095a23516320&sidx=0

    def parse(self, response):
        stations = {}
        station_items = []
        sel = Selector(response)
        report = sel.xpath('//pre[@id="ming"]/text()')

        # Getting HKO report time.
        report_time = self.get_report_time(report[0].extract())

        # Process the report line by line.
        for i in re.split('\n',report[0].extract()):
            last_station = ''
            # Getting basic information of weather station
            for id, e_name, c_name, lat, lon, height in self.stations:
                if re.sub(' ','',i[:6]) == c_name:
                    last_station = id
                    try:
                        station = stations[last_station]
                        station['source'] = self.SOURCE
                        station['country'] = self.COUNTRY
                        station['timezone'] = self.TIMEZONE
                    except KeyError:
                        stations[last_station] = {}
                        stations[last_station]['scraping_time'] = datetime.now(pytz.utc).isoformat()
                        stations[last_station]['local_time'] = report_time
                        stations[last_station]['utc_time'] = datetime.fromisoformat(report_time).astimezone(pytz.utc).isoformat()
                        stations[last_station]['city'] = e_name
                    stations[last_station]['source'] = self.SOURCE
                    stations[last_station]['country'] = self.COUNTRY
                    stations[last_station]['state'] = self.STATE
                    stations[last_station]['timezone'] = self.TIMEZONE
                    stations[last_station]['temp_unit'] = self.TEMPERATURE_UNIT
                    stations[last_station]['wind_speed_unit'] = self.WIND_SPEED_UNIT
                    stations[last_station]['latitude'] = lat
                    stations[last_station]['longitude'] = lon
                    stations[last_station]['sl_height'] = height

            data_line = re.sub('^\s', '', i[6:])
            data_line = re.sub('\*', ' ', data_line)
            data = re.split('\s+', data_line)
            if len(data) > 5:
                for j in range(0,len(data)):
                    if data[j].isdigit():
                        stations[last_station]['humidity'] = int(data[j])
                    elif last_station != '':
                        try:
                            if j == 1:
                                stations[last_station]['temperature'] = float(data[j])
                            elif j == 3:
                                stations[last_station]['temp_daily_max'] = float(data[j])
                            elif j == 5:
                                stations[last_station]['temp_daily_min'] = float(data[j])
                        except ValueError:
                            if j == 1:
                                stations[last_station]['temperature'] = 'N/A'
                            elif j == 3:
                                stations[last_station]['temp_daily_max'] = 'N/A'
                            elif j == 5:
                                stations[last_station]['temp_daily_min'] = 'N/A'
                        except KeyError:
                            logging.warning("KeyError on Regional Weather Information: station %s, field %s"%(last_station,j))
            elif len(data) == 5 and last_station != '':
                # Getting wind direction, wind speed, maximum gust.
                data[1] = re.sub(u'東南','SE', data[1])
                data[1] = re.sub(u'東北','NE', data[1])
                data[1] = re.sub(u'西南','SW', data[1])
                data[1] = re.sub(u'西北','NW', data[1])
                data[1] = re.sub(u'東','E', data[1])
                data[1] = re.sub(u'南','S', data[1])
                data[1] = re.sub(u'西','W', data[1])
                data[1] = re.sub(u'北','N', data[1])
                # Handling variable wind direction.
                if not(re.search(u'^[A-Z].*',data[1])):
                    data[1] = 'Variable'
                stations[last_station]['wind_direction'] = data[1]
                if data[1] != 'Variable':
                    try:
                        stations[last_station]['wind_speed'] = int(data[2])
                    except ValueError:
                        stations[last_station]['wind_speed'] = data[2]
                    try:
                        stations[last_station]['max_gust'] = int(data[3])
                    except ValueError:
                        stations[last_station]['max_gust'] = data[3]
                else:
                    stations[last_station]['wind_speed'] = 0
                    stations[last_station]['max_gust'] = 0
            elif len(data) == 3 and last_station != '':
                try:
                    stations[last_station]['sl_pressure'] = float(data[1])
                except ValueError:
                    stations[last_station]['sl_pressure'] = data[1]
            elif len(data) == 2 and last_station == 'wlp':
                # Special handling to Wetland Park sea-level pressure.
                stations[last_station]['sl_pressure'] = data[0]


        for key in stations:
            station_item = CurrentWeatherItem()
            for key2 in stations[key]:
                station_item[key2] = stations[key][key2]
            station_items.append(station_item)

        return station_items

    def get_report_time(self, report):
        report = report.split('\n')
        for i in report:
            if re.search('錄得的天氣資料', i):
                t = re.sub('錄得的天氣資料.*','', i)
                t = re.sub(' ','0', t)
                t = re.sub('[年月日時分]',' ', t)
                t = datetime.strptime(t,'%Y %m %d %H %M ').replace(tzinfo = pytz.timezone('Etc/GMT-8')).isoformat()
                return t


