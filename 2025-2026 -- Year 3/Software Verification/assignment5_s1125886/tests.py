import unittest
from curling import *
class TestGenerated(unittest.TestCase):
    
    def test_0(self):
        obj_358 = End(False)
        stone_358_0 = Stone(True, (1.5, -5.08), 1, False, False)
        add_358_0 = obj_358.add_stone(stone_358_0)
        stone_358_1 = Stone(False, (-2.07, -4.06), 1, False, False)
        add_358_1 = obj_358.add_stone(stone_358_1)
        stone_358_2 = Stone(True, (-1.16, 4.48), 2, False, False)
        add_358_2 = obj_358.add_stone(stone_358_2)
        var_358_red_won = obj_358.red_won()
        self.assertEqual(add_358_0, None)
        self.assertEqual(add_358_1, None)
        self.assertEqual(add_358_2, None)
        self.assertEqual(var_358_red_won, None)
        
    def test_1(self):
        obj_866 = Game()
        end_866_0 = End(True)
        add_end_866_0 = obj_866.add_end(end_866_0)
        end_866_1 = End(True)
        add_end_866_1 = obj_866.add_end(end_866_1)
        var_866_add_end = obj_866.add_end(end_866_0)
        self.assertEqual(add_end_866_0, None)
        self.assertEqual(add_end_866_1, None)
        
    def test_2(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_457 = End(False)
                stone_457_0 = Stone(True, (-1.41, -1.39), 1, False, False)
                add_457_0 = obj_457.add_stone(stone_457_0)
                var_457_add_stone = obj_457.add_stone(stone_457_0)
        
    def test_3(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_583 = Stone(False, (5.0, -8.0), 12, False, False)
        
    def test_4(self):
        obj_714 = End(False)
        stone_714_0 = Stone(True, (1.56, -2.52), 1, False, False)
        add_714_0 = obj_714.add_stone(stone_714_0)
        stone_714_1 = Stone(False, (1.25, -5.37), 1, False, False)
        add_714_1 = obj_714.add_stone(stone_714_1)
        var_714_score = obj_714.score()
        self.assertEqual(add_714_0, None)
        self.assertEqual(add_714_1, None)
        self.assertEqual(var_714_score, 0)
        
    def test_5(self):
        obj_454 = Game()
        end_454_0 = End(False)
        add_end_454_0 = obj_454.add_end(end_454_0)
        end_454_1 = End(False)
        add_end_454_1 = obj_454.add_end(end_454_1)
        end_454_2 = End(False)
        add_end_454_2 = obj_454.add_end(end_454_2)
        var_454_score = obj_454.score()
        self.assertEqual(add_end_454_0, None)
        self.assertEqual(add_end_454_1, None)
        self.assertEqual(add_end_454_2, None)
        self.assertEqual(var_454_score, (0, 0))
        
    def test_6(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_616 = Game()
                end_616_0 = End(False)
                add_end_616_0 = obj_616.add_end(end_616_0)
                end_616_1 = End(False)
                add_end_616_1 = obj_616.add_end(end_616_1)
                end_616_2 = End(True)
                add_end_616_2 = obj_616.add_end(end_616_2)
                var_616___str__ = obj_616.__str__()
        
    def test_7(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_283 = Game()
                end_283_0 = End(False)
                add_end_283_0 = obj_283.add_end(end_283_0)
                end_283_1 = End(True)
                add_end_283_1 = obj_283.add_end(end_283_1)
                end_283_2 = End(False)
                add_end_283_2 = obj_283.add_end(end_283_2)
                var_283_add_end = obj_283.add_end(end_283_1)
        
    def test_8(self):
        obj_523 = Stone(False, (-0.68, 0.18), 1, False, False)
        
    def test_9(self):
        obj_811 = Game()
        end_811_0 = End(False)
        add_end_811_0 = obj_811.add_end(end_811_0)
        var_811_add_end = obj_811.add_end(end_811_0)
        self.assertEqual(add_end_811_0, None)
        
    def test_10(self):
        obj_937 = Stone(True, (0.09, 2.82), 4, False, False)
        
    def test_11(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_231 = Game()
                end_231_0 = End(False)
                add_end_231_0 = obj_231.add_end(end_231_0)
                end_231_1 = End(True)
                add_end_231_1 = obj_231.add_end(end_231_1)
                var_231_add_end = obj_231.add_end(end_231_0)
        
    def test_12(self):
        obj_748 = Stone(False, (-2.41, 1.37), 4, True, True)
        
    def test_13(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_644 = End(False)
                stone_644_0 = Stone(True, (-0.53, -1.14), 1, False, False)
                add_644_0 = obj_644.add_stone(stone_644_0)
                stone_644_1 = Stone(False, (1.67, -2.25), 1, False, False)
                add_644_1 = obj_644.add_stone(stone_644_1)
                var_644_add_stone = obj_644.add_stone(stone_644_1)
        
    def test_14(self):
        obj_122 = End(True)
        stone_122_0 = Stone(False, (2.31, 4.79), 1, True, False)
        add_122_0 = obj_122.add_stone(stone_122_0)
        var_122_score = obj_122.score()
        self.assertEqual(add_122_0, None)
        self.assertEqual(var_122_score, 0)
        
    def test_15(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_517 = Game()
                end_517_0 = End(True)
                add_end_517_0 = obj_517.add_end(end_517_0)
                end_517_1 = End(False)
                add_end_517_1 = obj_517.add_end(end_517_1)
                var_517_add_end = obj_517.add_end(end_517_0)
        
    def test_16(self):
        obj_608 = Game()
        end_608_0 = End(True)
        add_end_608_0 = obj_608.add_end(end_608_0)
        var_608_display_scoreboard = obj_608.display_scoreboard()
        self.assertEqual(add_end_608_0, None)
        self.assertEqual(var_608_display_scoreboard, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_17(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_833 = Stone(True, (1.01, -0.29), 12, True, False)
        
    def test_18(self):
        obj_763 = End(False)
        stone_763_0 = Stone(True, (0.6, 3.22), 1, False, False)
        add_763_0 = obj_763.add_stone(stone_763_0)
        var_763___str__ = obj_763.__str__()
        self.assertEqual(add_763_0, None)
        self.assertEqual(var_763___str__, 'End with Yellow hammer and 1 stones')
        
    def test_19(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_53 = Stone(True, (-0.56, 1.55), 12, False, True)
        
    def test_20(self):
        obj_602 = End(False)
        stone_602_0 = Stone(True, (-2.02, 1.32), 1, False, False)
        add_602_0 = obj_602.add_stone(stone_602_0)
        stone_602_1 = Stone(False, (2.14, -3.13), 1, False, False)
        add_602_1 = obj_602.add_stone(stone_602_1)
        var_602___str__ = obj_602.__str__()
        self.assertEqual(add_602_0, None)
        self.assertEqual(add_602_1, None)
        self.assertEqual(var_602___str__, 'End with Yellow hammer and 2 stones')
        
    def test_21(self):
        obj_821 = End(False)
        stone_821_0 = Stone(True, (0.12, 2.3), 1, False, False)
        add_821_0 = obj_821.add_stone(stone_821_0)
        var_821___str__ = obj_821.__str__()
        self.assertEqual(add_821_0, None)
        self.assertEqual(var_821___str__, 'End with Yellow hammer and 1 stones')
        
    def test_22(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_606 = Game()
                end_606_0 = End(False)
                add_end_606_0 = obj_606.add_end(end_606_0)
                end_606_1 = End(True)
                add_end_606_1 = obj_606.add_end(end_606_1)
                var_606___str__ = obj_606.__str__()
        
    def test_23(self):
        obj_765 = Game()
        end_765_0 = End(False)
        add_end_765_0 = obj_765.add_end(end_765_0)
        end_765_1 = End(False)
        add_end_765_1 = obj_765.add_end(end_765_1)
        end_765_2 = End(False)
        add_end_765_2 = obj_765.add_end(end_765_2)
        var_765_score = obj_765.score()
        self.assertEqual(add_end_765_0, None)
        self.assertEqual(add_end_765_1, None)
        self.assertEqual(add_end_765_2, None)
        self.assertEqual(var_765_score, (0, 0))
        
    def test_24(self):
        obj_743 = End(False)
        stone_743_0 = Stone(True, (-0.81, -5.39), 1, False, False)
        add_743_0 = obj_743.add_stone(stone_743_0)
        stone_743_1 = Stone(False, (0.21, 1.5), 1, False, False)
        add_743_1 = obj_743.add_stone(stone_743_1)
        stone_743_2 = Stone(True, (1.4, 3.96), 2, False, False)
        add_743_2 = obj_743.add_stone(stone_743_2)
        var_743_overlaps_any_stone = obj_743.overlaps_any_stone(stone_743_2)
        self.assertEqual(add_743_0, None)
        self.assertEqual(add_743_1, None)
        self.assertEqual(add_743_2, None)
        self.assertEqual(var_743_overlaps_any_stone, True)
        
    def test_25(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_885 = Stone(False, (-2.59, -2.93), -1, True, True)
        
    def test_26(self):
        obj_58 = Stone(True, (2.15, -2.24), 10, True, False)
        
    def test_27(self):
        obj_500 = End(False)
        stone_500_0 = Stone(True, (0.51, -5.89), 1, False, False)
        add_500_0 = obj_500.add_stone(stone_500_0)
        var_500_red_won = obj_500.red_won()
        self.assertEqual(add_500_0, None)
        self.assertEqual(var_500_red_won, None)
        
    def test_28(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_860 = Game()
                end_860_0 = End(False)
                add_end_860_0 = obj_860.add_end(end_860_0)
                end_860_1 = End(True)
                add_end_860_1 = obj_860.add_end(end_860_1)
                var_860_add_end = obj_860.add_end(end_860_0)
        
    def test_29(self):
        obj_616 = Stone(True, (-1.22, -1.05), 3, False, False)
        
    def test_30(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_613 = Game()
                end_613_0 = End(False)
                add_end_613_0 = obj_613.add_end(end_613_0)
                end_613_1 = End(True)
                add_end_613_1 = obj_613.add_end(end_613_1)
                end_613_2 = End(False)
                add_end_613_2 = obj_613.add_end(end_613_2)
                var_613___str__ = obj_613.__str__()
        
    def test_31(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_965 = Stone(False, (-0.48, -6.48), -2, True, True)
        
    def test_32(self):
        obj_327 = Stone(False, (-1.62, 5.23), 2, False, False)
        
    def test_33(self):
        obj_76 = Stone(True, (0.37, -2.24), 6, True, True)
        
    def test_34(self):
        obj_995 = End(True)
        stone_995_0 = Stone(False, (-2.46, 2.31), 1, True, False)
        add_995_0 = obj_995.add_stone(stone_995_0)
        stone_995_1 = Stone(True, (0.03, 5.04), 1, True, False)
        add_995_1 = obj_995.add_stone(stone_995_1)
        var_995_score = obj_995.score()
        self.assertEqual(add_995_0, None)
        self.assertEqual(add_995_1, None)
        self.assertEqual(var_995_score, 0)
        
    def test_35(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_261 = Stone(True, (0.39, -4.72), 0, True, True)
        
    def test_36(self):
        obj_365 = End(True)
        stone_365_0 = Stone(False, (1.12, -2.64), 1, True, False)
        add_365_0 = obj_365.add_stone(stone_365_0)
        stone_365_1 = Stone(True, (0.37, -4.65), 1, True, False)
        add_365_1 = obj_365.add_stone(stone_365_1)
        var_365_red_won = obj_365.red_won()
        self.assertEqual(add_365_0, None)
        self.assertEqual(add_365_1, None)
        self.assertEqual(var_365_red_won, None)
        
    def test_37(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_2 = Game()
                end_2_0 = End(True)
                add_end_2_0 = obj_2.add_end(end_2_0)
                end_2_1 = End(False)
                add_end_2_1 = obj_2.add_end(end_2_1)
                end_2_2 = End(False)
                add_end_2_2 = obj_2.add_end(end_2_2)
                var_2_display_scoreboard = obj_2.display_scoreboard()
        
    def test_38(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_89 = Game()
                end_89_0 = End(True)
                add_end_89_0 = obj_89.add_end(end_89_0)
                end_89_1 = End(False)
                add_end_89_1 = obj_89.add_end(end_89_1)
                end_89_2 = End(True)
                add_end_89_2 = obj_89.add_end(end_89_2)
                var_89_display_scoreboard = obj_89.display_scoreboard()
        
    def test_39(self):
        obj_582 = Game()
        end_582_0 = End(False)
        add_end_582_0 = obj_582.add_end(end_582_0)
        end_582_1 = End(False)
        add_end_582_1 = obj_582.add_end(end_582_1)
        end_582_2 = End(False)
        add_end_582_2 = obj_582.add_end(end_582_2)
        var_582_score = obj_582.score()
        self.assertEqual(add_end_582_0, None)
        self.assertEqual(add_end_582_1, None)
        self.assertEqual(add_end_582_2, None)
        self.assertEqual(var_582_score, (0, 0))
        
    def test_40(self):
        obj_600 = Stone(False, (1.35, 1.02), 5, True, True)
        
    def test_41(self):
        obj_12 = End(False)
        stone_12_0 = Stone(True, (-0.34, -6.31), 1, False, False)
        add_12_0 = obj_12.add_stone(stone_12_0)
        var_12_drawn = obj_12.drawn()
        self.assertEqual(add_12_0, None)
        self.assertEqual(var_12_drawn, True)
        
    def test_42(self):
        obj_686 = End(True)
        stone_686_0 = Stone(False, (1.87, 4.83), 1, True, False)
        add_686_0 = obj_686.add_stone(stone_686_0)
        stone_686_1 = Stone(True, (1.38, -3.88), 1, True, False)
        add_686_1 = obj_686.add_stone(stone_686_1)
        stone_686_2 = Stone(False, (-2.09, -0.26), 2, True, False)
        add_686_2 = obj_686.add_stone(stone_686_2)
        var_686_red_won = obj_686.red_won()
        self.assertEqual(add_686_0, None)
        self.assertEqual(add_686_1, None)
        self.assertEqual(add_686_2, None)
        self.assertEqual(var_686_red_won, None)
        
    def test_43(self):
        obj_472 = Stone(False, (0.13, 0.77), 7, False, False)
        
    def test_44(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_314 = Stone(True, (0.94, 0.17), 11, True, False)
        
    def test_45(self):
        obj_978 = Game()
        end_978_0 = End(True)
        add_end_978_0 = obj_978.add_end(end_978_0)
        var_978_score = obj_978.score()
        self.assertEqual(add_end_978_0, None)
        self.assertEqual(var_978_score, (0, 0))
        
    def test_46(self):
        obj_135 = End(True)
        stone_135_0 = Stone(False, (-0.48, -4.09), 1, True, False)
        add_135_0 = obj_135.add_stone(stone_135_0)
        var_135_score = obj_135.score()
        self.assertEqual(add_135_0, None)
        self.assertEqual(var_135_score, 0)
        
    def test_47(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_190 = Stone(True, (2.93, 0.22), 12, False, True)
        
    def test_48(self):
        obj_979 = Game()
        end_979_0 = End(True)
        add_end_979_0 = obj_979.add_end(end_979_0)
        var_979_add_end = obj_979.add_end(end_979_0)
        self.assertEqual(add_end_979_0, None)
        
    def test_49(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_552 = Stone(True, (-2.9, -3.55), -2, True, True)
        
    def test_50(self):
        obj_616 = Stone(False, (0.6, -5.64), 2, True, True)
        
    def test_51(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_407 = Stone(False, (0.3, 1.32), 0, True, False)
        
    def test_52(self):
        obj_255 = End(True)
        stone_255_0 = Stone(False, (1.71, 5.44), 1, True, False)
        add_255_0 = obj_255.add_stone(stone_255_0)
        stone_255_1 = Stone(True, (-2.02, -5.18), 1, True, False)
        add_255_1 = obj_255.add_stone(stone_255_1)
        stone_255_2 = Stone(False, (-2.24, 2.06), 2, True, False)
        add_255_2 = obj_255.add_stone(stone_255_2)
        var_255_drawn = obj_255.drawn()
        self.assertEqual(add_255_0, None)
        self.assertEqual(add_255_1, None)
        self.assertEqual(add_255_2, None)
        self.assertEqual(var_255_drawn, True)
        
    def test_53(self):
        obj_171 = Game()
        end_171_0 = End(True)
        add_end_171_0 = obj_171.add_end(end_171_0)
        var_171_score = obj_171.score()
        self.assertEqual(add_end_171_0, None)
        self.assertEqual(var_171_score, (0, 0))
        
    def test_54(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_263 = End(True)
                stone_263_0 = Stone(False, (0.91, -4.52), 1, True, False)
                add_263_0 = obj_263.add_stone(stone_263_0)
                var_263_add_stone = obj_263.add_stone(stone_263_0)
        
    def test_55(self):
        obj_492 = End(True)
        stone_492_0 = Stone(False, (-1.3, 2.5), 1, True, False)
        add_492_0 = obj_492.add_stone(stone_492_0)
        stone_492_1 = Stone(True, (0.15, -1.0), 1, True, False)
        add_492_1 = obj_492.add_stone(stone_492_1)
        stone_492_2 = Stone(False, (2.41, -1.59), 2, True, False)
        add_492_2 = obj_492.add_stone(stone_492_2)
        var_492_red_won = obj_492.red_won()
        self.assertEqual(add_492_0, None)
        self.assertEqual(add_492_1, None)
        self.assertEqual(add_492_2, None)
        self.assertEqual(var_492_red_won, True)
        
    def test_56(self):
        obj_991 = Stone(False, (-0.1, -2.35), 4, True, True)
        
    def test_57(self):
        obj_816 = End(False)
        stone_816_0 = Stone(True, (1.67, 5.11), 1, False, False)
        add_816_0 = obj_816.add_stone(stone_816_0)
        var_816_red_won = obj_816.red_won()
        self.assertEqual(add_816_0, None)
        self.assertEqual(var_816_red_won, None)
        
    def test_58(self):
        obj_86 = End(False)
        stone_86_0 = Stone(True, (2.09, -4.98), 1, False, False)
        add_86_0 = obj_86.add_stone(stone_86_0)
        stone_86_1 = Stone(False, (-1.13, -0.41), 1, False, False)
        add_86_1 = obj_86.add_stone(stone_86_1)
        stone_86_2 = Stone(True, (0.29, -3.58), 2, False, False)
        add_86_2 = obj_86.add_stone(stone_86_2)
        var_86___str__ = obj_86.__str__()
        self.assertEqual(add_86_0, None)
        self.assertEqual(add_86_1, None)
        self.assertEqual(add_86_2, None)
        self.assertEqual(var_86___str__, 'End with Yellow hammer and 3 stones')
        
    def test_59(self):
        obj_782 = Game()
        end_782_0 = End(False)
        add_end_782_0 = obj_782.add_end(end_782_0)
        end_782_1 = End(False)
        add_end_782_1 = obj_782.add_end(end_782_1)
        var_782_add_end = obj_782.add_end(end_782_0)
        self.assertEqual(add_end_782_0, None)
        self.assertEqual(add_end_782_1, None)
        
    def test_60(self):
        obj_846 = Game()
        end_846_0 = End(True)
        add_end_846_0 = obj_846.add_end(end_846_0)
        var_846___str__ = obj_846.__str__()
        self.assertEqual(add_end_846_0, None)
        self.assertEqual(var_846___str__, 'Game with 1 ends')
        
    def test_61(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_538 = Stone(True, (0.36, 4.05), 11, True, True)
        
    def test_62(self):
        obj_966 = Stone(False, (1.82, -4.59), 5, True, True)
        
    def test_63(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_608 = Game()
                end_608_0 = End(False)
                add_end_608_0 = obj_608.add_end(end_608_0)
                end_608_1 = End(True)
                add_end_608_1 = obj_608.add_end(end_608_1)
                var_608___str__ = obj_608.__str__()
        
    def test_64(self):
        obj_304 = End(True)
        stone_304_0 = Stone(False, (1.99, 2.15), 1, True, False)
        add_304_0 = obj_304.add_stone(stone_304_0)
        stone_304_1 = Stone(True, (1.39, -1.36), 1, True, False)
        add_304_1 = obj_304.add_stone(stone_304_1)
        var_304___str__ = obj_304.__str__()
        self.assertEqual(add_304_0, None)
        self.assertEqual(add_304_1, None)
        self.assertEqual(var_304___str__, 'End with Red hammer and 2 stones')
        
    def test_65(self):
        obj_836 = Game()
        end_836_0 = End(True)
        add_end_836_0 = obj_836.add_end(end_836_0)
        var_836_display_scoreboard = obj_836.display_scoreboard()
        self.assertEqual(add_end_836_0, None)
        self.assertEqual(var_836_display_scoreboard, 'End |    1 | Total\n----|------|------\nRed | h  0 |     0\nYel |    0 |     0\n')
        
    def test_66(self):
        obj_999 = Game()
        end_999_0 = End(False)
        add_end_999_0 = obj_999.add_end(end_999_0)
        var_999_display_scoreboard = obj_999.display_scoreboard()
        self.assertEqual(add_end_999_0, None)
        self.assertEqual(var_999_display_scoreboard, 'End |    1 | Total\n----|------|------\nRed |    0 |     0\nYel | h  0 |     0\n')
        
    def test_67(self):
        obj_900 = Stone(False, (-0.78, 2.54), 10, True, False)
        
    def test_68(self):
        obj_244 = Stone(False, (1.72, 3.11), 2, True, False)
        
    def test_69(self):
        obj_63 = Stone(False, (-2.08, -5.55), 1, False, True)
        
    def test_70(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_878 = Stone(True, (1.51, -5.85), -2, True, True)
        
    def test_71(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_115 = Stone(True, (0.37, 2.97), -1, False, True)
                var_115_move = obj_115.move((-0.34, 0.37))
                var_115_move = obj_115.move((-0.34, 0.37), 4)
                var_115_move = obj_115.move((-0.34, 0.37), 4, True)
        
    def test_72(self):
        obj_500 = End(False)
        stone_500_0 = Stone(True, (-2.46, 4.65), 1, False, False)
        add_500_0 = obj_500.add_stone(stone_500_0)
        stone_500_1 = Stone(False, (1.1, 3.51), 1, False, False)
        add_500_1 = obj_500.add_stone(stone_500_1)
        stone_500_2 = Stone(True, (-1.59, 5.2), 2, False, False)
        add_500_2 = obj_500.add_stone(stone_500_2)
        var_500_drawn = obj_500.drawn()
        self.assertEqual(add_500_0, None)
        self.assertEqual(add_500_1, None)
        self.assertEqual(add_500_2, None)
        self.assertEqual(var_500_drawn, True)
        
    def test_73(self):
        obj_897 = End(True)
        stone_897_0 = Stone(False, (-0.43, -4.02), 1, True, False)
        add_897_0 = obj_897.add_stone(stone_897_0)
        stone_897_1 = Stone(True, (-0.38, 2.3), 1, True, False)
        add_897_1 = obj_897.add_stone(stone_897_1)
        var_897___str__ = obj_897.__str__()
        self.assertEqual(add_897_0, None)
        self.assertEqual(add_897_1, None)
        self.assertEqual(var_897___str__, 'End with Red hammer and 2 stones')
        
    def test_74(self):
        obj_976 = Stone(True, (-1.16, -2.81), 1, True, False)
        
    def test_75(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_220 = Stone(True, (-5.0, -8.0), 12, False, False)
        
    def test_76(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_960 = Game()
                end_960_0 = End(True)
                add_end_960_0 = obj_960.add_end(end_960_0)
                end_960_1 = End(False)
                add_end_960_1 = obj_960.add_end(end_960_1)
                end_960_2 = End(False)
                add_end_960_2 = obj_960.add_end(end_960_2)
                var_960_display_scoreboard = obj_960.display_scoreboard()
        
    def test_77(self):
        obj_995 = Stone(False, (2.44, -1.63), 10, False, True)
        
    def test_78(self):
        obj_516 = Game()
        end_516_0 = End(False)
        add_end_516_0 = obj_516.add_end(end_516_0)
        end_516_1 = End(False)
        add_end_516_1 = obj_516.add_end(end_516_1)
        var_516___str__ = obj_516.__str__()
        self.assertEqual(add_end_516_0, None)
        self.assertEqual(add_end_516_1, None)
        self.assertEqual(var_516___str__, 'Game with 2 ends')
        
    def test_79(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_304 = Stone(True, (-2.39, 4.88), 11, True, True)
        
    def test_80(self):
        with self.assertRaisesRegex(ValueError, "Cannot place two stones of the same color in a row."):
                obj_280 = End(True)
                stone_280_0 = Stone(False, (1.53, -1.76), 1, True, False)
                add_280_0 = obj_280.add_stone(stone_280_0)
                stone_280_1 = Stone(True, (2.07, -0.31), 1, True, False)
                add_280_1 = obj_280.add_stone(stone_280_1)
                stone_280_2 = Stone(False, (-0.84, 3.36), 2, True, False)
                add_280_2 = obj_280.add_stone(stone_280_2)
                var_280_add_stone = obj_280.add_stone(stone_280_2)
        
    def test_81(self):
        obj_949 = Game()
        end_949_0 = End(False)
        add_end_949_0 = obj_949.add_end(end_949_0)
        var_949_add_end = obj_949.add_end(end_949_0)
        self.assertEqual(add_end_949_0, None)
        
    def test_82(self):
        obj_647 = Stone(True, (-1.6, -2.33), 8, False, False)
        
    def test_83(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_856 = Game()
                end_856_0 = End(True)
                add_end_856_0 = obj_856.add_end(end_856_0)
                end_856_1 = End(False)
                add_end_856_1 = obj_856.add_end(end_856_1)
                var_856_score = obj_856.score()
        
    def test_84(self):
        obj_246 = End(True)
        stone_246_0 = Stone(False, (2.5, 3.67), 1, True, False)
        add_246_0 = obj_246.add_stone(stone_246_0)
        stone_246_1 = Stone(True, (-0.22, -4.01), 1, True, False)
        add_246_1 = obj_246.add_stone(stone_246_1)
        stone_246_2 = Stone(False, (-1.42, 0.57), 2, True, False)
        add_246_2 = obj_246.add_stone(stone_246_2)
        var_246_score = obj_246.score()
        self.assertEqual(add_246_0, None)
        self.assertEqual(add_246_1, None)
        self.assertEqual(add_246_2, None)
        self.assertEqual(var_246_score, 1)
        
    def test_85(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_459 = Game()
                end_459_0 = End(False)
                add_end_459_0 = obj_459.add_end(end_459_0)
                end_459_1 = End(True)
                add_end_459_1 = obj_459.add_end(end_459_1)
                var_459_display_scoreboard = obj_459.display_scoreboard()
        
    def test_86(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_932 = Game()
                end_932_0 = End(False)
                add_end_932_0 = obj_932.add_end(end_932_0)
                end_932_1 = End(False)
                add_end_932_1 = obj_932.add_end(end_932_1)
                end_932_2 = End(True)
                add_end_932_2 = obj_932.add_end(end_932_2)
                var_932___str__ = obj_932.__str__()
        
    def test_87(self):
        obj_757 = Game()
        end_757_0 = End(True)
        add_end_757_0 = obj_757.add_end(end_757_0)
        var_757___str__ = obj_757.__str__()
        self.assertEqual(add_end_757_0, None)
        self.assertEqual(var_757___str__, 'Game with 1 ends')
        
    def test_88(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_329 = Stone(False, (2.5, 4.71), 0, True, True)
                var_329_move = obj_329.move((-0.25, 0.35))
                var_329_move = obj_329.move((-0.25, 0.35), 2)
                var_329_move = obj_329.move((-0.25, 0.35), 2, True)
        
    def test_89(self):
        obj_341 = Stone(True, (-2.39, 2.47), 2, False, False)
        
    def test_90(self):
        with self.assertRaisesRegex(ValueError, "If the last end was a blank, the hammer should not switch to the other team."):
                obj_888 = Game()
                end_888_0 = End(False)
                add_end_888_0 = obj_888.add_end(end_888_0)
                end_888_1 = End(True)
                add_end_888_1 = obj_888.add_end(end_888_1)
                var_888___str__ = obj_888.__str__()
        
    def test_91(self):
        obj_22 = Stone(True, (-2.72, 2.41), 9, True, True)
        
    def test_92(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_89 = Stone(False, (-1.76, 2.63), -2, False, False)
        
    def test_93(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_467 = Stone(False, (-1.52, -3.6), 11, True, False)
        
    def test_94(self):
        obj_369 = Game()
        end_369_0 = End(True)
        add_end_369_0 = obj_369.add_end(end_369_0)
        var_369_add_end = obj_369.add_end(end_369_0)
        self.assertEqual(add_end_369_0, None)
        
    def test_95(self):
        obj_643 = Stone(False, (1.19, -0.07), 7, True, True)
        
    def test_96(self):
        obj_922 = Game()
        end_922_0 = End(False)
        add_end_922_0 = obj_922.add_end(end_922_0)
        var_922_red_winner = obj_922.red_winner()
        self.assertEqual(add_end_922_0, None)
        self.assertEqual(var_922_red_winner, None)
        
    def test_97(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_790 = Stone(False, (-0.94, -4.97), 0, False, True)
        
    def test_98(self):
        with self.assertRaisesRegex(TypeError, "Stone.move() missing 2 required positional arguments: 'in_round' and 'by_red'"):
                obj_768 = Stone(False, (1.93, -5.57), 7, False, True)
                var_768_move = obj_768.move((-5.0, 5.0))
                var_768_move = obj_768.move((-5.0, 5.0), 4)
                var_768_move = obj_768.move((-5.0, 5.0), 4, False)
        
    def test_99(self):
        with self.assertRaisesRegex(ValueError, "Round must be between 1 and 10."):
                obj_958 = Stone(True, (0.04, -1.89), -2, True, True)
        