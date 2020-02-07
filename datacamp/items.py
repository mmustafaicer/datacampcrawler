# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DataCampItem(scrapy.Item):
    # define the fields for your item here like:
    course_name = scrapy.Field()
    course_description = scrapy.Field()
    time_hours = scrapy.Field()
    videos = scrapy.Field()
    exercises = scrapy.Field()
    participants = scrapy.Field()
    xp_points = scrapy.Field()
    url = scrapy.Field()
