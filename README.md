# NourishNShare
The NourishNShare is a website for people looking for different types of recipes. Here you can share your recipes, like and comment on a recipe that you find interesting or have opinions on. 



[**Live site**]()

![Device Mockups](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/f3d03e20-a42c-4df1-8080-2123ca1fa42e)

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
- Easily find and open a recipe that I like.
- Interact with other users by sharing recipes, liking and commenting on a recipe.
- Be able to navigate the platform and access relevant information easily.
- Have my profile page that I can see my shared recipes.
- Have a visually appealing and responsive user interface.

## Site Owner Goals
- Create a fun and interactive website about different recipes from all over the world. 
- Users enjoy interaction with other users by liking and commenting.
- Want users to frequently come back to the website to look for new recipes.

## User Stories

<b>Following user stories was implemented in the project:</b>

- As a Site Admin, I can delete users so that I can manage my recipe website users 
- As a Site Admin, I can delete users so that I can manage my recipe website users
-As a Site Admin, I can create or edit the About page content so that it is available on the site
- As a Site User, I want to be able to register so that I can log in to the site
- As a Site User, I want to be able to access my profile so that I can edit it
- As a Site User, I can create recipes so that I can share them with other users
- As a Site User, I can comment on a post so that I can show what I think about the post
- As a Site User, I can use the contact form so that I can contact the admin of the blog
- As a Site User, I can search for different recipes so that I can find them faster
- As a Site User, I can open a recipe so that can see the instructions on how to make the food
As a Site user, I can go to the "about" page so that I can read about the writer/admin
- As a Site User, I can like recipes that are shared by users
- As a Site User, I can go to my profile so that I can view my shared recipes

<b>Following user stories was not implemented and labeled as "Won't Have"</b>

- As a Site User, I can rate recipes so that other users can see how good it is
- As a Site User, I can view my liked recipes so that I can access them easily


<hr>

## Agile Planning
[Link to the user stories project](https://github.com/users/Idehed/projects/5)
 
![User Stories](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/63bc04a4-d4e4-43e1-b145-5fdd7c71469b)

<hr>

# Features


## Navbar

__Fully responsive navbar with links to:__

    - Home page 
    - About page 
    - Recipes page
    - Contact page 
    - Create Recipe page (If the user is authenticated)
    - Profile page (If the user is authenticated)
    - Register page 
    - Sign out (If the user is authenticated)
    - Sign in 

The NourishNShare name and the lemon icon are also linked to the home page.



__Navbar for non-authenticated users__:

![Navbar non auth](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/0b9c9310-cb67-4ed8-b800-4fd35b4aeaa5)
__Navbar for authenticated users__:

![Navbar auth](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/ae7722fe-fefe-4cc7-b1d8-14549baa5efd)

__Navbar for non-authenticated and authenticated users mobile view__

![Navbar mobile view](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/a7bf6322-a765-4129-9583-45289afa9dab)

![Navbar mobile view](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/db040500-2068-4a39-afa5-7d5b76166d95)

![Navbar mobile view](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/04cce95a-adf1-440d-9399-3705d266bd40)

## Footer



![Footer](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/409f1944-9ecf-4077-be6d-d0a5e2b205b2)

The "Follow us here" text will disappear at 576px and below for more smoother footer look in mobile view.

<hr>

## Home page

__The Home page consists of:__

    - Welcoming home image 
    - Welcome text to make users feel welcome
    - See recipes button
    - Sign-in button 
    - Contact us button


![Home page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/603a4a93-7e2c-4e87-945e-b1280e3d7ccb)


<hr>

## About page

__The About page consists of:__

    - Picture of the Nourishnshare team eating 
    - About us text
    
![About page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/1cf8d2fd-3971-4760-b58b-0067e8203620)
    
This about page gives a small presentation of the Nourishnshare team.


<hr>

## Recipes page


    - Recipe posts
    
![Recipes page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/b277be70-9ca6-439a-8ab3-9001aecebf25)

Here all the recipes that have been uploaded are displayed with the latest first.

<hr>

## Recipes detail page


    - Image of the recipe 
    - Title
    - Information about the recipe
    - Comment and like section 


![Recipes detail page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/4ee93f55-032a-47a6-8ca7-d2c7483647c9)

The comment section allows the users to post, edit, and delete a comment on a recipe post.

![Recipes detail page comments](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/cf3ecc22-0903-4d3c-8b85-a06d74cbc76d)

The delete modal is shown if the user wants to delete their comment.
![Delete modal](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/d0d676dd-2a75-4a80-b94f-dc997be55f19)

If the user is authenticated the like button is clickable and changes color to green if liked. It also changed color to green when hovering for a better user experience.

![like button not clicked](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/c372058d-e1d9-40b4-90d7-6f1ff544489e)
![like button is clicked](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/52246d1c-db02-42c3-965d-2215d53e0b2e)

If the user is not authenticated the like button is not clickable.

![like button not logged in](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/42d22c69-ea9b-4236-8299-a8eceb1b54c8)

If the user is not authenticated the comment section has not buttons for comment, delete, or edit. A text with "Sign In" is displayed so the user can navigate to the sign-in page to be able to like and comment.

![comment section not authenticated](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/77dd5ff6-cb02-41a8-b1bd-dbc6c10c519e)



<hr>

## Contact Page

__The Contact page consists of:__
   
    - Contact form
    

__Contact form__

The contact form gives the user a way to contact the admin of the blog if they have any questions etc.

The fields the user needs to fill in are:

- Name
- Email
- Message

All of the fields are required to be filled in, if it's not the user will be prompted to fill in the field before sending. 
The email field needs to contain an email with @ in it to be sent.

![Contact page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/fd88f1a6-d48d-4729-b1d3-0bf01cde3c6e)

<hr>

## Create Recipe page

   - Create recipe form

__Create Recipe form__

The fields the user needs to fill in are:

- Title
- Description
- Recipe Ingredients
- Recipe Instructions
- Recipe Image
- Describe Image
- Calories

![Create Recipe page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/4d871867-3ad3-41a6-9d66-835372e90f14)
![Create Recipe page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9433eed5-9cd2-4327-aadd-299aa2b6c7d6)

After successfully adding the recipe a confirmation text is displayed.

<hr>

## Profile page 

  - Profile image 
  - About info
  - Shared recipes

On the profile page, the user can edit their profile
  - Change image 
  - Change text in bio

![Profile page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/7bcef48f-5c5e-41a1-abb7-f27a78cf66b6)

<hr>


## Sign in Page

![Sign in Page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/ae82e491-2a04-4539-b1b9-6c59efd58c43)

__The Sign in Page consists of:__

    - Sign in form

__Sign in form__

The login form allows the user to enter their credentials and authenticate to enter the site's authenticated state.

The login form also contains a link to the Register page in case the user is not already registered.


<hr>

## Sign out page

![Sign out page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/1727d354-1ae7-4d45-bb7e-2a22e5989fdd)


<hr>


## Register page

![Register page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/3ba19e8d-1a19-4330-86c9-028dd8031812)

__The Register page consists of:__

    - Sign up form

__Sign up form__

The Signup form which is provided by Django allows the user to enter credentials for registration on the site.

Through Django it contains all the functionality for secure registration and displays help text and error text to give the user feedback

The signup form also contains a link to the Sign in case the user already has an account.

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
  git clone https://github.com/Idehed/Recipe-foods-P4
```

Go to the project directory

```bash
  cd Recipe-foods-P4
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
  - favicon files were created at [Flaticon](https://www.flaticon.com/)
- balsamiq
  - wireframes were created using the app balsamiq wireframes.


**External Python Modules**
- asgiref==3.8.1
- black==24.4.0
- click==8.1.7
- cloudinary==1.39.1
- crispy-bootstrap5==2024.2
- dj-database-url==0.5.0
- Django==4.2.11
- django-allauth==0.57.2
- django-cloudinary-storage==0.3.0
- django-crispy-forms==2.1
- django-resized==1.0.2
- django-richtextfield==1.6.2
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- pathspec==0.12.1
- pillow==10.3.0
- psycopg2==2.9.9
- PyJWT==2.8.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.4.4
- whitenoise==6.5.0
 

<hr>

## Planning Project 

### Wireframes Balsamiq
<hr>
I created my wireframes using the Balsamiq app. 

## Home 
![Home Page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/82a09cfd-99d6-4cfa-8f3b-cbbc17fd8aff)

## About 
![About](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/0ec7ef75-450a-4262-9c9d-c9ec47599c85)

## Recipes 
![Recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/a1d2d2cc-cf15-4c73-b5eb-a50675060b2f)

## Recipes detail 
![Recipes inspect](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/225ae6d5-bd0d-4e03-ac6a-1388d65c92de)

## Contact 
![Contact](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9536339f-4ec7-4400-9e07-0f579432fa3b)

## Create recipe 
![Create recipe](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/77ed35ca-bdf9-4c9f-a205-ac653bcecbb3)

## Register 
![Register](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/c460d80e-1915-4854-bfe5-c92137d1bdcf)

## log in 
![Log in](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/f2cc0b02-99b5-41eb-bc0b-8fa99bfc4442)

## Profile 
![Pofile Page](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/17873baf-360f-4803-bb90-11f14b3ecf64)



<hr>

## Database schema

I created the database schema using the Lucidchart website.

![Database schema](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/279d1537-1328-49b2-8fb8-f00498d773a1)


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
- Certain features: 
  - Such as adding recipe( create, edit and delete)
  - Commenting and liking a recipe( create, edit and delete)
  - Seeing a profile page (edit)
<br> are reserved for authenticated users only.
- By requiring users to be logged in to access these features, the application enhances security and ensures that sensitive operations are performed by authorized individuals only.

<hr>

# Credits

__Media__:
- The lemon icon from [Flaticon](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/77ed35ca-bdf9-4c9f-a205-ac653bcecbb3)
- The like and comments icon from [Fontawesome](https://fontawesome.com/)
- Facebook, Instagram, Twitter, and Youtube icons from [Uxwing](https://uxwing.com/)
- The home and about images from [Unsplash](https://unsplash.com/)
<br> Home image credits to Ella Olsson <br> About image credits to Dan Gold
- I used this [YouTube](https://www.youtube.com/watch?v=PXqRPqDjDgc&ab_channel=Codemy.com) video to get me started with the like button.
- I used this [YouTube](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1&ab_channel=DeeMc) video to help me with my website.
- With the help of this [YouTube](https://www.youtube.com/watch?v=45QSuJaHEss&ab_channel=ADesignerWhoCodes) I was able to change the color of the hamburger nav icon.
- I learned more about the Redirects through this website [realpython](https://realpython.com/django-redirects/)

__Other Credits:__
- The recipe website is based on the I think therefore I blog that I have adapted to fit my project.
- Thanks to the Slack community for helping me when I got stuck.
- Thanks to my family who has helped me test my websites functionally.
- Thanks to my mentor Ronan Mc for his support and guidance.