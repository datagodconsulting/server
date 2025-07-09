from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import user, client, advocate, case, appointment, document, upload
from app.core.config import CORS_ALLOWED_ORIGINS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin for origin in CORS_ALLOWED_ORIGINS if origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(client.router)
app.include_router(advocate.router)
app.include_router(case.router)
app.include_router(appointment.router)
app.include_router(document.router)
app.include_router(upload.router) 