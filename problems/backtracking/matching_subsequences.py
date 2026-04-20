class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        s_with_indexes = list(enumerate(s))
        count = 0

        def is_valid(current_ch, current_path):
            if current_ch in current_path:
                return False

            if len(current_path) > 0 and current_path[-1][0] >= current_ch[0]:
                return False

            return True

        def backtrack(start, path=[]):
            nonlocal count

            word = "".join([ch for (_dx, ch) in path])
            while word in words:
                count += 1
                words.remove(word)

            # prune
            if count == len(words):
                return

            # is a leaf
            if start == s_with_indexes[-1]:
                return

            for ch in s_with_indexes:
                # prune
                if not is_valid(ch, path):
                    continue

                path.append(ch)
                backtrack(ch, path)
                path.pop()

        backtrack(0, [])
        return count


sol = Solution()
print(
    sol.numMatchingSubseq(
        "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac",
        [
            "wpddkvbnn",
            "lnagtva",
            "kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju",
            "rwpddkvbnnugln",
            "gloeofnpjqlkdsqvruvabjrikfwronbrdyyj",
            "vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos",
            "mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina",
            "rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip",
            "fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq",
            "qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx",
        ],
    )
)
