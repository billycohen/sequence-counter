import unittest

from app.solution import (
    IS_VOWEL,
    KEYPAD,
    KNIGHT_MOVES,
    MAX_NUMBER_OF_VOWELS,
    SequenceCounter,
)

TEST_SEQUENCE_LENGTH = 4


class TestSequenceCounter(unittest.TestCase):
    def test_count_sequences_full_keypad(self):
        counter = SequenceCounter(
            keypad=KEYPAD,
            target_sequence_length=TEST_SEQUENCE_LENGTH,
            max_count=MAX_NUMBER_OF_VOWELS,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        self.assertEqual(counter.count_sequences(), 732)

    def test_count_sequences_length_two(self):
        counter = SequenceCounter(
            keypad=KEYPAD,
            target_sequence_length=1,
            max_count=MAX_NUMBER_OF_VOWELS,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        self.assertEqual(counter.count_sequences(), len(counter.graph.keys()))

    def test_count_sequences_length_one(self):
        counter = SequenceCounter(
            keypad=[["A"]],
            target_sequence_length=1,
            max_count=2,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        self.assertEqual(counter.count_sequences(), 1)

    def test_count_sequences_tiny_keypad_length_two(self):
        counter = SequenceCounter(
            keypad=[["A", "B"]],
            target_sequence_length=2,
            max_count=2,
            valid_moves=[(0, 1), (0, -1)],  # left/right
            count_me=IS_VOWEL,
        )
        self.assertEqual(counter.count_sequences(), 2)

    def test_graph_contains_all_keys(self):
        counter = SequenceCounter(
            keypad=KEYPAD,
            target_sequence_length=TEST_SEQUENCE_LENGTH,
            max_count=MAX_NUMBER_OF_VOWELS,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        expected_keys = {
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "1",
            "2",
            "3",
        }
        self.assertEqual(set(counter.graph.keys()), expected_keys)

    def test_vowel_constraint_reduces_count(self):
        counter_two_vowels = SequenceCounter(
            keypad=KEYPAD,
            target_sequence_length=TEST_SEQUENCE_LENGTH,
            max_count=2,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        counter_zero_vowels = SequenceCounter(
            keypad=KEYPAD,
            target_sequence_length=TEST_SEQUENCE_LENGTH,
            max_count=0,
            valid_moves=KNIGHT_MOVES,
            count_me=IS_VOWEL,
        )
        self.assertGreater(
            counter_two_vowels.count_sequences(), counter_zero_vowels.count_sequences()
        )


if __name__ == "__main__":
    unittest.main()
