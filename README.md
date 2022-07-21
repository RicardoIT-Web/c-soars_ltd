# C-Soars Ltd.

Click [here](https://c-soars.herokuapp.com/) to view deployed site.  

# Contents

[C-Soars Ltd, The UAV/Drone Property Survey Company](#)

[UX](#ux)
+ [Purpose of the site](#purpose)
+ [Project Scoping & Agile Methodology](#project-scoping-and-agile-methodology)
+ [Wireframes](#wireframes)
+ [User Stories](#user-stories)

[Backend Features](#Backend-Features)
+ [The Service App](#the-service-app)
+ [The Useraccount App](#the-useraccount-app)
+ [The Briefcase app](#the-briefcase-app)
+ [The Contact app](#the-contact-app)
+ [The Newsletter app](#the-newsletter-app)
+ [The Payment app](#the-payment-app)

[Frontend Features](#Frontend-Features)
+ [The Home page](#the-home-page)
+ [The Services Page](#the-services-page)
+ [The My Account page](#the-myaccount-page)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks](#Frameworks-Libraries-and-Programs-Used)

[Testing](#testing)
+ [Lighthouse Testing](#lighthouse-testing)

[Bugs During Development](#bugs-during-development)

[Deployment](#deployment)
+ [Heroku](#Heroku)
+ [Installing Project Requirements](#installing-project-requirements)

[Acknowledgements](#acknowledgements)
+ [Online Resources](#online-resources)
+ [Tutorials](#tutorials)
+ [Assistance](#assistance)


# UX

## Purpose
----
This project was developed to satisfy my fifth and final Milestone Project for the full stack development program with [Code Institute](https://www.codeinstitute.net). 
For this project I have decided to create a fullstack e-commerce application for a Drone Property Surveying company. This application provides customers arriving at the home page with an immediate message stating exactly what the site is all about. 
The Customer can view and access links to social media to find out more about the company and they are also able to view the types of services that the company offers.


## Project Scoping and Agile Methodology

Using the Design Thinking approach to this project, some pre work was carried out to bring the ideas and functionality of the project to "paper". The application features together with the User Stories are included in the excel file included in the documents folder. This file can be access [here](https://github.com/RicardoIT-Web/c-soars_ltd/blob/main/documents/C-Soars%20-%20USER%20STORIES.xlsx).



## Wireframes 
This project is created using Bootstrap and Django frameworks. The built in tools for these frameworks already assist with site responsiveness, as a result, a Desktop approach first was adopted with the aim that responsive adjustments would be minor and is applied at the end of the projects' full creation.

Wireframes are created using [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB). 

The project was developed from initial wireframes and some modifications were made during the development process to ensure better UX.


#### The Home page
Where some sites demonstrate some django functionality on the landing page ie. the home page, for this project, the User is greeted with a main hero image, together with a Navbar and footer to guide the user to other features of the site, which covers some of the User Stories listed below.

![Home page](/documents/homepage_wf.jpg)


#### The Register page
The registration page is designed to be light on the eyes with no other objects distracting the User. 

![Register page](/documents/registrationpage_wf.jpg)


#### The Login page
The Login page is designed to be light on the eyes with no other objects distracting the User. 

![Login page](/documents/loginpage_wf.jpg)


#### The Services page
The services page was designed by using cards to illustrate the different types of services offered. This layout provides a very clear and useful way for the user to select a service. The cards contain a service name and description with images to assist in providing the User with an idea of what the service is for. Visitors to the site can only view name and description of services. In oder to view prices and to book a service Users must register an account and the pricing will automatically appear with in the card content together with a button to book the service.

![Services page](/documents/servicespage_wf.jpg)


#### The Services Details page
Once a User clicks on the button to book a service, they are taken to the services details page, which provides the user with confirmation of the service name, description, and price. Here the User can also adjust the quantity of the service required. As an example if a property manager has 2 properties to survey, they can increase the quantity to two. From this view, they can select to add service to briefcase and be taken to the briefcase page or they can return to the services page to add more types of services. 
An administrator will have the added feature of being able to edit or delete an existing service here.

![Service Details page](/documents/servicesdetailpage_wf.jpg)


#### The Briefcase page
Once a User clicks on the button to book a service, they can choose to return add more services or go to briefcase which provides the user with confirmation of the services selected, gives them the opportunity to increase, decrease or remove each service and also provides them with a grand total of the services requested.
Here the Users are also provided with a button to return to services if they wish to add more, or they can proceed to the payment form.

![Briefcase page](/documents/briefcasepage_wf.jpg)


#### The Payment page
Once a User clicks on the button to proceed to payment, the view will provide the User with a Purchase Order Summary including the total qty and price for the selected service.
Scrolling down they will see the payment form to fill in and be able to introduce a card payment via the card number feature provided by Stripe. The view will provide the user with a reminder of the amount they will be charged, and if User is happy, they can click complete payment. Stripe comes with an excellent service where by developers can simulate payments for testing purposes.

![Stripe Card Payment](/documents/stripe_card_number.jpg)


#### The Payment Successful page
Once a User has completed payment, they will be notified of payment successful with a summary of the purchase and invoicing details and a link taking them back to their account

![Stripe Card Payment](/documents/payment_successful.jpg)

## User Stories

In order to demonstrate an Agile approach to this project, GitHub issues were used as a Kanban board to record the user stories. The user stories were categorized into different User functions between the Admin and the User and each issue would be moved from the "to-do" board to the "done" board as the project progressed.

The Project Kanban board.

![Kanban Board](/documents/kanban_board.jpg)

### User stories

The User requirements were discussed at length with the site owner and User Stories were recorded and saved in the following file: [User Stores](https://github.com/RicardoIT-Web/c-soars_ltd/blob/main/documents/C-Soars%20-%20USER%20STORIES.xlsx)

# Backend Features

This project is built using Django, adopting the MVT (Models-Views-Templates) architecture.

## Services app

### The Services Model

The build of this project started with the services model. This model contains the data required for providing the several types of services the business would like to offer it's customers. This model will include data such as date service was created. The Category allocated to the service. A description of that service. It will also contain the pricing and images for each service.

### The Category Model

The Category model serves to categorize services. The Service model will use data from the category model to include in the Service descriptions

#### The Admin View

Employing all CRUD features - The administrator can Create, Read, Update and Delete any of these services.

## Useraccount app

### The UserAccount Model
This model will contain the personal detailed information of the individual or business registering for a service. Data from this model is used in several areas such as billing details and purchase history.

### The ReviewRating Model
This model hold data that allows Users to submit reviews of their purchased services. 

#### Admin view

Employing all CRUD features - The administrator can Create, Read, Update and Delete any of the ratings and UserAccounts.

## Briefcase app

### No Model Required
This app does not require a model. The data from this app to provide the User with a view of their shopping content stems from the services model. This app does contain a content.py file which includes the clever coding to that works out price times quantity of services and provides a grand total.

## Contact app

### Contact Model
This model contains the details of those wishing to raise an inquiry. The model contains the personal data required to allow the business to follow up on with answers.

## Newsletter app

### Subscriber Model
This model holds the the email data for the subscribers wishing to sign up to receive newsletters.

### newsletter Model
This model allows the administrator to fill in a newsletter subject and content and issue out to all subscribers in the mailing list.

## Newsletter app

### Order Model
The order model retains the data for invoicing the customers.

### OrderItem Model
This model assists in providing the data required post payment. This allows us to provide the User with a summary of the orders previously purchased.


# Frontend Features

### The home Page

The home page provides the visiting Users with a few links to explore.
The top navigation panel contains the main feature links including a search feature allowing visitors to run a search for a service type. They also have a home page link for ease of navigation back to the home page. Clicking on the logo also takes the Users back to the home page. The next link is the Services item which will direct the Users to the All Services page. Then they will see the Account item which they must be registered to access. if Users click on this link they are given the choice to either register or login. And finally we see the Briefcase item which contains the "Shopping Basket" for a user booking a service.

On the footer the users will see a copyright notification, a link to a contact form, link to the company social media accounts and finally a link to the CAA website specifically focused on the Drones Section.

![The Home Page](/documents/homepage.jpg)

### The Services Page

The services page includes all the services that the business will be offering at that time.

![The Services Page](/documents/servicespage.jpg)

### The My Accounts Page
This navigation item works in three ways. Its closed to visitors of the site. For registered users will have access to some features:

![The registered User Options](/documents/normaluserlogedin.jpg)

For administrators of the business, these will have added links to other services such as access to current inquiries, Services Management features, where they hold full CRUD functionality of the services offered and the ability to send out newsletters to subscribers.

![The administrator Options](/documents/logedin_superuser.jpg)

# Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python3.8

### Frameworks, Libraries and Programs Used

* Balsamique was used to create the wireframes as part of the project scoping phase of this project
* MS PowerPoint was used in the project scoping and Agile Methodology preparation phase
* Django v3.2 is used for the architecture of the project
* Postgresql is used for Object Relational database management of this project
* Bootstrap v5 is used for some of the styling on this project
* Fontawesome is used to provide some styling features on this project
* Google fonts is used on this project to provide font types


# Bugs During Development

During the development phase of this project, Heroku made several updates to every app in my account. At some point, my static files stopped connecting to the heroku app meaning I was able to view my project in deployed view but it was missing a lot of CSS styling.

To fix this with the support of the tutors at CI I went through the following steps;

* Access Heroku using the terminal

![Access Heroku - terminal](/documents/dugs_heroku_staticfiles.jpg)

* Enter your email
    * For the password, go into your Heroku profile and copy the API key
    * paste API key in terminal as your password.

![Access Heroku - terminal](/documents/dugs_heroku_staticfiles3.jpg)

* Once login confirmed
    * in the terminal type heroku run python manage.py collectstatic -a diners-3star-restaurant
    * you will be prompted to confirm Y or N

![Access Heroku - terminal](/documents/dugs_heroku_staticfiles5.jpg)

* Once I selected Y the problem was fixed and the static files were now being loaded to Heroku.


# Deployment

### Heroku

* Create an account with Heroku if you don't already have one. [Heroku](https://www.heroku.com/) www.heroku.com

## Installing Project Requirements

### In the terminal

* Install Postgresql: "pip3 install psycopg2-binary". Postgres is a way for the content to link to the database on the backend.
* Install Webserver: "pip3 install gunicorn". This replaces the development server once the app is deployed to Heroku.
* Create a requirements file: "pip3 freeze --local > requirements.txt". This creates a file to let heroku know which packages to install.

### In Heroku

* Open the Resources Tab
* Add Postgres to your app using search bar, select - Heroku Postgres
* Select Hobby Dev
* Open  the settings tab
* Click Reveal Config Vars - Heroku creates a Database_url variable
* Install a database url package: "pip3 install dj-database-url". This package allows us to parse the database url that Heroku created.
* Refreeze the requirements file: "pip3 freeze --local > requirements.txt".
* Get the url of the remote database: "heroku config". This displays the DATABASE URL FROM HEROKU in the terminal - Copy this value

### Django > settings.py

* Comment out the original DATABASE settings.
* Copy and Paste the DATABASE settings: "DATABASES = {'default': dj_database_url.parse('postgres://DATABASE URL FROM HEROKU')}"
* Import dj_database_url: "import dj_database_url". Import at top of settings.py.

### Back to the terminal

* Run migrations: "python3 manage.py migrate".
    * (If you get the error below while following these videos:django.db.utils.OperationalError: FATAL: role "somerandomletters" does not exist)
    * Please run the following command in the terminal to fix it:(unset PGHOSTADDR)

### In Gitpod

* If you are not using the CI full template - Create a new file, .gitignore: django_todo / .gitignore. Lists any files we don’t want to include in the Github Repository.

### Back to the terminal

* Add your files to the local git repo: git add .
* Commit the files.
* Push to remote repo.

### In Gitpod

* Create a new file: Procfile
    * Add gunicorn to Procfile - web: gunicorn django_todo.wsgi:application

### Back to the terminal

* Add the Procfile to the git Repo - git add Procfile
* Git Commit / push

### In heroku / settings tab

* Click Open App

### In the Browser

* Copy the url

### Django > In settings.py

* Paste in the url to ALLOWED_HOSTS value - ALLOWED_HOSTS = ['appname.herokuapp.com'] - Make sure to delete the Https structure at the start of the url & the final ‘/’

### In the Terminal

* Add settings.py file to gitpod repo - git add django_todo/settings.py
* git commit -m “Fixed Allowed_hosts”
* git push

### Django > In settings.py

* Add import os to settings.py
    * import os
* Git add, commit and push your repo to github once you have done this.

### Back to Heroku

* Open your app
* Open the Deploy Tab
* Select a Deployment Method Option - Github - Connect to Github
* Search for the Repo Name
* Click Connect
* Enable Automatic Deploys

### Django > In settings.py

* Get the Secret Key value using an environment variable
    * SECRET_KEY = os.environ.get('SECRET_KEY', '---secretkeyvalue---’)
* Replace the Heroku host value in ALLOWED_HOSTS - ALLOWED_HOSTS = [os.environ.get('appname.herokuapp.com')]
* Replace the Database URL value in DATABASES - 
    * DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }

### Back to Heroku

* Click the Settings tab
* Click Reveal Config Vars
* Add New Variable

* Wait for the Repo to deploy to Heroku
* Refresh the herokuapp in the browser
* The app should now be working


# Acknowledgements

### Online Resources

* CI Boutique Ado Walkthrough Project
* Bootstrap
* Heroku
* Stackoverflow
* Pexels.com
* Fontawesome
* Summernote
* GitHub / Gitpod


### People

* Matt Bodden
* Rohit Sharma
* CI Tutoring Team
