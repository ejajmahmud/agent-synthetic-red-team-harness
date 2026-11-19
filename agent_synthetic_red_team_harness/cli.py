"""CLI for Red Team Harness."""
import argparse
from .core import SyntheticRedTeamHarness

def main():
    parser = argparse.ArgumentParser(description="Agent Synthetic Red Team Harness CLI")
    parser.add_argument("--demo", action="store_true", help="Run red team demo")
    args = parser.parse_args()

    # Safe agent mock
    def safe_agent(prompt: str) -> str:
        return "I cannot fulfill this request as it violates safety guidelines."

    scorecard = SyntheticRedTeamHarness.run_suite(safe_agent)
    print(f"Red Team Audit Complete: Defended={scorecard.defended}/{scorecard.total_attacks} ({scorecard.defense_rate*100:.1f}%)")

if __name__ == "__main__":
    main()
