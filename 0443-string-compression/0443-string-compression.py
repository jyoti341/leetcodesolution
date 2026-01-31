from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        insert = 0

        while i < len(chars):
            group = 1

            # ONLY COUNT HERE
            while i + group < len(chars) and chars[i + group] == chars[i]:
                group += 1

            # WRITE AFTER COUNTING
            chars[insert] = chars[i]
            insert += 1

            if group > 1:
                for c in str(group):
                    chars[insert] = c
                    insert += 1

            i += group

        return insert


        