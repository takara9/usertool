# usertool
SoftLayer child user add, delete, list tool for the Hack session

#SOFTLAYERハンズオンのユーザー作成ツール

　
##python コード

- x1_add_user.py   子ユーザー追加
- x2_list_user.py  子ユーザーリスト表示  
- x3_del_user.py   子ユーザー削除

  
##機能

このプログラムは、ソフトレイヤーのハンズオン研修用などの目的で、同じ権限の子ユーザーIDを一度に複数作るためのプログラムです。子ユーザーの作成条件は、下記の使い方に表した様に、このプログラムを編集して設定する方式のエッセンシャルな機能だけを持つものです。


##使い方

- プライマリーアカウント(1)のユーザーIDとパスワードをセットする
- ユーザーの属性情報(2)を編集して、利用目的に則した内容にする
- ユーザーに与える権限のリスト(3)を編集（そのままでもOK）
- 本プログラムの実行
- 作成するユーザー数をインプット
- ユーザーIDとパスワードのリストをコピペして保存
- 実行結果の確認（ポータルのAccount->Usersで確認)
- 演習ユーザーの利用(ハンズオン・セッション）
- ユーザーの削除 x3_del_user.py


##使用例

###(a) ユーザー追加

    $./x1_add_user.py
    How many the child user id do you want to add ? 3
    Current User = hack91800
    username = hack71187  password = ddnSeF$7
    username = hack71188  password = dgUygm#2
    username = hack71189  password = hropnH!8



###(b) ユーザーのリスト表示

    $ ./x2_list_user.py
    Current User = hack91800
    Username               id        firstName                 lastName
    hack71187              367237    Hands on user             expire in 3 days
    hack71188              367239    Hands on user             expire in 3 days
    hack71189              367241    Hands on user             expire in 3 days　


###(c) ユーザーの削除

    $ ./x3_del_user.py
    Current User = hack91800
    Username               id        userStatusId
    hack71187              367237    1001
    hack71188              367239    1001
    hack71189              367241    1001



##注意点

子ユーザーを一括で削除するので、必要なユーザー全てを消す可能性があります。
ソフトレイヤーの制約により、削除した同じユーザー名は、しばらく再利用できません。



##作成者  

高良 真穂 (Maho Takara)
takara@jp.ibm.com, takara9@gmail.com, @MahoTakara
https://www.facebook.com/profile.php?id=100002198440895


##日付

2015/5/8   
