from __future__ import annotations

from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".jfif",
    ".webp",
    ".gif",
    ".bmp",
    ".svg",
}


def detect_media_type(file_path: Path) -> str:
    suffix = file_path.suffix.lower()

    if suffix in SUPPORTED_EXTENSIONS:
        return "image"

    return "unknown"


def list_media_files(media_dir: Path) -> list[dict[str, object]]:
    if not media_dir.exists():
        return []

    items: list[dict[str, object]] = []
    for file_path in sorted(media_dir.rglob("*"), key=lambda path: str(path).lower()):
        if not file_path.is_file():
            continue

        suffix = file_path.suffix.lower()
        if suffix not in SUPPORTED_EXTENSIONS:
            continue

        items.append(
            {
                "name": file_path.name,
                "path": str(file_path),
                "media_type": detect_media_type(file_path),
                "extension": suffix,
                "size_bytes": file_path.stat().st_size,
            }
        )

    return items
