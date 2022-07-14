# -*- coding: utf-8 -*-
import argparse
import json
import math
import sys
import requests


class zoneF(object):
    print("""
                \033[34m0zoneF是一款以终端命令行方式查询0.zone的工具
                            use: python 0zoneF.py 
                            Author: kento-sec\033[0m
    """)

    def __init__(self):
        self.heard = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.url = 'https://0.zone/api/data/'
        self.zone_key_id = "" # 此处添加api-key
        parser = argparse.ArgumentParser(description="0zoneF是一款以终端命令行方式查询0.zone的工具")
        parser.add_argument("-q", "--query", type=str, metavar="query", help="example: key=零零信安")
#         parser.add_argument("-t", "--title_type", type=str, metavar="title_type", default='site',help="site:信息系统 akp:移动客户端 sensitive:敏感目录 email:邮箱 doc:文档 code:代码 membe:人员")
        args = parser.parse_args()
        if len(sys.argv) != 3:
            print(
                "[-]  参数错误！\neg1:>>>python3 0zoneF.py -q key=零零信安")
        self.query = args.query
        self.search()

    def search(self):
        body = {"title": "", "title_type": "site", "page": 1, "pagesize": 40,
                "zone_key_id": self.zone_key_id
                }
        body['title'] = self.query
        response = requests.request("POST", url=self.url, headers=self.heard, data=body)
        json_data = json.loads(response.text)
        totalresults = json_data['total']
        print("\033[32m[o]一共获取到: "+str(totalresults) + "条数据\033[0m")
        totalpage = math.ceil(totalresults/40)
        if totalresults > 40:
            for page in range(0,totalpage+1):
                page +=1
                body2 = {"title": "", "title_type": "site", "page": page, "pagesize": 40,
                         "zone_key_id": self.zone_key_id
                         }
                body2['page'] = page
                body2['title'] = self.query
                response = requests.request("POST", url=self.url, headers=self.heard, data=body2)
                json_data = json.loads(response.text)
                for num in range(0,40):
                    try:
                        print(json_data['data'][num]['url'])
                        url = json_data['data'][num]['url']
                        with open("{}.txt".format(self.query), mode="a") as rp:
                            rp.write(url + "\n")
                    except:
                        break

        elif totalresults <= 40:
            for num in range(0, 40):
                try:
                    print(json_data['data'][num]['url'])
                except:
                    break
        print("\033[32m[o]搜索完成！\033[0m")


if __name__ == '__main__':
    zooeF = zoneF()
