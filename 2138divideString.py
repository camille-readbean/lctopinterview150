class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        acc = ''
        r = []
        for idx, ch in enumerate(s):
            if idx != 0 and idx % k == 0:
                r += [acc]
                acc = ''
            acc += ch
        if acc != '' and len(acc) != 0:
            acc += (k - len(acc)) * fill
            r += [acc]
        return r
