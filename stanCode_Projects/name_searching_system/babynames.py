"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # name_data(dict) ：key=新生兒名字；value(dict)=name在year的rank
    # year(str) 年代
    # rank(str) 該新生兒在當年的排名
    # name(str) 新生兒名字
    # 年份不同：都要加到name_data
    # 年份相同：檢查name,year是否已存在？若是，把name在year的rank存較低(數字較小)的排名
    if name in name_data:  # 如果已經有名字了
        if year in name_data[name]:  # 如果已經有year了
            if int(rank) < int(name_data[name][year]):  # 如果新的資料rank比較小
                name_data[name][year] = rank  # 取代原有資料
        else:
            name_data[name][year] = rank  # 輸入新的year與rank
    else:  # 如果還沒有名字
        name_data[name] = {}
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    # 使用add_data_for_name，把檔案名filename的文字檔加到name_data中
    # year：rank(1~1000),name1(男),name2(女)
    with open(filename, "r") as f:  # 開啟檔案
        for line in f:  # 一行行地找
            # 建立清單儲存資料
            # wrong code: for i in range(len(f)):
            word_list = line.split(",")  # 把line變成word_list
            if len(word_list) == 1:  # 如果是第一行(只儲存一個東西)
                year = word_list[0].strip()  # 儲存成年分
            else:
                rank = word_list[0].strip()
                name1 = word_list[1].strip()
                name2 = word_list[2].strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):  # 閱讀所有的files，return一個name_data字典
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for i in range(len(filenames)):  # 每個file都找過了
        filename = filenames[i]
        add_file(name_data, filename)  # file的資料都被加入到name_data
    return name_data


def search_names(name_data, target):
    # 擁有裝了資訊的name_data字典與文字片段target，return一個names(list)
    # 因為忘記該怎麼取字典的key而卡關過
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []
    target = target.upper()
    for key in name_data:  # 一個個找name_data的key word(name)
        key_change = key.upper()
        if target in key_change:
            names += [key]  # 把key word(name)儲存入list
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
