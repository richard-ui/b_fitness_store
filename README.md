# Django Framework Project

## B-Fitness Store

- Link to Project - [View](https://rickys-recipe-manager.herokuapp.com/)

![All_Devices](/static/img/responsive_image.png)

# Brief Introduction to the Project

The purpose of this project is to create an E-Commerce website that sells a range of items, which Customers are abliged to browse 
and purchase. 

## Target Audience

- The website is aimed at people who are interested in Exercise, generally who are keen Gym goers and wish to browse for items
  that will benefit there exercise.

## Data Details for Admin (test purposes for examiner to use)

- Username: rick123  
- Password: Muffin1234!


# UX User Stories

### First Time User's:

- As a First Time user, I want to understand the main concept of the site and learn the intention of its relevance.

- As a First time user, I want to be able to navigate the site in an easy and efficient way without any complex design.

- As a First Time user, I want to be able to register an Account

- As a First Time user, I want to be able to see a list of products displayed on the products page.

- As a First Time user, I want to be able to add a new product to my shopping bag.

### Returning User's:

- As a returning user, I want to be able to log in easily and efficiently.

- As a returning user, I want to be able to view my shopping bag and be able to update accordingly.

- As a returning user, I want to be able to purchase the current products in my shopping bag.

### Admin goals: 

- As an Admin, I want to be able to add a new product.

- As an Admin I want to be able to update or delete a specific product.

- As an Admin, I want to be a able to view a more detailed specification of the product I am interested in buying.

# Design

1. Colour Scheme
- The use of dark and light colours are used together in contrast on the page. For example the body is dark to represent a gym environment, whereas the Navigation bar/headings
  are bright so that the user can follow them easier. 

2. Typography
- The 'ubuntu' font is the main font used throughout the website with Sans-Serif as the fallback font in case for any reason the font is not supported by the browser.

# Wireframes

- Computer Wireframe - [View](https://github.com/richard-ui/Data-Centric-Project/blob/master/static/img/recipe_page.pdf) 

- Mobile Wireframe - [View](https://github.com/richard-ui/Data-Centric-Project/blob/master/static/img/recipe_page_mobile.pdf)

# Technologies Used

1. Bootstrap 4.5
2. Google Chrome 
4. JavaScript 
5. Font Awesome
6. jQuery
7. Git
8. GitHub
9. Gitpod
10. Balsamiq
11. Python and Python3
12. Django
13. Heroku
14. Jinja
15. Stripe
16. AWS

# Features
| Feature  | Details |
| ------------- | ------------- |
| Register  | The User can create an account which will be saved to the database and there details will be saved for future use.   |
| Login  | The user can log into their own account with personalised features.  |
| Log out  | There is a log out functionality on the page - this is especially important for users of a shared device.   |
| Add Product   | Admins can contribute adding a new product via the Add Product Page  |
| Edit Product | Admins are able to edit any of the available products.   |
| Delete Product   | Admins are able to delete their own products.  |
| Search function   | The users are able to search the product by 'Name'. This function is available whether a user is logged in or not.  |

# Features left to implement
| Feature  | Details |
| ------------- | ------------- |
| Pagination  | I would of liked the recipes to be listed by (5) records of recipes per page, but unfortunately it became more confusing and unfortunately I ran out of time.   |

# Bugs

- Once I found a way to implement jQuery's Autocomplete functionality, there was an issue with the list of product suggestions displayed from the search box.
  It would display behind the 'main-nav' and the 'delivery banner' elements. I fixed this by customizing the z-index of the 'ui-autocomplete' class in the css file so it would display infront of
  everything that it should.

# Testing

### User Testing for User Stories
### First Time User's:

- As a First Time user, I want to understand the main concept of the site and learn the intention of its relevance.

  i. Upon entering the site, it is clear to the user that the website is about something to do with Gym and Fitness, due to the sites background image. Also the use of dark colours on the site make
     it apparant makes the user feel that they are in a gym environment.
  
- As a First time user, I want to be able to navigate the site in an easy and efficient way without any complex design.

  i. The navigation is clear, with most of the site being a dark theme, the navigation is white making it stand out to the user.
  
  ii. These links are also dynamic as specific links will be shown depending on whether the user is logged in or not.

- As a First Time user, I want to be able to register

  i. In the navbar a link named register that when clicked will take the user to the register page.

  ii. They will then create using a username and password

- As a First Time user, I want to be able to browse and search for recipes.

  i. A card is displayed on the homepage allowing me to type in a recipe and click the seasrch button beside it.
  Recipes will display below.
  
  ii. If no recipes are found a "No results found" message will warn the user immediately.

- As a First Time user, I want to get inspiration for a recipe to make myself.

  i. The images have an effect on what food the user may desire
  
  ii. The Cuisines list in the dropdown provide nationalities, as they view them, they can think of recipes from one of these Countrie's.

### Returning User's:

- As a returning user, I want to be able to log in easily and efficiently.
  
  i.  In the navbar a link named 'login' will take me to the login page.

  ii. If they are a registered user, typing in their username and password will log them in.

- As a returning user, I want to be able to view my recipes on my own profile page.

  i. Created recipes made by the user can be displayed on the recipes/home page or their profile page once logged in.

- As a returning user, I want to be able to edit my existing recipes.

  i. All my recipes on the recipes page provide edit buttons.

  ii. When the edit button is clicked, this will take me to the edit recipe page with existing data displayed in the input boxes.

  iii. This will allow me to update multiple values, after the edit button is clicked, all values for that recipe will be updated.

- As a returning user, I want to be able to delete existing recipes.

  i. For each recipe a red delete button will be displayed below it. When pressed, a modal will appear asking for confirmation of deletion.

- As a returning user, I want to be able to add new recipes.

  i. A form allows for user input with creating a new recipe, inlcluding name, image and cuisine.

- As a returning user I want to be able to search a recipe from an input box and see suggestions depending on which letters I type.

### Admin User's:

- As an Admin, I want recipes added via the site to be stored in the correct format in the database. (jpg, png etc)

  i. Images that are about to be uploaded are validated for PNG or JPEG for formats.

- As an Admin, I want to be able to see who has added each recipe.

  i. Once logged in, The recipes page displays each recipe along with the User name who created it.

- As an Admin, I want to be able to Add, edit and delete recipes

  i. On the Recipes page their our edit and delete buttons below each recipe. They can interact with these as they wish.

- As an Admin, I want to be able to Add, edit and delete cuisine types.

  i. When the Admin is logged in, the 'Manage Cuisine's' tab on the navbar will display. Clicking this will take the user to the cuisines page
     where each cuisine will have an edit and delete button. From their they can modify as they wish.

### Further Testing

- The W3C Markup Validator was a feature used to validate all html elements on each page.

- The W3C CSS Validator Services were used to validate every snippet of css in the style sheet.

- JSHint was used to validate all the JavaScript code within each file.

- The website was tested on multiple browsers such as Microsoft Edge, Opera and FireFox, but the main one that was used was Chrome. This was because I was using the chrome extension at the time for gitpod and I felt chrome was fast and reliable.

- The website was viewed on iPhone, Android, Laptop and Desktop Devices. There was also use of the developer tools as a faster way to look at the site becoming responsive such as using the example devices in the tools area. Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

- The Responsinator tool was a feature used to view the deployed site and look to see how each device would display it. Device screens such as Android, iPhone and iPads were used to view on. In doing so they were viewed in a landscape and portrait perspective.

  ![All_Devices](/static/img/mobile_responsinator.png)

  ![All_Devices](/static/img/ipad_responsinator.png)

# Deployment

## Github Pages

1. Log in to GitHub
2. Locate the repositories and chose one that you want to Deploy
3. Press the "Settings"
4. Scroll down to the GitHub pages section
5. Under "Source" enter the drop down list with the first value of "None" and select "Master branch" instead
6. The page will refresh to be took to the top of the page
7. Scroll down until you get to the "Github pages" section to identify your now deployed link to your website

## Forking the Github repository

Forking the repsoitory means we are making a copy of the original version to edit and modify any changes without affecting the original.

1. Log in to GitHub and locate the Github Repository
2. At the top of the Repository (not top of the page) just above the "Settings" button on the menu, locate the "Fork" button
3. You should now have a copy of the original Repository in your GitHub Account

## Making a Local Clone

1. On the main page of the repository, click the down arrow Code button
2. Click the download icon under the relevant section to clone with either HTTPS, SSH or GitHub CLI
3. In Git Bash, change the current directory to the location you want the directory to be stored
4. Type git clone and then paste the URL you copied in step 2
5. An example for HTTPS: git clone https://github.com/richard-ui/Data-Centric-Project
6. Press enter - that's it, your clone has been completed!

## Heroku

### Deployment to Heroku

1. Install **gunicorn** from the terminal: `pip3 install gunicorn`
2. Freeze this into the **requirements.txt** file: `pip3 freeze > requirements.txt`
3. Create a **Procfile**, To tell Heroku to create a web dyno. add this to the file.
   - web: gunicorn <project_name>.wsgi:application
4. Now Push these newly created files to github using git push.
5. From terminal type 'heroku config:set DISABLE_COLLECTSTATIC=1 --app <APP_NAME>', So that Heroku won't try to collect static files when we deploy.
6. In **settings.py** use this to connect to Heroku Host 'ALLOWED_HOSTS = ['<APP_NAME>.herokuapp.com', 'localhost'] 
7. Log in to **Heroku**.
8. Select Create new app from the dropdown menu in the heroku dashboard.
9. Choose a name for your new app.
10. Navigate to the Deploy tab and under deployment method choose GitHub.
11. Press Connect to GitHub and enter your Github repository that you want to associate with. Now click connect.
12. Go to **Settings** tab, and under Config Vars choose **Reveal config Vars**.
13. Now enter the following values into the required slots in the table:

| Key  | Value |
| ------------- | ------------- |
| AWS_ACCESS_KEY_ID  |<YOUR_AWS_KEY>   |
| AWS_SECRET_ACCESS_KEY  | <YOUR_AWS_SECRET_KEY>  |
| DATBASE_URL  | <POSTGRES_LINK> |
| EMAIL_HOST_PASS   | <EMAIL_HOST_PASS_KEY>  |
| EMAIL_HOST_USER | <GMAIL_ACCOUNT_NAME> |
| SECRET_KEY | <APP_SECRET_KEY> |
| STRIPE_PUBLIC_KEY  | <YOUR_STRIPE_PUBLIC_KEY>  |
| STRIPE_SECRET_KEY  | <YOUR_STRIPE_SECRET_KEY>  |
| STRIPE_WH_SECRET | <STRIPE_WEBHOOK_SECRET_KEY> |
| USE_AWS  | True |


DISABLE_COLLECTSTATIC	1

14. In settings.py add the **secret key** from heroku:
    - SECRET_KEY = os.environ.get('SECRET_KEY, '')
15. Navigate back to the **Deploy** tab and under Automatic deploys choose **Enable Automatic Deploys**.
16. Under Manual deploy, select master and click **Deploy Branch**.
17. When app is completed downloading, press **Open app** from the header dashboard which will open up the app in a new tab in your browser.

# Content
- The product images were took from Sports Direct.
- 'Sports Direct' was used for clothing Descriptions.
- Powerhouse Fitness was used for Exercise Equipment Descriptions.

# Credits
## Code
- Slack was used to gather information about what jQuery code to use for implementing an image upload function() to the Cloudinary server.
- For the deletion of products, I used a defensive approach for the admin user, by placing a modal popup to confirm deletion.
  The code to help with this came from [CRUD USING AJAX & JSON](hhttps://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html)

# Acknowledgements
- My Mentor provided me with help and provided me access to Holly’s repository to view. This allowed me to locate the issues in my code and improve functionality that I may have been struggling with.
- Slack was used to help me with the image upload, so it can be used on the server.

 My friends and family who helped to test the site and to test payments of products.

- Girlfriend - Alexandra Connolly

