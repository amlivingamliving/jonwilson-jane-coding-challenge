from soccer_game_logic.main import Input

import unittest


class TestInput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_filename = "tests/input_test_file.txt"
        cls.stream = Input(cls.input_filename)

    def test_input_file(self):
        self.assertEqual(self.input_filename, self.stream.input_file)

    def test_input_iter(self):
        count = 1
        for item in self.stream:
            self.assertEqual(item.strip(), f"testing{count}")
            count += 1


if __name__ == "__main__":
    unittest.main()
