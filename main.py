import hashlib

from fastapi import FastAPI
from controllers import (
    group_controller,
    school_controller,
    degree_controller,
    promotion_controller,
    semester_controler,
    studytime_controller,
    studentgroup_controller,
    subject_controller,
    score_controller,
    auth_controller
)
from db.database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student API")

app.include_router(degree_controller.router)
app.include_router(school_controller.router)
app.include_router(promotion_controller.router)
app.include_router(semester_controler.router)
app.include_router(group_controller.router)
app.include_router(studytime_controller.router)
app.include_router(studentgroup_controller.router)
app.include_router(subject_controller.router)
app.include_router(score_controller.router)
# app.include_router(auth_controller.router)
