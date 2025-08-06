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

## Project Structure

- `manage.py` - Django management script
- `config/` - Django project configuration (settings, URLs, etc.)
- `game/` - Main app with game logic, models, views, and forms
- `MoneyMaker/` - Additional app (e.g., reviews, admin, images)
- `templates/` - HTML templates for the game and site
- `static/` and `staticfiles/` - Static assets (CSS, JS, images)

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.x
- pip

### Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd MoneyMaker
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser (optional):**
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

6. **Open your browser and go to:**  
    `http://127.0.0.1:8000/`

## How to Play

- Register or log in.
- Click "Start" on businesses to earn money.
- Buy upgrades and hire managers to automate earnings.
- Check the leaderboard to see your ranking.
- Leave a review or reply to others' reviews.

## License

This project is for educational purposes.

---

*Made with
