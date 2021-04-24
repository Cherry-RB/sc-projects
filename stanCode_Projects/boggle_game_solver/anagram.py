"""
File: anagram.py
Name:Cherry
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

may_anagrams_list = []
dic = {}
anagrams_list = []
times = 0


def main():
    global may_anagrams_list, anagrams_list, times
    print("Welcome to stanCode \" Anagram Generator\"(or -1 to quit)")
    read_dictionary()
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        else:
            may_anagrams_list = []
            anagrams_list = []
            times = 0
            find_anagrams(s)


def read_dictionary():
    global dic
    with open(FILE, "r") as f:
        for word in f:
            sub = word[0:1]
            word = word[:"\n".find(word)]
            if sub in dic:
                dic[sub] += [word]
            else:
                dic[sub] = []
                dic[sub] += [word]


def get_all_may_anagrams_list(s_list, letter_change_list):
    # 獲得要排列組合的字母的清單(s_list)、獲得全新的清單(letter_change_list)
    global may_anagrams_list
    # Base Case
    if len(s_list) == len(letter_change_list):
        may_anagrams_str = ""  # 建立新的字串，用來把排列好的清單(letter_change_list)變成字串(may_anagrams_str)
        for letter in letter_change_list:
            # 處理重複的字母
            while len(letter) != 1:  # 如果是重複的字母，把數字清掉
                letter = letter[0]
            may_anagrams_str += str(letter)
        if may_anagrams_str not in may_anagrams_list:
            may_anagrams_list += [may_anagrams_str]
    # Self-Similarity
    else:  # 排列組合
        for letter in s_list:
            if letter not in letter_change_list:
                letter_change_list += [letter]
                get_all_may_anagrams_list(s_list, letter_change_list)
                letter_change_list.pop()


def find_anagrams(s):
    """
    :param s:str, the word need to search in dictionary
    :return:(directly print)
    """
    # get all may_anagrams
    global anagrams_list, times
    s_list = []
    double_count = 0
    # 檢查詞語中有沒有重複的字母
    for i in range(len(s)):
        if s[i] in s[i + 1:]:  # 如果有重複，進行加工
            double_count += 1
            s_list += [s[i] + str(double_count)]
        else:
            s_list += s[i]
    # print(s_list)
    # 把詞語(沒有重複的字母)丟進去，獲得所有字母(含重複的字母)的排列組合
    get_all_may_anagrams_list(s_list, [])
    # print(may_anagrams_list)  # 到時交作業要刪掉
    # find anagrams in dictionary
    for i in range(len(may_anagrams_list)):
        if str(may_anagrams_list[i]) in dic[str(may_anagrams_list[i][0])]:
            anagrams_list += [may_anagrams_list[i]]
            times += 1
            print("Searching...")
            print("Find:" + str(may_anagrams_list[i]))
    print("Searching...")
    print(str(times) + "  anagrams:  "+str(anagrams_list))
    print("")


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
