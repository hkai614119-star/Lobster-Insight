from __future__ import annotations

from typing import List

from .heuristics import (
    classify_noise_and_temperature,
    classify_saturation,
    extract_fact_candidates,
    extract_quality_viewpoints,
)
from .models import AnalysisInput, AnalysisReport


class LobsterInsightEngine:
    """Lightweight demo engine for structured social-sentiment reports."""

    def analyze(self, payload: AnalysisInput) -> AnalysisReport:
        noise_level, emotional_temperature = classify_noise_and_temperature(payload.posts)
        saturation = classify_saturation(payload.posts)
        fact_extraction = extract_fact_candidates(payload.posts)
        quality_views = extract_quality_viewpoints(payload.posts)

        crowd_behavior = self._diagnose_crowd_behavior(payload.posts, saturation, emotional_temperature)
        risk = self._contrarian_risk(payload.posts, saturation, fact_extraction)
        actions = self._suggest_actions(saturation, emotional_temperature, fact_extraction)
        watch_next = self._watch_next(fact_extraction)
        verdict = self._verdict(saturation, fact_extraction, emotional_temperature)
        confidence, confidence_reason = self._confidence(fact_extraction, quality_views)

        return AnalysisReport(
            topic=payload.topic,
            noise_level=noise_level,
            emotional_temperature=emotional_temperature,
            narrative_saturation=saturation,
            fact_extraction=fact_extraction,
            crowd_behavior_diagnosis=crowd_behavior,
            minority_high_quality_viewpoints=quality_views or ["No clear minority high-quality viewpoint surfaced in this batch."],
            contrarian_risk_assessment=risk,
            suggested_action=actions,
            invalidation_watch_next=watch_next,
            final_one_line_verdict=verdict,
            confidence=confidence,
            confidence_reason=confidence_reason,
        )

    def _diagnose_crowd_behavior(self, posts: List[str], saturation: str, temp: str) -> str:
        if saturation in {"Overheated", "Saturated"}:
            return (
                "The crowd is repeating bullish excitement, compressing uncertainty into certainty, "
                "and treating rumor or momentum as confirmation."
            )
        if temp in {"Warm", "Hot"}:
            return "The crowd is leaning bullish and increasingly focused on momentum-driven interpretation."
        return "The crowd behavior appears mixed and not yet one-sided."

    def _contrarian_risk(self, posts: List[str], saturation: str, facts: List[str]) -> str:
        fact_text = " ".join(facts).lower()
        if saturation in {"Overheated", "Saturated"} and ("limited" in fact_text or "possible" in fact_text):
            return (
                "Sentiment may be running ahead of verification. Upside expectations look crowded while the fact base "
                "remains thin, increasing the risk of emotional chasing and expectation compression."
            )
        if saturation == "Crowded":
            return "Consensus may be getting busy enough that risk/reward is no longer as favorable as the narrative implies."
        return "The main risk is low-quality information rather than extreme sentiment saturation."

    def _suggest_actions(self, saturation: str, temp: str, facts: List[str]) -> List[str]:
        actions = []
        if saturation in {"Overheated", "Saturated"}:
            actions.append("Avoid chasing emotionally extended momentum.")
            actions.append("Wait for confirmation from concrete information rather than crowd repetition.")
            actions.append("Keep position size disciplined and reduce emotional exposure.")
        else:
            actions.append("Observe only until stronger confirmation appears.")
            actions.append("Track whether new information materially improves the fact base.")

        if any("listing" in fact.lower() or "partnership" in fact.lower() for fact in facts):
            actions.append("Watch for official details, timelines, or adoption metrics before upgrading conviction.")
        return actions

    def _watch_next(self, facts: List[str]) -> List[str]:
        watch = [
            "Official confirmation of any rumored catalyst.",
            "Concrete timeline information.",
            "Evidence of product usage, adoption, or measurable integration.",
        ]
        if any("listing" in fact.lower() for fact in facts):
            watch.append("Whether listing expectations are confirmed, denied, or delayed.")
        return watch

    def _verdict(self, saturation: str, facts: List[str], temp: str) -> str:
        if saturation in {"Overheated", "Saturated"}:
            return "The market mood is hot, but the information base is still too thin to justify emotional chasing."
        if temp in {"Warm", "Hot"}:
            return "Interest is building, but conviction should wait for better facts and less crowd-driven urgency."
        return "Signal quality remains mixed, so patient observation is smarter than excitement."

    def _confidence(self, facts: List[str], quality_views: List[str]) -> tuple[str, str]:
        if quality_views and not any("few clearly verifiable facts" in fact.lower() for fact in facts):
            return "Medium", "There is at least one quality counter-view, but hard verification is still limited."
        return "Low", "The current batch is dominated by hype language and weak factual density."

