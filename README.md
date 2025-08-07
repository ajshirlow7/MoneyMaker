# MoneyMaker - Incremental Clicker Game

## Table of Contents

- [Introduction](#introduction)
- [Project Outline](#project-outline)
- [Key Objectives](#key-objectives)
- [UX Design](#ux-design)
- [User Stories](#user-stories)
- [Color Design](#color-design)
- [Wireframes](#wireframes)
- [Imagery](#imagery)
- [Features](#features)
  - [General Features](#general-features)
  - [Agile Section](#agile-section)
  - [Responsive Design](#responsive-design)
  - [AI Implementation](#ai-implementation)
- [Testing](#testing)
- [Optimization](#optimization)
- [Database](#database)
- [Deployment](#deployment)
- [Credit](#credit)

---

## Introduction

MoneyMaker is a Django-based incremental clicker game where users run virtual businesses, earn money, purchase upgrades, hire managers for automation, and compete on a leaderboard. The project emphasizes accessibility, responsive design, and community engagement through reviews.

## Project Outline

This project simulates a business management experience in a fun, gamified way. Players start with a basic business and expand their empire by reinvesting earnings, unlocking new businesses, and automating processes.

## Key Objectives

- Provide an engaging incremental game experience.
- Allow users to register, save progress, and compete.
- Enable community interaction through reviews and replies.
- Ensure accessibility and responsiveness across devices.

## UX Design

- **Navigation:** Simple, intuitive navigation with clear calls to action.
- **Feedback:** Real-time updates on earnings and upgrades.
- **Accessibility:** Keyboard navigation, screen reader support, and high-contrast UI.

## User Stories

- As a new user, I want to easily register an account so I can save my progress and access the game from any device.
- As a returning user, I want to log in securely so I can continue building my business empire.
- As a player, I want to click on businesses to earn money so I can progress in the game.
- As a player, I want to purchase upgrades for my businesses so I can increase my earnings.
- As a player, I want to hire managers to automate my businesses so I can earn money even when not actively clicking.
- As a player, I want to unlock new types of businesses as I progress so the game remains engaging and rewarding.
- As a competitor, I want to view a leaderboard so I can compare my progress with other players and strive for a higher rank.
- As a community member, I want to leave reviews about the game so I can share my feedback and experiences.
- As a user, I want to read reviews and replies from other players so I can learn tips and feel part of the community.
- As a review author, I want to edit or delete my own reviews so I can manage my contributions.
- As a user with accessibility needs**, I want to navigate the site using only my keyboard and screen reader so I can play the game without barriers.
- As a mobile user, I want the game interface to adapt to my device so I can play comfortably on any screen size.

## Color Design

- Uses a high-contrast palette for readability and accessibility.
- Consistent color themes for business types and UI elements.

## Wireframes

- Wireframes were created for desktop and mobile layouts, focusing on clear business panels, upgrade buttons, and review sections.

## Imagery

- Uses simple, friendly icons for businesses and upgrades.
- All images include descriptive alt text for accessibility.

## Features

### General Features

- Incremental gameplay with multiple business types.
- Upgrades and managers for automation.
- Leaderboard for competition.
- Review and reply system.
- Authentication and user profiles.

### Agile Section

Throughout this project, I adopted an agile workflow and methodology. Due to time constraints, I continuously iterated and performed bug testing, focusing on refining the core features before expanding the project scope. For example, in this final version, authors can self-publish, while some features like the reading function were deprioritized. My main priority was to perfect the essential functionalities before moving on to additional features.

At the outset, I established a project board to track user stories and monitor progress using 'To Do', 'In Progress', and 'Done' columns. Each user story was assigned a 'MOSCOW' prioritization tag (Must have, Should have, Could have, Won't have), following the Kanban method for effective workflow management.

The evolution of the project can be seen by comparing the original wireframes with the current deployed website. Here is my project board:
<a href="https://github.com/users/ajshirlow7/projects/1" target="_blank" rel="noopener noreferrer">| MoneyMaker project board |</a>

### Responsive Design

- Fully responsive layout using Bootstrap.
- Optimized for desktop, tablet, and mobile devices.

### AI Implementation

- AI-driven suggestions for upgrades and business strategies (if applicable).
- Smart review moderation (if implemented).

## Testing

- Manual and automated testing for all major features.
- Accessibility tested with keyboard and screen readers.
- Lighthouse audits for performance and best practices.

Lighthouse scores:


![Lighthouse](images/lighthouse.png)

Nu Html Checker:

Homepage:
![htmlchecker](images/html.png)

Review Page:
![htmlchecker](images/review.png)

Leadboard Page:
![htmlchecker](images/leaderboard.png)

Play Page:
![htmlchecker](images/playpage.png)


CSS Validation:
![csschecker](images/css.png)

Javascript checker for the play page which uses javascript heavily for game functionality:

Play page:
![javachecker](images/javascript.png)

Python Validation:

Homepage:
![pythonchecker](images/pythonhome.png)

Leaderboard:
![pythonchecker](images/pythonleaderboard.png)

Review:
![pythonchecker](images/pythonreview.png)

Game:
![pythonchecker](images/pythongame.png)



## Optimization

- Optimized images and static files for fast loading.
- Database queries optimized for leaderboard and reviews.

## Database

- I used Code Institute's PostgreSQL database.
- Creating a database:

To create a database with Code Institute's PostgreSQL service:

1. Navigate to PostgreSQL from Code Institute.
2. Enter your student email address in the input field provided.
3. Click **Submit**.
4. Wait while the database is created.
5. Check your email for a confirmation message.
6. You will receive a URL that you can use to connect your app to your database.

## Deployment

- Deployed on Heroku for live demo.
- Static files managed with WhiteNoise.
- Continuous deployment via Git.

## Credit

- Developed by [Your Name/Team].
- Built with Django, Bootstrap, and open-source libraries.
- Icons and images from [sources, e.g., FontAwesome, Unsplash].
- Special thanks to the Django and open-source community.

---

*Made with Django and Bootstrap. For educational purposes only.*