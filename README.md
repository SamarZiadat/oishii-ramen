<h1  align="center">oishii ramen</h1>

[View the live project here](https://oishii-ramen.herokuapp.com/)

'oishii ramen' is a project designed and created for a fictional Japanese cookery course provider in Glasgow, Scotland. The Japanese word 'oishii' means 'delicious' or 'tasty' in English. The project functions as a website that provides details on the business and cookery courses that it facilitates on its premises. 

The website can be used by general users to view information on these courses, such as a description of the course and the skill level advised for attendees. Users can also sign up for the website, which provides them with additional functionality, such as the ability to manage their course bookings and leave reviews.

Staff at oishii ramen can use the admin login of the website to draft and publish courses, remove courses, approve user reviews, timetable the courses, and confirm/approve bookings for timetabled courses depending on available capacity.

![Responsive mockup](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/responsive-mockup.png?raw=true)

## Table of Contents
- [User Experience Design (UX)](https://github.com/SamarZiadat/oishii-ramen#user-experience-design-ux)
	 -   [The Strategy Plane](https://github.com/SamarZiadat/oishii-ramen#the-strategy-plane)
		    -   [Agile Project Management](https://github.com/SamarZiadat/oishii-ramen#agile-project-management)
		    -   [User Stories](https://github.com/SamarZiadat/oishii-ramen#user-stories)
	-   [The Scope Plane](https://github.com/SamarZiadat/oishii-ramen#the-scope-plane)
	-   [The Structure Plane](https://github.com/SamarZiadat/oishii-ramen#the-structure-plane)
	    -   [Features](https://github.com/SamarZiadat/oishii-ramen#features)
	    -   [Future Features](https://github.com/SamarZiadat/oishii-ramen#future-features)
	-   [The Skeleton Plane](https://github.com/SamarZiadat/oishii-ramen#the-skeleton-plane)
	    -   [Wireframes](https://github.com/SamarZiadat/oishii-ramen#wireframes)
	    -   [Database Design](https://github.com/SamarZiadat/oishii-ramen#database-design)
	    -   [Security](https://github.com/SamarZiadat/oishii-ramen#security)
	-   [The Surface Plane](https://github.com/SamarZiadat/oishii-ramen#the-surface-plane)
	    -   [Design](https://github.com/SamarZiadat/oishii-ramen#design)
	        -   [Colour Scheme](https://github.com/SamarZiadat/oishii-ramen#colour-scheme)
	        -   [Typography](https://github.com/SamarZiadat/oishii-ramen#typography)
	        -   [Imagery](https://github.com/SamarZiadat/oishii-ramen#imagery)
	-   [Technologies](https://github.com/SamarZiadat/oishii-ramen#technologies)
	-   [Testing](https://github.com/SamarZiadat/oishii-ramen#testing)
	-   [Deployment](https://github.com/SamarZiadat/oishii-ramen#deployment)
	    -   [Version Control](https://github.com/SamarZiadat/oishii-ramen#version-control)
	    -   [Heroku Deployment](https://github.com/SamarZiadat/oishii-ramen#heroku-deployment)
	    -   [Run Locally](https://github.com/SamarZiadat/oishii-ramen#run-locally)
	    -   [Fork Project](https://github.com/SamarZiadat/oishii-ramen#fork-project)
	-   [Credits](https://github.com/SamarZiadat/oishii-ramen#heroku-credits)
	    -   [Content](https://github.com/SamarZiadat/oishii-ramen#content)
	    -   [Acknowledgements](https://github.com/SamarZiadat/oishii-ramen#acknowledgements)

## User Experience Design (UX)

### The Strategy Plane

#### Agile Project Management

This project was managed using agile methodologies by delivering small features in incremental sprints. There were 4 sprints in total, spaced out evenly over four weeks. A kanban board was created using github projects and was utilised as a project management tool to help visualise work, limit work-in-progress, and maximise efficiency/flow. The Kanban board can be viewed [here](https://github.com/SamarZiadat/oishii-ramen/projects). 

Acceptance criteria was created in relation to each of the user stories. These stories were then assigned to an epic, and prioritised with the labels 'must have', 'should have' or 'could have'. All stories were organised within sprints, and acceptance criteria was completed in order of: 'must have' , then 'should have', and finally "could have". This approach was taken in order to ensure that all core requirements were definitely delivered, with the nice to have features implemented in an iterative way according to capacity.

[IMAGE OF KANBAN]

#### User Stories

-   US01: Illustrate purpose of application through UI
    -   As a  **Site User**  I can  **view the home page**  so that  **clearly understand the application purpose**
-   US02: Navigate
    -   As a  **Site User**  I can  **use the navigation bar**  so that  **I can easily easily navigate the application **
-   US03: View courses
    -   As a  **Site User**  I can  **view the courses available**  so that  **I can explore them in more detail**
-   US04: View course information
    -   As a  **Site User**  I can  **click on a course**  so that  **I can learn more about it**
-   US05: Book a course
    -   As a  **Site User**  I can  **book a timetabled course**  so that  **I can reserve places for myself and those accompanying me**
-   US06: View my booked courses
    -   As a  **Site User**  I can  **access a list of courses I have booked on to**  so that  **I can see the upcoming courses I have booked to attend**
-   US07: Cancel a booking
    -   As a  **Site User**  I can  **cancel an upcoming course I have booked onto**  so that  **my place can be reserved by someone else**
-   US08: Review a course
    -   As a  **Site User**  I can  **attach a review to a course**  so that  **I can give feedback and be involved in the community of attendees**
-   US09: View reviews
    -   As a  **Site User**  I can  **view reviews on individual courses**  so that  **I can make an informed decision on whether I would like to attend this course**
-   US10: Approve reviews
    -   As a  **Site Admin**  I can  **assess and then approve or disapprove reviews**  so that  **inappropriate content can be filtered out**
-   US11: Account registration and login
    -   As a  **Site User**  I can  **register for an account**  so that  **I can log in and then book a course, , view my upcoming and past bookings, and leave reviews on courses**
-   US12: Manage courses
    -   As a  **Site Admin**  I can  **create, read, update and delete courses and their timetables**  so that  **I can manage course details and availability**
-   US13: Create course drafts
    -   As a  **Site Admin**  I can  **create drafts for courses**  so that  **I can finish producing the content at a later date and publish once approved**
-   US14 Approve bookings
    -   As a  **Site Admin**  I can  **view and then approve or disapprove bookings**  so that  **course capacity can be managed**
-   US15 View past courses
    -   As a  **Site User**  I can  **access a list of past courses that I booked**  so that  **I can track courses I have completed**

### The Scope Plane

-   Home page with app information
-   Responsive Design - the app should be fully functional on all devices from 320px up
-   Hamburger menu for devices with a smaller viewport devices
- Ability to perform CRUD functionality on reservations
-   Restricted role based features

### Design

#### Wireframes

#### Entity-Relationship diagram for DBMS

Notes on the ER diagram:  
-   The ER diagram provided shows the logical data model. 
- The Users table in the ER diagrams is also a logical representation of the data captured during user registration and how it relates to the application data model. The Users table itself is not declared in the models.py file, but is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

![DBMS diagram](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/dbms-diagram.png?raw=true)

#### Logo
I used logo.com to generate a logo for
#### Colour Scheme
#### Typography


## Testing

### Validator Testing
- [HTML Validator](https://validator.w3.org/)
As this project uses Django templates the html has been validated by manually clicking through the application pages, copying the source of the rendered pages and then validating this version of the html using the W3C Validator (link shown above). To validate the HTML files all Django template tags were manually removed with the HTML code copied and inserted to the base template, including manually pasting in navigation and footer templates into all page testing.

     - Index Page:![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/index-html-summary.png?raw=true)
      -   Course Detail Page:![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/coursedetail-html-summary.png?raw=true)
       -   Bookings Page:
![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/mybooking-html-summary.png?raw=true)
        -   Course Add Page:
![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/courseadd-html-summary.png?raw=true)
         -   Edit Course Page:
![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/editcourse-html-summary.png?raw=true)

        -   Course Delete Confirmation Page:
![testing summary](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/deleteconfirm-html-summary.png?raw=true)

- [CSS Validator](https://jigsaw.w3.org/css-validator/)
The W3C CSS Validator Services were used to validate the CSS to ensure there were no errors. There was one warning that read: "Imported style sheets are not checked in direct input and file upload modes", which is fine as it's referring to a google fonts import.

	- Result summary:
![CSS validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/css-validation.png?raw=true)

- [Javascript Validator](https://jshint.com/):
JSHint was used to validate the JavaScript with no errors highlighted.
	- Result summary:
![JSHint validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/jshint-validation.png?raw=true)

- [PEP 8 Python Linter](https://pep8ci.herokuapp.com/):
PEP 8 Online linter (Python validator). The code passed without any errors on all files tested:

- Project settings.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-settings.png?raw=true)
- Project urls.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-orurls.png?raw=true)
- Application urls.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-projecturls.png?raw=true)
- admin.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-admin.png?raw=true)
- test_admin.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-test-admin.png?raw=true)
- forms.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-forms.png?raw=true)
- test_forms.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-test-forms.png?raw=true)
- models.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-models.png?raw=true)
- test_models.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-test-models.png?raw=true)
- views.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-views.png?raw=true)
- test_views.py result summary:
![PEP 8 validation image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/pythonlinter-test-views.png?raw=true)

### Automated Testing

-   [Jest](https://jestjs.io/)  was used to test the application javascript and jQuery code. The functionality tested was the code to fade out, slide up and remove any raised alert messages after a 5 second delay. The code is located in [Script JS](https://github.com/SamarZiadat/oishii-ramen/blob/main/static/js/script.js), the test is located in  [Test JS](https://github.com/SamarZiadat/oishii-ramen/blob/main/static/js/tests/script.test.js). 

- By installing the Jest framework and using the npm test command the following test suites were completed:
![Jest testing](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/jest-testing.png?raw=true)

-   [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/)  and Django TestCase was used to create automatic tests for Python files. The test reporting tool ’Coverage’ was installed to show the percentage of Python code that’s been covered by tests.
    
-   A total of 25 tests were written for the following files :
    
    -   [forms.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/forms.py)  test file:  [test_forms.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_forms.py)
    -   [models.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/models.py)  test file:  [test_models.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_models.py)
    -   [views.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/views.py)  test file:  [test_views.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_views.py)
    -   [admin.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/admin.py)  test file:  [test_admin.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_admin.py)  (tests were added for the customizations made to the django admin functionality)
-   Django test results and coverage:
![enter image description here](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/coverage-django-testing.png?raw=true)
## Deployment

### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘oishii-ramen’.

The following git commands were used throughout development to push code to the remote repo:

`git add <file>`  - This command was used to add the file(s) to the staging area before they are committed.

`git commit -m “commit message”`  - This command was used to commit changes to the local repository queue ready for the final step.

`git push`  - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

-   Navigate to heroku and create an account
-   Click the new button in the top right corner
-   Select create new app
-   Enter app name
-   Select region and click create app
-   Click the resources tab and search for Heroku Postgres
-   Select hobby dev and continue
-   Go to the settings tab and then click reveal config vars
-   Add the following config vars:
    -   SECRET_KEY: (Your secret key)
    -   DATABASE_URL: (This should already exist with add on of postgres)
    -   EMAIL_HOST_USER: (email address)
    -   EMAIL_HOST_PASS: (email app password)
    -   CLOUNDINARY_URL: (cloudinary api url)
-   Click the deploy tab
-   Scroll down to Connect to GitHub and sign in / authorize when prompted
-   In the search box, find the repositoy you want to deploy and click connect
-   Scroll down to Manual deploy and choose the main branch
-   Click deploy

The app should now be deployed.

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

-   Click on the code drop down button
-   Click on HTTPS
-   Copy the repository link to the clipboard
-   Open your IDE of choice (git must be installed for the next steps)
-   Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

-   Navigate to the GitHub Repository you want to fork.
    
-   On the top right of the page under the header, click the fork button.
    
-   This will create a duplicate of the full project in your GitHub Repository.
   

