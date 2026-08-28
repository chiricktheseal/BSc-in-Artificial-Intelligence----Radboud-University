import math
import random
from typing import Self


class Stone:
    RADIUS = 0.15

    def __init__(
        self,
        is_red: bool,
        xy: tuple[float, float],
        round: int,
        red_hammer: bool,
        burned: bool = False,
    ) -> None:
        if round < 1 or round > 10:
            raise ValueError("Round must be between 1 and 10.")

        self.out_of_play = False
        self.x, self.y = xy
        self.round = round
        self.is_red = is_red
        self.red_hammer = red_hammer

        if burned:
            self.burn()
        else:
            if self.is_out_of_bounds():
                raise ValueError("Stone position is out of bounds.")

    def is_out_of_play(self: Self) -> bool:
        return self.out_of_play

    def burn(self: Self) -> None:
        if self.out_of_play:
            raise ValueError("Stone is already out of play.")

        self.move_out_of_play()

    def move_out_of_play(self: Self) -> None:
        if self.out_of_play:
            raise ValueError("Stone is already out of play.")

        if self.is_red:
            self.x = -2.5
        else:
            self.x = 2.5

        self.y = 5.49
        self.out_of_play = True

    def move(self: Self, dxy: tuple[float, float], in_round: int, by_red: bool) -> bool:
        if self.out_of_play:
            raise ValueError("Cannot move an out-of-play stone.")

        old_x = self.x
        old_y = self.y

        self.x += dxy[0]
        self.y += dxy[1]

        if self.is_guard():
            if self.red_hammer and by_red or not self.red_hammer and not by_red:
                within_first_five_stones = in_round <= 3
            else:
                within_first_five_stones = in_round <= 2

            if within_first_five_stones and self.is_out_of_bounds():
                self.x = old_x
                self.y = old_y
                return False

        if self.is_out_of_bounds():
            self.move_out_of_play()

        return True

    def is_guard(self: Self) -> bool:
        if self.out_of_play:
            return False

        return (
            self.is_passed_hogline()
            and not self.is_in_house()
            and not self.is_out_of_bounds()
        )

    def is_out_of_bounds(self: Self) -> bool:
        if self.out_of_play:
            return False

        return self.x < -2.5 or self.x > 2.5 or self.y < -6.401 or self.y > 5.49

    def is_in_house(self: Self) -> bool:
        if self.out_of_play:
            return False

        return self.distance_to_center() <= 1.83

    def is_passed_hogline(self: Self) -> bool:
        if self.out_of_play:
            return False

        return self.y > -6.401

    def distance_to_center(self: Self) -> float:
        if self.out_of_play:
            raise ValueError("Cannot calculate distance to center for a burned stone.")

        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self: Self) -> str:
        color = "Red" if self.is_red else "Yellow"
        return f"{color} stone at ({self.x:.2f}, {self.y:.2f}), round {self.round}, {'burned' if self.out_of_play else 'active'}"


class End:
    def __init__(self, red_hammer: bool) -> None:
        self.red_hammer: bool = red_hammer
        self.stones: list[Stone] = []

    def add_stone(self: Self, stone: Stone) -> None:
        if len(self.stones) >= 16:
            raise ValueError("Cannot add more than 16 stones to an end.")

        if len(self.stones) == 0:
            if stone.is_red == self.red_hammer:
                raise ValueError(
                    "The first stone must be thrown by the team without the hammer."
                )
        elif self.stones[-1].is_red == stone.is_red:
            raise ValueError("Cannot place two stones of the same color in a row.")

        if stone.red_hammer != self.red_hammer:
            raise ValueError(
                "Stone's hammer status does not match the end's hammer status."
            )

        if stone.round != math.floor(len(self.stones) / 2) + 1:
            raise ValueError(
                "Stone's round does not match the expected round based on the number of stones already placed."
            )

        if self.overlaps_any_stone(stone):
            raise ValueError("Stone overlaps with an existing stone.")

        self.stones.append(stone)

    def overlaps_any_stone(self: Self, stone: Stone) -> bool:
        if stone.out_of_play:
            return False

        for s in self.stones:
            if (s.x - stone.x) ** 2 + (s.y - stone.y) ** 2 < (2 * Stone.RADIUS) ** 2:
                return True

        return False

    def red_won(self: Self) -> bool | None:
        good_stones = [s for s in self.stones if s.is_in_house()]

        if not good_stones:
            return None

        closest_stone = min(
            good_stones,
            key=lambda s: s.distance_to_center(),
        )

        return closest_stone.is_red

    def done(self: Self) -> bool:
        return len(self.stones) == 16

    def drawn(self: Self) -> bool:
        return self.red_won() is None

    def score(self: Self) -> int:
        good_stones = [s for s in self.stones if s.is_in_house()]

        if not good_stones:
            return 0

        closest_stone = min(
            good_stones,
            key=lambda s: s.distance_to_center(),
        )
        closest_oposite_color_stone = min(
            (s for s in good_stones if s.is_red != closest_stone.is_red),
            key=lambda s: s.distance_to_center(),
            default=None,
        )

        if closest_oposite_color_stone is None:
            return len(good_stones)

        score = 0
        for stone in good_stones:
            if stone.is_red == closest_oposite_color_stone.is_red:
                continue

            if (
                stone.distance_to_center()
                < closest_oposite_color_stone.distance_to_center()
            ):
                score += 1

        return score

    def __str__(self: Self) -> str:
        hammer_color = "Red" if self.red_hammer else "Yellow"
        return f"End with {hammer_color} hammer and {len(self.stones)} stones"


class Game:
    def __init__(self) -> None:
        self.ends: list[End] = []

    def add_end(self: Self, end: End) -> None:
        if len(self.ends) >= 10:
            raise ValueError("Cannot add more than 10 ends to a game.")

        if len(self.ends) > 0:
            last_end = self.ends[-1]
            red_won_last_end = last_end.red_won()
            if red_won_last_end is None and last_end.red_hammer != end.red_hammer:
                raise ValueError(
                    "If the last end was a blank, the hammer should not switch to the other team."
                )
            elif red_won_last_end and end.red_hammer:
                raise ValueError(
                    "If the last end was won by the red team, the hammer should switch to the yellow team."
                )
            elif red_won_last_end is False and end.red_hammer is False:
                raise ValueError(
                    "If the last end was won by the yellow team, the hammer should switch to the red team."
                )

        self.ends.append(end)

    def score(self: Self) -> tuple[int, int]:
        red_score = 0
        yellow_score = 0

        for end in self.ends:
            end_score = end.score()
            if end_score == 0:
                continue
            elif end.red_won():
                red_score += end_score
            else:
                yellow_score += end_score

        return red_score, yellow_score

    def display_scoreboard(self: Self) -> str:
        red_scores = []
        yellow_scores = []
        red_hammers = []
        for end in self.ends:
            red_hammers.append(end.red_hammer)
            end_score = end.score()
            if end_score == 0:
                red_scores.append(0)
                yellow_scores.append(0)
            elif end.red_won():
                red_scores.append(end_score)
                yellow_scores.append(0)
            else:
                red_scores.append(0)
                yellow_scores.append(end_score)

        red_total = sum(red_scores)
        yellow_total = sum(yellow_scores)

        scoreboard = (
            "End | "
            + " | ".join(f"{i+1:>4}" for i in range(len(self.ends)))
            + " | Total\n"
        )
        scoreboard += "----|" + "------|" * len(self.ends) + "------\n"
        scoreboard += (
            "Red | "
            + " | ".join(
                f"{'h' if r_h else ' ':>1}{score:>3}"
                for r_h, score in zip(red_hammers, red_scores)
            )
            + f" | {red_total:>5}\n"
        )
        scoreboard += (
            "Yel | "
            + " | ".join(
                f"{'h' if not r_h else ' ':>1}{score:>3}"
                for r_h, score in zip(red_hammers, yellow_scores)
            )
            + f" | {yellow_total:>5}\n"
        )
        return scoreboard

    def red_winner(self: Self) -> bool | None:
        red_score, yellow_score = self.score()
        if red_score > yellow_score:
            return True
        elif yellow_score > red_score:
            return False
        else:
            return None

    def __str__(self: Self) -> str:
        return f"Game with {len(self.ends)} ends"


if __name__ == "__main__":  # pragma: no cover
    # Show a full example game with 10 ends and a scoreboard
    game = Game()
    for i in range(10):
        red_hammer = (
            (
                game.ends[-1].red_hammer
                if game.ends[-1].drawn()
                else not game.ends[-1].red_won()
            )
            if game.ends
            else random.choice([True, False])
        )
        end = End(red_hammer)
        for j in range(16):
            for _ in range(10):  # Try placing a stone up to 10 times if it fails
                stone = Stone(
                    is_red=not red_hammer if j % 2 == 0 else red_hammer,
                    xy=(random.uniform(-2.5, 2.5), random.uniform(-6, 5.49)),
                    round=(j // 2) + 1,
                    red_hammer=end.red_hammer,
                    burned=random.uniform(0, 1) < 0.1,  # 10% chance to start burned
                )
                stone_added = False
                try:
                    end.add_stone(stone)
                    stone_added = True
                    if random.uniform(0, 1) < 0.1:  # 10% chance to move a stone
                        dxy = (random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
                        other_stone = random.choice(end.stones)
                        other_stone.move(dxy, in_round=stone.round, by_red=stone.is_red)
                    break
                except ValueError as e:
                    if stone_added:
                        end.stones.pop(-1)
                    continue
            else:
                raise RuntimeError("Failed to place a stone after 10 attempts.")

        game.add_end(end)
    print(game.display_scoreboard())
