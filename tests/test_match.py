from soccer_game_logic.main import Match

import unittest


class TestMatch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw_match_data = "Team Hello World 1, Team Foo Bar 2"
        cls.match = Match(cls.raw_match_data)

    def test_raw_match_data(self):
        self.assertEqual(self.raw_match_data, self.match.raw_match_data)

    def test_parse_raw_match_data(self):
        parsed_match_data = {"Team Hello World": 1, "Team Foo Bar": 2}
        self.assertEqual(self.match.parse_raw_match_data(), parsed_match_data)
        self.assertEqual(self.match.match_data, parsed_match_data)

    def test_match_result(self):
        match_result = {"Team Hello World": 0, "Team Foo Bar": 3}
        self.assertEqual(self.match.match_result, match_result)

    def test_tie(self):
        raw_match_data = "Team 1 2, Team 2 2"
        tie_match = Match(raw_match_data)
        match_result = {"Team 1": 1, "Team 2": 1}
        self.assertEqual(tie_match.match_result, match_result)


if __name__ == "__main__":
    unittest.main()
