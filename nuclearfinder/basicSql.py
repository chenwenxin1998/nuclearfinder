import pymysql

class BasicSql:
    def Search(self,nuclear):
        try:
            db = pymysql.connect("localhost", "root", "wasd1234", "nuclear",charset='gbk')
            cur = db.cursor()
            sql = "select * from nucleardata"
            # print(sql)
            result = cur.execute(sql)
            # result = cur.fetchall()
            # print(result)
            for each in result:
                temp = each[0]
                temp2 = temp.split()[2]
                print(temp2)
                if nuclear == temp2:
                    return each
            return False
        except :
            try:
                with open("data//基本元素.csv", 'r', encoding="gbk") as f_obj:
                    reader = f_obj.readlines()
                    for each in reader:  # 对文件进行遍历
                        temp = each.split(",")
                        temp1 = temp[0]
                        # print(temp1)
                        temp2 = temp1.split()
                        for x in temp2:
                            if nuclear == x:
                                return temp
            except:
                print("FileOpenWrong")
            print("error")
def main():
    a = BasicSql()
    print(a.Search("Fe"))
    # try:
    #     with open("data//基本元素.csv", 'r', encoding="gbk") as f_obj:
    #         reader = f_obj.readlines()
    #         for each in reader:  # 对文件进行遍历
    #             temp = each.split(",")
    #             temp1 = temp[0]
    #             # print(temp1)
    #             temp2 = temp1.split()
    #             for x in temp2:
    #                 if "Fe" == x:
    #                     print(temp)
                # if nuclear == temp2:
                #     return each
    # except:
    #     print("FileOpenWrong")

