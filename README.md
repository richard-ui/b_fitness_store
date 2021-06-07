# Django Framework Project

## B-Fitness Store

- Link to Project - [View](https://b-fitness-django-app.herokuapp.com/)

![All_Devices](/static/img/responsive_image.png)

# Brief Introduction to the Project

The purpose of this project is to create an E-Commerce website that sells a range of items, which Customers are abliged to browse 
and purchase. 

## Target Audience

- The website is aimed at people who are interested in Exercise, Shoppers who are keen Gym goers and wish to browse/buy items
  that will fulfill there exercise needs.

## Data Details for Admin (test purposes for examiner to use)

- Username: rick123  
- Password: muffin11


# UX User Stories

### First Time User's:

- As a First Time user, I want to understand the main concept of the site and learn the intention of its relevance.

- As a First time user, I want to be able to navigate the site in an easy and efficient way without any complex design.

- As a First Time user, I want to be able to register an Account

- As a First Time user, I want to be able to see a list of products displayed on the products page.

### Shopping User's:

- As a Shopper, I want to be able to log in easily and efficiently.

- As a Shopper, I want to be able to search for a product by Name or Description.

- As a Shopper, I want to be able to see a list of suggestions concerning the products.

- As a Shopper, I want to be able to search a product by Category

- As a Shopper, I want to be able to see more information about the certain product I am interested in buying.

- As a Shopper, I want to be able to adjust the quantity of the items in my bag

- As a Shopper, I want to be able to purchase the current products in my shopping bag.

- As a Shopper, I want to be able to view my shopping bag and be able to update accordingly.

### Admin goals: 

- As an Admin, I want to be able to add a new product.

- As an Admin I want to be able to update a specific product.

- As an Admin, I want to be able to delete a product.

# Design

1. Colour Scheme
- The use of dark and light colours are used together in contrast on the page. For example the body is dark to represent a gym environment, whereas the Navigation bar/headings
  are bright and big so that the user can see them easily.

2. Typography
- The 'ubuntu' font is the main font used throughout the website with Sans-Serif as the fallback font in case for any reason the font is not supported by the browser.

# Wireframes

- Computer Wireframe - [View](https://github.com/richard-ui/b_fitness_store/blob/master/media/product-page-computer.png) 

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
10. WireframePro
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
| Search function   | The users are able to search the product by 'Name' or 'Description'. This function is available whether a user is logged in or not.  |

# Features left to implement
| Feature  | Details |
| ------------- | ------------- |
| Pagination  | I would of liked the recipes to be listed by (5) records of recipes per page, but unfortunately it became more confusing and unfortunately I ran out of time.   |

# Bugs

- Once I found a way to implement jQuery's Autocomplete functionality, there was an issue with the list of product suggestions displayed from the search box.
  It would display behind the 'main-nav' and the 'delivery banner' elements. I fixed this by customizing the z-index of the 'ui-autocomplete' class in the base.css file so it would display infront of
  everything that it should.

# Testing

### User Testing for User Stories
### First Time User's:

- As a First Time user, I want to understand the main concept of the site and learn the intention of its relevance.

  i. Upon entering the site, users are automatically greeted with a clean and easily readable bootstrap navigation bar, with the Title and logo of a Dumbell that clearly represents exercise.

  ii. The Background is an image of weight training, therefore the user can understand a quick and efficent way to understand that the site sells 'GYM' equipment.

- As a First time user, I want to be able to navigate the site in an easy and efficient way without any complex design.

  i. The use of a navigation bar is at the top of the page with links and 'icons' to emphasise them.

- As a First Time user, I want to be able to register an Account

  i. The user can navigate to the register page by going to the account link on the navbar. Depending on whether they are logged in or not it will show different drop down options.

- As a First Time user, I want to be able to see a list of products displayed on the products page.
  
  i. When the user first visits, the home page displays a shop now button which they can use to navigate the products page. This opens up a table of products that the user can see.
  
  ii. They can also use the dropdown list with the option 'All Products' which perform the same request.

### Shopper User's:

- As a Shopper, I want to be able to log in easily and efficiently.

  i. If the user has an account, they can login by navigating the 'Account' tab and pressing Sign in.

- As a Shopper, I want to be able to search for a product by Name or Description.

  i. Once the user has typed in their some letters into the search box, they can press the red search button which will load a list of products relating to the word.

- As a Shopper, I want to be able to see a list of suggestions concerning the products.

  i. The user can type 3 letters into the search box and a list of product suggestions will display concerning them letters in bold.

- As a Shopper, I want to be able to search a product by Category

  i. As soon as the user enters the website there is a number of dropped lists with certain categories inside them. If the user clicks one, a list of products relating to that category will display on the page.

  ii. These categories include sorting "by price" and "by rating", with "gym equipment" and "sports shoes" being some of the product categories to name a few.

- As a Shopper, I want to be able to see more information about the certain product I am interested in buying.

  i. On the products page, the User can click on any single product where they will enter a product detail page to read about it. This displays more details about the product, that the user may not of seen otherwise. 

- As a Shopper, I want to be able to adjust the quantity of the items in my bag

  i. The use of a dropdown box is next to item on the product page.

  ii. This stores a list of numbers that the user can select to adjust the quantity.

- As a Shopper, I want to be able to purchase the current products in my shopping bag.

  i. After the customer is happy with their current products, they can press the buy now button and a notification will appear at the top navigation alerting them that the payment has been made. A notification should also be sent to their email
     confirming that the payment went through.

- As a Shopper, I want to be able to view my shopping bag and be able to update accordingly.

  i. The user can click on the 'Shopping cart' Icon with the price of the shop underneath it on the navigation bar.

  ii. If their is items in their cart, the user can update the items quantity or decide to remove it.

### Admin User's:

- As an Admin, I want to be able to add a new product.
  
  i. The admin can access the products management page from the accounts navigation link. From here they can enter information into a form creating a new product.

- As an Admin I want to be able to update a specific product.
  
  i. When admin enters the product page, underneath each item there is an to option to delete. When pressed an edit product page will appear and
     allows admin to customize the product.

- As an Admin, I want to be able to delete a product.
  
  i. Admin clicks the red delete button on any product, then a Modal will display asking them confirmation to delete.

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
- For the deletion of products, I used a defensive approach for the admin user, by placing a modal popup to confirm deletion.
  The code to help with this came from [CRUD USING AJAX & JSON](https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html)
- To help me with displaying the autocomplete suggestions infront of the navigation bar, I used [Stack Overflow](https://stackoverflow.com/questions/6762174/jquery-uis-autocomplete-not-display-well-z-index-issue) 
- Credited the autocomplete search functionality from '[codebands](https://www.youtube.com/watch?v=-oLVZp1NQVE)' channel on Youtube.
- Used Code from this website to provide the page with pagination options. [Django Pagination](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)

# Acknowledgements
- My Mentor provided me with help and provided me access to Holly’s repository to view. This allowed me to locate the issues in my code and improve functionality that I may have been struggling with.
- Slack was used to help me with the image upload, so it can be used on the server.

 My friends and family who helped to test the site and to test payments of products.

- Girlfriend - Alexandra Connolly

- Friend - Ashley Wilson
