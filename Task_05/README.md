# TimeTickQuiz 
*A fast-paced command-line quiz game powered by the Open Trivia Database API.* 

---

## Overview  
**TimeTickQuiz** is a Python-based CLI quiz game where you race against a countdown timer to answer trivia questions. 
It uses: 
- **Open Trivia Database API** for live questions 
- **Threads** for real-time timers 
- **Rich** for colorful, engaging console output 
- **JSON** for storing user profiles & scores 

Your goal: answer as many questions as possible before the clock runs out and become the **TimeTickQuiz Champion**! 

---

##  Features  
-  User profiles with persistent scoring (saved in `profiles.json`) 
-  Fetches live trivia questions (categories, difficulties, types) 
-  Configurable countdown timer per question (default: 15s) 
-  Stylish console UI with **rich** (colors, highlights, feedback) 
-  Instant feedback for correct/incorrect answers 
-  Saves scores & progress across sessions 

---

##  Project Structure  

```
TimeTickQuiz-2/
├── src/
│   ├── main.py            # Entry point, handles CLI & game loop
│   ├── quiz_engine.py     # Core quiz logic (questions, scoring, timer)
│   ├── user_profile.py    # Manages user profiles & score persistence
│   ├── utils.py           # Helpers (API fetch, formatting, timers)
├── profiles.json          # Stores player profiles & scores
├── requirements.txt       # Python dependencies
├── README.md              # This file
```

---

##  Installation  

### 1. Clone the Repo  
```bash
git clone https://github.com/Kota-Jagadeesh/TimeTickQuiz-2.git
cd TimeTickQuiz-2/src
```

### 2. Create Virtual Environment  
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Requirements  
```bash
pip install -r requirements.txt
```

---

##  Running the Game  
Run the quiz from inside the `src/` folder: 
```bash
python main.py
```

At startup, you’ll: 
1. Enter a **username** (new users are added to `profiles.json`). 
2. Choose **quiz settings**: number of questions, category, difficulty, question type, and time limit. 
3. Play the quiz, answer before the countdown runs out! 

---

##  Example Gameplay  

```text
Welcome, User! 
Fetching 5 questions from Open Trivia DB...

Question 1/5 (15s left) 🕒
Category: General Knowledge | Difficulty: Easy

What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome

> Your answer: C
Correct! +10 points

...
```

At the end, you’ll see your **total score** and it will be saved to `profiles.json`. 

---

##  Tech Stack  
- **Python 3.8+** 
- **Requests** : API fetching 
- **Rich** : Console UI 
- **Threading** : Timers 
- **JSON** : Profiles & persistence 

---

