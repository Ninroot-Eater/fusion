import csv

def get_lst(csv_file, mode="r", encode="utf-8"):
    x = csv.reader(open(csv_file,f"{mode}",encoding=encode))
    x = [i for i in x]
    del x[0]
    return x


def main(usin):
    daddy = get_lst(usin["file_daddy"])
    mommy = get_lst(usin["file_mommy"])
    baby = open("baby.csv", "w", encoding="utf-8")

    dic = {}
    for i in mommy:
        k = i[usin["uni_mom"]]
        lst = []
        for j in usin["lst_mom"]:
            lst.append((j[0], i[j[1]]))
        dic[k] = lst

    dupli = []
    for i in daddy:
        k = i[usin['uni_dad']]

        if k in dic.keys() and k not in dupli:
            dupli.append(k)

            lst = []
            for j in usin["lst_dad"]:
                lst.append((j[0], i[j[1]]))
            dic[k] += lst

    wr = csv.writer(baby)

    for i in dic.keys():
        lst = [''] * 64
        lst[0] = i
        for j in dic[i]:
            lst[j[0]] = j[1]
        wr.writerow(lst)






