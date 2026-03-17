from __future__ import annotations

import re
from collections import Counter
from typing import Iterable, List, Tuple

HYPE_PATTERNS = [
    r"to the moon",
    r"last chance",
    r"10x",
    r"cannot fail",
    r"guaranteed",
    r"easy money",
    r"smart money",
    r"regret not buying",
    r"explode",
    r"all[- ]?time high",
    r"melt faces",
]

FACT_PATTERNS = [
    r"partnership",
    r"listing",
    r"adoption",
    r"product usage",
    r"timeline",
    r"revenue",
    r"integration",
    r"announcement",
    r"metrics",
]

QUALITY_PATTERNS = [
    r"but",
    r"however",
    r"lack",
    r"little concrete information",
    r"timing",
    r"adoption",
    r"product usage",
    r"risk",
    r"details",
]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())



def count_pattern_hits(texts: Iterable[str], patterns: List[str]) -> int:
    joined = "\n".join(normalize(t) for t in texts)
    return sum(1 for p in patterns if re.search(p, joined, re.IGNORECASE))



def repeated_phrases(texts: Iterable[str], top_n: int = 10) -> List[Tuple[str, int]]:
    tokens: List[str] = []
    for text in texts:
        words = re.findall(r"[a-zA-Z]{4,}", normalize(text))
        tokens.extend(words)
    counts = Counter(tokens)
    return [(word, count) for word, count in counts.most_common(top_n) if count > 1]



def classify_noise_and_temperature(posts: List[str]) -> Tuple[str, str]:
    hype_hits = count_pattern_hits(posts, HYPE_PATTERNS)
    repeats = len(repeated_phrases(posts, top_n=8))
    score = hype_hits + repeats

    if score >= 8:
        return "Extreme", "Euphoric"
    if score >= 5:
        return "High", "Hot"
    if score >= 3:
        return "Medium", "Warm"
    return "Low", "Cold"



def classify_saturation(posts: List[str]) -> str:
    hype_hits = count_pattern_hits(posts, HYPE_PATTERNS)
    fact_hits = count_pattern_hits(posts, FACT_PATTERNS)
    repeats = len(repeated_phrases(posts, top_n=8))

    if hype_hits >= 4 and repeats >= 3 and fact_hits <= 3:
        return "Saturated"
    if hype_hits >= 3 and repeats >= 2:
        return "Overheated"
    if repeats >= 2:
        return "Crowded"
    if fact_hits >= 2:
        return "Building"
    return "Early"



def extract_fact_candidates(posts: List[str]) -> List[str]:
    facts: List[str] = []
    joined = "\n".join(posts).lower()

    if "partnership" in joined:
        facts.append("There is discussion of a possible partnership or partnership-related catalyst.")
    if "listing" in joined:
        facts.append("There is discussion of possible listing expectations.")
    if "product usage" in joined or "adoption" in joined:
        facts.append("Concrete product usage or adoption details appear limited or contested.")
    if "timeline" in joined:
        facts.append("Timing information is mentioned as missing or unclear.")
    if not facts:
        facts.append("Most visible content is emotional or speculative, with few clearly verifiable facts.")
    return facts



def extract_quality_viewpoints(posts: List[str]) -> List[str]:
    quality = []
    for post in posts:
        p = normalize(post)
        if any(re.search(pattern, p, re.IGNORECASE) for pattern in QUALITY_PATTERNS):
            quality.append(post.strip())
    deduped = []
    seen = set()
    for item in quality:
        key = item.lower()
        if key not in seen:
            deduped.append(item)
            seen.add(key)
    return deduped[:3]

