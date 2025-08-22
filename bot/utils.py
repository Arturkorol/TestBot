from __future__ import annotations

from typing import Any


async def generate_request_pdf(data: Any) -> bytes:
    """Generate a PDF representation of the provided data.

    This is a stub implementation that simply encodes the string
    representation of ``data`` into bytes. Real implementations would
    create a proper PDF file.
    """

    return str(data).encode("utf-8")


async def send_email(content: bytes) -> None:
    """Send an e-mail with the provided content.

    This stub does not actually send anything but provides the expected
    interface for the rest of the application.
    """

    return None
