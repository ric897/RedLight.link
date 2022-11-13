# RedLight.link
Mental health assistance system

## Documentation

### The purpose of this document is to document the existing system and to assist in the further development of the system

## Tech Stack

This website is built with Django and passes data dynammically to html views using Django's built in system. On the frontend, TailwindCSS is utilized to style the HTML pages. 

## Functions

At the moment, we use Django's built in authentication system. During signup, users are asked to store their phone number and an emergency contact's phone number that will be stored in their user table. After authentication, the homepage changes, using Django tempaltes, to house a single button that, when pressed, sends an SMS message to the stored emergency contact using the Twilio API.

Most of the functionality is handled in the views.py file (under AIUpload/views.py). Note that the Twilio authentication keys have been removed from the repo for security reasons. Additionally, it would be worth taking a look at the models.py file to view the custom user configuration used to house phone numbers.

## Installation 

To install this on your computer you will need to follow a few steps:

First, make sure to have git, pip, and python install on your comuter. Next run the commands:

`pip install twilio'
'pip install crispy-tailwind'
`pip install django`

Finally. after you clone the rep, cd into usqiapp and run the command:

`python3 manage.py runserver`

Now you should be able to go to go to "localhost:8000" on a browser and you should see the website.
