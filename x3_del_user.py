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
#  2015/5/8  初版リリース
#  2015/8/13 ユーザーIDとAPI-KEYを初回実行時だけ入力する様に改良
#

import SoftLayer
import random
import string
import requests
import user_account as ua

#
# メイン
#
if __name__ == '__main__':

    requests.packages.urllib3.disable_warnings()
    clt = ua.api_login()
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






