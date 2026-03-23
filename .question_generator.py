import random


# ===============================
# MNC COMPANY INTERVIEW ROUNDS
# (Google, Microsoft, Amazon)
# ===============================

MNC_QUESTIONS = {

    "python": {

        1: [
            "Tell me about yourself",
            "Explain Python and its features",
            "What are Python data types?",
            "What is the difference between list and tuple?"
        ],

        2: [
            "Write a Python program to reverse a string",
            "Write a Python program to find duplicate elements in a list",
            "Explain list comprehension with example",
            "Write a program to check palindrome"
        ],

        3: [
            "Explain multithreading in Python",
            "What is GIL in Python?",
            "Explain decorators",
            "Explain generators vs iterators"
        ],

        4: [
            "Why do you want to join our company?",
            "What are your strengths and weaknesses?",
            "Where do you see yourself in 5 years?",
            "Tell me about a challenge you faced"
        ]
    },


    "data science": {

        1: [
            "What is Data Science?",
            "Explain Machine Learning types",
            "Difference between AI and ML",
            "Explain supervised learning"
        ],

        2: [
            "Explain Linear Regression",
            "What is overfitting?",
            "Explain train test split",
            "Explain bias vs variance"
        ],

        3: [
            "Explain Random Forest",
            "Explain Gradient Boosting",
            "Explain Neural Networks",
            "Explain Cross Validation"
        ],

        4: [
            "Why Data Science?",
            "Explain your projects",
            "What motivates you?",
            "Why should we hire you?"
        ]
    },


    "java": {

        1: [
            "Explain Java and its features",
            "What is OOP?",
            "Explain JVM",
            "Difference between JDK and JRE"
        ],

        2: [
            "Write a Java program to reverse string",
            "Explain ArrayList",
            "Explain exception handling",
            "Explain collections framework"
        ],

        3: [
            "Explain multithreading",
            "Explain synchronization",
            "Explain design patterns",
            "Explain Spring Boot"
        ],

        4: [
            "Why Java?",
            "Tell me about yourself",
            "Why should we hire you?",
            "Your career goals?"
        ]
    }
}


# ===============================
# SERVICE COMPANY QUESTIONS
# (Infosys, TCS, Wipro)
# ===============================

SERVICE_QUESTIONS = {

    "python": {

        1: [
            "Tell me about yourself",
            "What is Python?",
            "Explain variables",
            "Explain loops"
        ],

        2: [
            "Explain functions",
            "Explain OOP",
            "Explain list and tuple",
            "Explain dictionary"
        ],

        3: [
            "Why should we hire you?",
            "Are you willing to relocate?",
            "Explain your project",
            "What are your strengths?"
        ]
    },


    "data science": {

        1: [
            "What is Data Science?",
            "Explain ML basics",
            "Explain datasets",
            "Explain pandas"
        ],

        2: [
            "Explain regression",
            "Explain classification",
            "Explain model training",
            "Explain accuracy"
        ],

        3: [
            "Why Data Science?",
            "Explain your project",
            "Why should we hire you?",
            "Your strengths?"
        ]
    },


    "java": {

        1: [
            "Explain Java",
            "Explain OOP",
            "Explain variables",
            "Explain loops"
        ],

        2: [
            "Explain classes and objects",
            "Explain inheritance",
            "Explain polymorphism",
            "Explain exception handling"
        ],

        3: [
            "Why Java?",
            "Explain your project",
            "Why should we hire you?",
            "Your strengths?"
        ]
    }
}


# ===============================
# DEFAULT QUESTIONS
# ===============================

DEFAULT_QUESTIONS = {
    1: ["Tell me about yourself"],
    2: ["Explain your technical skills"],
    3: ["Explain your project"],
    4: ["Why should we hire you?"]
}


# ===============================
# MAIN FUNCTION
# ===============================

def generate_question(domain, company_type, round_number):

    domain = domain.lower()

    try:

        # MNC COMPANY
        if company_type == "mnc":

            if domain in MNC_QUESTIONS:
                questions = MNC_QUESTIONS[domain].get(round_number)

                if questions:
                    return random.choice(questions)

        # SERVICE COMPANY
        else:

            if domain in SERVICE_QUESTIONS:
                questions = SERVICE_QUESTIONS[domain].get(round_number)

                if questions:
                    return random.choice(questions)

        # DEFAULT FALLBACK
        return random.choice(DEFAULT_QUESTIONS.get(round_number, DEFAULT_QUESTIONS[1]))

    except Exception as e:

        print("Question generation error:", e)

        return "Tell me about yourself"



# ==================================================
# HR ROUND QUESTIONS FUNCTION (ADDED ONLY)
# ==================================================

def get_hr_questions():

    hr_questions = [

        "Tell me about yourself",

        "Why do you want to join our company?",

        "What are your strengths and weaknesses?",

        "Where do you see yourself in 5 years?",

        "Tell me about a challenge you faced",

        "Why should we hire you?",

        "Describe a difficult situation and how you handled it",

        "What motivates you to work?",

        "How do you handle pressure at work?",

        "What are your career goals?"

    ]

    return random.sample(hr_questions, 5)