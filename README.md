# news-scraper
Web-scraper for news articles from BBC News using Scrapy, a small personal project for scraping, please refrain from using this for commercial purposes  
*NOTE: Requires [virtualenv](http://virtualenv.readthedocs.org/en/latest/),
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)*

## Installation

* Fork this repository
* `$ cd Scraper`
* `$ pip install Scrapy`

# Settings.py

* Identify yourself on with USER_AGENT
* Make sure ROBOTSTXT_OBEY is True
* You can modify the DOWNLOAD_DELAY and AUTOTHROTTLE_ENABLED, default should be 1 second per download

# Usage

* `$ cd Scraper`
* `$ scrapy crawl news`
* Or you can save the results into files such as json
* `$ scrapy crawl news -o results.json`

Enjoy and crawl responsibly!
