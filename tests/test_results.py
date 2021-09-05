from soccer_game_logic.main import Results, MatchDay

import unittest
from unittest.mock import patch


class NotResults:
    def __init__(self):
        self.match_day = 0
        self.day = MatchDay()
        self._results = {}

    def print(self):
        self._update_results()
        sorted_top_3 = (sorted(self._results.items(), key=lambda x: (-x[1], x[0])))[:3]
        message = [f"\nMatchday {self.match_day}"] + [
            f"{x[0]}, {x[1]}" for x in sorted_top_3
        ]
        print("\n".join(message))

    def _update_results(self):
        self.match_day += 1
        for team, points in self.day:
            total_points = self._results.get(team, 0)
            self._results[team] = total_points + points

    def __call__(self, match):
        if self.day.new_day(match):
            self.print()
            self.day = MatchDay()
        self.day(match)


class TestResults(unittest.TestCase):
    def test_init(self):
        results = Results()
        self.assertEqual(results._match_day, 0)
        self.assertEqual(type(results.day), MatchDay)
        self.assertEqual(results._results, {})

    def test_call(self):
        match_result = {"Team 1": 3, "Team 2": 0}
        results = Results()
        self.assertEqual(results.day.day, {})

        results(match_result)
        self.assertEqual(results.day.day, match_result)

    def test_update_results(self):
        match_result = {"Team 1": 3, "Team 2": 0}
        results = Results()
        results(match_result)
        results._update_results()
        self.assertEqual(results._match_day, 1)
        self.assertEqual(results._results, match_result)

        new_match_result = {"Team 3": 3, "Team 4": 0}
        results(new_match_result)
        match_result.update(new_match_result)
        self.assertEqual(results.day.day, match_result)

    @patch("builtins.print")
    def test_print(self, mock_print):
        results = Results()
        match_results = [
            {"Team 1": 3, "Team 2": 0},
            {"Team 3": 1, "Team 4": 1},
            {"Team 5": 1, "Team 6": 1},
            {"Team 7": 6, "Team 8": 0},
        ]
        for match_result in match_results:
            results(match_result)

        results.print()
        mock_print.assert_called_with("\nMatchday 1\nTeam 7, 6\nTeam 1, 3\nTeam 3, 1")


if __name__ == "__main__":
    unittest.main()
