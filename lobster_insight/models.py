from __future__ import annotations

from typing import List
from pydantic import BaseModel, Field


class AnalysisInput(BaseModel):
    topic: str = Field(..., description="Topic or narrative being analyzed")
    posts: List[str] = Field(..., min_length=1, description="Social posts to analyze")


class AnalysisReport(BaseModel):
    topic: str
    noise_level: str
    emotional_temperature: str
    narrative_saturation: str
    fact_extraction: List[str]
    crowd_behavior_diagnosis: str
    minority_high_quality_viewpoints: List[str]
    contrarian_risk_assessment: str
    suggested_action: List[str]
    invalidation_watch_next: List[str]
    final_one_line_verdict: str
    confidence: str
    confidence_reason: str

