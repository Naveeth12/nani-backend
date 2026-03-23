from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os
import random

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

static_path = os.path.join(BASE_DIR, "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

interview_session = {}

class AnswerData(BaseModel):
    answers: dict


# ---------------------------
# ✅ LEVEL 2 CORRECT ANSWERS (ALL 30)
# ---------------------------

correct_answers = {
    "q0": "programming language",
    "q1": "def",
    "q2": "dictionary",
    "q3": "hyper text markup language",
    "q4": "styling",
    "q5": "python",
    "q6": "<a>",
    "q7": "react",
    "q8": ".py",
    "q9": "class",
    "q10": "database",
    "q11": "append",
    "q12": "hyper text transfer protocol",
    "q13": "flask",
    "q14": "#",

    "q15": ["guido van rossum"],
    "q16": ["structure"],
    "q17": ["design"],
    "q18": ["browser"],
    "q19": ["fast"],
    "q20": ["databases"],
    "q21": ["javascript"],
    "q22": ["def"],
    "q23": ["key and value", "key value"],
    "q24": ["cpu"],
    "q25": ["html"],
    "q26": ["style"],
    "q27": ["object oriented", "object oriented programming"],
    "q28": ["version"],
    "q29": ["users"]
}


# ---------------------------
# LEVEL 3 QUESTIONS
# ---------------------------

level3_questions = [
    {"question":"Write a Python program to reverse a string."},
    {"question":"Write a Python program to check if a number is prime."},
    {"question":"Write a program to find the largest number in a list."},
    {"question":"Write a Python program to count vowels in a string."},
    {"question":"Write a program to find factorial of a number."},
    {"question":"Write a Python program to remove duplicates from a list."},
    {"question":"Write a program to check palindrome."},
    {"question":"Write a Python program to sort a list without using sort()."}
]


# ---------------------------
# FEEDBACK FUNCTIONS
# ---------------------------

def level1_feedback(score):
    if score >= 40:
        return "Excellent aptitude skills."
    elif score >= 30:
        return "Good logical ability."
    elif score >= 20:
        return "Average performance."
    else:
        return "Needs improvement."


def level2_feedback(score):
    if score >= 25:
        return "Excellent technical knowledge."
    elif score >= 15:
        return "Good knowledge but needs improvement."
    else:
        return "Technical skills need improvement."


def level3_feedback(score):
    if score >= 6:
        return "Excellent coding and problem solving skills."
    elif score >= 4:
        return "Good coding ability."
    elif score >= 2:
        return "Average coding skills."
    else:
        return "Needs improvement in coding logic."


# ---------------------------
# HOME
# ---------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


# ---------------------------
# START INTERVIEW
# ---------------------------

@app.post("/start_interview", response_class=HTMLResponse)
async def start_interview(request: Request):

    form = await request.form()
    company = form.get("company")

    interview_session["company_type"] = company

    return templates.TemplateResponse("aptitude.html", {"request":request})


# ---------------------------
# SUBMIT LEVEL 1
# ---------------------------

@app.post("/submit_aptitude", response_class=HTMLResponse)
async def submit_aptitude(request: Request, data: AnswerData):

    score = len(data.answers)

    feedback = level1_feedback(score)
    qualified = score >= 30

    return templates.TemplateResponse(
        "aptitude_result.html",
        {
            "request":request,
            "score":score,
            "feedback":feedback,
            "qualified":qualified
        }
    )


# ---------------------------
# LEVEL 2 PAGE
# ---------------------------

@app.get("/level2", response_class=HTMLResponse)
async def level2_page(request: Request):

    return templates.TemplateResponse(
        "level2.html",
        {"request":request}
    )


# ---------------------------
# ✅ FINAL LEVEL 2 SUBMIT (FIXED)
# ---------------------------

@app.post("/submit_level2", response_class=HTMLResponse)
async def submit_level2(request: Request):

    form = await request.form()
    form_dict = dict(form)

    print("FORM KEYS:", list(form_dict.keys()))

    score = 0

    for key, correct in correct_answers.items():

        user_answer = form_dict.get(key, "").strip().lower()

        print(f"{key} USER:", user_answer)

        if isinstance(correct, list):
            if user_answer in [c.lower() for c in correct]:
                score += 1
        else:
            if user_answer == correct.lower():
                score += 1

    print("FINAL SCORE:", score)

    feedback = f"You scored {score} out of 30"

    return templates.TemplateResponse(
        "level2_result.html",
        {
            "request": request,
            "score": score,
            "feedback": feedback
        }
    )


# ---------------------------
# LEVEL 3 ROUTE
# ---------------------------

@app.get("/level3")
async def level3(request: Request):

    questions = [
        "Explain OOP concepts",
        "What is polymorphism?",
        "Explain Python decorators"
    ]

    return templates.TemplateResponse(
        "level3.html",
        {"request": request, "questions": questions}
    )


# ---------------------------
# ✅ FIXED REDIRECT ONLY
# ---------------------------

@app.post("/submit_level3")
async def submit_level3(request: Request):

    return RedirectResponse(url="/jam_round", status_code=302)


# ---------------------------
# JAM ROUND
# ---------------------------

@app.get("/jam_round")
async def jam_round(request: Request):

    topic = random.choice([
        "Artificial Intelligence",
        "Future of Work",
        "Climate Change",
        "Remote Jobs"
    ])

    return templates.TemplateResponse(
        "jam_round.html",
        {"request": request, "topic": topic}
    )


# ---------------------------
# ✅ UPDATED SUBMIT JAM (YOUR LOGIC ADDED)
# ---------------------------

@app.post("/submit_jam")
async def submit_jam(request: Request):

    data = await request.json()
    speech = data.get("speech", "").lower()

    confidence_words = [
        "confident", "strong", "sure", "definitely", "clearly",
        "i believe", "i think", "future", "growth", "success"
    ]

    filler_words = [
        "um", "uh", "like", "you know", "basically", "actually"
    ]

    confidence_score = 0

    for word in confidence_words:
        if word in speech:
            confidence_score += 5

    penalty = 0
    for word in filler_words:
        if word in speech:
            penalty += 2

    final_score = max(0, min(100, confidence_score - penalty + 50))

    qualified = final_score >= 45

    return templates.TemplateResponse(
        "jam_result.html",
        {
            "request": request,
            "score": final_score,
            "qualified": qualified,
            "confidence": final_score,
            "improvement": 100 - final_score
        }
    )


# ---------------------------
# HR RESULT
# ---------------------------

@app.get("/hr_result", response_class=HTMLResponse)
async def hr_result(request: Request):

    score = 8
    feedback = "Good communication and confidence."

    return templates.TemplateResponse(
        "hr_result.html",
        {
            "request":request,
            "score":score,
            "feedback":feedback
        }
    )


class HRData(BaseModel):
    answers:list


# ---------------------------
# LEVEL 5 HR ROUND
# ---------------------------

@app.get("/level5")
async def level5(request: Request):

    questions = [
        "Tell me about yourself",
        "Why should we hire you?",
        "Describe a challenge you faced",
        "What are your strengths?",
        "Where do you see yourself in five years?"
    ]

    return templates.TemplateResponse(
        "hr_round.html",
        {
            "request": request,
            "questions": questions
        }
    )


@app.post("/submit_hr",response_class=HTMLResponse)
async def submit_hr(request:Request,data:HRData):

    answers = data.answers

    scores = [7 for _ in answers]

    score = sum(scores) / len(scores)

    feedback = (
        "Excellent communication." if score > 8
        else "Good communication." if score > 6
        else "Needs improvement."
    )

    return templates.TemplateResponse(
        "hr_result.html",
        {
            "request":request,
            "score":score,
            "feedback":feedback
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)