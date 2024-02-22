from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users,auth, votes
from fastapi.middleware.cors import CORSMiddleware



    



# models.Base.metadata.create_all(bind=engine)


app =FastAPI()

origins = [
    "https://www.google.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.google.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
async def home():
    return {"message":"This is home"}
    
    
    

        


    
    

    
    