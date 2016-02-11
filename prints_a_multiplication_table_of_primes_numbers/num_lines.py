# -*- coding: utf-8 -*-

__all__ = ["NumLines"]


class NumLines(object):
    """
    Given a num list, and generate a number lines table which looks like,

            2   3   5   7  11
         2  4   6  10  14  22
         3  6   9  15  21  33
         5 10  15  25  35  55
         7 14  21  35  49  77
        11 22  33  55  77 121
    """

    @staticmethod
    def generate(nums):
        assert len(nums) > 0
        lines = list()

        """
        # 1. the main part
          4   6  10  14  22
          6   9  15  21  33
         10  15  25  35  55
         14  21  35  49  77
         22  33  55  77 121
        """
        for n1 in nums:
            curr_line = list()
            for n2 in nums:
                curr_line.append(n1 * n2)
            lines.append(curr_line)

        """
        # 2. complete the rest
        """
        # 2.1 fix the first column
        lines = [([nums[idx]] + line) for idx, line in enumerate(lines)]
        # 2.2 prepend the first row
        lines.insert(0, [""] + nums)

        return lines
