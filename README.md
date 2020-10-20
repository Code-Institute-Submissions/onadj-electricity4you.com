# Code Institute Milestone Project 4 - Full Stack Frameworks with Django

---

Electricity4You

---

- The transition of electric vehicles is no longer unknown. We are witnessing that in the world in the field of the automotive industry, the production of electric vehicles is growing day by day. At the same time, the same new vehicles have a new more modern design. Here we ask ourselves what happens to vintage vehicles? This site is intended for people who have grown up and live today with timeless design, something that new vehicles will never have and that is the soul.

![alt text](https://github.com/onadj/electricity4you.com/blob/master/media/jumbotron.jpg)

---

- Live Website: https://electricity4you.herokuapp.com/

- GitHub Repo: https://github.com/onadj/electricity4you.com

---

# UX

- User stories:

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

- Create a transparent webshop where customers come first, where website visitors can read experiences, questions and reviews from customers and potential customers in a transparent way

---

# Structure

- Minimalistic design with black background, green and white color.

---

# Technologies Used:

- The languages, frameworks, libraries and other tools utilised for building this web-app are:

- Gitpod - Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the web-app.
- GitHub - GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently during the development of the web-app.
- Heroku - This is a cloud based application platform that allows deployment of an application to the web and connection to the database.
- SQlite3 - SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.
- PostgreSQL - PostgreSQL is a powerful, open source object-relational database system.
- Django 3.1.1 - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- AWS S3 - Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance
- Balsamiq - fUsed for design of ireframes.

---

# Front-End Technologies:

- HTML 5
- CSS3
- Bootstrap 4.5.2
- JavaScript
- jQuery
- Google Fonts
- Adobe Photoshop

---

# Back-End Technologies:

- asgiref==3.2.10
- boto3==1.15.18
- botocore==1.18.18
- dj-database-url==0.5.0
- Django==3.1.1
- django-allauth==0.42.0
- django-countries==6.1.3
- django-crispy-forms==1.9.2
- django-storages==1.10.1
- gunicorn==20.0.4
- jmespath==0.10.0
- oauthlib==3.1.0
- Pillow==7.2.0
- psycopg2-binary==2.8.6
- python3-openid==3.2.0
- pytz==2020.1
- requests-oauthlib==1.3.0
- s3transfer==0.3.3
- sqlparse==0.3.1
- stripe==2.51.0

---

# Deployment:

1. The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding.
2. Using this method as a sanity check for the development enabled me to restore the site back to previous stages when it functioned correctly or easily find lost pieces of code.
3. To deploy the project to Github the following steps were taken:
created a master branch in Github repository
Used Local AWS Cloud9 and Gitpod environment used to build the site
4. Committed files to the staging area using bash terminal commands: git status; git add (specify directory); git commit -m"add message"
5. Pushed files to the working environment using git push, which then updates the repository
6. To deploy the project to Heroku the following steps were taken:
7. Created a Heroku account @ https://signup.heroku.com/
8. Create requirements.txt file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type pip3 freeze --local > requirements.txt.
9. To install the Heroku command line on Gitpod, use the following command npm install  heroku
10. Using the New buton, Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod application and Heroku that would allow us to push our changes using Git to update the application at any given time.
11. To login to Heroku from the CLI, use the command heroku login -i
12. To get the application up and running a Procfile is required that istructs Heroku which file is the entry point. Use the following command to create this: echo web: python app.py
13. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands: git add . git commit -m "etc message" git push
14. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
15. To connect an existing repository from Github to Heroku use the following CLI syntax: heroku git:remote -a [followed by name of Heroku app]
16. To push to Heroku Master Branch, then simply use git push heroku master
17. To scale dynos and run the app in Heroku, use the CLI command: heroku ps:scale web=1
18. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku.
 To do this go to Settings tab > Config Variables and input: AWS_ACCESS_KEY_ID; AWS_SECRET_ACCESS_KEY; DATABASE_URL; DISABLE_COLLECTSTATIC; EMAIL_ADDRESS; EMAIL_PASSWORD EMAIL_PASSWORD; SECRET_KEY; STRIPE_PUBLISHABLE; STRIPE_SECRET.
19. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
20. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands mmakemigrations and migrate from the command line.
21. Once the build in Heroku is complete, click the Open app button.
22. Created AWS account for storing static and media files
23. Connected Django with S3
24. Made functionality for sending real mail from gmail
25. Objects can then be added to the new postgres database using the Admin Panel and logging in with your superuser credentials

---

# Features Left to Implement:

- Make members club - started but not finished
- Make functionality that owner of page can change delivery time and put that on separate section on website - started but not finished
- Make functionality that customers who buyed product can send rating of purchased product
- Add more products
- Make own logo of page

---

# Special Thanks:

- I would like to thank the Code Institute for its excellent support over the past year. I especially want to thank all the members of the Code Institute Tutors Support who had great patience and kindness in my every question.










