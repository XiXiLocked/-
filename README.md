# 人人影视开源字幕查找器
最近（2024/12/6) 人人影视开源了20年的字幕。但是东西很多(20+G),目录结构复杂，不方便查找，所以我整理了一份放进sqlite里方便查找。

字幕存放的地方很分散，有直接放在某某文件夹下的，也有哈希掉名字只能从开源的数据库里挖到信息的。所以本查找器会从 中文名，英文名，文件名多方面查找。


# How To Use

```
python main.py Trapped
```
或者
```
python main.py "Trapped"
```
就会从数据库`rrys_sub.sqlite3`里找带`Trapped`的文件，并返回他在哪个rar里.
```
创业公司 第一季第六集 StartUp S01E06 StartUp+S01E06+Bootstrapped+1080p+WEB-DL+AAC2.0+H.264.zip
         字幕备份.part07.rar 2016/0910/33baac336a4c5b0543993757d30f18fd.zip
畸变第1季第4集（精校） Freakish.S01E04 Freakish.S01E04.Trapped.720p.HULU.WEBRip.AAC2.0.H.264-NTb.zip
         字幕备份.part07.rar 2016/1124/f7e0416205bd267d348e6e876248c24d.zip
紧急呼救 第1季 第9集【精校】 9-1-1.S01E09 9-1-1.S01E09.zip
         字幕备份.part08.rar 2018/0320/b57874ca15403edb1a38766d1a6b2d0d.zip
我制服了魔鬼 I.Trapped.The.Devil I.Trapped.The.Devil.2019.1080p.WEB-DL.DD5.1.H264-FGT.rar
         字幕备份.part09.rar 2019/0504/3d06292f8a8c9ceb290fd11dcb5531b8.rar
悬浮聚会 第二季第十集 Light.as.a.Feather.S02E10 Light.as.a.Feather.S02E10.Trapped.as.a.Rat.1080p.AMZN.WEB-DL.DDP2.0.H.264-NTb.zip
         字幕备份.part01.rar 2020/0428/cdc1e3b7cf028f02f88b23c01d4a4ead.zip
哈莉·奎茵 第2季第3集 Harley Quinn S02E03 Harley.Quinn.S02E03.Trapped.1080p.DCU.WEB-DL.DDP5.1.H264-NTb.zip
         字幕备份.part01.rar 2020/0418/8ede21a0b5ad3b0bf4b7ca50e3bf302a.zip
[呼救无门].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/system/misc/subs/other/200904/[呼救无门].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
[鍛兼晳鏃犻棬].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/system/misc/subs/other/200904/[鍛兼晳鏃犻棬].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
[閸涘吋鏅抽弮鐘绘，].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/system/misc/subs/other/200904/[閸涘吋鏅抽弮鐘绘，].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
[呼救无门].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/uploads/files/specialt_name/[呼救无门].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
[鍛兼晳鏃犻棬].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/uploads/files/specialt_name/[鍛兼晳鏃犻棬].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
[閸涘吋鏅抽弮鐘绘，].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
         字幕备份.part03.rar files/uploads/files/specialt_name/[閸涘吋鏅抽弮鐘绘，].Trapped.Ashes.2006.Limited.DVDRiP.XviD-iNTiMiD.avi.rar
```



## 数据库样本
```
sqlite> .tables
subtitle             subtitle_in_rar    
subtitle_format_rel  subtitle_lang_rel 

sqlite> select count(*) from subtitle;
56134

sqlite> select * from subtitle limit 3;
10001|非常人贩2|Transporter2 2005|0|0|0|720p|1|trans|其他字幕|/中英/|/ASS/|./files/system/misc/subs/c/200904/c93749152900f479ae80f7760006fdee20080315010030.rar|非常人贩1||3231|1121|0|0|0|1|1241016405
10002|色即是空2|Sex Is Zero 2|0|0|0|DVDRip.XviD.AC3-BTlaide|1|trans|电影字幕|/简体/|/ASS/|./files/system/misc/subs/0-9/200904/2d9bc22e47fd8f26bd7440454c1b381020080314160903.zip|色即是空1||30291|10859|0|0|0|1|1241016404
10003|迷失第四季第7集|LOST第四季第7集|0|0|0|hdtv.xvid-dot|1|trans|欧美剧字幕|/简体/繁体/英文/|/SRT/|./files/system/misc/subs/e/200904/e0b27bd0d62dc1a8a921ac7c00d18e6d20080314074559.rar|迷失第四季第7集||158|88|0|0|0|1|1241016404


sqlite> select count(*) from subtitle_lang_rel;
46549

sqlite> select * from subtitle_lang_rel limit 3;
10001|cnen
10002|cn
10003|cn

sqlite> select count(*) from subtitle_format_rel;
27298

sqlite> select * from subtitle_format_rel limit 3;
10001|ass
10002|ass
10003|srt

sqlite> select count(*) from subtitle_in_rar;
117302

sqlite> select * from subtitle_in_rar limit 3;
2020/0101/01c9640a80725b5fa36cb5aa647fcc8b.srt|字幕备份.part01.rar
2020/0101/102097b9d278ba6f0dbd6db528f7c1fc.srt|字幕备份.part01.rar
2020/0101/177d99c1e9ff13e3f4c4714a873bf011.txt|字幕备份.part01.rar
```