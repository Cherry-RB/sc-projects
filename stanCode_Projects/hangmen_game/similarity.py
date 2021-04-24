"""
File: similarity.py
Name:Cherry
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    step:
        1.cut the long_sequence to become cut_sequence
        2.comparing the similarity between cut_sequence and short_sequence
    considering:
        1.How many variables I need?  # (有多少變數？被切分的段、最高分的段、相似度分數、最高分)
            (1)cut_sequence (2)best_sequence (3)similarity (4)highest_similarity
        2.What fixed number I would usually need?  # (固定的數？long的長度、short的長度(每一段比較多少次)、比較多少段)
            (1)len(long_sequence)
            (2)len(short_sequence) == the times of comparing each cut_sequence
            (3)the amount of cut_sequence == len(long_sequence)-len(short_sequence)+1
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match?')
    long_sequence = long_sequence.upper()
    short_sequence = short_sequence.upper()
    best_sequence = ''
    highest_similarity = 0
    for i in range(len(long_sequence)-len(short_sequence)+1):  # repeat comparing different cut_sequence(比較多少段)
        # step1.cut the long_sequence to become cut_sequence
        cut_sequence = ''  # make new variable of cut_sequence(新竹籤「被切分的段」)
        while len(cut_sequence) != len(short_sequence):  # (一個個字母串上去，直到竹籤長度等於short_sequence)
            for k in range(len(short_sequence)):      # (每段起始串的位置)
                cut_sequence += long_sequence[i+k]
        # get cut_sequence!!!  # (就會得到「被切分的段」)
        if i == 0:
            best_sequence = cut_sequence  # get best_sequence!(得到「最高分的段」)
            similarity = 0  # get similarity!(變數「相似度分數」)
            highest_similarity = similarity  # get highest_similarity!(得到「最高分」)
        # step2.comparing the similarity between cut_sequence and short_sequence
        similarity = 0
        for j in range(len(short_sequence)):  # (每一段比較多少次)
            if cut_sequence[j] == short_sequence[j]:  # (當同個位置上，「被切分的段」=short_sequence)
                similarity += 1  # (變數「相似度分數」+1)
        # according to the newest comparing renew the variables(依據最新的比較，更新「最高分的段」與「最高分」)
        if similarity > highest_similarity:
            best_sequence = cut_sequence
            highest_similarity = similarity
    print('The best match is ' + str(best_sequence))


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
