# News Conspiracy Detection System

## Overview
This project is an AI-powered News Conspiracy Detection System that evaluates the credibility of news headlines using a machine learning model. It consists of a **Flask** backend and a **React.js** frontend.

The backend is responsible for:
- Handling API requests for conspiracy score prediction.
- Managing a PostgreSQL database to store news headlines and their associated scores.

The frontend provides:
- A user-friendly interface to input news headlines.
- Display of conspiracy scores and stored news articles.
- An admin panel for CRUD operations on stored news articles.

## Machine Learning Model Used
The project employs a **TF-IDF based Logistic Regression Model** for text classification. This model is trained to detect suspicious words, clickbait, and misinformation in news headlines. Additional enhancements can include transformer-based models like BERT for improved accuracy.


---

## Project Structure
```
news-conspiracy-detection/
│── backend/                 # Flask Backend
│   ├── models/              # Machine Learning Models
│   ├── routes/              # API Routes
│   ├── database/            # Database Configuration
│   ├── static/              # Optional (for static files)
│   ├── templates/           # Optional (for Jinja2 templates)
│   ├── app.py               # Main Flask App
│   ├── config.py            # Configuration File
│   ├── wsgi.py              # Entry Point for Deployment
│   ├── requirements.txt     # Dependencies List
│
│── frontend/                # React.js Frontend
│   ├── src/
│   │   ├── components/      # UI Components
│   │   ├── pages/           # Pages
│   │   ├── services/        # API Calls
│   │   ├── styles/          # Styling Files
│   │   ├── App.js           # Main App Component
│   │   ├── index.js         # Entry Point
│   ├── public/              # Static files like index.html
│   ├── package.json         # Dependencies
│   ├── .env                 # Environment Variables
```

---

## Installation Guide

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL

### Backend Setup (Flask)
1. Navigate to the backend folder:
   ```sh
   cd backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables in a `.env` file:
   ```sh
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://username:password@localhost:5432/news_db
   ```
5. Initialize the database:
   ```sh
   python database/db.py
   ```
6. Run the backend:
   ```sh
   flask run
   ```
   Backend will be available at `http://127.0.0.1:5000/`

### Frontend Setup (React.js)
1. Navigate to the frontend folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend:
   ```sh
   npm start
   ```
   Frontend will be available at `http://localhost:3000/`

---

## API Endpoints

### 1. Predict Conspiracy Score
- **Endpoint:** `POST /api/predict`
- **Description:** Predicts conspiracy score for a given news headline.
- **Request Body:**
  ```json
  {
    "headline": "Breaking news: Alien spaceship landed!"
  }
  ```
- **Response:**
  ```json
  {
    "score": 85.4,
    "category": "Highly Conspiratorial"
  }
  ```

### 2. Get Stored News Articles
- **Endpoint:** `GET /api/news`
- **Description:** Fetch all stored news articles and their conspiracy scores.
- **Response:**
  ```json
  [
    {"id": 1, "headline": "Breaking news: Alien spaceship landed!", "score": 85.4},
    {"id": 2, "headline": "Stock market rises unexpectedly", "score": 20.3}
  ]
  ```

### 3. Add News Article
- **Endpoint:** `POST /api/news`
- **Description:** Stores a news article and its conspiracy score.
- **Request Body:**
  ```json
  {
    "headline": "Moon landing was faked!",
    "score": 95.6
  }
  ```
- **Response:**
  ```json
  {"message": "News article added successfully!"}
  ```

### 4. Delete News Article
- **Endpoint:** `DELETE /api/news/<id>`
- **Description:** Deletes a stored news article.
- **Response:**
  ```json
  {"message": "News article deleted!"}
  ```

---

## Technologies Used
### **Backend**
- Flask (Python)
- PostgreSQL
- SQLAlchemy
- Machine Learning (Text Classification)

### **Frontend**
- React.js
- Axios (for API requests)
- Bootstrap (for styling)

---


## Features
- **Interactive Input Widget**: Users can enter any headline and receive a Conspiracy Score (0-100%).
- **Existing Dataset Processing**: Displays and manages preloaded news headlines.
- **Custom NLP Model**: Detects misinformation dynamically.
- **CRUD Operations**: Users can delete news headlines.
- **Optional Enhancements**: Highlights suspicious words and performs sentiment analysis.

## Tech Stack
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **NLP Tools**: NLTK, Scikit-learn


## Future Improvements
- Improve model accuracy using transformer models (BERT, RoBERTa).
- Implement a real-time news feed integration.
- Enhance UI with visualization of conspiracy trends.




