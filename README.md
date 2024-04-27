# NourishNShare



[**Live site**]()

![Device Mockups](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/76f70c61-0819-4b0a-996f-a4d94c288090)

# Content

- [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Stories](#user-stories)
  - [Agile Planning](#agile-planning)
- [Features](#features)
  - [Navbar](#navbar)
  - [Footer](#footer)
  - [Home page](#home-page)
  - [About Page](#about-page)
  - [Recipes page](#recipes-page)
  - [Recipes detail page](#recipes-detail-page)
  - [Contact Page](#contact-page)
  - [Create Recipe page](#create-recipe-page)
  - [Profile page](#profile-page)
  - [Sign in Page](#sign-in-page)
  - [Sign out page](#sign-out-page)
  - [Register Page](#register-page)
- [Testing](#testing)
- [Validators](#validators)
- [Heroku Deployment](#heroku-deployment)
- [Run Locally](#run-locally)
- [Technologies](#technologies)
- [Planning](#planning)
  - [Wireframes](#wireframes)
  - [Database schema and Flowchart](#database-schema-and-flowchart)
- [Security](#security)
- [Credits](#credits)

<hr>

# Project Goals

## User Goals


## Site Owner Goals


## User Stories

<b>Following user stories was implemeneted in the project:</b>

* 

<b>Following user stories was not implemented and labeled as "Wont Have"</b>

*


<hr>

## Agile Planning
[Link to the user stories project]()
 
![User Stories]()

<hr>

# Features


## Navbar

__Fully responsive navbar with links to:__

    -

__Logo hyperlinked to home page:__
![Logo]()



__Navbar for non-authenticated users__:

![Navbar non auth]()
__Navbar for authenticated users__:

![Navbar auth]()

___Purpose of feature:___
Provide users with an easy and straight-forward way to navigate the site


## Footer



![Footer]()

___Purpose of feature:___
Provide users with a way to connect with me and check out my GitHub profile and social media accounts.

<hr>

## Home page

__The Home page consists of:__

    - 


<hr>

## About page

__The About page consists of:__



__About Section__


<hr>

## Recipes page

![Recipes page]()

<hr>

## Recipes detail page

![Recipes detail page]()

<hr>

## Contact Page

![Contact Page]()

__The Contact page consists of:__


__Contact form__

The contact form gives the user a way to contact the admin of the blog if they have any questions etc.

The fields the user needs to fill in is:

- Name
- Email
- Message

_Additional_: All of the fields are required to be filled in, if it's not the user will be prompted to fill in the field before sending. 
The email field needs to contain an email with @ in it to be sent.

___Purpose of feature:___
Provide users with a way to contact the admin and creator of the site.

<hr>

## Create Recipe page

![Create Recipe page]()

<hr>

## Profile page 

![Profile page]()

<hr>


## Sign in Page

![Sign in Page]()

__The Sign in Page consists of:__

    - Sign in form

__Sign in form__

The login form allows the user to enter their credentials and authenticate to enter the sites authenticated state.

The login form also contains a link to the [Register page]() in case the user is not already registered.

___Purpose of feature:___
Provide users with a way to login to the site.

<hr>

## Sign out page

![Sign out page]()


<hr>


## Register page

![Register page]()

__The Register page consists of:__

    - Sign up form

__Sign up form__

The Sign up form which is provided by django allows the user to enter credentials for registration on the site.

Through django it contains all the functionality for a secure registration and displays help text and error text to give the user feedback

The sign up form also contains a link to the [Login page]() in case the user already has an account.

___Purpose of feature:___
Provide users with a way to register an account on the site.

<hr>

# Testing

__Manual testing__

The website has been manually tested and everything has been documented in the testing.md file.

Click here to go to: [Testing and validation](testing.md)

<hr>

# Validators

All validation can be found in the testing.md file.

Click here to go to: [Testing and validation](testing.md)

<hr>

# Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

<hr>

# Run Locally

Clone the project

```bash
  git clone https://github.com/linx02/project-hub.git
```

Go to the project directory

```bash
  cd project_hub
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server

```bash
  python3 manage.py runserver
```

Note that you will have to setup your own database and API connections using these steps:

1. Create a file name "env.py" in the projects root directory.
2. Copy and paste this code in the env.py file and replace values with your own:

```python
import os

os.environ["DATABASE_URL"]=YOUR_DATABASE_URL
os.environ["SECRET_KEY"]=YOUR_SECRET_KEY
os.environ["CLOUDINARY_SECRET"]=YOUR_CLOUDINARY_SECRET
os.environ["THUMIO_AUTH"]=YOUR_THUMIO_AUTH_KEY
```
<hr>

# Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#


**External Python Modules**
* asgiref==3.7.2 - Used for building asynchronous Python web applications, especially with django.
* cloudinary==1.29.0 - Cloundinary was set up for use but no custom uploads were made, settings remain for future development
* crispy-bootstrap5==0.6 - This was used to allow bootstrap5 use with crispy forms
* dj-database-url==0.5.0 - Used to parse database url for production environment
* dj3-cloudinary-storage==0.0.6 - Storage system to work with cloudinary
* Django==4.2.10 - Framework used to build the application
* django-allauth==0.57.2 - Used for the sites authentication system, sign up, sign in, logout, password resets ect.
* django-crispy-forms==2.1 - Used to style the forms on render
* gunicorn==20.1.0 - Installed as dependency with another package
* oauthlib==3.2.0 - Installed as dependency with another package
* psycopg2==2.9.9 - Needed for heroku deployment
* PyJWT==2.8.0 - Installed as dependency with another package
* python3-openid==3.2.0 - Installed as dependency with another package
* requests-oauthlib==1.3.1 - Installed as dependency with another package (allauth authentication)
* sqlparse==0.4.4 - Installed as dependency with another package
* urllib3==1.26.18 - Installed as dependency with another package
* whitenoise==5.3.0 - Used to serve static files directly without use of static resource provider like cloundinary

<hr>

## Wireframes 

## Home 
![Home Page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/82a09cfd-99d6-4cfa-8f3b-cbbc17fd8aff)

## Recipes 
![Recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/a1d2d2cc-cf15-4c73-b5eb-a50675060b2f)

## Recipes detail 
![Recipes inspect](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/225ae6d5-bd0d-4e03-ac6a-1388d65c92de)

## About 
![About](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/0ec7ef75-450a-4262-9c9d-c9ec47599c85)

## Contact 
![Contact](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9536339f-4ec7-4400-9e07-0f579432fa3b)

## Register page
![Register](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/c460d80e-1915-4854-bfe5-c92137d1bdcf)

## log in page
![Log in](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/f2cc0b02-99b5-41eb-bc0b-8fa99bfc4442)

## Profile page
![Pofile Page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/17873baf-360f-4803-bb90-11f14b3ecf64)



<hr>

## Database schema and Flowchart

![Database schema]()

![Flowchart]()


__Data storing__:

[PostgreSQL](https://www.postgresql.org/): Database management system used.

[Cloudinary](https://cloudinary.com/): For storing image files in the cloud.

<hr>

# Security

## Cross-Site Request Forgery (CSRF) Protection
- Implementing CSRF protection helps prevent malicious websites from executing unauthorized actions on behalf of authenticated users.
- Django provides built-in CSRF protection by including a CSRF token with each form submission and verifying it on the server side.

## Django Allauth for Authentication and Authorization
- Django Allauth is an authentication and authorization framework that provides features like registration, login, password management, and social authentication.
- It ensures secure user authentication and authorization processes.

## Restricted Features for Authenticated Users
- Certain features, such as creating, editing, or deleting comments , are reserved for authenticated users only.
- By requiring users to be logged in to access these features, the application enhances security and ensures that sensitive operations are performed by authorized individuals only.

<hr>

# Credits
__Media__:


