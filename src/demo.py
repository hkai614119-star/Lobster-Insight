from __future__ import annotations

import argparse
import json
from pathlib import Path

from lobster_insight.engine import LobsterInsightEngine
from lobster_insight.models import AnalysisInput
from lobster_insight.render import to_markdown



def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Lobster Insight demo pipeline.")
    parser.add_argument("--input", required=True, help="Path to a JSON file with topic and posts.")
    parser.add_argument("--json-out", help="Optional path to write JSON report.")
    parser.add_argument("--md-out", help="Optional path to write markdown report.")
    args = parser.parse_args()

    input_path = Path(args.input)
    payload_dict = json.loads(input_path.read_text(encoding="utf-8"))
    payload = AnalysisInput.model_validate(payload_dict)

    engine = LobsterInsightEngine()
    report = engine.analyze(payload)

    report_json = report.model_dump_json(indent=2)
    report_md = to_markdown(report)

    print("=== JSON REPORT ===")
    print(report_json)
    print("\n=== MARKDOWN REPORT ===\n")
    print(report_md)

    if args.json_out:
        Path(args.json_out).write_text(report_json, encoding="utf-8")
    if args.md_out:
        Path(args.md_out).write_text(report_md, encoding="utf-8")


if __name__ == "__main__":
    main()

