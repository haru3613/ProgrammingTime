def valid_parentheses(string):
    # 篩選出所有括號
    import re
    new_list = [s for s in list(string) if re.search("\(|\)",s)]

    if len(new_list) % 2 != 0: return False
    if len(new_list) == 0: return True
    if new_list[0]==")" or new_list[-1]=="(": return False
    # 先找到最後一個"(", 再用begin index去抓取第一個")"
    for i in range(len(new_list)//2):
        try:
            last_one = "".join(new_list).rindex("(")
            first_one = "".join(new_list).index(")", last_one)
        except:
            return False
        del new_list[first_one]
        del new_list[last_one]

    if len(new_list)==0:
        return True
    else:
        return False