# MoneyMaker - Incremental Clicker Game

MoneyMaker is a Django-based incremental clicker game where users can earn virtual money by running businesses, purchase upgrades, hire managers for automation, and compete on the leaderboard. Users can also leave reviews and reply to others.

🌐 Live Demo
[Try MoneyMaker now!](https://moneymaker-82ffd9f04b3c.herokuapp.com/)

## Features

- **Incremental Gameplay:** Run businesses like Lemonade Stand, Car Wash, and Pizza Shop to earn money.
- **Upgrades & Managers:** Buy upgrades to increase earnings and hire managers to automate businesses.
- **Leaderboard:** Compete with other users for the highest earnings.
- **User Reviews:** Leave reviews and replies for the game.
- **Authentication:** Register and log in to save your progress.
- **Responsive UI:** Clean, modern interface built with Bootstrap.

### CRUD Functionality

MoneyMaker implements full CRUD (Create, Read, Update, Delete) functionality for user-generated content, specifically in the review system:

- **Create:** Authenticated users can create new reviews for the game, sharing their feedback and experiences.
- **Read:** All users can view existing reviews and replies, allowing for community engagement and transparency.
- **Update:** Users can edit their own reviews to correct or update their feedback.
- **Delete:** Users have the ability to delete their own reviews if they wish to remove their comments.

This CRUD system ensures that users have control over their contributions and can interact meaningfully with the MoneyMaker community.

#### Project Structure

- `manage.py` - Django management script
- `config/` - Django project configuration (settings, URLs, etc.)
- `game/` - Main app with game logic, models, views, and forms
- `MoneyMaker/` - Additional app (e.g., reviews, admin, images)
- `templates/` - HTML templates for the game and site
- `static/` and `staticfiles/` - Static assets (CSS, JS, images)

 ##### Technology Stack

- **Backend Framework:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Database:** SQLite (default, can be switched to PostgreSQL or MySQL)
- **Authentication:** Django built-in authentication system
- **Deployment:** Heroku (for live demo)
- **Version Control:** Git
- **Other Tools:** Django Admin, pip (Python package manager)

######  Performance & Accessibility
![Lighthouse Performance Results](/images/moneymaker_lighthouse.png)






