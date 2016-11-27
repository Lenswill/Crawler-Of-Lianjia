# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	info = scrapy.Field()
	local = scrapy.Field()
	house_layout = scrapy.Field()
	house_square = scrapy.Field()
	house_orientation = scrapy.Field()
	district = scrapy.Field()
	floor = scrapy.Field()
	building_year = scrapy.Field()
	price_month = scrapy.Field()
	person_views = scrapy.Field()
	tags = scrapy.Field()
class LianjiaUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	store_url = scrapy.Field()
	page_no = scrapy.Field()
class LianjiaErshouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	house_code = scrapy.Field()
	price_total = scrapy.Field()
	ctime = scrapy.Field()
	title = scrapy.Field()
	frame_hall_num = scrapy.Field()
	tags = scrapy.Field()
	house_area = scrapy.Field()
	community_id = scrapy.Field()
	community_name = scrapy.Field()
	is_two_five = scrapy.Field()
	frame_bedroom_num = scrapy.Field()
