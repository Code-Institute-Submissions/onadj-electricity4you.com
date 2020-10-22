# Code Institute Milestone Project 4 - Full Stack Frameworks with Django

---

## Electricity4You

---

The transition of electric vehicles is no longer unknown. We are witnessing that in the world in the field of the automotive industry, the production of electric vehicles is growing day by day. At the same time, the same new vehicles have a new more modern design. Here we ask ourselves what happens to vintage vehicles? This site is intended for people who have grown up and live today with timeless design, something that new vehicles will never have and that is the soul.
This webshop is planned to be released into live production by the end of 2020 by when the new company will be open.
Images of products and prices currently on the page in live production will not be present, they are here only for the presentation of the website.

![alt text](https://github.com/onadj/electricity4you.com/blob/master/media/jumbotron.jpg)

---

 Live Website: https://electricity4you.herokuapp.com/

 GitHub Repo: https://github.com/onadj/electricity4you.com

---

# UX

 User stories:

- I want to find out web page with electric vintage chooper and bicycle

- I want to buy vintage electric chooper or bicycle, but from website which has transparent communication in the form of a Blog

- I want to see on the page not only products with prices, I want to see live Blog with customers Posts and possibility to make my own Posts, I want to see how many likes has a specific Post, and I want too see Posts only from registered visitors or customers with date of Post made

- I want to edit or delete my Post or like someone else’s post

- I want to find on page latest News from site owner about upcoming vehicles and promotions

---

# Owner site goal

- Build a webshop that sells vintage electric choppers and bicycles

- Site owner's goal: Earn money on each product purchased from page

- Create a web application that allows users to have live Blog and live News about upcoming vehicles and promotions

- Create a transparent webshop where customers come first, where website visitors can read experiences, questions and reviews from customers and potential customers in a transparent way in Blog section

- I want to track Blog visitors (potentional new customers), use it as a sales improvement

---

# Structure

- Minimalistic design with black background, green and white color.

---

# Mockup

 ### Home Page:

 ![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/homepage.png)

 ### All Products:

 ![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/allproducts.png)

### Choppers:

![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/choppers.png)

### Bicycles:

![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/bicycles.png)

### News:

![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/news.png)

### Blog:

![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/blog.png)

---

# Technologies Used:

- HTML5
- CSS3
- Bootstrap 4.5.2
- JavaScript
- jQuery
- Google Fonts
- Adobe Photoshop
- Gitpod 
- GitHub 
- Heroku 
- SQlite3 
- PostgreSQL 
- Django
- AWS S3 - Amazon Simple Storage Service (Amazon S3)
- Python
- Stripe
- FontAwesome
- Boto3

---

# Deployment:

- project setup, made new repo in GitHub with name electricity4you
- pip3 install django
- django-admin startproject electricity4you
- touch .gitignore
- in .gitignore file added *.sqlite3 *.pyc and --pycache
- python3 manage.py migrate
- python3 manage.py createsuperuser
- git add ; . git commit -m "initial commit" ; git push
- pip3 install django-allauth
- in setting of app added django-allauth documentation
- python3 manage.py migrate
- python3 manage.py runserver  ; link/admin got access to django administration
- verify superuser
- pip3 freeze > requirements.txt
- mkdir templates/allauth
- cp -r ../.p-modules/lib/python3.8/site-packages/allauth/templates/*
- added bootstrap documentation / startertemplate
- pyhon3 manage.py startapp home
- mkdir -p home/templates/home
-  in home folder made index.html
- made home page and top header
- mkdir templates/includes , in this folder made main-nav.html and mobile-top-header.html
- python3 manage.py startapp products
- mkdir products/fixtures added two json files in fixtures folder
- python3 manage.py makemigrations
- python3 manage.py migrate
- mkdir -p products/templates/products here added needed html files
- connected products html files with main navbar
- in mobile-top-header.html/main-nav.html added needed code to make search functionality, sorting by price, category, rating and added javascript for for sorting
  products from A-Z and low to high price
- python3 manage.py startapp bag
- added templates folder with html files
- connected with mobile-top-header.html
- made new file in bag folder context.py for bag context and delivery logic
- in products folder added functionality for select size of clothes
- added jquery code uncomppressed minified for removing products from bag
- added 4 toast html files(success, error, info and warning)
- python3 manage.py startapp checkout and as allways added code to models.py
- python3 manage.py makemigrations
- python3 manage.py migrate
- added admin, signals and forms - built in feature of django
- in checkout folder made own static file
- python3 install pillow
- python install django-crispy-forms
- made account for stripe
- added code form stripe documentation in base.html
- in checkout views.py added stripe-public-key
- in checkout folder made new folder JS and made file stripe-elements.js in this file added code from stripe documentation
- added css code from stripe documentation in checkout.css
- pip3 install stripe
- in settings added STRIPE CURRENCY
- in terminal => export STRIPE_SECRET_KEY and STRIPE_PUBLIC_KEY, in gitpod in enviroment variables added STRIPE_SECRET_KEY and STRIPE_PUBLIC_KEY
  so no need to repeat the entry in terminal
- from stripe documentation took client,js code and added in stripe_elements.js
- in checkout templates folderu all html files customized to work properly
- in checkbox folder made webhook_handler.py
- in checkbox folder made webhook.py here added code from stripe documentation
- in settings.py off our app added STRIPE_WH...
- tested on the stripe website stripe/developers/webhooks/added endpoint in our link at the end added /checkout/wh clicked receive all events test ok
- took signing secret key from stripe website and added in terminal as export STRIPE_WH_SECRET=""
- again testing on stripe website with send test webhook 
- part with stripe is finished - completed webhook handler added checkout form, data caching in payment intent
- pip3 install django-countries
- pip3 freeze > requirements.txt
- made / templates / allauth html files to work properly
- testing confirmation mail for login, for now confirmation mail is in terminal
- updated profile and product form to work required(added product admin functionality for adding, editing, deleting products)
- added widget django forms for fixing the image field - in product folder added widget.py and in templates made custom_clearable_file_input.html
- made new acc on heroku
- on heroku new app/ name of app: electricity4you/resources/add-ons/chosing heroku postgres/hobby dev-free
- pip3 install dj-database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.tx
- in settings.py added DATABASES: ...
- heroku/settings/config vars added postgrees://
- python3 manage.py migrate
- python3 manage.py loaddata categories
- python3 manage.py loaddata products
- pip3 install gunicorn
- pip3 freeze > requirements.txt
- made Procfile
- in heroku config set DISABLE_COLLECTSTATIC = 1 --app electricity4you
- conected heroku with github repo
- added django secret key generator in heroku config vars 
- created aws account for static files and media
- aws.amazon.com
- personal type/S3/create bucket
- name of bucket is name electricity4you
- block all public access/bucket properties/static webhosting/use this bucket to host/index and error.html
- permission/cors configuration
- bucket policy/policy generator/S3 Bucket policy/principal added */ and copied ARN
- added code in Bucket policy tab
- on the end of my app added /*
- access control list/public access/ chose everyone and clicked on ACCESS CONTROL
- created AWS GROUPS, PoliciEs AND users :
- Services took IAM, took Groups
- made group name: manage-electricity4you/next/next/create group
- took policies/JSON tab/import managed policy
- AmazonS3FullAcces/import
- AmazonS3, choose my bucket/permission.from bucket policy copied ARN in create policy/JSON
- review policy/ groups/permission/attach policy
- add user/ added onagy-electricity4you-staticfiles-user
- access type choose pragrammatic access/permission/ choose only manage-electricity4you
- Tags/next/create user
- download .csv/Access key ID Secret acces key
- pip3 install boto3
- pip3 install django-storages
- pip3 freeze > requirements.txt
- in settings.py added USE_AWS
- git push heroku master on Amazon S3 created static folder
- settings.py added #cache control
- in AWS S3 created folder media/uploaded images from my pc
- manage public permission GRANT PUBLIC READ ACCESS TO THIS OBJECT and upload
- copied token from stripe and added endpoint; https://electricity4you.herokuapp.com/checkout/wh
- sending mail with django:
- used gmail/settings/accounts and import/other settings/security/2 step verification/get started/app passwords/mail/django/generate
- 16 key password added in heroku config vars
- on the end fixed css, font and other
- for the requirements of Code Institute made two more models
- models is in news app and blog app
- for every installed app, name of app is added in settings, new url, path, templates, views and models are made
- final look heroku Config Vars :
![alt text](https://github.com/onadj/electricity4you.com/blob/master/mockups/herokuconfigvars.png)
 
---

# Testing:

- https://validator.w3.org/ (spotted few main errors and fixed)
- http://jigsaw.w3.org/css-validator/ (spotted few main errors and fixed, left warning about bootstrap)
- I was testing the site with Chrome developer tools on my desktop PC, and with Samsung Galaxy A50, Samsung Galaxy Tab A6, iPhone 7 and with Firefox to make sure compatibility and responsiveness are working
- When testing this app, to make a payment, the following details should be used:
Card number: 4242 4242 4242 4242, CVC: any three numbers, Date: any future date, ZIP Code: any five numbers.

---

# Features Left to Implement:

- Make members club - started but not finished
- Make functionality that owner of page can change delivery time/shipping and put that on separate section on website - started but not finished
- Make functionality that customers who buyed product can send rating of purchased product
- Make Blog only for owners of site, for faster communication in company,started as newblog but didn't finished
- Add more products
- Make own logo of page

---

# Media, Credit and Information

- All images for this project were obtained from Google Images
- https://electrek.co/2019/06/24/regent-no-1-retro-electric-motorcycle/

---

# Code 

- https://stackoverflow.com/

- https://codepen.io/

- https://www.w3schools.com/

- https://www.youtube.com/

- https://docs.djangoproject.com/en/3.1/

- https://developedbyed.com/

- https://codemy.com/

- https://www.udemy.com/

- https://www.freecodecamp.org/

- Code Institute Slack

- Boutique ado Mini project from Code Institute


--- 

# Special Thanks:

- I would like to thank the Code Institute for its excellent support over the past year. I especially want to thank all the members of the Code Institute Tutors Support who had great patience,helpfulness and kindness in my every question.










