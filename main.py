from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import uuid
from app.inference import run_inference
from pathlib import Path
import os
import traceback



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "KTSA API is running"}

UPLOAD_DIR = Path("inference/images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Create a temp dir to save uploaded image
        temp_dir = Path("inference/images")
        temp_dir.mkdir(parents=True, exist_ok=True)

        # Save uploaded image
        #unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run inference
        result = run_inference(source_path=file_path)

        # Return basic success (modify as per result format from detect_count)
        return JSONResponse(content={"status": "success", "image_processed": file.filename, "output_dir": "runs/detect/exp" })

    except Exception as e:
        traceback.print_exc()
        return JSONResponse({"status": "error", "detail": str(e)}, status_code=500)
