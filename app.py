from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel
import subprocess
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        process = subprocess.run(["python", "main.py"], capture_output=True, text=True)
        if process.returncode == 0:
            return Response("Training successful!")
        else:
            return Response(f"Training failed: {process.stderr}")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
async def predict_route(request: PredictRequest):
    try:
        obj = PredictionPipeline()
        result = obj.predict(request.text)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)