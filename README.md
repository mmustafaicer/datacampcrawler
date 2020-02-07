# DataCamp Crawler

## Problem Statement.

We have a starting [webpage](https://www.datacamp.com/courses/tech:python). There are a list of courses related to Python programming language. 

![start_url](https://user-images.githubusercontent.com/46098464/74062126-2fe91700-49b3-11ea-93c4-3be35245d061.png)

Each links redirects user to that specific course page. That course page some information such as:

- course name
- course description
- number of exercises
- participants
- time hours
- url
- videos
- xp points

![example](https://user-images.githubusercontent.com/46098464/74062143-36778e80-49b3-11ea-9960-82b3b3ddd82a.png)

We need to collect these information for each course. The output should be like this.

------

![excel](https://user-images.githubusercontent.com/46098464/74062148-38415200-49b3-11ea-9c46-10133be16dfe.png)

# Run

Make sure you have `scrapy` installed in your environment. Navigate to desired folder. And create a Scrapy project from console:

```shell
scrapy startproject datacamp
````
Copy this project files into that datacamp folder. It should be `..../datacamp/datacamp.../`

Open console, change directory to that inside datacamp folder. And run the following command:

```shell
scrapy crawl my_scraper -o datacamp.csv
```
