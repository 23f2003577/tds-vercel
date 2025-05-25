from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/api")
def search(request: Request):
    parameters = list()

    for param in request.query_params.keys():
        parameters.append(param)

    return {"parameters": parameters}
