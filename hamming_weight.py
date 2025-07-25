class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_scanner = 0
        while 2 ** (bit_scanner + 1) <= n:
            bit_scanner += 1
        counts = 0
        while n:
            if 2 ** (bit_scanner) <= n:
                counts += 1
                n -= 2 ** (bit_scanner)
            else:
                bit_scanner -= 1
        return counts
