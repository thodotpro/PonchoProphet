# backend/app/schemas.py
# This file is the contract between Dev A and Dev B.
# Neither side changes it without telling the other.

from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    session_id: str          # Dev B generates this (uuid4) in the Vue app
    location: str            # e.g. "Vienna, Austria"
    message: str             # e.g. "What should I wear today?"

class ChatResponse(BaseModel):
    session_id: str
    answer: str              # The outfit recommendation text
    weather_summary: str     # e.g. "12°C, light rain" — shown in the UI
    active_agent: str        # e.g. "outfit_agent" — powers the StatusBadge component
    cache_hit: bool          # Dev B shows a small cache indicator with this