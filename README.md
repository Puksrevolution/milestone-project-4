Milestone Project 4
======

## **Fancy Shoes | Your Online Shop for Shoes**
By: [Marina Christen](mailto:puksbusinessworld@gmail.com), October 2021<br>
This webpage is the last Milestone Project which is a part of the Full Stack Web Development Program of [Code Institute](https://www.codeinstitute.net/).


Live Project
======

[View the live project here](https://msp4-fancy-shoes.herokuapp.com/)


Screenshot
======

All screenshots created using [Am I responsive](http://ami.responsivedesign.is/).

<img src="Documentation/screenshots/screenshot_fancy-shoes.jpg">

---
### **Contents** ###

- [Project](#project)
  - [Project Description](#project-description)
  - [Project Requirements](#project-requirements)
  - [Project Goals](#project-goals)
  - [Website Description](#website-description)
  - [Website Owner's Goals](#website-owners-goals)
- [UX Design](#ux-design)
  - [User Stories](#user-stories)
    - [Viewing and Navigation](#viewing-and-navigation)
    - [Registration and User Accounts](#registration-and-user-accounts)
    - [Sorting and Searching](#sorting-and-earching)
    - [Purchasing and Checkout](#purchasing-and-checkout)
    - [Admin and Store Management](#admin-and-store-management)
- [Design](#design)
  - [Colours](#colours)
  - [Wireframes](#wireframes)
  - [Responsive Front-end Design](#responsive-front-end-design)
  - [Back-end Design](#back-end-design)
  - [Site Construction](#site-construction)
    - [Topology](#topology)
  - [Database Schema](#database-schema)
    - [Fixtures JSON File creation](#fixtures-json-file-creation)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Database](#database)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Features](#features)    
  - [User Stories Implemented](#user-stories-implemented)  
  - [CRUD Functionality](#crud-functionality)
  - [Messages](#messages)
  - [Defensive Programming](#defensive-programming)
  - [Additional Site Features](#additional-site-features)
  - [Future Features](#future-features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Cloning Milestone Project 4 from GitHub](#cloning-milestone-project-4-from-github)
    - [Prerequisites](#prerequisites)
    - [Cloning the GitHub repository](#cloning-the-github-repository)
    - [Creation of a Python Virtual Environment](#creation-of-a-python-virtual-environment)
    - [Install the App dependencies and external libraries](#install-the-app-dependencies-and-external-libraries)
    - [Create the database in sqlite3](#create-the-database-in-sqlite3)
    - [Create .env file](#create-env-file)
    - [Run the application locally](#run-the-application-locally)
  - [Deploying Milestone Project 4 app to Heroku](#deploying-milestone-project-4-app-to-heroku)
    - [Creating the Heroku app](#creating-the-heroku-app)
    - [Adding a PostgreSQL database to Heroku](#adding-a-postgresql-database-to-heroku)
    - [Load the data into PostgreSQL](#load-the-data-into-postgresql)
    - [Push your repository to GitHub](#push-you-repository-to-github)
    - [Launch the app](#launch-the-app)
- [Credits](#credits)
  - [Images](#images)  
  - [Acknowledgements](#acknowledgements)

---

Project
======

### **Project Description** ###
The goal of this project is to build a full-stack site based around business logic used to control a centrally-owned dataset and to showcase the knowledge of HTML, CSS, JavaScript and Python+Django I gained so far in this course.

To set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

### **Project Requirements** ###
- HTML
- CSS
- JavaScript
- Python+Django
- Relational database (recommending MySQL or Postgres)
- Stripe payments
- Additional libraries and APIs

### **Project Goals** ###
- To build something awesome to be proud of
- To make effective use of course knowledge and fulfill all given requirements
- To make a project with a great looking layout, that works and that is practical
- To create a web application that makes the user want to stay and use with pleasure

### **Website Description** ###
![Fancy Shoes logo](Documentation/images/FancyShoes.png)

Fancy Shoes is a (fictitious) online retailer providing footwear for sale. The idea for this final project is to provide the visitor with a fully functioning, interactive e-commerce website providing easy, familiar navigation and allowing the simulated purchase of items from the store.

The site functionality will allow a common shopping experience for the visitor by providing a shopping cart to save chosen items, a secure checkout / payment facility and order confirmation using both on-screen messages and friendly, personalised emailed message.

### **Website Owner's Goals** ###
- To build awareness of the brand
- To increase traffic to the site
- To provide a simple and easy shopping experience
- To provide easy and simple to understandable information
- To be visually striking to catch attention and provoke curiosity to explore the page
- To encourage advertisers to place their ads on the page

[Back to Table of contents](#table-of-contents)

---

UX DESIGN
===

### **User Stories** ###

#### **Viewing and Navigation** ####

As a **shopper**,<br>

1. I want to be able to view a list of products so that I can choose some items to purchase.
2. I want to be able to filter products that I am interested in without searching through all the products.
3. I want to be able to select individual products to see more detailed information and add the item to my shopping cart.
4. I want to be able to see any product special offers, new arrivals and available deals, taking advantage of any reduced prices shown.
5. I want to be able to see items I have placed in my shopping cart easily so that I can keep track of what I am buying
6. I want to be able to see breadcrumb navigation links to see where I am on the site easily.

#### **Registration and User Accounts** ####

As a **shopper**,<br>

7. I want to be able to register for an account to make future purchases easier.
8. I want to be able to easily log in and out of my account so that I can access my personal account information.
9. I want to be able to receive and email requireing me to verify my email account to finish account registeration.
10. I want to be able to log in and have a personal profile page containing my delivery details and order history.
11. I want to be able to save and update my delivery information on my personal profile page.

#### **Sorting and Searching** ####

As a **shopper**,<br>

12. I want to be able to sort the available products by name, price, sub-category or product type.
13. I want to be able to filter and group products for men and women.
14. I want to be able to see how many products are available based on the sorting / filtering I have applied.
15. I want to be able to search for a product by name, type or sub-category.

#### **Purchasing and Checkout** ####

As a **shopper**,<br>

16. I want to be able to easily select the size and quantity of a product when adding it to the shopping cart.
17. I want to be able to view the items in my shopping cart waiting to be purchased, seeing the sub-total, delivery costs and grand total amounts.
18. I want to be able to easily update the items in the shopping cart by changing the quantities of products or remove them from the cart.
19. I want to be able to checkout securely where I can enter my delivery and credit card payment details with confidence.
20. I want to be able to view an order confirmation page as well as receive and email order confirmation once the transaction has succeeded.

#### **Admin and Store Management** ###

As a **store owner**,

21. I want to be able to add new products to my store.
22. I want to be able to edit / update the current product details and replace the product image file.
23. I want to be able to delete a product that is no longer for sale.


[Back to contents](#contents)

---

Design
===

### **Colours** ###

I chose the colours mainly from the standard [Bootstrap Colours](https://getbootstrap.com/docs/4.0/utilities/colors/) and applied classes to the template sections as they go comfortably with the light colors of the contemporary ones Websites of shoe retailers based on this project website.
The colour schemes is created by using [Coolors](https://coolors.co/).

![Coolors.co Palette](Documentation/images/coolors_palette.png)

- *text* (#343A40) - Gunmetal
- *bg-blue* (#6DB1BF) - Maximum Blue
- *hover effects and buttons* (#6DB1BF) - Blue Crayola
- *bg-success and buttons* (#28A745) - Green Pantone
- *bg-warning and buttons* (#FFC107) - Mikado Yellow
- *text and buttons* (#DC3545) - Rusty Red

### **Wireframes** ###

I designed the site mock-ups using [Balsamiq wireframes](https://balsamiq.com/). 

- [Home Page](Documentation/wireframes/home.png)
- [User Registration](Documentation/wireframes/register.png)
- [User Log In](Documentation/wireframes/login.png)
- [My Profile](Documentation/wireframes/my-profile.png)
- [Products](Documentation/wireframes/products.png)
- [Product](Documentation/wireframes/product-page.png)
- [Admin Product Management - Add a Product](Documentation/wireframes/product-management.png)
- [Admin Product Management - Edit a product](Documentation/wireframes/edit-product.png)
- [Shopping Cart](Documentation/wireframes/shopping-cart.png)
- [Checkout](Documentation/wireframes/checkout.png)
- [Checkout Success](Documentation/wireframes/checkout-success.png)


### **Responsive Front-end Design** ###

- Responsive mobile first design using a Bootstrap v4.6 framework
- Django Template language is used to create the site's front-end dynamic content.

### **Back-end Design** ###

- The app is created using Python3 and Django framework to create an application structured using the Model-View-Controller (MVC) pattern.
- The site is deployed via a Heroku app linked to a GitHub repository.
- The dynamic content is served utilising a PostgreSQL relational database with static files and media stored on an AWS S3 bucket.

### **Site Construction** ##

#### Topology ####

- User Logged Out


![Topology - User logged out](Documentation/topology/topology_user_logged_out.png)


- User Logged In


![Topology - User logged out](Documentation/topology/topology_user_logged_in.png)


- Admin / Super User Logged In


![Topology - User logged out](Documentation/topology/topology_admin.png)

### **Database Schema** ###

![Entity-Relationship Diagram](Documentation/wireframes/db_schema.png)

#### **Fixtures JSON File creation** ####

The data set for this project was sourced from the [Fashion Product Images](https://www.kaggle.com/paramaggarwal/fashion-product-images-dataset) from www.kaggle.com.

The images needed to be curated down and were manually sorted through to a manageable number for this project and were copied into a separate folder.

The .csv file were converted into a JSON file and the products needed some manually customizing and addition information like price, discount_price, sku, size and special_offer.

[Back to contents](#contents)

---

Technologies
===

### **Languages** ###

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used to create the interactive functionality of the website
- [Python3](https://www.python.org/)
  - Used to create the main application functionality


### **Database** ###

- [PostgreSQL](https://www.postgresql.org/)
  - A powerful, open-source object-relational database.
- [sqlite3](https://www.sqlitetutorial.net/sqlite-python/)
  - Default database created with Django used for app development on localhost.

### **Libraries / Frameworks** ###

- [Bootstrap5](https://getbootstrap.com/)
  - Used to design a mobile-first responsive website layout.
- [Django](https://www.djangoproject.com/)
  - A high-level Python Web framework.
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
  - Python user authentication and login plugin for Django.
- [Stripe](https://stripe.com/en-gb)
  - Online payments platform used for the shopping basket functionality.
- [Green Unicorn (gunicorn)](https://gunicorn.org/)
  - Python WSGI HTTP Server for Unix used on the Heroku deployment.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  - PostgreSQL database adapter for Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/)
  - Python Image Library image processing capabilities.
- [sqlparse](https://pypi.org/project/sqlparse/)
  - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  - AWS SDK for Python (Boto3) used to create, configure, and manage AWS S3 services.
- [jQuery](https://jquery.com/)
  - Used for the initialisation of the Bootstrap components functionality and enhance the shopping bag functionality.
- [Django Template Language](https://docs.djangoproject.com/en/3.2/ref/templates/language/)
  - Templating language for Python.



### **Tools** ###

- [Git](https://git-scm.com/)
  - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - Used to store, host and deploy the project files and source code after being pushed from Git.
- [Gitpod](https://www.gitpod.io/)
  - An online IDE linked to the GitHub repository used for the majority of the code development.
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
  - Used for icons to enhance headings and add emphasis to text.
- [Google fonts](https://fonts.google.com/)
  - Used for the website fonts.
- [Heroku](https://www.heroku.com)
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [AWS S3](https://aws.amazon.com/s3/)
  - Amazon Simple Storage Service (Amazon S3) is an object storage service used to store the site static files
- [convertcsv](https://www.convertcsv.com/csv-to-json.htm)
  - Online CSV to JSON conversion tool
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  - The Django Secret Key Generator is used to generate a new SECRET_KEY for environment variables.
- [Balsamiq wireframes](https://balsamiq.com/)
  - An online tool to designed the site mock-ups.
- [Coolors](https://coolors.co/)
  - An online tool used to choose the website colour scheme.
- [paint.net](https://www.getpaint.net/roadmap.html)
  - Used to create the Icon, Favicon and Logo/Brand of the webpage and the database entity-relationship diagram.
- [favicon.io](https://favicon.io/)
  - Used to create the website favicons
- [Am I Responsive?](http://ami.responsivedesign.is/)
  - A tool for taking a quick snapshot of the responsive breakpoints of the website to visualize how the site will look on different device screen sizes in one place. The resulting screenshot is also used as the README.md logo image.

[Back to contents](#contents)

---

Features
===

### **User Stories Implemented** ###

| User Story ID | Features Implemented |
| --- | --- |
| 1 | The Products page shows a full list of products with a product image, name, price and sub-category labels. The products are displayed in a grid format with 4 columns on larger displays and reducing down to 1 column on mobile displays. |
| 2, 4 & 13 | The navbar allows users to filter the products by gender, sub-category and article type as well as special offers categories. The navbar menus are arranged to provide quick access to defined sorting criteria to assist the user to quickly find the types of products they want. |
| 3 | Each product image in the Products page can be clicked to open the item product page selected. The product page includes all the same information as the Products page, but includes a quantity selector and a size selector, as well as allowing the user to return to the main products page or add the item to the shopping cart. |
| 5 & 17 | The user can click the shopping cart icon in the top right corner of the navbar to be taken to the cart page where each shopping cart item is listed with a product image, product details, unit price, quantity selector and a sub-total column. A toast message pop-up window appears each time the user adds an item to the shopping basket as a secondary way to easily keep track of the items to be purchased. Delivery cost and grand total amounts are also displayed on the shopping cart page. |
| 6 | The breadcrumbs navigation links are shown just below the delivery banner in the upper left corner of the main page block. They show the current page and provide navigation links back to the Home page or other related pages. |
| 7 & 9 | Users can click the My Account link in the navbar and select Register from the dropdown menu. The user is directed to the Sign-Up page where they must enter their email address, username and a password. An email is sent to the user to verify the account email address before registration is complete.  |
| 8 | Users can click the My Account link in the navbar and select Log In from the dropdown menu. The user is directed to the Log In page where they must enter their username and a password. Once logged in, users can click the My Account link in the navbar and select Logout from the dropdown menu.  |
| 10 & 11 | Users who are logged in can click the My Account link in the navbar and select My Profile from the dropdown menu. The user is directed to the My Profile page where they can see their saved delivery details and order history records. Users can update and save their details from the My Profile page.|
| 12 | A sorting selector is available on the Products page with a number of sorting options to list the products in both ascending and descending order. |
| 14 | The products page displays the total number of products returned by the search query. |
| 15 | The navbar has a search box visible on larger displays or can be revealed when tapping the search icon on mobile displays. The user can search for a product by name, type or sub-category. |
| 16 | Users can select the size and the quantity from the individual product page when adding the item to the shopping cart. |
| 18 | Items in the shopping cart can have their individual quantities updated between 1 and 99 or remove the item if no longer needed. |
| 19 | Secure checkout and payment is provided by the integrated Stripe online credit card payment system. |
| 20 | Once an order is completed, the user is shown an order confirmation page detailing the order information, order details, delivery address and billing information. |
| 21 | Logged in store owners (admin / super users) have access to a Product Management page where new products can be added. |
| 22 & 23 | Logged in store owners (admin / super users) have access to edit and delete buttons for all products on the site. The edit button opens and edit product page where the store owner can update the product details. |

### **CRUD Functionality** ###

| Site Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| Products | | All Products | | |
| Products | | | | Delete Single Product |
| Product Page | | Single Product | | |
| Product Page | | | | Delete Single Product |
| Add Product | Add New Product | | | |
| Edit Product | | Single Product | | |
| Edit Product | | | Update Single Product | |
| Shopping Cart | | All Products | | |
| Shopping Cart | | | Update Product Quantity (Session) | |
| Shopping Cart | | | | Remove Product (Session) |
| Checkout | | All Products | | |
| Checkout | Create Order | | | |
| Checkout | Create Order Line Items | | | |
| Checkout | | User Delivery Details | | |
| Checkout | | | Update User Details | |
| Checkout | | | Update Product Quantity (Session) | |
| Checkout | | | | Remove Product (Session) |
| Sign Up | Add New User | | | |
| Log In | | User Details | | |
| Profile | | User Details | | |
| Profile | | User's Orders | | |
| Profile | | | Update Delivery Details | |


### **Messages** ###

- [Bootstrap Toasts](https://getbootstrap.com/docs/4.3/components/toasts/) are used with customised templates to show:
  - Errors - Django messages are displayed within the Toast body section with a red coloured top border of the header
  - Info - Django messages are displayed within the Toast body section with a teal coloured top border of the header
  - Success - Django messages are displayed within the Toast body section with a green coloured top border of the header
    - If the shopping cart grand total is greater than zero, the success toast also shows the user their current shopping cart contents with sub-total, delivery and grand total amounts.

### **Defensive Programming** ###

- In order to try to maintain the site security, defensive programming to prevent "brute force" loading of restricted pages was introduced.
  - At its simplest level, certain pages are removed from view unless a user is authenticated by being logged in or not.
  - Where appropriate, Python views functions are also modified by Django `@login_required` decorators to restrict user access to inappropriate pages.
  - Editing of products is restricted to super-users or admins using if...else conditions to check user authentication.


### **Additional Site Features** ###

- A set of friendly HTTP Error landing pages for site visitors to see if a requested page is unavailable or cannot be accessed.
  - The pages provide a message to the user and a button to click to return the visitor to the homepage.
  - HTTP 404, 500 & 503 errors are handled with custom templates to cover the most common events.

### **Future Features** ###

- Django Pagination to allow limiting the number of products per page to vastly improve the site performance while allowing full product inventory to be displayed across multiple pages.

- performance improvements with product image loading by replacing .jpg image media files with .webp versions to reduce the network payload by around 50% for mobile devices.

- Account user registration using social media accounts such as Google, Facebook or LinkedIn.

- Additional tables for stock inventory control to create dynamic updates of the available sizes, stock quantities and In Stock / Out of Stock indicators.

- Discount codes functionality within the checkout app with a database table codes and validity from / to date ranges.

- More product categories like cleaning and care products or accessories for shoes


[Back to contents](#contents)

---

Testing
===

- Testing information can be found in a separate [TESTING.md](TESTING.md) file.


[Back to contents](#contents)

---
Bugs
===

Bug description

[Back to contents](#contents)

---

Deployment
===

The website was developed using Gitpod and using Git pushed to GitHub, which hosts the repository.

### **Cloning Milestone Project 4 from GitHub** ###

#### **Prerequisites** ###

Ensure the following are installed locally on your computer:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control

*Please ensure you have an account created at [Stripe](https://stripe.com/gb) in order to use the online payment processing for the checkout app.*

#### **Cloning the GitHub repository** ####

- navigate to [Puksrevolution/milestone-project-4](https://github.com/Puksrevolution/milestone-project-4) GitHub repository.
- Click the **Code** button
- **Copy** the clone url in the dropdown menu
- Using your favourite IDE open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone milestone-project-4:

```Python
git clone https://github.com/Puksrevolution/milestone-project-4.git
```


#### **Creation of a Python Virtual Environment** ####


*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html) to understand how to create a virtual environment.*


#### **Install the App dependencies and external libraries** ####

- In your IDE terminal window, install the dependencies from the requirements.txt file with the following command:

```Python
pip3 install -r requirements.txt
```


#### **Create the database in sqlite3** ####

The installaton of the requirements.txt file will initialise the sqlite3 development database locally.

Run the following commands to create the database tables:

- Check there are no changes to the models already configured.

```Python
python3 manage.py makemigrations --dry-run
```

- Check which migrations will be applied.

```Python
python3 manage.py migrate --plan

```

- Apply the migrations.

```Python
python3 manage.py migrate
```

Load the fixtures files into the database in the following order:

```Python
python3 manage.py loaddata gender
python3 manage.py loaddata category
python3 manage.py loaddata sub_category
python3 manage.py loaddata article_type
python3 manage.py loaddata special_offer
python3 manage.py loaddata products
```

#### **Create .env file** ####

- Import and initialise environ in settings.py.
  - A helpful guide can be found [here](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)
- The .env file should contain at least the following information:

```Python
DEVELOPMENT=True
SECRET_KEY=[YOUR SECRET KEY]
STRIPE_PUBLIC_KEY=[YOUR STRIPE PUBLIC KEY]
STRIPE_SECRET_KEY=[YOUR STRIPE SECRET KEY]
STRIPE_WH_SECRET=[YOUR STRIPE WEBHOOK SECRET KEY]
```

- Please ensure you add in your own `SECRET_KEY`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`  and `STRIPE_WH_SECRET` values.
- The Stripe keys can be found in the Developers section under API Keys and Webhooks of your [Stripe Account](https://stripe.com/gb)
- ***Important:*** Add the `.env` file to your `.gitignore` file before pushing your files to any public git repository.


#### **Run the application locally** ####

- To run the application, enter the following command into the terminal window:

```Python
python3 manage.py runserver
```

### **Deploying milestone-project-4 app to Heroku** ###

#### **Creating the Heroku app** ####

*Please ensure you have an account created at [Heroku](https://signup.heroku.com/login) in order to deploy the app.*

- Log in to your Heroku account dashboard and create a new app.
- Enter the App name.
  - This needs to be unique.
- Choose a geographical region closest to where you live.
  - Options available on a free account are ***United States*** or ***Europe***


#### **Adding a PostgreSQL database to Heroku** ####

- Select the **Resources** tab on your Heroku app dashboard
- Select `Heroku Postgres` as a new add-on with a Plan name of `Hobby Dev - Free`
- Heroku will build the PostgresQL database instance and add a config variable automatically.


#### **Load the data into PostgreSQL** ####

- Add the following variable to the `.env` file:
```Python
DATABASE_URL=[YOUR POSTGRESQL DATABASE URL FROM HEROKU CONFIG VARS]
```

- Apply the migrations to the Heroku PostgreSQl database tables.

```Python
python3 manage.py migrate
```

- Load the fixtures files into the PostgreSQL database in the following order:

```Python
python3 manage.py loaddata gender
python3 manage.py loaddata category
python3 manage.py loaddata sub_category
python3 manage.py loaddata article_type
python3 manage.py loaddata special_offer
python3 manage.py loaddata products
```

### **Push your repository to GitHub** ###
 - In the Heroku App Settings page, open the section Config Vars
 - Add all the environmant variables from your local `.env` file into the Heroku Config Vars:

| Key | Value |
| --- | --- |
| SECRET_KEY | [YOUR SECRET KEY] |
| STRIPE_PUBLIC_KEY | [YOUR STRIPE PUBLIC KEY] |
| STRIPE_SECRET_KEY | [YOUR STRIPE SECRET KEY] |
| STRIPE_WH_SECRET | [YOUR STRIPE WEBHOOK SECRET KEY] |
| DATABASE_URL | [YOUR POSTGRESQL DATABASE URL] |
| EMAIL_HOST_PASS | [YOUR GMAIL APP SIGN IN PASSWORD] |
| EMAIL_HOST_USER | [YOUR ORDER CONFIRMATION EMAIL ADDRESS FROM GMAIL]

- In the Heroku App Deploy page:
  - Select GitHub from the Deployment Method options.
  - Select Connect to GitHub.
  - Log in to your GitHub account from Heroku to link the App to GitHub.
  - Search for and select the repository to be linked in GitHub.
  - Select Connect.
  - Select Enable Automatic Deployment from the GitHub Master / Main branch.

#### **Launch the app** ####

- Click Open App in Heroku to launch the App in a new browser window.

***Note: The static files served from GitHub will be much slower to load than running locally. It is recommended to copy the static files to an online service such as an AWS S3 Bucket and connect this to Heroku.***


[Back to contents](#contents)

---

Credits
===

### **Images** ###

- **Product Images**
  - [Dataset: E-commerce Product Images](https://www.kaggle.com/vikashrajluhaniwal/fashion-images)
    - Credit: vikashrajluhaniwal @ www.kaggle.com
    - The dataset consists of 2906 images and associated one .csv data files containing the product information.

- **Home Page**
  - All homepage images were source as free to use from pixabay.com under their [license agreement](https://unsplash.com/license)
  - [Woman Fashion](https://pixabay.com/de/photos/schuhe-frau-kleidung-frauen-mode-285331/) - Photo by [smilenesita](https://pixabay.com/de/users/smilenesita-164334/) on [Pixabay](https://pixabay.com/)
  - [Brown Shoes](https://pixabay.com/de/photos/braune-schuhe-schn%c3%bcrschuhe-1150071/) - Photo by [Free-Photos](https://pixabay.com/de/users/free-photos-242387/) on [Pixabay](https://pixabay.com/)
  - [Shoes](https://pixabay.com/vectors/shoe-shoes-boot-boots-sneakers-4791312/) - Photo by [TJFREE](https://pixabay.com/users/tjfree-9771479/) on [Pixabay](https://pixabay.com/)

- **Favicon**
   - The Favicon image were source as free to use from pixabay.com under their [license agreement](https://unsplash.com/license)
  - [Shoe Prints](https://pixabay.com/de/vectors/fu%c3%9fabdr%c3%bccke-m%c3%a4nner-druckt-schuhe-151189/) - Photo by [OpenClipart-Vectors](https://pixabay.com/de/users/openclipart-vectors-30363/) on [Pixabay](https://pixabay.com/)
  

Acknowledgements
===

- [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/) Course material - in particular the Boutique Ado Django mini project
- [Simon Vardy](https://github.com/simonjvardy) for code snippets and README.md content.
- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) Documentation and code snippets used to build most of the templates
