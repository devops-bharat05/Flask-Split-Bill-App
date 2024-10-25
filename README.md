# Flask Bill Split Application (Google Pay Style) 🧾💰

## Overview

This is a Flask-based web application that replicates a bill-splitting functionality similar to Google Pay's "Split Bill" feature. Users can create accounts, join groups, add expenses, and split bills either equally or using custom splits. The app supports user authentication, group management, and expense tracking with categories.

Additionally, the application is containerized using **Docker** for easy deployment and portability.

## Features 🚀
- 👤 **User Authentication**: Signup, Login, and Logout functionality.
- 👥 **Group Management**: Users can create and manage expense-sharing groups.
- 💰 **Expense Categorization**: Expenses can be categorized (e.g., food, travel, entertainment).
- ➗ **Equal or Custom Split**: Users can choose between splitting bills equally or specifying custom amounts for each participant.
- 💸 **Settle Up**: Display who owes how much, making it easy to settle up expenses.

## Tech Stack 🛠️
- **Backend**: Flask (Python)
- **Database**: SQLite (for simplicity; can be extended to PostgreSQL or MySQL)
- **Frontend**: HTML, CSS (via Flask templates)
- **Containerization**: Docker
- **Authentication**: Flask-Login

## Prerequisites 📝
- **Python 3.7+**: Make sure Python is installed on your machine.
- **Docker**: For containerization and running the application in a Docker container.

## Local Setup Instructions 🖥️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/flask-bill-split.git
   cd flask-bill-split
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   Run the following command to initialize the SQLite database:
   ```bash
   flask shell
   from app import db
   db.create_all()
   exit()
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   Open [http://localhost:5000](http://localhost:5000) to view the app.

## Docker Setup 🐋

To containerize the app using Docker, follow these steps:

1. **Build the Docker Image**:
   ```bash
   docker build -t flask-bill-split .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 flask-bill-split
   ```

   The application will be accessible at [http://localhost:5000](http://localhost:5000).

### Optional: Using Docker Compose

You can use Docker Compose to simplify the setup:

1. **Create `docker-compose.yml`**:
   ```yaml
   version: '3'
   services:
     app:
       build: .
       ports:
         - "5000:5000"
       environment:
         - FLASK_ENV=development
   ```

2. **Run the App with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

## Project Structure 🗂️

```
.
├── app.py                # Main Flask app
├── models.py             # Database models
├── templates/            # HTML templates for Flask
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── signup.html       # Signup page
│   ├── group.html        # Group management page
│   ├── add_expense.html  # Add new expense form
│   ├── result.html       # Display split results
├── static/               # Static assets (CSS, JS)
│   └── styles.css        # Basic CSS styling
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Optional Docker Compose file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## API Endpoints (Routes) 🛤️

- `/` (GET): Home page displaying user's groups and option to create a new group.
- `/signup` (GET/POST): Signup page for user registration.
- `/login` (GET/POST): Login page for existing users.
- `/logout` (GET): Logs the user out and redirects to home.
- `/group` (GET/POST): Create or view groups.
- `/add_expense/<group_id>` (GET/POST): Add new expense to a group.
- `/calculate/<group_id>` (GET): Calculate how much each user owes in a group.

## Screenshots 🖼️
### Home Page
![Home Page](./screenshots/homepage.png)

### Add Expense
![Add Expense](./screenshots/add_expense.png)

### Result Page
![Result](./screenshots/result.png)

## Future Enhancements 🚀
- 🔄 **Integration with Payment Gateway**: Add integration to pay/settle up debts online.
- 📊 **Expense Reports**: Generate monthly reports for each group.
- 📧 **Email Notifications**: Notify users about group updates and pending balances.
- 🌐 **Multi-Language Support**: Expand to support different languages.

## Contributing 🤝
Feel free to fork the repository and submit pull requests. Contributions are welcome for bug fixes, new features, and documentation improvements.

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a new pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact ☎️

For any questions or suggestions, feel free to contact me:
- Email: bharatbhushan05@outlook.com
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourusername)
- GitHub: https://github.com/devops-bharat05

