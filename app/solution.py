from typing import Final, List, Optional, Dict, Callable


KEYPAD: Final[List[List[Optional[str]]]] = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    [None, "1", "2", "3", None],
]

TARGET_SEQUENCE_LENGTH: Final[int] = 10
MAX_NUMBER_OF_VOWELS: Final[int] = 2


def IS_VOWEL(key: str) -> bool:
    return key in ["A", "E", "I", "O", "U"]


# Represents valid changes to a row and column index to get new potential move
KNIGHT_MOVES: Final[List[tuple]] = [
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
]


class SequenceCounter:
    def __init__(
        self,
        keypad: List[List[str]],
        target_sequence_length: int,
        max_count: int,
        valid_moves: List[tuple[int, int]],
        count_me: Callable[int, bool],
    ) -> None:
        self.keypad = keypad
        self.target_sequence_length = target_sequence_length
        self.max_count = max_count
        self.valid_moves = valid_moves
        self.count_me = count_me
        self.graph = self._create_graph()

    def _get_valid_moves(
        self, row_index: int, column_index: int, row_length: int, column_length: int
    ) -> List[str]:
        """
        Get all valid moves originating from self.keypad[row_index][column_index]
        """
        valid_moves = []
        for row_operand, column_operand in self.valid_moves:
            new_row = row_index + row_operand
            new_column = column_index + column_operand
            new_key_exists = (0 <= new_row < row_length) and (
                0 <= new_column < column_length
            )

            if new_key_exists:
                new_key = self.keypad[new_row][new_column]

                if not new_key:
                    continue

                valid_moves.append(new_key)

        return valid_moves

    def _create_graph(self) -> Dict[str, List[str]]:
        """
        Create a graph (dictionary) data structure mapping keys (node) to valid new keys (edges)
        """
        graph = {}
        row_length = len(self.keypad)
        column_length = len(self.keypad[0])

        for row_index in range(row_length):
            for column_index in range(column_length):
                key = self.keypad[row_index][column_index]

                if not key:
                    continue

                valid_moves = self._get_valid_moves(
                    row_index=row_index,
                    column_index=column_index,
                    row_length=row_length,
                    column_length=column_length,
                )
                graph[key] = valid_moves

        return graph

    def _get_sequences(
        self, key: str, sequence: Optional[List[str]] = None, count: int = 0
    ) -> List[List[str]]:
        """
        Get all valid sequences originating from key.
        """
        sequences = []

        if sequence is None:
            sequence = [key]

        if self.count_me(key):
            count += 1

        if count > self.max_count:
            return []

        if len(sequence) == self.target_sequence_length:
            return [sequence]

        valid_moves = self.graph[key]
        for next_key in valid_moves:
            sequences.extend(
                self._get_sequences(
                    key=next_key, sequence=sequence + [next_key], count=count
                )
            )

        return sequences

    def count_sequences(self) -> int:
        """
        Count the sum of distinct sequences that can be made using the keypad
        """
        sequences = []

        for key in self.graph.keys():
            sequences.extend(self._get_sequences(key=key))

        return len(sequences)


if __name__ == "__main__":
    sequence_counter = SequenceCounter(
        keypad=KEYPAD,
        target_sequence_length=TARGET_SEQUENCE_LENGTH,
        max_count=MAX_NUMBER_OF_VOWELS,
        valid_moves=KNIGHT_MOVES,
        count_me=IS_VOWEL,
    )

    total_sequences = sequence_counter.count_sequences()
    print(total_sequences)
