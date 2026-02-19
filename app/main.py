# from fastapi import FastAPI, UploadFile
# from app.api import upload_router, verify_router

# app = FastAPI()

# app.include_router(upload_router.router)


from fastapi import FastAPI
from app.db.database import engine
from app.db.models import Base
from app.api.upload_router import router as upload_router
from app.api.verify_router import router as verify_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)
app.include_router(verify_router)

