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

- As a user, I want to register and log in so my progress is saved.
- As a player, I want to earn money by clicking and automate businesses.
- As a competitor, I want to see my ranking on the leaderboard.
- As a community member, I want to leave and read reviews.

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

- Features were developed iteratively with regular feedback and testing.
- User stories and tasks tracked using a project board.

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

## Optimization

- Optimized images and static files for fast loading.
- Database queries optimized for leaderboard and reviews.

## Database

- Django ORM with SQLite (default), easily switchable to PostgreSQL or MySQL.
- Models for users, businesses, upgrades, reviews, and leaderboard entries.

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