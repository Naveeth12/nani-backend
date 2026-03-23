# backend/Aptitude_engine.py

def get_aptitude_questions():

    questions = [
        {"q": "10 + 5 ?", "options": ["10","15","20","25"], "answer": "15"},
        {"q": "20 / 4 ?", "options": ["2","4","5","10"], "answer": "5"},
        {"q": "9 * 3 ?", "options": ["18","21","27","30"], "answer": "27"},
        {"q": "12 + 8 ?", "options": ["18","20","21","22"], "answer": "20"},
        {"q": "30 / 5 ?", "options": ["3","4","6","7"], "answer": "6"},
        {"q": "7 * 6 ?", "options": ["36","40","42","48"], "answer": "42"},
        {"q": "15 + 10 ?", "options": ["20","25","30","35"], "answer": "25"},
        {"q": "50 / 10 ?", "options": ["2","5","8","10"], "answer": "5"},
        {"q": "8 * 8 ?", "options": ["56","60","64","70"], "answer": "64"},
        {"q": "18 + 12 ?", "options": ["28","30","32","36"], "answer": "30"},
    ]

    # duplicate to reach 50 questions
    while len(questions) < 50:
        questions = questions + questions

    return questions[:50]