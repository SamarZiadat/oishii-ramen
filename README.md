<h1  align="center">oishii ramen</h1>

[View the live project here](https://oishii-ramen.herokuapp.com/)

'oishii ramen' is an app designed and created for a fictional Japanese restaurant of the same name in Glasgow, Scotland. The Japanese word 'oishii' means 'delicious' or 'tasty' in English. The app is a management system designed for staff to view and manage customer reservations. It also provides customers with an online booking system where they can view and manage their own reservations.

## Table of Contents
- [User Experience Design (UX)](https://github.com/SamarZiadat/oishii-ramen#user-experience-design-ux)
	 -   [The Strategy Plane](https://github.com/SamarZiadat/oishii-ramen#the-strategy-plane)
		    -   [Site Goals](https://github.com/SamarZiadat/oishii-ramen#site-goals)
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

#### Site Goals
The site is aimed to help restaurant staff to easily view, keep up-to-date-with and manage upcoming reservations, editing and deleting these bookings as necessary.

The site also aims to provide customers with an online system to book, update or cancel reservations without the need to call or email the restaurant. 

#### Agile Project Management

This project was managed using agile methodologies by delivering small features in incremental sprints. There were 4 sprints in total, spaced out evenly over four weeks. A kanban board was created using github projects and was utilised as a project management tool to help visualise work, limit work-in-progress, and maximise efficiency/flow. The Kanban board can be viewed [here](https://github.com/SamarZiadat/oishii-ramen/projects). 

All requirements were created in relation to the user stories. Requirements were then assigned to epics (milestones) and prioritised with the labels 'must have', 'should have' or 'could have'. All 5 epics were organised within sprints, and requirements were completed in order of: 'must have' stories first, 'should have' stories, and then finally "could have" stories. This approach was taken in order to ensure that all core requirements were definitely delivered, with the nice to have features implemented in an iterative way according to capacity.

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
-   US05: Book a hike
    -   As a  **Site User**  I can  **book a timetabled course**  so that  **I can reserve places for myself and those accompanying me**
-   US06: View my booked courses
    -   As a  **Site User**  I can  **access a list of courses I have booked on to**  so that  **I can see the upcoming courses I have booked to attend**
-   US07: Cancel a booking
    -   As a  **Site User**  I can  **cancel an upcoming course I have booked onto**  so that  **my place can be reserved by someone else**
-   US08: Review a course
    -   As a  **Site User**  I can  **attach a review to a course**  so that  **I can give feedback and be involved in the community of attendees**
-   US11: View reviews
    -   As a  **Site User**  I can  **view reviews on individual courses**  so that  **I can make an informed decision on whether I would like to attend this course**
-   US12: Approve reviews
    -   As a  **Site Admin**  I can  **assess and then approve or disapprove reviews**  so that  **inappropriate content can be filtered out**
-   US13: Account registration and login
    -   As a  **Site User**  I can  **register for an account**  so that  **I can log in and then book a course, , view my upcoming and past bookings, and leave reviews on courses**
-   US14: Manage courses
    -   As a  **Site Admin**  I can  **create, read, update and delete courses and their timetables**  so that  **I can manage course details and availability**
-   US15: Create course drafts
    -   As a  **Site Admin**  I can  **create drafts for courses**  so that  **I can finish producing the content at a later date and publish once approved**
-   US16 Approve bookings
    -   As a  **Site Admin**  I can  **view and then approve or disapprove bookings**  so that  **course capacity can be managed**
-   US17 View past courses
    -   As a  **Site User**  I can  **access a list of past courses that I booked**  so that  **I can track courses I have completed**

### The Scope Plane

-   Home page with restaurant information
-   Responsive Design - the app should be fully functional on all devices from 320px up
-   Hamburger menu for devices with a smaller viewport devices
- Ability to perform CRUD functionality on reservations
-   Restricted role based features
