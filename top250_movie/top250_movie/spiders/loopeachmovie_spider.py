import scrapy

class loopeachmovieSpider(scrapy.Spider):
	name = 'loopeachmovie'
	start_urls = ['http://www.imdb.com/chart/top?ref_=nv_mv_250_6']
	
	def parse(self,response):
	    # follow links to each movie page from top250 rated movie
	    for href in response.css('td.titleColumn').css('a::attr(href)').extract():
		yield scrapy.Request(response.urljoin(href),
				     callback = self.parse_movie)


	def parse_movie(self,response):
	    
	    yield {
		'name' : response.css('div.title_wrapper').css('h1::text').extract()[0],
		'year' : response.css('div.title_wrapper').css('span a::text').extract(),
		'length' :response.css('div.title_wrapper').css('div.subtext').css('time::text').extract(),
		'genre': response.css('div.title_wrapper').css('div.subtext').css('span::text').extract(),
        	'writer':response.css('div.plot_summary').css('div.credit_summary_item').css('a span::text').extract(),
        	'Description':response.css('div.plot_summary').css('div.summary_text').css('div::text').extract()
		}
