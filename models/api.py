#
# api.py
#
# Server API models.
#

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel

from .token_usage import TokenUsage


class Role(str, Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"

class Message(BaseModel):
    role: Role
    content: str

class Capability(str, Enum):
    ASSISTANT_KNOWLEDGE = "assistant_knowledge"
    WEB_SEARCH = "web_search"
    VISION = "vision"
    REVERSE_IMAGE_SEARCH = "reverse_image_search"
    IMAGE_GENERATION = "image_generation"

class SearchEngine(str, Enum):
    GOOGLE_REVERSE_IMAGE = "google_reverse_image"
    GOOGLE_LENS = "google_lens"
    GOOGLE = "google"
    GOOGLE_JOBS = "google_jobs"
    GOOGLE_NEWS = "google_news"
    GOOGLE_SHOPPING = "google_shopping"
    GOOGLE_TRAVEL = "google_travel"
    GOOGLE_LOCAL = "google_local"
    GOOGLE_IMERSIVE_PRODUCT = "google_immersive_product"
    GOOGLE_FINANCE = "google_finance"
    GOOGLE_EVENTS = "google_events"
    GOOGLE_SCHOLAR = "google_scholar"

class SearchAPI(Enum):
    SERP = "serp"
    DATAFORSEO = "dataforseo"
    PERPLEXITY = "perplexity"

class VisionModel(str, Enum):
    GPT4O = "gpt-4o"
    GPT4Vision = "gpt-4-vision-preview"
    CLAUDE_HAIKU = "claude-3-haiku-20240307"
    CLAUDE_SONNET = "claude-3-sonnet-20240229"
    CLAUDE_OPUS = "claude-3-opus-20240229"

class GenerateImageService(str, Enum):
    REPLICATE   = "replicate"

class MultimodalRequest(BaseModel):
    messages: Optional[List[Message]]
    prompt: Optional[str] = ""
    noa_system_prompt: Optional[str] = None
    local_time: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    generate_image_service: Optional[GenerateImageService] = GenerateImageService.REPLICATE

class MultimodalResponse(BaseModel):
    user_prompt: str
    response: str
    image: str
    token_usage_by_model: Dict[str, TokenUsage]
    capabilities_used: List[Capability]
    timings: Dict[str, float]
    stream_finished: bool = True

class ExtractLearnedContextRequest(BaseModel):
    messages: List[Message]
    existing_learned_context: Dict[str, str]

class ExtractLearnedContextResponse(BaseModel):
    learned_context: Dict[str, str]
    token_usage_by_model: Dict[str, TokenUsage]