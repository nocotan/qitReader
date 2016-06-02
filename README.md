#qitReader
Qiita Reader in konsole
=========================================

OverView  
##Description
Qiitaをコンソール上で見ることができます。  
黒い画面から出たくない人向け......  
UNIXコマンドを扱うように操作、閲覧することができます。  
##Usage  
初回認証が必要
```
$ python3 qit_reader.py
YOUR ACCESS TOKEN: <your_access_token>
```

```
QitReader[user] ~ $
QitReader[user] ~ $ ls
all_items  follow_items  all_tags  follow_tags
QitReader[user] ~ $ cd all_items
QitReader[user] ~/all_items $ ls
[0] 記事1  [1] 記事2  [2] 記事3 ......
......
QitReader[user] ~/all_items $ 0
**************************内容表示*************************************

```
