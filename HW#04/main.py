# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     print(letter + suffix)
#
# # task 1
# s = 'Python'
# for i in range(len(s)):
#     print(s[i])
#
# # task 2
# s = 'London isthe Capital of GB.'
# new_s_1 = s[0:9]
# new_s_2 = s[9:]
# print(new_s_1 + " " + new_s_2)


# task 3
# def get_diff(word1, word2):
#     for letter in word1:
#         if letter not in word2:
#             print(letter)
#
#
# # task 4
# def compare(let, st):
#     for letter in st:
#         if let < letter:
#             print(let, "стоит по алфавиту до", letter)
#         elif let > letter:
#             print(let, "стоит по алфавиту после", letter)
#         else:
#             print(let, "стоит на том же месте что и", letter)
#
#
# # task 5
# def search_substr(subst, st):
#     subst = subst.lower()
#     st = st.lower()
#     if subst not in st:
#         print("Not found")
#     else:
#         print("Found")
#
#
# # task 6
# def is_palindrome(word):              # 01234
#     print(word[len(word)-1::-1])      # banab
#     if word == word[-1::-1]:
#         print("yes")
#     else:
#         print("no")
#
#
# def reverse(str):
#     print(str[-1::-1])
#
#
# def is_reverse(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     i = 0
#     j = len(word2) - 1
#     while j > 0:
#         if word1[i] != word2[j]:
#             return False
#         i = i + 1
#         j = j - 1
#     return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # get_diff("qwwert", "qwvvvvt")
    # compare('e', 'nice')
    # search_substr('gr', 'I am GREEN')
    # search_substr('GW', 'I am GREEN')
    # is_palindrome("banana")
    # reverse("Everset")
    #
    # print(is_reverse("stop", "pots"))
