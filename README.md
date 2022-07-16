# C-Soars Ltd.

Click [here]() to view deployed site.  

# Contents

[Diners 3Star Restaurant](#diners-3star-restaurant)

[UX](#ux)
+ [Purpose of the site](#purpose)
+ [Project Scoping & Agile Methodology](#project-scoping-and-agile-methodology)
+ [Wireframes](#wireframes)
+ [User Stories](#user-stories)

[Backend Features](#Backend-Features)
+ [The Table Model](#the-table-model)
+ [The Booking Model](#the-booking-model)
+ [The Contact Model](#the-contact-model)

[Frontend Features](#Frontend-Features)
+ [The Menu page](#the-home-page)
+ [The Contacts Page](#the-contacts-page)
+ [The Booking page](#the-booking-page)
+ [The Social Media accounts](#the-social-media-accounts)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks](#Frameworks-Libraries-and-Programs-Used)

[Code Validation](#code-validation)
+ [HTML Validation](#html-validation)
+ [CSS Validation](#css-validation)
+ [Python Validation](#python-validation)

[Testing](#testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [Manual Testing](#manual-testing)

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
This project was developed to satisfy my fourth Milestone Project for the full stack development program with [Code Institute](https://www.codeinstitute.net). For this project I have decided to create an imaginary beautiful 3star Michelin restaurant serving customers staying at the nearby beach Hotel. The restaurant allows customers to book tables with the added feature of allowing customers to select between three locations within the restaurant, these being outside, window seat or in the main hall areas. This current release will be restricted to a maximum of 2 tables outside sitting 2 people on each table. 2 window tables each sitting a maximum of 4 people on each table and 2 hall tables each sitting a maximum of 6 people on each table.

The restaurant prides itself in providing their customers with a more inclusive experience by allowing customers to visit the kitchen area, speak to the chef and their team and be able to have a little taste of any Menu meal before ordering.


## Project Scoping and Agile Methodology

Using the Design Thinking approach to this project, some prework was carried out to bring the ideas and functionality of the project to "paper". Powerpoint slides are used to illustrate this process beginning with a problem statement, the slides also include Entity Relationship diagrams and map os how all epics link to their respective User Stories. Each User Story will include steps that aim to fulfill the CRUD (create-read-update-delete) functionalities expected with any database application.

The raw data can be downloaded from [here](https://github.com/RicardoIT-Web/diners-3star-restaurant/blob/main/media/agile_methodology/Diners-3Star-Restaurant_project_Scoping.pptx).


## Wireframes 
This project is created using Bootstrap and Django frameworks. The built in tools for these frameworks already assist with site responsiveness, as a result, a Desktop approach first was adopted with the aim that responsive adjustments would be minor and is applied at the end of the projects' full creation.

Wireframes are created using [Balsamiq](https://balsamiq.com/wireframes/?gclid=Cj0KCQiAubmPBhCyARIsAJWNpiMYzrk_0rLzl3vgYKRLXwnX7rpqyQiUFdyt3xHGpRiHlZlozwO_pvcaAvUFEALw_wcB). 

The project was developed from initial wireframes and some modifications were made during the development process to ensure better UX.


#### The Home page
Where some sites demonstrate some django functionality on the landing page ie. the home page, for this project, the landing page shows the basic features one would expect to see for a restaurant site. The User is greeted with a main hero image, together with a Navbar, offcanvas navbar and footer to guide the user to other features of the site, which covers some of the User Stories listed below.

![Home page](/media/wireframes/homepage_wf.jpg)

![Offcanvas Navbar](/media/wireframes/offcanvas_navbar_wf.jpg)


#### The Register page
The registration page is designed to be light on the eyes to the User. There are 3 cards above the registration form which aim to remind the customers of the special services available to them should they wish to take advantage.

![Register page](/media/wireframes/register_page_wf.jpg)


#### The Login page
The login page initially looked bare and was missing a little something with just the Login form for the User to fill in. At this point it was decided the a hero image in the background would improve this UX.

![Login page](/media/wireframes/login_page_wf.jpg)


#### The Menu page
After carrying out some research into this Menu section, it was found that a lot of restaurants actually have fixed, unchanged menus. As a result it was decided that this restaurant would have a fixed unchanged menu for this first release. In future releases of this project the administrator will have control of this functionality and will be able to make changes to the Menu of the restaurant.

![Menu page](/media/wireframes/menu_wf.jpg)


## User Stories

In order to demonstrate an Agile approach to this project, GitHub issues were used as a Kanban board to record the user stories. The user stories were categorized into different User functions between the Admin and the User and each issue would be moved from the "to-do" board to the "done" board as the project progressed.

The Project Kanban board.

![Kanban Board](/media/images/agile_kanban_img.jpg)

### User stories - Admin features
The following user stories were satisfied by the creation of the Restaurant app, which include these features:


[User Story #1](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/1) As a administrator I can click on the navbar and select "login" so that I can make a booking on behalf of a customer.

[User Story #2](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/2) As a administrator I can view pending customer bookings so that I can approve or reject reservation requests.

[User Story #3](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/3) As a administrator I can view User Contact details so that I can reach out to them regarding their booking requests.

[User Story #4](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/4) As a administrator I can access the menu section so that I can remove existing menu and replace with new menu.

[User Story #11](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/11) As a administrator I can manage the table layouts so that I can have flexibility with moving tables around to meet demand.

### User stories - User features
The following user stories were satisfied by downloading the Django Allauth application which provides the project with built in tools to manage authentication, registration and account management:

[User Story #5](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/5) As a User I can click on Menu in the navbar so that I can view the days specials.

[User Story #6](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/6) As a User I can Click on navbar and select "contacts" so that I can view the restaurants contact details.

[User Story #7](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/7) As a User I can click on navbar and select "register" so that I can create a personal account.

[User Story #8](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/8) As a User I can login by inserting my email and password so that I can create a booking.

[User Story #9](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/9) As a User I can go to the navbar and select login so that I can book a table.

[User Story #10](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/10) As an authenticated User I can click on the navbar and select "Bookings" so that I can book a table.

# Backend Features

This project is built using Django, adopting the MVT (Models-Views-Templates) architecture. The restaurant app which contains the MVT architecture to make this site interactive has three main models:

### The Table Model

The Table model is created to provide the restaurant with a more flexible approach of managing tables pending customer demand. This feature is only available to the restaurant administrator. As an example, in the winter months the outside tables might be moved indoors as the demand for outdoor space might be reduced or eliminated. This model provides an administrator with the functionality to be able to do just that.

#### The Admin View

Employing all CRUD features - The administrator can Create, Read, Update and Delete any of these tables.
![The Table Model](/media/images/table_management_admin_img.jpg)


### The Booking Model

The booking model allows both the site administrator and the User to make a booking. The booking form requires that a table is selected, the number of guests attending, the date of the reservation, a start time and an end time. The form also contains a comments section to allow both the admin and the User to provide any comments such as any dietry restriction or perhaps raise any questions.

#### Admin view

Employing all CRUD features - The administrator can Create, Read, Update and Delete any of the bookings.
![The Booking Model](/media/images/admin_booking_form.jpg)

### The Contact Model

The contact model allows the User to fill in a form and raise any queries. The Admin might receive a call and can use this form to keep a record of any queries riased. The data is "posted" to the PostgreSQL table. This in turn allows that data to be accessed by the administrator to act and respond to the User regarding any queries or suggestions. The admin view comes with an added feature of "Actioned" status to allow the restaurant to track opened and closed enquiries.

#### Admin view

Employing all CRUD features - The administrator can Create, Read, Update and Delete any of the Contacts form.
![The Contact Model](/media/images/admin_contact_form.jpg)


# Frontend Features

There are of course other features on this site that would be expected. The site contains an offcanvas navigation panel provided with the assistance of Bootstrap5, which holds repeated links as seen on the top navbar of the main page view, but also contains links to the following items:

* The Menu page
* The Contacts Page
* The Booking page
* The Social Media accounts
* Confirmation of Booking received
* Alert message of unavailable table.

The main navbar and the offcanvas navigation is available to the User at all times.

![Offcanvas Navbar](/media/images/offcanvas_navbar_img.jpg)

### The Menu Page

The Menu page will satisfy User Story #5, as referenced in the User stories section above. The User is able to click on the link and is directed to the Menu page which is an image of a fixed Menu which for this first release will not be changeable.

![The Menu Page](/media/images/menu_pg.jpg)

### The Contacts Page

The contacts page satisfies User Story #6 and contains a simple form for the User to be able to reach out to the restaurant for answers to any queries or even to make and suggestions. The User can contact the restaurant via the provided form, or the page contains address details and contact phone number as alternative options. The map feature on the page is just a simple map illustrating the location of the restaurant. Should the User opt to call the restaurant, the administrator also has access to a contact form in the admin environment allowing the restaurant to keep a record of any external enquiries as detailed above.

#### The User View

![The Contacts Page](/media/images/user_contact_form_user_view.jpg)

#### The Admin View

![The Contacts Page](/media/images/user_contact_form_admin_view.jpg)

### The Booking Page

The booking page completes User Story #10 and allows a User to make a reservation at the restaurant. If the User is not authenticated, when they click on the bookings link they will be met with a message stating that they must be logged in if they wish to make a reservation. This feature does provide the User with an alternative which they can opt to select, this alternative takes them to the contacts form where they can raise a request and the restaurant will make the reservation on their behalf.

#### The Booking Message

![Not Authenticated Booking Message](/media/images/not_authenticated_user_booking_page.jpg)

#### The Alternative message

![Not Authenticated Alternative Message](/media/images/not_authenticated_user_booking_page_alt_message.jpg)

### The Social Media Accounts

The social media account links allow the Users to find out more about what other updates and activities the restaurant are involved in. By selecting one of these, the respective accounts will open up on a new tab.

# Technologies Used

### Languages Used

* HTML5
* CSS3
* Python3.8

### Frameworks, Libraries and Programs Used

* Balsamique was used to create the wireframes as part of the project scoping phase of this project
* MS PowerPoint was used in the project scoping and Agile Methodology preperation phase
* Django v3.2 is used for the architecture of the project
* Postgresql is used for Object Relational database management of this project
* Bootstrap v5 is used for some of the styling on this project
* Cloudinary is used as a media file storage location
* Fontawesome is used to provide some styling features on this project
* Google fonts is used on this project to provide font types
* Google maps is used to provide a visual image of the location of the restaurant.


# Code Validation

### HTML Validation

I have gone through all of the HTML files and copied them directly into HTML validator.

There are no errors identified in any html files.

### CSS Validation

I have copied and pasted the entire CSS sheet into the CSS validator with a result of no errors reported.

### Python Validation

I have copied and pasted all the .py files into the python validator with a result of no errors reported.

### JavaScrit Validation

I have copied and pasted the javascript file into the jhint validator with a result of no errors reported.

# Testing

### Lighthouse Validation

The lighthouse assessment returned back an accesibility result of 91%. Unfortunately the performance level is very low.

## Manual Testing

User Story [#1](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/1)

Can the administrator Log in?

A superuser was created with the built in tools from Django. This allows the administrator to login using their selected credentials. Test passed.

![Admin Login Test](/media/images/admin_login_test.jpg)

User Story [#2](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/2)

Can the administrator approve and / or reject a User booking?

Once the administrator is logged in, they can view the list of existing bookings.

User Story [#3](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/3)

Can the admin view the Users contact details?

The contact form allows the User to fill in their name and preferred contact. This detail is saved and send to the admin view where they are able to view the required details to respond to User.

User Story [#4](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/4)

Can the admin and the User view the menu?

For this first release, both the admin and the User can view the menu which is a fixed menu, by clicking on the menu link on the website.

User Story [#5](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/5)

Similar to User Story 4 both admin and User can now access the menu without being logged in.

User Story [#6](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/6)

Can the User view Restaurant Contacts?

The contacts page allows the user to fill in a form to reach out for any queries or suggestions. This page also contains the restaurant contact details and a map to localise the restaurants position.

User Story [#7](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/7)

Is there a registration feature?

The navbar include a link which will direct the user to the registration page.

User Story [#8](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/8)

Can the User Register?

The Registration page allows the user to introduce their deitails and other essential credentials allowing the user to register on the website.

User Story [#9](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/9)

Is there a login page?

The navbar include a link which will direct the user to the login page. The user can insert their credetials and click login. The user is then directed to the home page.

User Story [#10](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/10)

Can the User and admin make a reservation?

The booking model was created for this feature. If the User and the admin is logged in, they will be able to make a reservation. the admin can either use the frontend option or log in to the admin environment and make the reservation from that location also.

User Story [#10](https://github.com/RicardoIT-Web/diners-3star-restaurant/issues/10)

Can the admin make changes to the table arrangements?

The table model was created for this functionality. The admin can access the admin environment and make changes to the table layout as required.

# Bugs During Development

During the development phase of this project, Heroku made serveral updates to every app in my account. At some point, my static files stopped connecting to the heroku app meaning I was able to view my project in deployed view but it was missing a lot of CSS styiling.

To fix this with the support of the tutors at CI I went through the following steps;

* Access Heroku using the terminal

![Access Heroku - terminal](/media/images/dugs_heroku_staticfiles.jpg)

* Enter your email
    * For the password, go into your Heroku profile and copy the API key
    * paste API key in terminal as your password.

![Access Heroku - terminal](/media/images/dugs_heroku_staticfiles3.jpg)

* Once login confirmed
    * in the terminal type heroku run python manage.py collectstatic -a diners-3star-restaurant
    * you will be prompted to confirm Y or N

![Access Heroku - terminal](/media/images/dugs_heroku_staticfiles5.jpg)

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

* Paste in the url to ALLOWED_HOSTS value - ALLOWED_HOSTS = ['diners-3star-restaurant.herokuapp.com'] - Make sure to delete the Https structure at the start of the url & the final ‘/’

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
* Replace the Heroku host value in ALLOWED_HOSTS - ALLOWED_HOSTS = [os.environ.get('diners-3star-restaurant.herokuapp.com')]
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

* CI Blog Walkthrough Project
* Bootstrap
* Heroku
* Stackoverflow
* Pexels.com
* Fontawesome
* Cloudinary
* Summernote
* GitHub / Gitpod


### People

* Matt Bodden
* DarshanDev
* Rohit Sharma
* CI Tutoring Team
