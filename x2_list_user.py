#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 研修用ユーザーのリストツール
#  
#  機能
#    このプログラムは、ソフトレイヤーのハンズオン研修用などの目的で、
#    子ユーザーのリストを表示します。
#    
#　使い方
#　　1. プライマリーアカウントのユーザーIDとパスワードをセットする(1)
#    2. 本プログラムの実行
#
#  注意点
#    ポータル画面に表示されなユーザーが表示される事があります。
#
#  作成者  Maho Takara   takara@jp.ibm.com
#  2015/5/8   


import SoftLayer
import random
import string

#
#  プライマリーアカウントの
#    ユーザーIDとパスワード  (1)
#

username='hack91800'
api_key='52083f49009962983409b0309e89a95edf0deb052b2ab566289ab2a5915712c4'


#
# APIログイン
#
def api_login():
    client = SoftLayer.Client(username, api_key )
    try:
        object_mask = 'id,username,firstName,lastName'
        ret = client['Account'].getCurrentUser(mask=object_mask)
        print "Current User = %s " % ret['username']
    except SoftLayer.SoftLayerAPIError as e:
        print("faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        return False

    return client


#
#
# メイン
#
#
if __name__ == '__main__':

    clt = api_login()
    if clt == False:
        print "Failed: api_login()"
        exit(1)

    #
    # 子ユーザーのリスト
    #
    try:
        object_mask = 'id,username,firstName,lastName'
        ret = clt['Account'].getCurrentUser(mask=object_mask)
        ret = clt['SoftLayer_User_Customer'].getChildUsers(mask=object_mask,id=ret['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        exit(1)

    print "%-16s       %-6s    %-15s           %-15s" % ("Username", "id", "firstName", "lastName")

    for x in ret:
        ret2 = clt['SoftLayer_User_Customer'].isMasterUser(id=x['id'])
        if ret2 != True:
            print "%-16s       %-6d    %-15s           %-15s" % (x['username'],x['id'],x['firstName'],x['lastName'])


#exit(0)





