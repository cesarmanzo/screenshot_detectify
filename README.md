# Detectify Coding Challenge - Screenshot as a Service

A project to capture screenshots of webpages. Demo: [cesarmanzo.com:8000](http://cesarmanzo.com:8000)

Select File or List to input your webpages. If you want your screenshots to be Full Page, click the checkbox. To view all the past screenshots, click on "View Past Screenshots"

## To run the project

### Requirements

- Python3
- Django
- Postgresql
- [Chromedriver](http://chromedriver.chromium.org/downloads)


`echo PATH=.:$PATH`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

I tried to make Docker work, but failed because of the Chromedriver, so I uploaded the project to [cesarmanzo.com:8000](http://cesarmanzo.com:8000) so you can play with it.


## TODO

- Deeply analyze the core function of the application. Maybe Webdriver is not the fastest nor the best, so I would analyze and consider if we can develop our own service exclusively for taking screenshots. This way we can make it faster, lighter, and use much less resources, which translates into lower costs and more profit or lower price for the customers.

- Implement Scrolling. I put two ways of taking a screenshot: Simple (Just a 720p screenshot) and Fullpage (Total height of the page). But I found in the end that Fullpage doesn't always work with all pages, since some of them need to be scrolled to load content. The downside is that this one takes more time and resources.

- Allow users to download all the images as a .ZIP

- Add custom scripts to modify CSS and remove things which we don't want, like certain Pop Ups or defects in some pages.

- Add some way to automatically detect the best setting for each page, be it Fullpage or Scrollable, to optimize all the resources.

- Add tests.

- Let users know which webpage didn't worked.

- Build an amazing frontend

- Make it an API

- Add users and authentication

- Error management



## To serve 1,000,000 daily requests

That means almost 12 requests per second on average. First we would need to completely optimize the application as much as we can. Webdriver may not be the best thing, so we could develop a faster solution or maybe use another plugin. If we try to serve a high number of requests in unoptimized code, bad things will happen. We could say it's "easy" to simply add resources, but that's not the point.

We would need to go asynchronous with something like asyncio/aiohttp. This is the best way to achieve the number of requests that we need. We would need to modify the already optimized code to make it async friendly.

In the current configuration, it's running on a Linux server from Linode also using Nginx and Gunicorn. We could continue to use it this way, but is not the optimal way. In my simple test using headless Chromium I needed around 200MB to run the process and take a Fullpage screenshot. Considering that it took around ~4 seconds each time and doing simple math, that means something like each second at 12 requests is 2.4Gb. But since the process keeps open Chrome for ~4 seconds, that means 9.6 Gb approximately. A 16Gb server would do the job fine. BUT what about the CPU? We would need to analyze if we can let customers wait in a queue or adding more resources. 

The best thing would be to port it to use Google Cloud or Amazon Elastic to self-manage the app and adjust the resources as needed so we don't need to have a dedicated team working on this and also so we know that it'll handle sudden peaks, maybe using Kubernetes to also deploy in real time all the updates. What if suddenly 2,000,000 requests come in one day? With these cloud services we would not have a problem.

The database can handle itself just fine, we would just need to tweak a few configurations and decide where are we going to put it. Currently, it's along the application, but we must move it to something like Amazon RDS or it's own server. If somehow we decide that is better a NoSQL database, Django is NoSQL friendly so we would have no problems setting it up.

To store the images, we could use Amazon S3 to just save the reference in the database and keep it clean and fast. Amazon's storage is cheap and we could even offer to keep the images forever (for paid customers, maybe?).

Security wise, we could use the Cloudfare service to prevent any DDOS attack that may occur. We would also need to properly set all the permissions for users and run security tests and scanners (like Detectify, wink, wink) to ensure that our security is top notch. We would modify the API to ensure that only authenticated users can access it, that all the information is isolated too. Configre the CORS, security headers

Testing. As the application grows, we would need to work using TDD. Testing first, coding after. We would need to add automated testing using some CI tool, like CircleCI or TravisCI to test each pull request and commit from specific branches against our test suite. We can also use Selenium to run the frontend tests.

Sandbox environment. Based on testing, if the testing is right, we can automatically deploy our app to a sandbox environment in which we can continue to run more tests and have our playground.

Set up a SRE team for disaster recovery and best practices in the architecture and infrastructure, high availability, monitoring, etc.
