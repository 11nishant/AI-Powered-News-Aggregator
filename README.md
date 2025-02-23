# News Conspiracy Detection System

## Overview
The AI-Powered News Aggregator is a web-based application that analyzes news headlines and assigns a Conspiracy Score (0-100%) using ML models. The system helps detect clickbait, misinformation, and neutral news dynamically, empowering users to evaluate the credibility of headlines. It consists of a **Flask** backend and a **React.js** frontend.

The backend is responsible for:
- Handling API requests for conspiracy score prediction.
- Managing a PostgreSQL database to store news headlines and their associated scores.

The frontend provides:
- A user-friendly interface to input news headlines.
- Display of conspiracy scores and stored news articles.
- An admin panel for CRUD operations on stored news articles.

## Machine Learning Model Used
The project employs a **TF-IDF Vectorizer with an SVM classifier for the Conspiracy Score and Logistic Regression Model** for text classification. This model is trained to detect suspicious words, clickbait, and misinformation in news headlines. Additional enhancements can include transformer-based models like BERT for improved accuracy.


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


## ⚙️ How the Application Works

### **1️⃣ User Inputs a Headline (Frontend)**
📌 The user enters a news headline in an input form on the frontend.  
📌 **Code Used:**  
- `src/components/InputForm.js` → Handles user input & form submission.  
- `src/services/api.js` → Sends the headline to the backend.  

```js
const response = await axios.post(`${BASE_URL}/predict`, { headline });
```

---

### **2️⃣ Headline Sent to Backend API (Flask)**
📌 The backend receives the headline and passes it to the AI model for analysis.  
📌 **Code Used:**  
- `routes/predict.py` → Defines the `/predict` API endpoint.  
- `models/text_classifier.py` → ML model calculates the conspiracy score.  

```python
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    headline = data.get('headline')
    score = text_classifier.get_conspiracy_score(headline)
    return jsonify({'score': score})
```

---

### **3️⃣ AI Model Analyzes the Headline (ML Processing)**
📌 The AI model runs NLP-based analysis to predict the **Conspiracy Score (0-100)**.  
📌 **Code Used:**  
- `models/text_classifier.py` → Loads pre-trained NLP model.  

```python
def get_conspiracy_score(headline):
    processed_text = preprocess_text(headline)
    prediction = model.predict([processed_text])
    return float(prediction[0])
```

---

### **4️⃣ Backend Returns Conspiracy Score**
📌 The Flask API sends the conspiracy score back to the React frontend.  
📌 **Code Used:**  
- `routes/predict.py` (returns the result as JSON).  

```python
return jsonify({'score': score})
```

---

### **5️⃣ Frontend Displays the Conspiracy Score**
📌 The frontend receives the score and updates the UI.  
📌 **Code Used:**  
- `src/components/ScoreDisplay.js` → Displays the score visually.  

```js
<p>Conspiracy Score: {score}</p>
```

---

### **6️⃣ Save the Headline & Score in Database**
📌 Store the analyzed headline in the database.  
📌 **Code Used:**  
- `routes/news_crud.py` → Handles saving news to PostgreSQL.  

```python
@app.route('/news', methods=['POST'])
def save_news():
    data = request.json
    headline = data.get('headline')
    score = data.get('score')
    db.insert_news(headline, score)
    return jsonify({'message': 'News saved successfully'})
```

---

### **7️⃣ User Views All Stored News**
📌 Users can view previously analyzed headlines in a list.  
📌 **Code Used:**  
- `routes/news_crud.py` → Fetches stored news from PostgreSQL.  
- `src/components/NewsList.js` → Displays the stored news.  

```js
const response = await axios.get(`${BASE_URL}/news`);
setNewsList(response.data);
```

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

## 🎥 Demo Video  

<a href="https://drive.google.com/file/d/1v0EfzFkYodFFd7GAqwWMKdf4KKj2QKvx/view?usp=drive_link">
    <img src="image.png" alt="Watch the Demo" width="500">
</a>  








