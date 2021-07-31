set1 = {3, 4, 5}
set2 = {5, 6, 7}

union = set1 | set2

diff_1_2 = set1 - set2
diff_2_1 = set2 - set1

intersection = set1 & set2

symmetrical_diff = set1 ^ set2

symmetrical_diff.update(set2)
symmetrical_diff.discard(1)

remove_duplicate = lambda some_list: list(set(some_list))