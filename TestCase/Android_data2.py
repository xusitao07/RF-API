# coding=utf-8

import pymysql

class Do:
    def do_dql(self, sql):
        global id
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com',db='num_pro', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        sql = sql
        cursor.execute(sql)
        connection.commit()
        results = cursor.fetchall()
        print (results)
        for row in results:
            id = row["id"]
        connection.close()
        return id

examinUrl = {
    "examinUrl":"http://admin.tjs.com/server/product/update_status.html"
}
Sql2 = "SELECT id FROM n_product WHERE NAME = 'app'"
pc = Do()
establisID = pc.do_dql(Sql2)
print (establisID,'\n')
examinPostDate = {
    "examinPostDate":{
        "product_id": establisID,
        "verifyed": "Y",
        "remark":"123"
    }

}
