<h1  align="center">oishii ramen</h1>

[View the live project here](link)

'oishii ramen' is an app designed and created for a fictional Japanese restaurant of the same name in Glasgow, Scotland. The Japanese word 'oishii' means 'delicious' or 'tasty' in English. The app is a management system designed for staff to view and manage customer reservations. It also provides customers with an online booking system where they can view and manage their own reservations.

## Table of Contents
- [User Experience Design (UX)]()
	 -   [The Strategy Plane]()
		    -   Site Goals
		    -   Agile Methodology
		    -   Epics
		    -   User Stories
	-   [The Scope Plane]()
	-   [The Structure Plane]()
	    -   Features
	    -   Future Features
	-   [The Skeleton Plane]()
	    -   Wireframes
	    -   Database Design
	    -   Security
	-   [The Surface Plane]()
	    -   Design
	        -   Colour Scheme
	        -   Typography
	        -   Imagery
	-   [Technologies]()
	-   [Testing]()
	-   [Deployment]()
	    -   Version Control
	    -   Heroku Deployment
	    -   Run Locally
	    -   Fork Project
	-   [Credits]()
	    -   [Content]()
	    -   [Acknowledgements]()

## User Experience Design (UX)

### The Strategy Plane

#### Site Goals
The site is aimed to help restaurant staff to easily view, keep up-to-date-with and manage upcoming reservations, editing and deleting these bookings as necessary.

The site also aims to provide customers with an online system to book, update or cancel reservations without the need to call or email the restaurant. 

#### Agile Methodology

This project was managed using agile methodologies by delivering small features in incremental sprints. There were 4 sprints in total, spaced out evenly over four weeks. A kanban board was created using github projects and was utilised as a project management tool to help visualise work, limit work-in-progress, and maximise efficiency/flow. The Kanban board can be viewed [here](https://github.com/SamarZiadat/oishii-ramen/projects). 

All requirements were created in relation to the user stories. Requirements were then assigned to epics (milestones) and prioritised with the labels 'must have', 'should have' or 'could have'. All 5 epics were organised within sprints, and requirements were completed in order of: 'must have' stories first, 'should have' stories, and then finally "could have" stories. This approach was taken in order to ensure that all core requirements were definitely delivered, with the nice to have features implemented in an iterative way according to capacity.

[IMAGE OF KANBAN]

#### User Stories

**Epic 1 - Base Setup**

This epic is for all stories needed for the base set up of the application. This was the first epic to be delivered as all other features depend on this structure's existence.

-   As a new user, I would like to clearly see the site's purpose, so that I can decide whether or not to sign up for an account.  `(MUST HAVE)`
- As a new user, I would like to easily navigate the site, so that I can easily access the information I need.  `(MUST HAVE)`
-   As a user, I would like access the restaurants contact details, so that I can easily get in touch.  `(MUST HAVE)`
-   As a user, I would like to easily find the restaurant's social media channels, so that I can stay up-to-date with the business online.  `(MUST HAVE)`
-  As a user, I would like view the restaurant location on Google Maps, so that I can easily access directions to the venue.  `(SHOULD HAVE)`
- As a user, I would like to preview a selection of the restaurant's Instagram posts, so that I can get an idea of what they post on Instagram before I decide whether to follow them on Instagram or not.  `(COULD HAVE)`
-   As a user, I want to be able to put the website into dark mode so that I can make the website easier to see at night.  `(COULD HAVE)`

**Epic 2 - Authentication Epic**

This epic is for all stories related to the registration, login and authorisation of views. This epic provides critical functionality; allowing staff and customers to view and manage reservations securely. It also excludes unauthorised users from being able to gain access to information or complete actions that they shouldn't.

-   As a site administrator, I should be able to access an area only for restaurant staff to see, so that I can view and manage all the existing customer reservations securely.  `(MUST HAVE)`
-  As a site administrator, I would like to log in to my area, so that I can access and manage information securely.  `(MUST HAVE)`
-   As a site administrator, I would like to log out of my account, so that I can end my session on my current device.  `(MUST HAVE)`
- As a new user, I should be able to sign up for an area only for me to see, so that I can view and manage my reservations and personal information securely.  `(MUST HAVE)`
- As a registered user, I should be able to access an area only for me to see, so that I can view and manage my reservations and personal information securely.  `(MUST HAVE)`
-   As a registered user, I would like to log in to my account, so that I can access my details and reservations.  `(MUST HAVE)`
-   As a registered user, I would like to log out of my account, so that I can end my session on my current device.  `(MUST HAVE)`

**Epic 3 - Reservations**

This epic is for all stories that relate to creating, viewing, amending and deleting reservations. This allows staff to view and manage upcoming reservations, and for customers to book and manage their own reservations.

-   As a site administrator, I should be able to cancel reservations from any registered user, so that I can keep the restaurant bookings up-to-date for both staff and customers.  `(MUST HAVE)`
- As a site administrator, I should be able to view all reservations, so that I am up to date with capacity. `(MUST HAVE)`
-   As a site administrator, I should be able to edit a reservation from any registered user, so that I can keep the restaurant bookings up-to-date for both staff and customers.  `(SHOULD HAVE)`
- As a site administrator, I should be able to make a reservation for registered and unregistered users, so that I can make reservations for customers who do not use the website.  `(COULD HAVE)`
-    As a registered user, I would like to make my reservation/s, so that I am guaranteed a seat when I visit the restaurant.  `(MUST HAVE)`
- As a registered user, I should be able to cancel my reservation/s, so that I can keep the restaurant up-to-date with my booking.  `(MUST HAVE)`
-   As a registered user, I would like to view my reservation/s, so that I can check the details when needed.  `(MUST HAVE)`
-   As a registered user, I would like to amend my reservation/s, so that the restaurant is kept up-to-date with my booking.  `(MUST HAVE)`
- As a registered user, I would like to easily navigate the site, so that I can easily access the information I need.  `(MUST HAVE)`
-    As a registered user, I would like to amend my details, so that the restaurant has the most up-to-date details to identify me.  `(SHOULD HAVE)`
-  As a registered user, I would like to reset my password if I forget it, so that I can regain access to my account.  `(SHOULD HAVE)`

**Epic 4 - Deployment Epic**

This epic is for all stories related to deploying the app to heroku so that the application is live for use.

- As a developer, I need to deploy the project to heroku so that it is live for all users `(MUST HAVE)`

**Epic 5 - Documentation**

This epic is for all stories relating to the documentation of the software development lifecycle of the application, and how it can be utilised by users.

- As a developer, I need to complete the readme documentation so that it an informative first contact that developers and users will have with the app  `(MUST HAVE)`
-  As a developer, I need to complete testing of the app to ensure it works correctly and as expected `(MUST HAVE)`

### The Scope Plane

-   Home page with restaurant information
-   Responsive Design - the app should be fully functional on all devices from 320px up
-   Hamburger menu for devices with a smaller viewport devices
- Ability to perform CRUD functionality on reservations
-   Restricted role based features
