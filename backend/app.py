from typing import Union
from fastapi import FastAPI
# from agents.image_extractor_from_files import get_file
from backend.agents import image_extractor_from_files
from pydantic import BaseModel
from fastapi import UploadFile, File, HTTPException
import tempfile
import base64
import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

class FileURL(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/url-file")
async def receive_url_file(payload: FileURL):
    await image_extractor_from_files.get_file(payload.url)
    # Add logic to process the file at payload.url
    return {"status": "File received", "file_url": payload.url}

@app.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    allowed = {"png", "jpeg", "jpg", "docx", "pptx", "xlsx", "pdf"}
    ext = file.filename.rsplit(".", 1)[-1].lower()
    
    # if ext not in allowed:
    #     raise HTTPException(status_code=400, detail="File type not allowed.")
    ext = "." + ext

    # else:
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        image_urls = []

        tmp.write(await file.read())
        tmp.flush()
        print(f"Temporary file created: {tmp.name}")
        output = await image_extractor_from_files.get_file(tmp.name)
        if isinstance(output, list):
            for i in range(0,len(output)):
                output[i] = output[i].replace("\\n\\n", "\n")

    return {"output": output}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=3100)

