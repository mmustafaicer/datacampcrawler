import scrapy
from datacamp.items import DataCampItem

class DataCamp(scrapy.Spider):
    name = "my_scraper"

    # define the start url
    start_urls = ["https://datacamp.com/courses/tech:python"]

    # define parser for each course page to extract info
    def parse(self, response):
        for href in response.xpath("//div[contains(@class, 'js-course-bookmarking course-block')]/a[contains(@class, 'course-block__link ds-snowplow-link-course-block')]//@href"):
            # add the scheme, eg http://
            url = "https://datacamp.com" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        
    def parse_dir_contents(self, response):

        item = DataCampItem()

        # getting the course name
        item['course_name'] = response.xpath("//h1[contains(@class, 'header-hero__title')]/text()").extract()

        # getting the course description
        item['course_description'] = response.xpath("//p[contains(@class, 'home-header__description dc-u-color-white')]/descendant::text()").extract()

        # time
        item['time_hours'] = "".join(response.xpath("//ul[contains(@class, 'header-hero__stats')]//li[contains(@class, 'header-hero__stat header-hero__stat--hours')]/descendant::text()").extract()).split()[0]

        # number of videos
        item['videos'] = "".join(response.xpath("//ul[contains(@class, 'header-hero__stats')]//li[contains(@class, 'header-hero__stat header-hero__stat--videos')]/descendant::text()").extract()).split()[0]

        # number of exercises
        item['exercises'] = "".join(response.xpath("//ul[contains(@class, 'header-hero__stats')]//li[contains(@class, 'header-hero__stat header-hero__stat--exercises')]/descendant::text()").extract()).split()[0]

        # number of participants
        item['participants'] = "".join(response.xpath("//ul[contains(@class, 'header-hero__stats')]//li[contains(@class, 'header-hero__stat header-hero__stat--participants')]/descendant::text()").extract()).split()[0]

        # number of XP points
        item['xp_points'] = "".join(response.xpath("//ul[contains(@class, 'header-hero__stats')]//li[contains(@class, 'header-hero__stat header-hero__stat--xp')]/descendant::text()").extract()).split()[0]

        # url
        item['url'] = response.xpath("//link[@rel='canonical']/@href").extract() 

        yield item