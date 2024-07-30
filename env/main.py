from fastapi import FastAPI
from config import engine
import router
import model 

model.Base.metadata.create_all(bind=engine)




app = FastAPI()


@app.get('/')
async def root():
    return {"message": "This is an API for React CRUD By CowanSoodLorr 65070141. You can go to path /users to check API structure."}

app.include_router(router.router, prefix="/users" , tags=["users"])
