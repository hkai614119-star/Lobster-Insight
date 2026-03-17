from __future__ import annotations

from .models import AnalysisReport



def to_markdown(report: AnalysisReport) -> str:
    lines = [
        "# Lobster Insight Report",
        "",
        f"**Topic:** {report.topic}",
        "",
        "## 1. Noise Level",
        report.noise_level,
        "",
        "## 2. Emotional Temperature",
        report.emotional_temperature,
        "",
        "## 3. Narrative Saturation",
        report.narrative_saturation,
        "",
        "## 4. Fact Extraction",
    ]
    lines.extend([f"- {item}" for item in report.fact_extraction])
    lines.extend([
        "",
        "## 5. Crowd Behavior Diagnosis",
        report.crowd_behavior_diagnosis,
        "",
        "## 6. Minority High-Quality Viewpoints",
    ])
    lines.extend([f"- {item}" for item in report.minority_high_quality_viewpoints])
    lines.extend([
        "",
        "## 7. Contrarian Risk Assessment",
        report.contrarian_risk_assessment,
        "",
        "## 8. Suggested Action",
    ])
    lines.extend([f"- {item}" for item in report.suggested_action])
    lines.extend([
        "",
        "## 9. Invalidation / What to Watch Next",
    ])
    lines.extend([f"- {item}" for item in report.invalidation_watch_next])
    lines.extend([
        "",
        "## 10. Final One-Line Verdict",
        report.final_one_line_verdict,
        "",
        f"**Confidence:** {report.confidence}",
        f"**Reason:** {report.confidence_reason}",
    ])
    return "\n".join(lines)
