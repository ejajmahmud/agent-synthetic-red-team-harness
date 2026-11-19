"""Tests for Red Team Harness."""
import unittest
from agent_synthetic_red_team_harness.core import SyntheticRedTeamHarness

class TestSyntheticRedTeamHarness(unittest.TestCase):
    def test_harness_audit(self):
        safe_fn = lambda p: "Access denied"
        card = SyntheticRedTeamHarness.run_suite(safe_fn)
        self.assertEqual(card.defense_rate, 1.0)
        self.assertEqual(card.bypassed, 0)
