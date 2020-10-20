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

### Biciycles:

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

1. The web-site is designed in the Gitpod environment and regularly committed to GitHub after each crucial piece of coding.
2. Using this method as a  check for the development enabled me to restore the site back to previous stages when it functioned correctly or easily find lost pieces of code.
3. To deploy the project to Github the following steps were taken:
created a master branch in Github repository
Used Gitpod environment to build the site
4. Committed files to the staging area using bash terminal commands: git add . ;  git commit -m "add message" and git push
5. Pushed files to the working environment using git push, which then updates the repository
6. To deploy the project to Heroku the following steps were taken:
7. Created a Heroku account
8. Create requirements.txt file in Gitpod workspace for Heroku to understand installation files to run app. From CLI type type pip3 freeze --local > requirements.txt.
9. To install the Heroku command line on Gitpod, use the following command npm install  heroku
10. Create a new app with apropriate title and server in Heroku. This creates a connection between the Gitpod/GitHub repo application and Heroku that would allow us to push our changes using Git to update the application at any given time.
11. To login to Heroku from the CLI, use the command heroku login -i
12. To get the application up and running a Procfile is required to give instruction Heroku which file is the entry point. Use the following command to create this: echo web: python app.py
13. Code that is prepared to be pushed from Github to Heroku can be executed following the CLI commands: git add . git commit -m "etc message" git push, somethimes I need to login in  heroku with heroku login -i and push to heroku with  git push heroku master
14. Now that the relevant code is pushed to Github, it can also be pushed to Heroku from the chosen branch (e.g. Master)
15. To push to Heroku Master Branch, then simply use git push heroku master
16. To scale dynos and run the app in Heroku, use the CLI command: heroku ps:scale web=1
17. In order for the server instance on Heroku to know how to run our application, we need to specify a few Config Vars in Heroku.
 To do this go to Settings tab > Config Variables and input: AWS_ACCESS_KEY_ID; AWS_SECRET_ACCESS_KEY; DATABASE_URL; DISABLE_COLLECTSTATIC; EMAIL_ADDRESS; EMAIL_PASSWORD EMAIL_PASSWORD; SECRET_KEY; STRIPE_PUBLISHABLE; STRIPE_SECRET.
18. The following syntax will need to be added to your settings.py file to access the SECRET KEY for the new database URL DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
19. The Database can then be migrated to the Heroku Postgres (postgresql) database using the the commands mmakemigrations and migrate from the command line.
20. Once the build in Heroku is complete, click the Open app button.
21. Created AWS account for storing static and media files
22. Connected Django with S3
23. Made functionality for sending real mail from gmail
24. Objects can then be added to the new database using the Admin Panel  (Product and Site Management) and logging in with your superuser credentials

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
- Add more products
- Make own logo of page

---

# Media and Information

- All images for this project were obtained from Google Images

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


--- 

# Special Thanks:

- I would like to thank the Code Institute for its excellent support over the past year. I especially want to thank all the members of the Code Institute Tutors Support who had great patience,helpfulness and kindness in my every question.










