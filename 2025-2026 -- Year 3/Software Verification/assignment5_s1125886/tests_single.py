import unittest
from curling import *
class TestGenerated(unittest.TestCase):
    
    def test_0(self):
        obj_940 = End(True)
        stone_940_0 = Stone(False, (2.37, -2.75), 1, True, False)
        add_940_0 = obj_940.add_stone(stone_940_0)
        stone_940_1 = Stone(True, (-0.75, 3.13), 1, True, False)
        add_940_1 = obj_940.add_stone(stone_940_1)
        stone_940_2 = Stone(False, (1.92, 5.14), 2, True, False)
        add_940_2 = obj_940.add_stone(stone_940_2)
        var_940_score = obj_940.score()
        self.assertEqual(add_940_0, None)
        self.assertEqual(add_940_1, None)
        self.assertEqual(add_940_2, None)
        self.assertEqual(var_940_score, 0)
        
    def test_1(self):
        obj_491 = Stone(True, (1.63, 1.56), 6, True, False)
        
    def test_2(self):
        obj_679 = Stone(False, (-1.99, -0.4), 3, True, True)
        
    def test_3(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
                obj_920 = End(True)
                stone_920_0 = Stone(False, (-0.97, 1.86), 1, True, False)
                add_920_0 = obj_920.add_stone(stone_920_0)
                stone_920_1 = Stone(True, (1.95, -4.6), 1, True, False)
                add_920_1 = obj_920.add_stone(stone_920_1)
                var_920_add_stone = obj_920.add_stone(stone_920_0)
        
    def test_4(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_715 = Game()
                end_715_0 = End(False)
                add_end_715_0 = obj_715.add_end(end_715_0)
                end_715_1 = End(True)
                add_end_715_1 = obj_715.add_end(end_715_1)
                end_715_2 = End(True)
                add_end_715_2 = obj_715.add_end(end_715_2)
                var_715_add_end = obj_715.add_end(end_715_1)
        
    def test_5(self):
        obj_360 = End(True)
        stone_360_0 = Stone(False, (1.65, 2.23), 1, True, False)
        add_360_0 = obj_360.add_stone(stone_360_0)
        var_360_overlaps_any_stone = obj_360.overlaps_any_stone(stone_360_0)
        self.assertEqual(add_360_0, None)
        self.assertEqual(var_360_overlaps_any_stone, True)
        
    def test_6(self):
        obj_255 = End(True)
        stone_255_0 = Stone(False, (-0.76, -3.97), 1, True, False)
        add_255_0 = obj_255.add_stone(stone_255_0)
        stone_255_1 = Stone(True, (1.86, 4.12), 1, True, False)
        add_255_1 = obj_255.add_stone(stone_255_1)
        stone_255_2 = Stone(False, (-2.49, -4.07), 2, True, False)
        add_255_2 = obj_255.add_stone(stone_255_2)
        var_255_done = obj_255.done()
        self.assertEqual(add_255_0, None)
        self.assertEqual(add_255_1, None)
        self.assertEqual(add_255_2, None)
        self.assertEqual(var_255_done, False)
        
    def test_7(self):
        obj_604 = Game()
        end_604_0 = End(False)
        add_end_604_0 = obj_604.add_end(end_604_0)
        end_604_1 = End(False)
        add_end_604_1 = obj_604.add_end(end_604_1)
        var_604_add_end = obj_604.add_end(end_604_0)
        self.assertEqual(add_end_604_0, None)
        self.assertEqual(add_end_604_1, None)
        
    def test_8(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_823 = End(True)
                stone_823_0 = Stone(False, (0.95, -4.45), 1, True, False)
                add_823_0 = obj_823.add_stone(stone_823_0)
                var_823_add_stone = obj_823.add_stone(stone_823_0)
        
    def test_9(self):
        obj_993 = Game()
        end_993_0 = End(True)
        add_end_993_0 = obj_993.add_end(end_993_0)
        var_993_score = obj_993.score()
        self.assertEqual(add_end_993_0, None)
        self.assertEqual(var_993_score, (0, 0))
        
    def test_10(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_186 = Game()
                end_186_0 = End(True)
                add_end_186_0 = obj_186.add_end(end_186_0)
                end_186_1 = End(False)
                add_end_186_1 = obj_186.add_end(end_186_1)
                end_186_2 = End(True)
                add_end_186_2 = obj_186.add_end(end_186_2)
                var_186_red_winner = obj_186.red_winner()
        
    def test_11(self):
        obj_914 = End(True)
        stone_914_0 = Stone(False, (-2.16, 4.09), 1, True, False)
        add_914_0 = obj_914.add_stone(stone_914_0)
        var_914_done = obj_914.done()
        self.assertEqual(add_914_0, None)
        self.assertEqual(var_914_done, False)
        
    def test_12(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_775 = Stone(False, (-1.24, -1.8), -2, False, True)
        
    def test_13(self):
        obj_858 = End(False)
        stone_858_0 = Stone(True, (0.01, -1.58), 1, False, False)
        add_858_0 = obj_858.add_stone(stone_858_0)
        var_858_red_won = obj_858.red_won()
        self.assertEqual(add_858_0, None)
        self.assertEqual(var_858_red_won, True)
        
    def test_14(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_734 = Game()
                end_734_0 = End(True)
                add_end_734_0 = obj_734.add_end(end_734_0)
                end_734_1 = End(False)
                add_end_734_1 = obj_734.add_end(end_734_1)
                end_734_2 = End(False)
                add_end_734_2 = obj_734.add_end(end_734_2)
                var_734_add_end = obj_734.add_end(end_734_2)
        
    def test_15(self):
        obj_110 = End(False)
        stone_110_0 = Stone(True, (-0.54, 3.81), 1, False, False)
        add_110_0 = obj_110.add_stone(stone_110_0)
        var_110___str__ = obj_110.__str__()
        self.assertEqual(add_110_0, None)
        self.assertEqual(var_110___str__, 'End with Yellow hammer and 1 stones')
        
    def test_16(self):
        obj_566 = Game()
        end_566_0 = End(True)
        add_end_566_0 = obj_566.add_end(end_566_0)
        end_566_1 = End(True)
        add_end_566_1 = obj_566.add_end(end_566_1)
        var_566_add_end = obj_566.add_end(end_566_0)
        self.assertEqual(add_end_566_0, None)
        self.assertEqual(add_end_566_1, None)
        
    def test_17(self):
        obj_828 = Stone(True, (1.89, 1.67), 2, True, False)
        
    def test_18(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_177 = Stone(True, (1.11, -0.01), 12, False, False)
        
    def test_19(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_290 = End(True)
                stone_290_0 = Stone(False, (1.24, 3.8), 1, True, False)
                add_290_0 = obj_290.add_stone(stone_290_0)
                stone_290_1 = Stone(True, (-0.59, 1.95), 1, True, False)
                add_290_1 = obj_290.add_stone(stone_290_1)
                stone_290_2 = Stone(False, (-1.03, -0.4), 2, True, False)
                add_290_2 = obj_290.add_stone(stone_290_2)
                var_290_add_stone = obj_290.add_stone(stone_290_2)
        
    def test_20(self):
        with self.assertRaisesRegex(TypeError, "Stone.move() missing 2 required positional arguments: 'in_round' and 'by_red'"):
                obj_0 = Stone(False, (1.12, -2.02), 5, True, False)
                var_0_move = obj_0.move((-5.0, 5.0))
                var_0_move = obj_0.move((-5.0, 5.0), 1)
                var_0_move = obj_0.move((-5.0, 5.0), 1, False)
        
    def test_21(self):
        obj_156 = Stone(False, (1.51, 1.74), 1, False, True)
        
    def test_22(self):
        obj_587 = Game()
        end_587_0 = End(True)
        add_end_587_0 = obj_587.add_end(end_587_0)
        var_587_add_end = obj_587.add_end(end_587_0)
        self.assertEqual(add_end_587_0, None)
        
    def test_23(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_12 = Game()
                end_12_0 = End(False)
                add_end_12_0 = obj_12.add_end(end_12_0)
                end_12_1 = End(True)
                add_end_12_1 = obj_12.add_end(end_12_1)
                end_12_2 = End(False)
                add_end_12_2 = obj_12.add_end(end_12_2)
                var_12_red_winner = obj_12.red_winner()
        
    def test_24(self):
        obj_286 = End(False)
        stone_286_0 = Stone(True, (-0.05, -1.68), 1, False, False)
        add_286_0 = obj_286.add_stone(stone_286_0)
        stone_286_1 = Stone(False, (1.3, -4.4), 1, False, False)
        add_286_1 = obj_286.add_stone(stone_286_1)
        var_286___str__ = obj_286.__str__()
        self.assertEqual(add_286_0, None)
        self.assertEqual(add_286_1, None)
        self.assertEqual(var_286___str__, 'End with Yellow hammer and 2 stones')
        
    def test_25(self):
        obj_973 = Stone(True, (1.35, -2.81), 1, False, True)
        
    def test_26(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_964 = Game()
                end_964_0 = End(True)
                add_end_964_0 = obj_964.add_end(end_964_0)
                end_964_1 = End(True)
                add_end_964_1 = obj_964.add_end(end_964_1)
                end_964_2 = End(False)
                add_end_964_2 = obj_964.add_end(end_964_2)
                var_964_score = obj_964.score()
        
    def test_27(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_727 = Game()
                end_727_0 = End(False)
                add_end_727_0 = obj_727.add_end(end_727_0)
                end_727_1 = End(True)
                add_end_727_1 = obj_727.add_end(end_727_1)
                end_727_2 = End(True)
                add_end_727_2 = obj_727.add_end(end_727_2)
                var_727_red_winner = obj_727.red_winner()
        
    def test_28(self):
        obj_645 = Stone(True, (1.94, -5.17), 4, True, False)
        
    def test_29(self):
        with self.assertRaisesRegex(TypeError, "Stone.move() missing 2 required positional arguments: 'in_round' and 'by_red'"):
                obj_226 = Stone(False, (2.16, -6.01), 3, False, True)
                var_226_move = obj_226.move((5.0, -5.0))
                var_226_move = obj_226.move((5.0, -5.0), 8)
                var_226_move = obj_226.move((5.0, -5.0), 8, True)
        
    def test_30(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
                obj_696 = Stone(True, (5.0, 6.0), 6, True, False)
        
    def test_31(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_490 = Stone(False, (1.67, 0.29), 11, False, True)
        
    def test_32(self):
        obj_753 = End(True)
        stone_753_0 = Stone(False, (-1.5, -3.38), 1, True, False)
        add_753_0 = obj_753.add_stone(stone_753_0)
        stone_753_1 = Stone(True, (0.99, 0.52), 1, True, False)
        add_753_1 = obj_753.add_stone(stone_753_1)
        stone_753_2 = Stone(False, (-2.01, -2.97), 2, True, False)
        add_753_2 = obj_753.add_stone(stone_753_2)
        var_753_drawn = obj_753.drawn()
        self.assertEqual(add_753_0, None)
        self.assertEqual(add_753_1, None)
        self.assertEqual(add_753_2, None)
        self.assertEqual(var_753_drawn, False)
        
    def test_33(self):
        obj_655 = Game()
        end_655_0 = End(True)
        add_end_655_0 = obj_655.add_end(end_655_0)
        end_655_1 = End(True)
        add_end_655_1 = obj_655.add_end(end_655_1)
        var_655_display_scoreboard = obj_655.display_scoreboard()
        self.assertEqual(add_end_655_0, None)
        self.assertEqual(add_end_655_1, None)
        self.assertEqual(var_655_display_scoreboard, 'End |    1 |    2 | Total\n----|------|------|------\nRed | h  0 | h  0 |     0\nYel |    0 |    0 |     0\n')
        
    def test_34(self):
        obj_507 = End(True)
        stone_507_0 = Stone(False, (0.31, -5.63), 1, True, False)
        add_507_0 = obj_507.add_stone(stone_507_0)
        stone_507_1 = Stone(True, (-0.32, -0.24), 1, True, False)
        add_507_1 = obj_507.add_stone(stone_507_1)
        stone_507_2 = Stone(False, (1.82, 3.66), 2, True, False)
        add_507_2 = obj_507.add_stone(stone_507_2)
        var_507_score = obj_507.score()
        self.assertEqual(add_507_0, None)
        self.assertEqual(add_507_1, None)
        self.assertEqual(add_507_2, None)
        self.assertEqual(var_507_score, 1)
        
    def test_35(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_499 = Game()
                end_499_0 = End(False)
                add_end_499_0 = obj_499.add_end(end_499_0)
                end_499_1 = End(True)
                add_end_499_1 = obj_499.add_end(end_499_1)
                var_499_display_scoreboard = obj_499.display_scoreboard()
        
    def test_36(self):
        obj_689 = Game()
        end_689_0 = End(True)
        add_end_689_0 = obj_689.add_end(end_689_0)
        end_689_1 = End(True)
        add_end_689_1 = obj_689.add_end(end_689_1)
        end_689_2 = End(True)
        add_end_689_2 = obj_689.add_end(end_689_2)
        var_689_add_end = obj_689.add_end(end_689_0)
        self.assertEqual(add_end_689_0, None)
        self.assertEqual(add_end_689_1, None)
        self.assertEqual(add_end_689_2, None)
        
    def test_37(self):
        obj_77 = End(False)
        stone_77_0 = Stone(True, (-1.8, -4.18), 1, False, False)
        add_77_0 = obj_77.add_stone(stone_77_0)
        stone_77_1 = Stone(False, (2.28, -5.74), 1, False, False)
        add_77_1 = obj_77.add_stone(stone_77_1)
        var_77_red_won = obj_77.red_won()
        self.assertEqual(add_77_0, None)
        self.assertEqual(add_77_1, None)
        self.assertEqual(var_77_red_won, None)
        
    def test_38(self):
        obj_952 = Game()
        end_952_0 = End(True)
        add_end_952_0 = obj_952.add_end(end_952_0)
        end_952_1 = End(True)
        add_end_952_1 = obj_952.add_end(end_952_1)
        end_952_2 = End(True)
        add_end_952_2 = obj_952.add_end(end_952_2)
        var_952___str__ = obj_952.__str__()
        self.assertEqual(add_end_952_0, None)
        self.assertEqual(add_end_952_1, None)
        self.assertEqual(add_end_952_2, None)
        self.assertEqual(var_952___str__, 'Game with 3 ends')
        
    def test_39(self):
        obj_261 = End(True)
        stone_261_0 = Stone(False, (2.08, 2.93), 1, True, False)
        add_261_0 = obj_261.add_stone(stone_261_0)
        stone_261_1 = Stone(True, (0.99, -5.85), 1, True, False)
        add_261_1 = obj_261.add_stone(stone_261_1)
        stone_261_2 = Stone(False, (-1.31, -0.59), 2, True, False)
        add_261_2 = obj_261.add_stone(stone_261_2)
        var_261_red_won = obj_261.red_won()
        self.assertEqual(add_261_0, None)
        self.assertEqual(add_261_1, None)
        self.assertEqual(add_261_2, None)
        self.assertEqual(var_261_red_won, False)
        
    def test_40(self):
        obj_596 = End(True)
        stone_596_0 = Stone(False, (-1.8, 4.19), 1, True, False)
        add_596_0 = obj_596.add_stone(stone_596_0)
        stone_596_1 = Stone(True, (-1.44, 5.35), 1, True, False)
        add_596_1 = obj_596.add_stone(stone_596_1)
        var_596_red_won = obj_596.red_won()
        self.assertEqual(add_596_0, None)
        self.assertEqual(add_596_1, None)
        self.assertEqual(var_596_red_won, None)
        
    def test_41(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_69 = Game()
                end_69_0 = End(False)
                add_end_69_0 = obj_69.add_end(end_69_0)
                end_69_1 = End(True)
                add_end_69_1 = obj_69.add_end(end_69_1)
                end_69_2 = End(False)
                add_end_69_2 = obj_69.add_end(end_69_2)
                var_69___str__ = obj_69.__str__()
        
    def test_42(self):
        obj_860 = Stone(False, (0.87, -5.56), 5, False, True)
        
    def test_43(self):
        obj_259 = End(True)
        stone_259_0 = Stone(False, (-0.85, -2.09), 1, True, False)
        add_259_0 = obj_259.add_stone(stone_259_0)
        var_259_score = obj_259.score()
        self.assertEqual(add_259_0, None)
        self.assertEqual(var_259_score, 0)
        
    def test_44(self):
        obj_702 = End(True)
        stone_702_0 = Stone(False, (1.87, -1.34), 1, True, False)
        add_702_0 = obj_702.add_stone(stone_702_0)
        stone_702_1 = Stone(True, (-1.01, 4.65), 1, True, False)
        add_702_1 = obj_702.add_stone(stone_702_1)
        var_702_score = obj_702.score()
        self.assertEqual(add_702_0, None)
        self.assertEqual(add_702_1, None)
        self.assertEqual(var_702_score, 0)
        
    def test_45(self):
        obj_771 = End(False)
        stone_771_0 = Stone(True, (0.03, 1.98), 1, False, False)
        add_771_0 = obj_771.add_stone(stone_771_0)
        stone_771_1 = Stone(False, (-1.36, 1.74), 1, False, False)
        add_771_1 = obj_771.add_stone(stone_771_1)
        stone_771_2 = Stone(True, (0.1, -2.82), 2, False, False)
        add_771_2 = obj_771.add_stone(stone_771_2)
        var_771_done = obj_771.done()
        self.assertEqual(add_771_0, None)
        self.assertEqual(add_771_1, None)
        self.assertEqual(add_771_2, None)
        self.assertEqual(var_771_done, False)
        
    def test_46(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_566 = Stone(True, (1.13, -2.81), 11, True, True)
        
    def test_47(self):
        obj_832 = Game()
        end_832_0 = End(True)
        add_end_832_0 = obj_832.add_end(end_832_0)
        var_832_add_end = obj_832.add_end(end_832_0)
        self.assertEqual(add_end_832_0, None)
        
    def test_48(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
                obj_980 = End(True)
                stone_980_0 = Stone(False, (0.21, 3.37), 1, True, False)
                add_980_0 = obj_980.add_stone(stone_980_0)
                stone_980_1 = Stone(True, (-0.07, -4.23), 1, True, False)
                add_980_1 = obj_980.add_stone(stone_980_1)
                stone_980_2 = Stone(False, (1.4, 1.82), 2, True, False)
                add_980_2 = obj_980.add_stone(stone_980_2)
                var_980_add_stone = obj_980.add_stone(stone_980_1)
        
    def test_49(self):
        obj_319 = Stone(False, (1.24, 4.04), 2, True, True)
        
    def test_50(self):
        obj_941 = End(True)
        stone_941_0 = Stone(False, (1.25, -1.6), 1, True, False)
        add_941_0 = obj_941.add_stone(stone_941_0)
        var_941___str__ = obj_941.__str__()
        self.assertEqual(add_941_0, None)
        self.assertEqual(var_941___str__, 'End with Red hammer and 1 stones')
        
    def test_51(self):
        obj_659 = Game()
        end_659_0 = End(False)
        add_end_659_0 = obj_659.add_end(end_659_0)
        end_659_1 = End(False)
        add_end_659_1 = obj_659.add_end(end_659_1)
        var_659_score = obj_659.score()
        self.assertEqual(add_end_659_0, None)
        self.assertEqual(add_end_659_1, None)
        self.assertEqual(var_659_score, (0, 0))
        
    def test_52(self):
        obj_637 = End(False)
        stone_637_0 = Stone(True, (-1.36, 1.96), 1, False, False)
        add_637_0 = obj_637.add_stone(stone_637_0)
        stone_637_1 = Stone(False, (2.01, 3.71), 1, False, False)
        add_637_1 = obj_637.add_stone(stone_637_1)
        var_637_overlaps_any_stone = obj_637.overlaps_any_stone(stone_637_0)
        self.assertEqual(add_637_0, None)
        self.assertEqual(add_637_1, None)
        self.assertEqual(var_637_overlaps_any_stone, True)
        
    def test_53(self):
        obj_269 = End(True)
        stone_269_0 = Stone(False, (-2.03, -2.51), 1, True, False)
        add_269_0 = obj_269.add_stone(stone_269_0)
        stone_269_1 = Stone(True, (-1.7, 1.25), 1, True, False)
        add_269_1 = obj_269.add_stone(stone_269_1)
        var_269_score = obj_269.score()
        self.assertEqual(add_269_0, None)
        self.assertEqual(add_269_1, None)
        self.assertEqual(var_269_score, 0)
        
    def test_54(self):
        obj_452 = Stone(False, (0.76, 1.73), 4, True, False)
        
    def test_55(self):
        obj_309 = End(False)
        stone_309_0 = Stone(True, (-2.15, -5.32), 1, False, False)
        add_309_0 = obj_309.add_stone(stone_309_0)
        stone_309_1 = Stone(False, (0.36, -4.15), 1, False, False)
        add_309_1 = obj_309.add_stone(stone_309_1)
        var_309___str__ = obj_309.__str__()
        self.assertEqual(add_309_0, None)
        self.assertEqual(add_309_1, None)
        self.assertEqual(var_309___str__, 'End with Yellow hammer and 2 stones')
        
    def test_56(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_992 = Stone(False, (-2.21, 0.25), -2, False, True)
        
    def test_57(self):
        obj_77 = Game()
        end_77_0 = End(True)
        add_end_77_0 = obj_77.add_end(end_77_0)
        end_77_1 = End(True)
        add_end_77_1 = obj_77.add_end(end_77_1)
        var_77_add_end = obj_77.add_end(end_77_0)
        self.assertEqual(add_end_77_0, None)
        self.assertEqual(add_end_77_1, None)
        
    def test_58(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_274 = Game()
                end_274_0 = End(False)
                add_end_274_0 = obj_274.add_end(end_274_0)
                end_274_1 = End(True)
                add_end_274_1 = obj_274.add_end(end_274_1)
                end_274_2 = End(True)
                add_end_274_2 = obj_274.add_end(end_274_2)
                var_274_red_winner = obj_274.red_winner()
        
    def test_59(self):
        obj_371 = End(False)
        stone_371_0 = Stone(True, (-0.92, -1.76), 1, False, False)
        add_371_0 = obj_371.add_stone(stone_371_0)
        stone_371_1 = Stone(False, (-0.92, -0.9), 1, False, False)
        add_371_1 = obj_371.add_stone(stone_371_1)
        var_371_overlaps_any_stone = obj_371.overlaps_any_stone(stone_371_1)
        self.assertEqual(add_371_0, None)
        self.assertEqual(add_371_1, None)
        self.assertEqual(var_371_overlaps_any_stone, True)
        
    def test_60(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_994 = Game()
                end_994_0 = End(True)
                add_end_994_0 = obj_994.add_end(end_994_0)
                end_994_1 = End(False)
                add_end_994_1 = obj_994.add_end(end_994_1)
                end_994_2 = End(False)
                add_end_994_2 = obj_994.add_end(end_994_2)
                var_994___str__ = obj_994.__str__()
        
    def test_61(self):
        obj_400 = Game()
        end_400_0 = End(True)
        add_end_400_0 = obj_400.add_end(end_400_0)
        end_400_1 = End(True)
        add_end_400_1 = obj_400.add_end(end_400_1)
        end_400_2 = End(True)
        add_end_400_2 = obj_400.add_end(end_400_2)
        var_400_red_winner = obj_400.red_winner()
        self.assertEqual(add_end_400_0, None)
        self.assertEqual(add_end_400_1, None)
        self.assertEqual(add_end_400_2, None)
        self.assertEqual(var_400_red_winner, None)
        
    def test_62(self):
        obj_568 = Stone(True, (0.1, -3.99), 4, True, True)
        
    def test_63(self):
        obj_539 = Game()
        end_539_0 = End(False)
        add_end_539_0 = obj_539.add_end(end_539_0)
        end_539_1 = End(False)
        add_end_539_1 = obj_539.add_end(end_539_1)
        var_539___str__ = obj_539.__str__()
        self.assertEqual(add_end_539_0, None)
        self.assertEqual(add_end_539_1, None)
        self.assertEqual(var_539___str__, 'Game with 2 ends')
        
    def test_64(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_995 = Game()
                end_995_0 = End(False)
                add_end_995_0 = obj_995.add_end(end_995_0)
                end_995_1 = End(True)
                add_end_995_1 = obj_995.add_end(end_995_1)
                end_995_2 = End(False)
                add_end_995_2 = obj_995.add_end(end_995_2)
                var_995_display_scoreboard = obj_995.display_scoreboard()
        
    def test_65(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_145 = Stone(True, (-3.0, -8.0), -2, False, False)
        
    def test_66(self):
        obj_812 = Stone(False, (1.06, -4.9), 4, True, False)
        
    def test_67(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_322 = Game()
                end_322_0 = End(True)
                add_end_322_0 = obj_322.add_end(end_322_0)
                end_322_1 = End(False)
                add_end_322_1 = obj_322.add_end(end_322_1)
                end_322_2 = End(False)
                add_end_322_2 = obj_322.add_end(end_322_2)
                var_322_score = obj_322.score()
        
    def test_68(self):
        obj_950 = End(False)
        stone_950_0 = Stone(True, (-1.3, -5.27), 1, False, False)
        add_950_0 = obj_950.add_stone(stone_950_0)
        var_950_red_won = obj_950.red_won()
        self.assertEqual(add_950_0, None)
        self.assertEqual(var_950_red_won, None)
        
    def test_69(self):
        with self.assertRaisesRegex(ValueError, "Stone position is out of bounds."):
                obj_123 = Stone(False, (5.0, 6.0), 9, True, False)
        
    def test_70(self):
        obj_992 = Stone(True, (-1.89, 1.22), 9, False, False)
        
    def test_71(self):
        obj_407 = Game()
        end_407_0 = End(True)
        add_end_407_0 = obj_407.add_end(end_407_0)
        end_407_1 = End(True)
        add_end_407_1 = obj_407.add_end(end_407_1)
        var_407___str__ = obj_407.__str__()
        self.assertEqual(add_end_407_0, None)
        self.assertEqual(add_end_407_1, None)
        self.assertEqual(var_407___str__, 'Game with 2 ends')
        
    def test_72(self):
        obj_62 = Game()
        end_62_0 = End(True)
        add_end_62_0 = obj_62.add_end(end_62_0)
        end_62_1 = End(True)
        add_end_62_1 = obj_62.add_end(end_62_1)
        var_62___str__ = obj_62.__str__()
        self.assertEqual(add_end_62_0, None)
        self.assertEqual(add_end_62_1, None)
        self.assertEqual(var_62___str__, 'Game with 2 ends')
        
    def test_73(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_749 = Game()
                end_749_0 = End(False)
                add_end_749_0 = obj_749.add_end(end_749_0)
                end_749_1 = End(True)
                add_end_749_1 = obj_749.add_end(end_749_1)
                end_749_2 = End(True)
                add_end_749_2 = obj_749.add_end(end_749_2)
                var_749_add_end = obj_749.add_end(end_749_0)
        
    def test_74(self):
        obj_156 = Stone(False, (-1.49, 1.7), 2, True, True)
        
    def test_75(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_768 = Game()
                end_768_0 = End(True)
                add_end_768_0 = obj_768.add_end(end_768_0)
                end_768_1 = End(False)
                add_end_768_1 = obj_768.add_end(end_768_1)
                var_768___str__ = obj_768.__str__()
        
    def test_76(self):
        obj_871 = Stone(True, (2.23, 0.12), 10, True, False)
        
    def test_77(self):
        obj_953 = Stone(False, (1.61, 5.76), 9, False, True)
        
    def test_78(self):
        obj_475 = End(True)
        stone_475_0 = Stone(False, (-1.19, -3.31), 1, True, False)
        add_475_0 = obj_475.add_stone(stone_475_0)
        stone_475_1 = Stone(True, (-1.84, -1.11), 1, True, False)
        add_475_1 = obj_475.add_stone(stone_475_1)
        stone_475_2 = Stone(False, (0.87, -3.25), 2, True, False)
        add_475_2 = obj_475.add_stone(stone_475_2)
        var_475_score = obj_475.score()
        self.assertEqual(add_475_0, None)
        self.assertEqual(add_475_1, None)
        self.assertEqual(add_475_2, None)
        self.assertEqual(var_475_score, 0)
        
    def test_79(self):
        obj_714 = Stone(True, (-0.79, 4.41), 5, False, True)
        
    def test_80(self):
        obj_963 = End(True)
        stone_963_0 = Stone(False, (-0.67, -1.18), 1, True, False)
        add_963_0 = obj_963.add_stone(stone_963_0)
        var_963_red_won = obj_963.red_won()
        self.assertEqual(add_963_0, None)
        self.assertEqual(var_963_red_won, False)
        
    def test_81(self):
        obj_849 = Stone(True, (0.16, 3.52), 5, False, False)
        
    def test_82(self):
        obj_349 = Game()
        end_349_0 = End(False)
        add_end_349_0 = obj_349.add_end(end_349_0)
        var_349_score = obj_349.score()
        self.assertEqual(add_end_349_0, None)
        self.assertEqual(var_349_score, (0, 0))
        
    def test_83(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_342 = Game()
                end_342_0 = End(False)
                add_end_342_0 = obj_342.add_end(end_342_0)
                end_342_1 = End(True)
                add_end_342_1 = obj_342.add_end(end_342_1)
                var_342_score = obj_342.score()
        
    def test_84(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_553 = Stone(True, (-2.35, 2.27), -1, True, False)
        
    def test_85(self):
        obj_160 = Game()
        end_160_0 = End(True)
        add_end_160_0 = obj_160.add_end(end_160_0)
        var_160___str__ = obj_160.__str__()
        self.assertEqual(add_end_160_0, None)
        self.assertEqual(var_160___str__, 'Game with 1 ends')
        
    def test_86(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
                obj_941 = End(True)
                stone_941_0 = Stone(False, (1.46, 0.02), 1, True, False)
                add_941_0 = obj_941.add_stone(stone_941_0)
                stone_941_1 = Stone(True, (1.64, 0.92), 1, True, False)
                add_941_1 = obj_941.add_stone(stone_941_1)
                var_941_add_stone = obj_941.add_stone(stone_941_0)
        
    def test_87(self):
        obj_376 = End(True)
        stone_376_0 = Stone(False, (-1.88, 0.84), 1, True, False)
        add_376_0 = obj_376.add_stone(stone_376_0)
        stone_376_1 = Stone(True, (-2.29, 3.86), 1, True, False)
        add_376_1 = obj_376.add_stone(stone_376_1)
        var_376_red_won = obj_376.red_won()
        self.assertEqual(add_376_0, None)
        self.assertEqual(add_376_1, None)
        self.assertEqual(var_376_red_won, None)
        
    def test_88(self):
        obj_988 = Stone(True, (-0.67, -0.47), 7, True, False)
        
    def test_89(self):
        obj_306 = Game()
        end_306_0 = End(False)
        add_end_306_0 = obj_306.add_end(end_306_0)
        var_306_red_winner = obj_306.red_winner()
        self.assertEqual(add_end_306_0, None)
        self.assertEqual(var_306_red_winner, None)
        
    def test_90(self):
        with self.assertRaisesRegex(ValueError, "Stone's round does not match the expected round based on the number of stones already placed."):
                obj_221 = End(True)
                stone_221_0 = Stone(False, (-0.03, -4.07), 1, True, False)
                add_221_0 = obj_221.add_stone(stone_221_0)
                stone_221_1 = Stone(True, (-1.44, 0.85), 1, True, False)
                add_221_1 = obj_221.add_stone(stone_221_1)
                stone_221_2 = Stone(False, (-1.68, -3.16), 2, True, False)
                add_221_2 = obj_221.add_stone(stone_221_2)
                var_221_add_stone = obj_221.add_stone(stone_221_1)
        
    def test_91(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_697 = Stone(True, (-1.07, -6.0), 12, True, False)
        
    def test_92(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_537 = Stone(True, (-0.07, 0.48), -2, True, False)
                var_537_move = obj_537.move((-0.44, -0.4))
                var_537_move = obj_537.move((-0.44, -0.4), 8)
                var_537_move = obj_537.move((-0.44, -0.4), 8, False)
        
    def test_93(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_565 = Stone(True, (-1.28, -2.67), 11, False, False)
        
    def test_94(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_218 = Game()
                end_218_0 = End(False)
                add_end_218_0 = obj_218.add_end(end_218_0)
                end_218_1 = End(True)
                add_end_218_1 = obj_218.add_end(end_218_1)
                end_218_2 = End(False)
                add_end_218_2 = obj_218.add_end(end_218_2)
                var_218_display_scoreboard = obj_218.display_scoreboard()
        
    def test_95(self):
        obj_95 = End(True)
        stone_95_0 = Stone(False, (1.65, -3.33), 1, True, False)
        add_95_0 = obj_95.add_stone(stone_95_0)
        stone_95_1 = Stone(True, (-1.42, 3.77), 1, True, False)
        add_95_1 = obj_95.add_stone(stone_95_1)
        var_95_red_won = obj_95.red_won()
        self.assertEqual(add_95_0, None)
        self.assertEqual(add_95_1, None)
        self.assertEqual(var_95_red_won, None)
        
    def test_96(self):
        obj_581 = End(False)
        stone_581_0 = Stone(True, (1.78, -2.27), 1, False, False)
        add_581_0 = obj_581.add_stone(stone_581_0)
        stone_581_1 = Stone(False, (0.53, -4.66), 1, False, False)
        add_581_1 = obj_581.add_stone(stone_581_1)
        var_581_overlaps_any_stone = obj_581.overlaps_any_stone(stone_581_1)
        self.assertEqual(add_581_0, None)
        self.assertEqual(add_581_1, None)
        self.assertEqual(var_581_overlaps_any_stone, True)
        
    def test_97(self):
        obj_910 = End(True)
        stone_910_0 = Stone(False, (1.47, -0.55), 1, True, False)
        add_910_0 = obj_910.add_stone(stone_910_0)
        stone_910_1 = Stone(True, (-2.27, -1.78), 1, True, False)
        add_910_1 = obj_910.add_stone(stone_910_1)
        var_910_drawn = obj_910.drawn()
        self.assertEqual(add_910_0, None)
        self.assertEqual(add_910_1, None)
        self.assertEqual(var_910_drawn, False)
        
    def test_98(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_69 = Stone(False, (2.38, 0.79), 11, True, False)
                var_69_move = obj_69.move((0.48, -0.35))
                var_69_move = obj_69.move((0.48, -0.35), 8)
                var_69_move = obj_69.move((0.48, -0.35), 8, False)
        
    def test_99(self):
        obj_374 = Stone(True, (-1.97, -1.89), 9, False, False)
        