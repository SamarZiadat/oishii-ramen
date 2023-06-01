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
	-   [The Surface Plane](https://github.com/SamarZiadat/oishii-ramen#the-surface-plane)
	    -   [Design](https://github.com/SamarZiadat/oishii-ramen#design)
	-   [Technologies](https://github.com/SamarZiadat/oishii-ramen#technologies)
	-   [Testing](https://github.com/SamarZiadat/oishii-ramen#testing)
	-   [Deployment](https://github.com/SamarZiadat/oishii-ramen#deployment)
	-   [Credits](https://github.com/SamarZiadat/oishii-ramen#heroku-credits)

## User Experience Design (UX)

### The Strategy Plane

#### Agile Project Management

This project was managed using agile methodologies by delivering small features in incremental sprints. There were 4 sprints in total, spaced out evenly over four weeks. A kanban board was created using github projects and was utilised as a project management tool to help visualise work, limit work-in-progress, and maximise efficiency/flow. The Kanban board can be viewed [here](https://github.com/SamarZiadat/oishii-ramen/projects). 

Acceptance criteria was created in relation to each of the user stories. These stories were then assigned to an epic, and prioritised with the labels 'must have', 'should have' or 'could have'. All stories were organised within sprints, and acceptance criteria was completed in order of: 'must have' , then 'should have', and finally "could have". This approach was taken in order to ensure that all core requirements were definitely delivered, with the nice to have features implemented in an iterative way according to capacity.

![Image of Kanban](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/kanban.png?raw=true)

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
- Ability to perform CRUD functionality
-   Restricted role based features

### The Structure Plane

#### Features

**F01 Navigation Bar**
    
 The navigation bar has a consistent look and placement each page supporting easy and intuitive navigation. It includes a Logo and links. If the user is not signed in then links available are the Home, Sign up and Sign in pages. If a user is signed in then the links available are the Home, Bookings and Sign out pages. If a staff (admin) user is signed in, the links available are all links available to a user with the addition of the Add Course link.
    
The navigation bar is responsive on multiple screen sizes - on smaller screens it coverts to a 'burger' menu style. When a user is logged in, they are notified which account they are signed in with by their name appearing in the navigation bar.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-default-nav.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-nav-user.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-nav-admin.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-hamburger-nav.png?raw=true)

**F02 Landing page image and text**

At the top of the landing page (Home page) there is an area that includes a photograph and a text overlay which together clearly identify the purpose of the site as a place to find and book Japanese culinary courses in Glasgow, Scotland. There is also a call-to-action button that directs the user to the Sign Up page. 

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-landing-image.png?raw=true)

**F03 Course Summaries**

Further down on the landing page is a list of course summaries. Each summary includes an image, the course title, details on cost and course duration, and easy to read badges outlining the skill-level requirements for the course - beginner/intermediate/advanced. At a glance the user can decide quickly if this is a course that might appeal to them and be suitable to them. To keep the page uncluttered, summaries are limited to a maximum of 6 per page, with pagination available when more than 6 courses exist.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-landing-summaries.png?raw=true)

**F04 Course Detail Page**

When a user clicks on a course summary title on the landing page they are brought to the Course Detail page for the clicked course. Here the user is shown a full description of the course and all of the approved reviews for the course which are listed in order most recent first. Only users who are signed in can review a course or book a timetabled course. Staff (admin) users are the only users who can delete or edit a course.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-course-detail.png?raw=true)

**F05 Review a Course**

In order to review a course a user must be signed in. A review can be added on any Course Detail page. The user enters their review in a text box and clicks on a button to submit. The review must be approved by a staff (admin) user before it will be visible on the Course Detail page.

To approve reviews the admin user logs in to the admin pages, opens the Reviews table, selects the review(s) to be approved, chooses the 'Approve reviews' action from the drop-down menu and clicks 'Go'. Alternatively, they can be approved one at a time by clicking on the review row to open it, updating the value in the approved field and saving the update.

All comments approved for a course are shown on that course's Course Detail page in the order of newest first.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-course-review-and-booking.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-admin-review.png?raw=true)

**F06 Book a Course**

In order to book a course a user must be signed in. A course can be booked from its Course Detail page. The user selects a course date/time from the drop-down list of scheduled courses and can choose a number 1 to 5 to indicate how many people they want included on their booking. Then the user clicks on the Book button to complete the booking and get re-directed to their Bookings page to see all of their upcoming and past bookings.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-course-review-and-booking.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-admin-approve-booking.png?raw=true)

**F07 Edit a Course**

In order to edit a course a user must be signed in and that user must be a staff (admin) user. A course can be edited from its Course Detail page. The staff user selects the 'Edit Course' link, which directs them to the 'Edit Course' page (the 'Edit Course' link and page can only be viewed by staff users). 

On the 'Edit Course' page, the staff user is given the option to edit any information about the course via a form. If they decide not to edit the course, they can click the 'Cancel' button, which redirects them back to the Course detail page. If they do decide to make changes and are happy with their changes, they can click the 'Confirm' button. When they click the 'Confirm' button, the edits save, they are redirected to the updated Course Detail page, and a success message appears as an alert confirming that changes were made.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-edit-delete-course.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-edit-course.png?raw=true)

**F08 Delete a Course**

In order to delete a course a user must be signed in and that user must be a staff (admin) user. A course can be deleted from its Course Detail page. The staff user selects the 'Delete Course' link, which directs them to the 'Delete Course Confirm' page (the 'Delete Course' link and page can only be viewed by staff users). 

On the 'Delete Course Confirm' page, the staff user provided with a form that asks them to confirm if they would like to delete the course. If they confirm by clicking the 'Delete' button, the course deletes, they are redirected to the landing page, and a success message appears as an alert confirming the deletion.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-edit-delete-course.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-confirm-deletion.png?raw=true)

**F09 Add a Course**

In order to add a course a user must be signed in and that user must be a staff (admin) user. A course can be added from any page on the website. In order to add a course, the staff user selects the 'Add Course' link from the navigation bar, which directs them to the 'Add Course' page (the 'Add Course' link and page can only be viewed by staff users). 

On the 'Add Course' page, the staff user is provided with a form to add all necessary information about the course. If they decide not to add a course, they can click the 'Cancel' button, which redirects them back to the landing page. If they do decide to add a course and fill in all required fields, they can click the 'Confirm' button. 

When they click the 'Confirm' button, the course is added, they are redirected to the landing page, and a success message appears as an alert confirming that the course was added. This course is added a draft course, and so will not appear on the landing page until it is 'published' via the Django admin pages.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-add-course.png?raw=true)
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-publish-course.png?raw=true)

**F10 Bookings Page**

In order to access the Bookings page a user must be signed in. The Bookings page provides a convenient place for the user to quickly view their upcoming and past bookings. By clicking on the image associated with the booking the user can go to the Course Detail page for the course. The booking also shows the number of people the booking is for and whether or not the booking has been confirmed/approved.

If the logged in user is a staff (admin) user, then they have permissions to view all booking made by all users in one easy location. This allows staff to have a quick overview of all the bookings that have been made, and which bookings they still need to approve.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-bookings-page.png?raw=true)

**F11 Cancel a Course Booking**

The Booking page can only be viewed by logged in users. In order for a user to cancel a course booking that they made, the user that booked the course must be signed in. They can view the course booking on the Bookings page and cancel by clicking on the 'Cancel' button associated with the booking. The user will be prompted to confirm that they really want to cancel, to prevent them accidentally deleting their booking. Bookings with a timetabled date set in the past cannot be cancelled.

If a staff (admin) user would like to cancel a booking made by any user, they must be first signed in as a staff user. They can view all course bookings made by all users on the Bookings page and cancel by clicking on the 'Cancel' button associated with the booking. They will be prompted to confirm in the same way as outlined above, and also cannot cancel bookings that have a timetabled date set in the past.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-cancel-booking.png?raw=true)

**F12 User authentication**

The application provides the following user authentication related functions :

-   User Sign up
    
    -   A user needs to be registered before they can sign in. The option to 'Sign up' appears on the navigation bar when no user is currently signed in. To sign up, the user needs to provide a) a username which has not already been registered, b) an optional email address and c) a password which they must enter. Once registered a user can sign in.
    
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-signup.png?raw=true)

- User Sign in
	-   Once registered a user can sign in. To sign in the user must provide a) a registered username and b) the password for the username. Once signed in they will have access to extra functionality, namely :
	    -   can review a course
	    -   can book courses
	    -   can cancel courses
	    
![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-signin.png?raw=true)

- User Sign out
	-   A signed in user can Sign out by clicking on the 'Sign out' link on the navigation bar. The user simply needs to confirm the action by clicking on the Sign out button on the page.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-signout.png?raw=true)

**F13 Add a Timetable for a Course**

The admin user adds timetables for courses by using Django admin pages. To add a new date/time for a course the admin user can use the '+ Add' link for the Timetable table. To fill in the data fields a course needs to be selected from the drop-down list of existing courses and a date and time needs to be specified.

Once a new timetable for a course is added it becomes available for booking on that course's Course Detail page (as long as the date/time assigned to the course is not in the past).

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-add-timetable.png?raw=true)

**F14 On-screen Messages**

To enhance usability of the application, user messages appear on-screen to confirm when certain actions have happened or report on problems. For successful operations, a message will appear at the top of the screen and then fade-out/slide-up after 5 seconds.

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-messages.png?raw=true)

**F15 Footer**

The Footer is present on all pages of the website, featured at the bottom. On the left-hand side there a greyscale version of the logo, in the middle are the business' contact details and address, and to the right are the business' social media links. 

![Feature image](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/features/feature-footer.png?raw=true)

#### Future Features
Features which could be implemented in the future:

-   **Develop custom JavaScript modals**
    
    Dialogs that ask users to confirm their actions, such as confirming that they would like to sign out or delete a booking, are currently very basic and could be improved to have a modal format consistent with the application's UI.
    
-   **Improve UI with intuitive timetable calendar**
    
    Ideally the selection of booking dates and times would use a more sophisticated and intuitive visual calendar with available days and times selectable and colour-coded.
    
-   **Add course capacity handling functionality**

    Ensuring that bookings do not exceed capacity is currently handled by requiring that the staff (admin) user to approve bookings via the Django admin. This could be improved by including a capacity limit field in the timetable table and adding logic to calculate remaining spaces available as part of data validation on booking.
    
-   **Continue to build custom front-end for admin functionality**

    The overall look and feel of the Django admin pages is not consistent with the rest of the app. Reliance on Django admin pages could be eliminated with continued work on front-end and crud for staff (admin) users.

- **Introduce verified reviews**
	
	Currently there is no logic to check whether a reviewer of a course has actually taken the course. Developing a method to check this and then label the reviewer/their review with a 'Verified Student' label would an option.
    
## The Skeleton Plane

### Wireframes

At the beginning of this project and as a part of the planning process, wireframes were created using Balsamiq. The wireframes were used to get a basic idea of how the site might look when finished, both on desktop and mobile devices.

Wireframes were created for the following pages and features:

- **Home page:**
![Wireframe](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/wireframe-home.png?raw=true)

- **Course Detail page:**
![Wireframe](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/wireframe-course-detail.png?raw=true)

- **Booking page:**
![Wireframe](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/wireframe-booking.png?raw=true)

### Database Design

**Entity-Relationship diagram for DBMS**

Notes on the ER diagram:  
-   The ER diagram provided shows the logical data model. 
- The Users table in the ER diagrams is also a logical representation of the data captured during user registration and how it relates to the application data model. The Users table itself is not declared in the models.py file, but is handled by the django modules and this logical view does not reflect all columns and constraints etc. used by the physical data tables in the database.

![DBMS diagram](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/dbms-diagram.png?raw=true)

## The Surface Plane

### Design 

A brand board was created for this project:

![Brand Board](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/brand-board.png?raw=true)

- **Colour Scheme**

	The colour scheme for was chosen with Japanese culture in mind, as this app is built for booking Japanese culinary courses. The colour scheme was also chosen with a focus on accessibility and contrast. The colours of red and white were decided on, and then the exact hex colours and colour scheme were created by the https://coolors.co/ colour scheme generator.

- **Logo**

	The logo was created with the [logo.com](https://logo.com/) logo generator. I selected the typography, colour scheme, and icon, and then the generator created variations of this logo, which were used through the website and as the favicon.

- **Typography**

	Carter One Regular was used as the logo font, as it both fit the theme for the business and was clearly legible but interesting. Cantarell was imported from [Google Fonts](https://fonts.google.com/specimen/Cantarell/about) as the website's main font, as it is both a highly legible font. I also found that Cantarell is similar to, but more intriguing than, sans-serif (the backup font for the website).

- **Imagery**

	The images chosen for the website were sourced from free stock image provider Pexels, with a heavy dependence on a collection by [Katerina Holmes](https://www.pexels.com/@katerina-holmes/). Images from this collection, and any other images from Pexels, were chosen for their fresh but muted quality and the subject matter of the app.

## Technologies

### Languages:

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JQuery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks and Libraries:

-   [Bootstrap:](https://getbootstrap.com/)  Bootstrap CSS Framework used for styling and to build responsive web pages.
-   [Cloudinary:](https://cloudinary.com/)  Used to store all static files.
-   [Coverage:](https://coverage.readthedocs.io/en/latest/index.html)  Used for measuring code coverage of Python test files.
-   [Django:](https://www.djangoproject.com/)  Main Python framework used in the development.
-   [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html)  Used for authentication and account registration.
-   [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)  Used to simplify the rendering of Django forms.
-   [dj_database_url:](https://pypi.org/project/dj-database-url/)  Used to allow database urls to connect to the postgres database.
-   [Gunicorn:](https://gunicorn.org/)  Green Unicorn, used as the Web Server to run Django on Heroku.
-   [Jest:](https://jestjs.io/)  A JavaScript Testing Framework, used for automated tests.
-  [jQuery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js)  used to fade out alert messages
-   [psycopg2:](https://pypi.org/project/psycopg2/)  Used PostgreSQL database adapter.
- [pytest-black](https://pypi.org/project/pytest-black/): To enable automatic and continual format checking with black during development
-   [Summernote:](https://github.com/summernote/django-summernote)  To provide a WYSIWYG editor for customizing new blog content and add images.

### Software and Web Applications:

-   [Balsamiq:](https://balsamiq.com/)  Used to create the wireframes.
-   [Chrome DevTools:](https://developer.chrome.com/docs/devtools/)  Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
- [Coolers](https://coolors.co/): Used to generate the app's colour scheme.
- [dbdiagram.io](https://dbdiagram.io/home) : Used to create the Entity Relationship diagrams for the application data model.
-   [Font Awesome:](https://fontawesome.com/)  Used throughout the site to add icons for aesthetic and UX purposes.
-   [Git:](https://git-scm.com/)  Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub:](https://github.com/)  GitHub is used to store the projects code after being pushed from Git and to create the Kanban board used for this project.
-   [Google Fonts:](https://fonts.google.com/)  To import font which is used throughout the site. Added fallback font.
- [Logo.com](https://logo.com/): Used to generate the logo.
- [Tech Sini](https://techsini.com/multi-mockup/): Used to generate the mockup of the final website on several apple devices.
-   [Heroku:](https://www.heroku.com/)  For deployment and hosting of the application.
-   [ElephantSQL:](https://www.elephantsql.com/): Configured and optimise the PostgreSQL database used for this application.
-   [HTML Validator:](https://validator.w3.org/)  Check your code for HTML validation.
-   [JSHint:](https://jshint.com/)  Check code for JavaScript validation.
-   [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/)  Check your code for CSS validation.

## Testing

### Browser Compatibility
Chrome DevTools was used to test the responsiveness of the application on different screen sizes. In addition, testing has been carried out on the following browsers:
-   Chrome Version 107.0.5304.87
-   Edge Version 107.0.1418.24
-   Firefox Version 94.0.1
-   Safari on macOS (Safari Version 15.6)

### Validator Testing
- [HTML Validator](https://validator.w3.org/):
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

- [CSS Validator](https://jigsaw.w3.org/css-validator/):
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

-   [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/)  and Django TestCase was used to create automatic tests for Python files. A total of 25 tests were written for the following files:
    
    -   [forms.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/forms.py)  test file:  [test_forms.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_forms.py)
    -   [models.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/models.py)  test file:  [test_models.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_models.py)
    -   [views.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/views.py)  test file:  [test_views.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_views.py)
    -   [admin.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/admin.py)  test file:  [test_admin.py](https://github.com/SamarZiadat/oishii-ramen/blob/main/booking/test_admin.py)  (tests were added for the customizations made to the django admin functionality)
    
-   The Django's test reporting tool '[Coverage](https://coverage.readthedocs.io/en/7.2.7/)' was installed to show the percentage of Python code that’s been covered by tests:
![enter image description here](https://github.com/SamarZiadat/oishii-ramen/blob/main/documentation/testing/coverage-django-testing.png?raw=true)

### User Stories Testing

To further ensure this application is working correctly and functions as expected, manual testing was also performed. User Stories were tested successfully to verify that all acceptance criteria was met by the application features.

- **US01: Illustrate purpose of application through UI**

	As a  **Site User**  I can  **view the home page**  so that  **clearly understand the application purpose**
	
	- Acceptance Criteria:**
		-   Suitable graphics on screen
		-   Text on screen briefly introducing the application purpose
		-   Navigation items on screen clearly labelled with their function

	- I have tested:
		-   That suitable images were used throughout the website
		-   That the text on landing page suitably introduces the application purpose
		-   That the navbar nav-items were clearly labelled with their function

- **US02: Navigate**

	As a  **Site User**  I can  **use the navigation bar**  so that **I can easily easily navigate the application **
	- Acceptance Critera:
		-   Navigation menu available at the top of each screen with either the items listed across the screen or accessible via a "hamburger" menu on smaller screen sizes.
		-   Consistent menu style across each of the pages available to the site user
		-   Clear indication on screen of the page/function the user is currently accessing
		
	- I have tested:
		-   That the navbar is available at the top of each screen with either the items listed across the screen or accessible via a "hamburger" menu on smaller screen sizes
		-   That navigation.html is loaded in the base.html, and that all pages extend base.html, so menu is consistent in style and function on every page
		-   All pages have a clear page title that describes the page function the user is currently accessing

- **US03: View Courses**

	As a  **Site User**  I can  **view the courses available**  so that  **I can explore them in more detail**

	- Acceptance Criteria:
		-   all published courses can be viewed
		-   Image, title, skill level, date and start time shown on screen for each course

	- I have tested:
		- That all published courses can be viewed on landing summaries and on course detail pages
		-  That image, title, skill level are visible on landing page and course detail page, and that date and start time are shown on booking portal

-   **US04: View course information**

	As a  **Site User**  I can  **click on a course**  so that  **I can learn more about it**
	- Acceptance Criteria:
		-  As a Site User I can click on a course so that I can view its full details

	- I have tested:
		-  I have tests that when course title is clicked on landing page course summaries, the correct course detail page is loaded 

-   **US05: Book a course**

	As a  **Site User**  I can  **book a timetabled course**  so that  **I can reserve places for myself and those accompanying me**
	- Acceptance Criteria:
		-   user must be registered and logged in to reserve a place on a course
		-   user can select a date for the course
		-   user can reserve multiple places on the course up a max of 5
		
	- I have tested:
		-   That the booking portal on the course detail page is only visible to registered users who are logged in 
		-   That users can select a date for the course on the booking portal
		-   That users can reserve multiple places on the course (up a max of 5) on the booking portal
	
-   **US06: View my booked courses**

	As a  **Site User**  I can  **access a list of courses I have booked on to**  so that  **I can see the upcoming courses I have booked to attend**
	- Acceptance Criteria:
		-   User must be registered and logged in to view their bookings
		-   User can only access their own bookings
		-   Bookings are listed in course date order - soonest at the top of the list
		-   Functionality to cancel a course booking is accessible

	- I have tested:
		-   That only registered users who are logged in can gain access to the booking page and the booking link in the navbar
		-   That, apart from staff (admin) users, logged in users can only access their own bookings 
		-   That bookings are listed in course date order on the booking page, with soonest at the top of the list
		-   That users can cancel a course booking easily via the booking page
	
-   **US07: Cancel a booking**

	As a  **Site User**  I can  **cancel an upcoming course I have booked onto**  so that  **my place can be reserved by someone else**
	- Acceptance Criteria:
		- User must be registered and logged in to cancel a booking
		-   Users can only cancel bookings they have made themselves

	- I have tested:
		- That only  registered and logged in users have access to the booking portal (and the cancel booking button in turn)
		-   That (non-admin) users can only see their own bookings on their book page, and so can only cancel those bookings
	
-   **US08: Review a course**

	As a  **Site User**  I can  **attach a review to a course**  so that  **I can give feedback and be involved in the community of attendees**
	- Acceptance Criteria:
		-  User must be registered and logged in to submit a review
		-   Submitted reviews must be approved by the Site Admin user before they are visible to other users
	
	- I have tested:
		-  That only registered and logged in users can access the review post form
		-   That all submitted reviews are available to approve in the Django admin portal (which is only accessible to logged in staff/admin users)
	
-   **US09: View reviews**

	As a  **Site User**  I can  **view reviews on individual courses**  so that  **I can make an informed decision on whether I would like to attend this course**
	    	
	- Acceptance Criteria:
		- Approved reviews to be visible on the course detailed information page

	- I have tested:
		- That all approved reviews are visible on the course detail page by referencing and comparing those reviews to the approved reviews on the Django admin pages
    	
-   **US10: Approve reviews**

	As a  **Site Admin**  I can  **assess and then approve or disapprove reviews**  so that  **inappropriate content can be filtered out**
	- Acceptance Criteria:
		-   Site Admin can select one or more reviews to approve from the admin page
		-   Reviews can only be approved by the Site Admin

	- I have tested:
		-   Staff (admin) users can select one or more reviews to approve on the Django admin page
		-   That only staff (admin) users can gain access to the Django admin pages
	
-   **US11: Account registration and login**

	As a  **Site User**  I can  **register for an account**  so that  **I can log in and then book a course, , view my upcoming and past bookings, and leave reviews on courses**
	- Acceptance Criteria:
		-   to register, a user must enter a username and password (email is optional)
		-   user should not be able to register the same username or email address more than once
		-   user should not be able to login unless they have completed the registration step

	- I have tested:
		-  That users only sign up for an account on sign up form if they have entered a username and password
		-   That users can't use the sign up form to sign up with the same username or email address more than once 
		-   That only user information used to successfully sign in can be used for successful log in
	
-   **US12: Manage courses**

	As a  **Site Admin**  I can  **create, read, update and delete courses and their timetables**  so that  **I can manage course details and availability**
	- Acceptance Criteria:
		-   Admin user can create a new course from the admin site page - adding all relevant course information - image, description, slug etc.
		-   Admin user can modify data for an existing course.
		-   Once saved and "published" new courses or updates to courses become visible to general site users.
		-   Deleting a course causes all linked reviews, timetables and booking information to also be deleted
    
    - I have tested:
		-   That staff (admin) users can add a new course from the Django admin page and from the 'add course' link on the navbar 
		-   That staff (admin) users can edit course information from the Django admin page and the course detail page via website front-end
		-   That once added/saved and "published" new courses or updates to courses become visible to all users on the landing page and course detail page
		-   That staff (admin) users can delete courses from the Django admin page and the course detail page. Once courses are deleted I have tested that this causes all linked reviews, timetables and booking information to also be deleted

-   **US13: Create course drafts**

	As a  **Site Admin**  I can  **create drafts for courses**  so that  **I can finish producing the content at a later date and publish once approved**
	- Acceptance Criteria:
    	- Site Admin should be able to create and edit a course then select it's state as "draft" or "published"
		-   Only "published" courses should be visible to general users.
    
    - I have tested:
	    - That staff (admin) users can set created and edited courses to either "draft" or "published"
		-   That only "published" courses are visible to users on landing page
    	
-   **US14 Approve bookings**

	As a  **Site Admin**  I can  **view and then approve or disapprove bookings**  so that  **course capacity can be managed**
    - Acceptance Criteria:
    	-   Site Admin can select one or more bookings to approve from the admin page
		-   Bookings can only be approved by the Site Admin
    
    - I have tested:
		-   That staff (admin) users can select one or more bookings to approve from the Django admin pages
		-   That the Django admin pages can only be access by staff (admin) users

-   **US15 View past courses**

	As a  **Site User**  I can  **access a list of past courses that I booked**  so that  **I can track courses I have completed**
	- Acceptance Criteria:
		-   User must be registered and logged in to view their past bookings
		-   User can only access their own bookings
		-   Bookings are listed in course date order - most recent at the top of the list
		-   Courses in the past cannot be cancelled

	- I have tested:
		- 	That users can only gain access to the booking page and booking link in the navbar when they are registered and logged in
		-   That non-staff users can only access their own bookings on the Booking page 
		-   That bookings on the Booking page are listed in course date order - most recent at the top of the list
		-   That past courses on the Bookings page do not have the functionality of a cancel button

### Known bugs
- Currently no known bugs.


## Deployment

Detailed below are instructions on how to clone this project repository and the steps to configure and deploy the application. Code Institute also provides a summary of similar process steps here :  [CI Cheat Sheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

1.  How to Clone the Repository
2. Create a new PostgreSQL database instance on ElephantSQL
3.  Create Application on Heroku
4.  Configure Cloudinary to host images used by the application
5.  Connect the Heroku app to the GitHub repository
6.  Executing automated tests
7.  Final Deployment steps

### How to Clone the Repository

-   Go to the [https://github.com/SamarZiadat/oishii-ramen](https://github.com/SamarZiadat/oishii-ramen)  repository on GitHub
    
-   Click the "Code" button to the right of the screen, click HTTPs and copy the link there
    
-   Open a GitBash terminal and navigate to the directory where you want to locate the clone
    
-   On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
    
-   To install the packages required by the application use the command : pip install -r requirements.txt
    
-   When developing and running the application locally set DEBUG=True in the settings.py file
    
-   Changes made to the local clone can be pushed back to the repository using the following commands :
    
    -   git add  _filenames_  (or "." to add all changed files)
    -   git commit -m  _"text message describing changes"_
    -   git push
-   N.B. Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku
    
### Create a new PostgreSQL database instance on ElephantSQL

- Log in to [ElephantSQL.com](https://www.elephantsql.com/) to access your dashboard
- Click “Create New Instance”
- Set up your plan
- Give your plan a  Name  (this is commonly the name of the project)
    -   Select the  Tiny Turtle (Free)  plan
    -   You can leave the  Tags  field blank
- Select “Select Region”
- Select a data center near you
	- If you receive a message saying "Error: No cluster available in your-chosen-data-center  yet", choose another region.  Note:  You're free to use any of the available free data centers, be it AWS, Azure or any of the other providers.
- Then click “Review”
- Check your details are correct and then click “Create instance”
- Return to the ElephantSQL dashboard and click on the  database instance name  for this project
- In the URL section, click the copy icon to copy the database URL

### Create Application on Heroku

-   Log in to Heroku at  [https://heroku.com](https://heroku.com/)  - create an account if needed.
-   From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
-   On the Create New App page, enter a unique name for the application and select region. Then click Create app.
-   Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - add the url from ElephantSQL to DATABASE_URL 
-   Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.
-   Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols.
-   The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :
    -   DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
    -   SECRET_KEY = os.environ.get('SECRET_KEY')
-   In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate
-   Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt
-   Commit and push any local changes to GitHub.
-   In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure Cloudinary to host static files used by the application

-   Log in to Cloudinary - create an account if needed. To create the account provide your name, email and set up a password. For "primary interest" you can choose "Programmable Media for image and video API". Click "Create Account" and you will be sent an email to verify your account and bring you to the dashboard.
-   From the dashboard, copy the "API Environment variable" value by clicking on the "Copy to clipboard" link.
-   Log in to Heroku and go to the Application Configuration page for the application. Click on Settings and click on the "Reveal Config Vars" button.
-   Add a new Config Var called CLOUDINARY_URL and assign it the value copied from the Cloudinary dashboard, but remove the "CLOUDINARY_URL=" at the beginning of the string.
-   In order to be able to run the application on localhost, also add the CLOUDINARY_URL environment variable and value to env.py

### Connect the Heroku app to the GitHub repository

-   Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.
-   Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository and click on Connect to link up the Heroku app to the GitHub repository code.
-   Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.
-   The application can be run from the Application Configuration page by clicking on the Open App button.

### Executing automated tests

-   The existing automated jquery/javascript test can be executed using jest as follows :
    -   If jest is not installed then run the command : npm install --save-dev jest
    -   Run the js test file using the command : npm test
-   The existing automated django/python tests are executed using unittest as follows :
    -   Run the python tests using the command : python3 manage.py test
    -   To run just a subset of the tests, then append the application and test file name to the command, e.g. : python3 manage.py test booking.test_models
-   Test coverage for the django/python tests can be reviewed using the coverage tool :
    -   If coverage is not installed then run the command : pip3 install coverage
    -   Execute the following series of commands to determine test coverage :
        -   coverage run --source=booking manage.py test
        -   coverage report

### Final Deployment steps

Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows :

-   Set DEBUG flag to False in settings.py
-   Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
-   Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt
-   Push files to GitHub
-   In the Heroku Config Vars for the application delete this environment variable : DISABLE_COLLECTSTATIC
-   On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch

## Credits

-   [Balsamiq:](https://balsamiq.com/)  Used to create the wireframes.
-   [Bootstrap documentation:](https://getbootstrap.com/docs/5.3/getting-started/introduction/)  Bootstrap documentation used for styling and to build responsive web pages.
-   [Code Institute:](https://codeinstitute.net/)  Walkthrough modules in Full Stack Frameworks.
-   [Code Institute Slack Community:](https://app.slack.com/)  Slack community for troubleshooting and FAQ.
-   [Code Institute Tutor Support:](https://app.slack.com/)  For help and support.
-   [Django documentation:](https://docs.djangoproject.com/en/4.1/)  Everything you need to know about Django.
-   [Jest Docs:](https://jestjs.io/docs/getting-started)  For JavaScript testing.
-   [Stack Overflow:](https://stackoverflow.com/)  For troubleshooting and FAQ.
-   [W3Schools:](https://www.w3schools.com/)  Online Web Tutorials.

### Acknowledgements

-   My mentor at Code Institute Brian Macharia for code review, help and feedback. Very much appreciated!