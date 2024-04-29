## Manual testing

Navigation:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| Navbar logo |  When pressed takes you to homepage | Success | 
| Search bar | When you search for a recipe in the search bar it will display on a new page | Success |
| Home link |	When pressed takes you to homepage | Success |
| About link |	When pressed takes you to about page | Success |
| Recipes link | When pressed takes you to recipes page | Success |
| Contact link| When pressed takes you to contact page | Success |
| Create Recipes link |  When pressed takes you to create recipes page | Success |
| Profile link |  When pressed takes you to profile page  | Success  |
| Register link |  When pressed takes you to register page   | Success |
| Sign out link |  When pressed takes you to sign out page   | Success |
| Sign in link |   When pressed takes you to sign in  | Success |
| Facebooks icon | When pressed takes you to Facebook in a new page | Success |
| Instagram icon | When pressed takes you to Instagram in a new page | Success |
| Twitter icon | When pressed takes you to Twitter | Success |
| Youtube icon | When pressed takes you to Youtube | Success |
| Hamburger dropdown | When pressed the navbar is displayed | Success |

- The Profile, register and sign out navigation links will only be displayed when the user is logged in.
- The hamburger icon is only displayed from 992px and under.

### HOME PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| See Recipes button | When pressed takes you to the recipes page | Success |
| Contact us button | When pressed takes you to the contact page  | Success |
| Sign in button | When pressed takes you to the contact page  | Success |
- Sing in button will only be shown if the user is not logged in and is changes with "contact us" button.

### ABOUT PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |

### RECIPES PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Recipes |	 When hovered the picture and text get slight bigger and when pressed takes you to the detail view of that recipe | Success |


### RECIPES DETAIL PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Edit recipe button|	You can edit your own recipe by pressing the edit button and it will take you to the edit recipe page | Success |
| Delete recipe button | You can press the delete button and the user will be directed to the delete confirm page | Success |
| Delete confirm page | When pressing the delete button the recipe will be deleted. A confirm text willbe shown. | Success |
| Like button | When pressed it will be shown 1 more like and a text will be shown confirming that you have liked the recipe | Success |
| Comment button | The text you written in the body for leave a comment will be posted on that recipe as a comment. A confirm text will be shown.| Success |
| Edit comment button | When pressed the user can edit their comment | Success |
| Delete comment button | When pressed a delete modal will be shown | Success |
| Delete modal | When pressing on close button the modal closes and when you press delete button the comment will deleted. A confirm text will be shown | Success |
| Sign in link | When pressed the user gets directed to the sign in page | Success |

- The sing in link will only be displayed if the user is not logged in and can not comment or like a recipe.

### CONTACT PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Contact form | Your cna type text in every field wihout errors | Success |
| Contact from | Can only be sent if all the required fields are filled | Success |
| Submit button | Sending the message to the admin and a confirm text will be shown | Success |

### CREATE RECIPE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Create recipe form| You can type text in every field without errors | Success |
| Create recipe button | When pressed the recipe creates but only if all the required fields are filled | Success |

### PROFILE PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Edit button |	When pressed a modal for editing will be shown | Success |
| Edit modal button | When the edit button in the modal is pressed the profile is updated | Success |

### REGISTER PAGE:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Register form | You can type text in every field without errors | Success |
| Sign up button | If pressed the user is being registerd but only if all the required fields are filled | Success |
| Sign in link | When pressed takes you to the sign in page | Success |

### SIGN OUT:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Sign out button |	When pressed the user gets signed out and a confirm sing out text will be shown | Success |
| Buy cheese button | returns product list view of all cheeses | Success |
| Buy beer button | returns product list view of all beers | Success |

### SIGN IN:

| Feature Tested                        | Expected Outcome                 | Result  |
| ------------------------------------- | -------------------------------- | ------- |
| DOM |	all page elements load as expected |	Success |
| Sing in form | You can type text in every field without errors  | Success |
| Sing in button | When pressed the user will be logged in and a confirm sign in text is shown but only if all the required fields are filled | Success |
| Sign up link | When pressed takes you to the sign up page  | Success |


## Automated testing

__HTML and CSS__

All the html and css files ran through the W3C validator.

- W3C CSS Validator: ![Result](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/668c0e4d-8b85-4789-b37e-1ad891fd4133)

- W3C HTML Validator: All html code passed without any errors except the profile page, about page and create recipe page.
All errors were caused by either Allauth or Summernote and is nothing i can do to that. Here are the errors : 
![Errors](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/997b3487-9a79-462e-9302-2ae772ab96e6)
![Errors](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/36f7aea4-8850-4cf4-a634-11155757eb6c)
![Errors](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/f80dfd58-224a-47bf-b728-d7465004a81c)
![Errors](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/ea3329ec-4fe6-4cf2-833b-fa96b0868579)
![Errors](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/be960f8d-63df-4461-9a41-4716a85fbf5a)

__Python__

All files ran through Code Institutes [Python Linter](https://pep8ci.herokuapp.com/#)
<br> Every .py file passes without any errors.
![pep8](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/a594690e-0b93-4607-91d4-5afbf9030487)

__Javascript__

All files ran through the [JSHint Linter](https://jshint.com/) without any errors.

![JSHint Linter](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/c693f166-b23a-47e7-b3d2-a730df6fb912)


__Lighthouse__

## Home page 

Mobile View ![mobile home](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/63b91638-68c3-4a42-b02c-7670bc732e41)

Desktop View ![desktop home](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/8964c0fb-d44b-40b6-a722-1212383fc49f)

## About page 

Mobile View ![mobile about](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/eddb4bdb-c861-4fd9-ab51-765296e66b1a)

Desktop View ![desktop about](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/da1145c4-a49b-4702-ab14-e2d722b8a761)

## Recipes page 

Mobile View ![mobile recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/93d6eb9e-92de-48d0-a99e-645db00c0d13)

Desktop View ![desktop recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9946e963-93b5-4fc4-a0c0-a541df95741a)

## Recipe Detail page

Mobile View ![mobile recipe detail](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/91feb58e-e842-4fe5-bf77-77c1b45a9cd7)

Desktop View ![desktop recipe detail](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/afa8f5ef-b917-451e-8bdd-eba39682e24e)

## Contact page

Mobile View ![mobile contact](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/88249629-9ad3-4a79-9f28-12d53c4552b6)

Desktop view ![dekstop contact](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9ff7c976-1f5a-4214-bb80-ed56c8b02d46)

## Create Recipes page

Mobile View ![mobile create recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/38f34510-b98a-4e9f-954b-a32f1fffa734)

Desktop View ![desktop create recipes](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/6e253db1-abca-4f10-a3bd-e0280bb7361e)

## Profile page 

Mobile View ![mobile profile](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/fb63e1c7-1ee0-4ff7-9d43-d9006e38ce10)

Desktop View ![desktop profile](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/a3a2bd79-8c3a-4b11-bb76-909290315d1e)

## Register page 

Mobile View ![mobile register](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/4d5e573a-37b0-49fa-8321-87dff3a76fcc)

Desktop View ![desktop register](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/de826169-a9fc-4ee4-8aab-10924858b816)

## Sign out page 

Mobile View ![mobile sign in](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/8e3d1ccd-4f26-4b9e-8812-1ac9047a7139)

Desktop View ![desktop sign in](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/c93ef482-971f-443b-9faa-1d6adff5dec5)

## Sign in page 

Mobile View ![mobile sign out](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/298c9f50-ea4b-4f8f-ae07-b92f09079937)

Desktop View ![desktop sign out](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/e75f8e7d-57eb-4ae7-be95-f9453f603e1f)


<hr> 

## Bugs

No bugs on the website now that I know of.

Bugs that I found but I manage to solve them:
- I got this error when trying to delete my own comment. When I tried to exit the modal that open when I pressed "Delete" it display an error in the console. Had to search for it and found a solution on [Stackoverflow](https://stackoverflow.com/). 
I had to implement if commentElement !== null in the javascript for editbuttons.
![error delete](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/9bae2144-cddc-4ddd-a06d-e4e40af44d79)

- I got and favicon.ico 404 error and did not know what to do. Realized I just needed to add my own favicon and the error disappeared.

- Got an error when I was trying to connect user.id and profile.id. Do not know why it happend but I got help from slack with deleting the sqlite3 file. Then I just needed to create a new superuser and It solved it!  
![error profile](https://github.com/Idehed/Recipe-foods-P4/assets/146822758/6d15392b-382c-4f3b-a96d-0d6dada52acc)