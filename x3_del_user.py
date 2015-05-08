#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 研修用ユーザーの削除ツール
#  
#  機能
#    このプログラムは、ソフトレイヤーのハンズオン研修用などの目的で作成した
#    子ユーザーIDを一度に削除するプログラムです。
#    
#　使い方
#　　1. 実行ユーザーのユーザーIDとAPI-KEY（パスワード）をセットする(1)
#    2. 本プログラムの実行
#
#  注意点
#    自ユーザーの子ユーザーを一度に消します。消してはいけないユーザーを区別しません。
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
    client = SoftLayer.Client(username=username, api_key=api_key )
    try:
        object_mask = 'id,username,firstName,lastName'
        ret = client['Account'].getCurrentUser(mask=object_mask)
        print "Current User = %s " % ret['username']
    except SoftLayer.SoftLayerAPIError as e:
        print("faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        return False

    return client

#
# メイン
#
if __name__ == '__main__':

    clt = api_login()
    if clt == False:
        print "Failed: api_login()"
        exit(1)

    #
    # 子ユーザーの削除
    #
    try:
        object_mask = 'id,username,firstName,lastName,userStatusId'
        ret = clt['Account'].getCurrentUser(mask=object_mask)
        ret = clt['SoftLayer_User_Customer'].getChildUsers(mask=object_mask,id=ret['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
        exit(1)

    print "%-16s       %-6s    %-5s" % ("Username", "id", "userStatusId")
    for x in ret:
        ret2 = clt['SoftLayer_User_Customer'].isMasterUser(id=x['id'])
        if ret2 != True:
            print "%-16s       %-6d    %-5d" % (x['username'],x['id'],x['userStatusId'])

            #user={'userStatusId': 1003} # INACTIVE
            user={'userStatusId': 1021} # CANCEL_PENDING
            try:
                account = clt['SoftLayer_User_Customer'].editObject(user,id=x['id'])
            except SoftLayer.SoftLayerAPIError as e:
                print("faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
                exit(1)






