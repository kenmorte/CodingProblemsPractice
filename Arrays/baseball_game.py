# https://leetcode.com/problems/baseball-game/description/

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = 0
        previous_valid_scores = []
        for op in ops:
            score = 0
            if op == '+':
                # Represents that the points you get in this round are the sum of the last two valid round's points.
                if len(previous_valid_scores) == 0:
                    continue
                elif len(previous_valid_scores) == 1:
                    score += previous_valid_scores[0]
                else:
                    score += previous_valid_scores[-1] + previous_valid_scores[-2]
                result += score
                previous_valid_scores.append(score)
            elif op == 'D':
                # Represents that the points you get in this round are the doubled data of the last valid round's points.
                if len(previous_valid_scores) == 0:
                    continue
                score += 2 * previous_valid_scores[-1]
                result += score
                previous_valid_scores.append(score)
            elif op == 'C':
                # Represents the last valid round's points you get were invalid and should be removed.
                if len(previous_valid_scores) == 0:
                    continue
                score = previous_valid_scores.pop()
                result -= score
            else:
                # Directly represents the number of points you get in this round.
                score = int(op)
                result += score
                previous_valid_scores.append(score)
        return result
