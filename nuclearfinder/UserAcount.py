import pymysql
import json
class UserAcount():
    def Judge(self,username,password):
        try:
            db = pymysql.connect("localhost", "root", "wasd1234", "useracount", charset='utf8')
            cur = db.cursor()
            # sql = "select * from useracount where username = '"+username+"'and password = '"+password+"'"
            print(sql)
            result = cur.execute(sql)
            result = cur.fetchall()
            print(result)
            for each in result:
                print(each)
            if(result):
                return True
            else:
                return False
        except:
            print("运行文件格式")
            try:
                with open("data//user.json", 'r', encoding="utf-8") as f_obj:
                    UserAcount = {'username': 'chenwenxin', 'password': "123456"}
                    # json.dump(UserAcount,f_obj)
                    user = json.load(f_obj)
                    if username == user['username'] and password == user['password']:
                        # print("登陆成功")
                        return True
                    else:
                        return False
            except:
                print("FileOpenWrong")
