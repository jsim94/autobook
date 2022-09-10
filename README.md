# Autobook

## What goal is the site designed to achieve?

This site is designed for being a social destination for the car community to share their own projects with friends as well as gain inspiration from shared posts by other users.

## What is the demograhic of the site's users?

This app will be targeted towards members of the automotive community looking for a place to share their projects with other users.

## What data is being used?

This app will use https://www.carqueryapi.com/ to gain relevant data tied to users cars for more information and interactivity. It'll contain more in depth data about the vehicle such as drivetrain specs, etc.

## - What does the database schema look like?

There will be tables for users, projects, and posts, and direct message groups, and messages. There will also be joining tables between users and posts for likes, users and users for friends.

## - What kinds of issues might occur with the API?

Some requests possibly might not return valid information which will have to be handled.

## - What functionality will the app include?

There will be a messaging system between single users as well as group messaging.

## - What will the user flow look like?

The user will start at a homepage asking for a login or signup, then redirect to a home page to show friends posts, then related car posts, followed by all recent posts. There will be a navbar showing a link to the users profile page as well as a dropdown for message groups that leads to specific conversations. On the profile page a user will be able to add a car to their profile and write posts and associate them to the car. In the navbar will be a search bar to search users or cars, which will return a list of found users by first name, last name, username, or cars by model or name.

# DB Schema

![DB schema](/assets/images/schema.png)
