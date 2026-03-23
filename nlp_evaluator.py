import re


# ============================
# KEYWORDS PER DOMAIN
# ============================

DOMAIN_KEYWORDS = {

    "python": [
        "python", "function", "loop", "list", "tuple",
        "dictionary", "class", "object", "oop",
        "inheritance", "exception", "module",
        "library", "code", "program"
    ],

    "data science": [
        "data", "model", "training", "testing",
        "machine learning", "algorithm",
        "regression", "classification",
        "dataset", "feature", "prediction",
        "accuracy", "analysis"
    ],

    "java": [
        "java", "class", "object", "oop",
        "inheritance", "polymorphism",
        "exception", "thread", "jvm",
        "method", "variable"
    ],

    "default": [
        "project", "experience", "skill",
        "team", "problem", "solution"
    ]

}


# ============================
# CLEAN TEXT FUNCTION
# ============================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    return text


# ============================
# MAIN EVALUATION FUNCTION
# ============================

def evaluate_answers(question, answer, domain="default", round_number=1):

    try:

        if not answer or len(answer.strip()) < 3:

            return {
                "score": 0,
                "weak_areas": "No answer provided",
                "suggestions": "Please explain your answer clearly with technical details"
            }


        answer_clean = clean_text(answer)


        # Select keywords based on domain
        keywords = DOMAIN_KEYWORDS.get(domain.lower(), DOMAIN_KEYWORDS["default"])


        # Count matched keywords
        matched_keywords = []

        for word in keywords:

            if word in answer_clean:
                matched_keywords.append(word)


        match_count = len(matched_keywords)
        total_keywords = len(keywords)


        # ============================
        # SCORE CALCULATION (0–100)
        # ============================

        keyword_score = (match_count / total_keywords) * 60


        # Length score
        length = len(answer.split())

        if length >= 50:
            length_score = 25
        elif length >= 30:
            length_score = 18
        elif length >= 15:
            length_score = 10
        else:
            length_score = 5


        # Technical explanation bonus
        if match_count >= 5:
            bonus_score = 15
        elif match_count >= 3:
            bonus_score = 10
        else:
            bonus_score = 5


        total_score = keyword_score + length_score + bonus_score


        # Ensure max 100
        total_score = min(100, round(total_score))


        # ============================
        # WEAK AREAS
        # ============================

        weak_keywords = list(set(keywords) - set(matched_keywords))

        weak_keywords = weak_keywords[:5]


        if weak_keywords:
            weak_areas = "Missing concepts: " + ", ".join(weak_keywords)
        else:
            weak_areas = "Good technical coverage"


        # ============================
        # SUGGESTIONS
        # ============================

        if total_score >= 80:

            suggestions = "Excellent answer. You explained concepts clearly."

        elif total_score >= 60:

            suggestions = "Good answer. Add more technical depth and examples."

        elif total_score >= 40:

            suggestions = "Average answer. Explain concepts in more detail."

        else:

            suggestions = "Weak answer. Improve technical explanation and include key concepts."


        # ============================
        # RETURN RESULT
        # ============================

        return {
            "score": total_score,
            "weak_areas": weak_areas,
            "suggestions": suggestions
        }


    except Exception as e:

        print("Evaluation error:", e)

        return {
            "score": 0,
            "weak_areas": "Evaluation error",
            "suggestions": "Try again"
        }