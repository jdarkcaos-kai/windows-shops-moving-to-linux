import os
from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI(title="Windows shops moving to Linux?")

@app.get("/health")
def health():
    return {"status": "ok", "product": "P-0009"}

@app.get("/", include_in_schema=False)
@app.get("/{_spa_path:path}", include_in_schema=False)
async def _serve_spa(_spa_path: str = ""):
    import os as _os
    _idx = _os.path.join(_os.path.dirname(__file__), "..", "frontend", "index.html")
    if not _os.path.exists(_idx):
        _idx = "frontend/index.html"
    if _os.path.exists(_idx):
        return FileResponse(_idx, media_type="text/html")
    from fastapi.responses import JSONResponse
    return JSONResponse({"error": "frontend not found"}, status_code=404)
