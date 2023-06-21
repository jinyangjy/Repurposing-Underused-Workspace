import unittest
from Repurposing_underused_workspace import select_sections

class RideTest(unittest.TestCase):
    def test_selectsections_6(self):
        occupancy_probability = [
                    [19, 76, 38, 22],
                    [56, 20, 54, 68],
                    [71, 86, 15, 99],
                    [81, 82, 82, 22],
                    [36, 22, 22, 93]
                    ]
        expected = [98, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 2)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expected)

    def test_edge_case_duplicate_occ_check(self):
        occupancy_probability = [
                            [57, 76, 38, 22],
                            [56, 94, 54, 68],
                            [71, 86, 86, 99],
                            [81,  0,  0, 60],
                            [36, 22, 43, 93]
                            ]
        # Getting one of the following results should be fine
        expec_res_1 = [184, [(0, 3), (1, 2), (2, 1), (3, 1), (4, 1)]]
        expec_res_2 = [184, [(0, 3), (1, 2), (2, 2), (3, 2), (4, 1)]]
        expec_res_3 = [184, [(0, 3), (1, 2), (2, 1), (3, 2), (4, 1)]]
        expec_res_4 = [184, [(0, 3), (1, 2), (2, 2), (3, 1), (4, 1)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expec_res_1 or my_res == expec_res_2 or my_res == expec_res_3 or my_res == expec_res_4)

    def test_ed_stem_occupancy(self):
        occupancy_probability = [[57, 11, 14, 19, 63, 50, 61, 50, 40,  0,  46],
                         [ 2, 42, 98, 84, 56,  5, 33, 87, 60, 19,  91],
                         [84, 23, 37, 36, 38, 89, 72, 13, 48, 88,  46],
                         [36, 91, 11,  1,  5,  3, 38, 58, 37, 24,  39],
                         [52, 74, 67, 41, 76, 29, 38, 61, 74, 42,  10],
                         [46, 25, 38, 16, 50,  7, 99, 34, 79, 83,  19],
                         [76, 68, 74, 48, 38, 11, 46, 25, 31, 10,  73],
                         [99,  4, 65, 22, 12, 47, 18, 45, 63, 85,  17],
                         [35, 86, 91, 69, 50, 20, 72, 34, 24, 69, 100],
                         [20,  7, 63, 92, 33, 81, 22, 79, 85, 39,  21],
                         [98, 22, 37, 54, 28, 89, 50, 95, 59, 17,  88],
                         [13, 86, 98, 26, 30,  3, 93, 97, 59,  1,  23],
                         [39, 62, 48, 37, 35, 84, 87, 91, 63, 66,  21]]

        expected = [273, [(0, 1), (1, 0), (2, 1), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 5), (9, 4), (10, 4), (11, 5), (12, 4)]]
        self.assertEqual(expected, select_sections(occupancy_probability))

    def test_ed_stem_occupancy2(self):
        occupancy_probability = [[32, 86, 95, 15, 68, 90],
                         [91, 88, 96, 51, 64, 66],
                         [17, 70, 13,  9, 90, 17],
                         [17, 15, 38, 12, 53, 17],
                         [29,  6, 18, 27, 66, 48],
                         [74, 43, 76, 44,  3,  1],
                         [89,  1,  8, 24, 45, 62],
                         [ 3, 98, 99, 89,  6, 66]]
        expected_1 = [147, [(0, 3), (1, 3), (2, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 0)]]
        expected_2 = [147, [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 4), (6, 3), (7, 4)]]
        ret = select_sections(occupancy_probability)
        self.assertTrue(ret == expected_1 or ret == expected_2)

if __name__ == "__main__":
    unittest.main(argv=['ignored', '-v'], exit=False)