class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        sorted(tokens)
        print(tokens)
        score = 0
        while tokens and (score or min(tokens) <= power):
            if min(tokens) <= power:
                    score += 1
                    power -= min(tokens)
                    tokens.remove(min(tokens))
            elif score:
                if len(tokens) < 2:
                    # you are giving up a score for no other coin
                    break
                else:
                    score -= 1
                    power += max(tokens)
                    tokens.remove(max(tokens))
            else:
                print("err")
        return score
            