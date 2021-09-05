from soccer_game_logic.main import MatchDay

import unittest


class TestMatchDay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.day = {"Team 1": 1, "Team 2": 2, "Team 3": 3, "Team 4": 4}

    def test_day(self):
        self.assertEqual(MatchDay().day, {})

    def test_iter(self):
        match_day = MatchDay()
        match_day.day = self.day
        for item in match_day:
            self.assertIn(item[0], self.day.keys())
            self.assertEqual(item[1], self.day.get(item[0]))

    def test_new_day(self):
        match_day = MatchDay()
        match_day.day = self.day

        same_day_match = {"Team 5": 5, "Team 6": 6}
        self.assertFalse(match_day.new_day(same_day_match))

        new_day_match = {"Team 1": 1, "Team 4": 4}
        self.assertTrue(match_day.new_day(new_day_match))

    def test_call(self):
        match_day = MatchDay()
        match_1 = {"Team 1": 1, "Team 2": 2}
        match_2 = {"Team 3": 3, "Team 4": 4}
        self.assertEqual(match_day.day, {})

        match_day(match_1)
        self.assertEqual(match_day.day, match_1)

        match_day(match_2)
        self.assertNotEqual(match_day.day, match_1)

        match_1.update(match_2)
        self.assertEqual(match_day.day, match_1)


if __name__ == "__main__":
    unittest.main()
