#coding = utf-8
import pymysql
import re
def JudgeChinese(s):
    for c in s:
        if not ('\u4e00' <= c <= '\u9fa5'):
            return False
        return True
class NuclearSql:

    def Search(self,nuclear,num):
        try:
            db = pymysql.connect("localhost", "root", "wasd1234", "nuclear",charset='utf8')
            cur = db.cursor()
            sql = "select * from nuclear where name = '"+nuclear+"'"
            result = cur.execute(sql)
            # result = cur.fetchall()
            # cur.close()

            for each in result:
                if str(each[2])==str(nuclear) and int(each[0]) ==int(num) :
                    return each
            return False
        except :#如果数据库连接异常，就直接使用本地文件进行查找。
            # print("error")
            if JudgeChinese(nuclear) == False:
                try:
                    with open("data//AllDATA1.csv", 'r', encoding="utf8") as f_obj:
                        reader = f_obj.readlines()
                        for each in reader:  # 对文件进行遍历
                            temp = each.split(",")
                            if ((temp[2]).lower() == (nuclear).lower() and temp[0] == num):  # 如果遇到从查找元素将他返回，否则返回False;
                                # print(temp)
                                return temp
                        f_obj.close()
                        return False
                except:
                    print("文件操作有错！！！")
            else:
                try:
                    with open("data//AllDATA1.csv", 'r', encoding="utf8") as f_obj:
                        reader = f_obj.readlines()
                        for each in reader:  # 对文件进行遍历
                            temp = each.split(",")
                            if (temp[1] == nuclear and temp[0] == num):  # 如果遇到从查找元素将他返回，否则返回False;
                                # print(temp)
                                return temp
                        f_obj.close()
                        return False
                except:
                    print("文件操作有错！！！")
    def _search(self,nuclear):#当只输入某个元素的时候
        if JudgeChinese(nuclear) == False:#如果输入的是非中文
            try:
                with open("data//AllDATA1.csv", 'r', encoding="utf8") as f_obj:
                    reader = f_obj.readlines()
                    result = []
                    for each in reader:  # 对文件进行遍历
                        temp = each.split(",")
                        if (temp[2].lower() == nuclear.lower()):  # 如果遇到从查找元素将他返回，否则返回False;
                            # print(temp)
                            result.append(temp)
                    f_obj.close()
                    return result
            except:
                print("错一")
        else:
            try:
                with open("data//AllDATA1.csv", 'r', encoding="utf8") as f_obj:
                    reader = f_obj.readlines()
                    result = []
                    for each in reader:  # 对文件进行遍历
                        temp = each.split(",")
                        if (temp[1] == nuclear):  # 如果遇到从查找元素将他返回，否则返回False;
                            # print(temp)
                            result.append(temp)
                    f_obj.close()
                    return result
            except:
                print("错二")



    def Show(self):
        try:
            db = pymysql.connect("localhost", "root", "wasd1234", "nuclear",charset='utf8')
            cur = db.cursor()
            # sql = "select * from nuclear "
            result = cur.execute(sql)
            result = cur.fetchall()
            # cur.close()
            return result
        except:
            x  = []
            try:
                with open("data//AllDATA1.csv", 'r', encoding="utf8") as f_obj:
                    reader = f_obj.readlines()
                    for each in reader:  # 对文件进行遍历
                        temp = each.split(",")
                        # print(temp)
                        # print(temp)
                        x.append(temp)
                    return  x
            except:
                print("show wrong")
            return False
# def main(nuclear,number):
#     try:
#         with open("dataall1.csv", 'r', encoding="utf-8") as f_obj:
#             reader = f_obj.readlines()
#             for each in reader:  # 对文件进行遍历
#                 temp = each.split(",")
#                 if (temp[2] == nuclear and temp[0] == number):  # 如果遇到从查找元素将他返回，否则返回False;
#                     print(temp)
#                     return temp
#             f_obj.close()
#             return False
#     except:
#         print("文件操作有错！！！")
    # n = NuclearSql()
    # print(n.Search("Fe","56"))
    # print(n.Show())
    # print(type(n.Show()))
    # items = ['呵呵', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    # print(type(items))
    #          ,'m','n','o','p','q','r','s','t']
    # x = input("输入")
    # y = x.split( )
    # for each in y:
    #     print(y)
    # z = re.split('(\d+)' , x)
    # for each in z:
    #     print(each)
    # print(n.Search(z[0],int(z[1])))

if __name__ =="__main__":
    # main("Fe","56")
    n = NuclearSql()

    print(n._search("铁"))
    # print(n.Show())
    # print(n.Show())