from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .scanner import list_media_files

app = FastAPI(
    title="Inspiration Library Local Processor",
    version="0.1.0",
    description="Local media ingestion and metadata processing for the inspiration library.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MEDIA_DIR = Path(__file__).resolve().parents[3] / "Medias"


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "inspiration-local-processor"}


@app.get("/api/media")
def media() -> dict[str, object]:
    items = list_media_files(MEDIA_DIR)
    return {
        "folder": str(MEDIA_DIR),
        "count": len(items),
        "items": items,
    }


@app.get("/api/media/summary")
def summary() -> dict[str, object]:
    items = list_media_files(MEDIA_DIR)
    return {
        "folder": str(MEDIA_DIR),
        "image_count": len(items),
        "media_types": {"image": len(items)},
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
