from sqlalchemy.orm import Session
import models


# =====================================
# CREATE USER
# =====================================
def create_user(db: Session, name: str, email: str, branch: str, domain: str):

    # Check if user already exists
    existing_user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if existing_user:
        return existing_user

    user = models.User(
        name=name,
        email=email,
        branch=branch,
        domain=domain
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# =====================================
# GET USER BY EMAIL
# =====================================
def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(
        models.User.email == email
    ).first()


# =====================================
# GET ALL USERS
# =====================================
def get_users(db: Session):

    return db.query(models.User).all()


# =====================================
# SAVE INTERVIEW RESULT
# =====================================
def save_interview(

    db: Session,
    user_id: int,
    question: str,
    answer: str,
    score: int,
    weak_areas: str,
    suggestions: str

):

    interview = models.Interview(

        user_id=user_id,
        question=question,
        answer=answer,
        score=score,
        weak_areas=weak_areas,
        suggestions=suggestions
    )

    db.add(interview)
    db.commit()
    db.refresh(interview)

    return interview


# =====================================
# GET INTERVIEWS BY USER
# =====================================
def get_user_interviews(db: Session, user_id: int):

    return db.query(models.Interview).filter(
        models.Interview.user_id == user_id
    ).all()


# =====================================
# GET ALL INTERVIEWS
# =====================================
def get_all_interviews(db: Session):

    return db.query(models.Interview).all()