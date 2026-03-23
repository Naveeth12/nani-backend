def generate_feedback(score, level=1):

    if level == 1:
        if score >= 2:
            return f"Great job! You passed Level 1 with score {score}."
        else:
            return f"You scored {score}. Improve basic aptitude and try again."

    if level == 2:
        if score >= 2:
            return f"Excellent! You cleared Level 2 with score {score}."
        else:
            return f"You scored {score}. Practice more advanced problems."

    return f"Your score is {score}."


def level2_feedback(score):

    if score >= 25:
        return "Excellent technical knowledge!"

    elif score >= 20:
        return "Good technical understanding."

    else:
        return "You need to improve technical skills."