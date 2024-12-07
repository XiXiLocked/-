
from create_sql.parse_sql import *
from create_sql.create_sqlite import *
from create_sql.query import *


def test_parse_sql():
    sample = r"""(64625,'雪国列车 第1季第7集','Snowpiercer S01E07',40078,0,0,'Snowpiercer.S01E07.The.Universe.Is.Indifferent.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTG',1,'zimuzu','欧美剧字幕','/简体/繁体/英文/中英/','/SRT/ASS/','2020/0629/ae527ff4c66b5fdb1c8bd198ba2ff42c.zip','Snowpiercer.S01E07.The.Universe.Is.Indifferent.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTG.zip','',1225,669,0,0,0,3640975,1593431639),(64626,'阴阳魔界 第二季第五集【精校】','The Twilight Zone S02E05',37666,0,0,'The.Twilight.Zone.2019.S02E05.Among.the.Untrodden.720p.AMZN.WEB-DL.DDP5.1.H.264-NTb',1,'zimuzu','欧美剧字幕','/简体/繁体/英文/中英/','/SRT/ASS/','2020/1223/1f8ce08e5a7574188da4b9315d626fca.zip','The.Twilight.Zone.2019.S02E05.Among.the.Untrodden.720p.AMZN.WEB-DL.DDP5.1.H.264-NTb.zip','',195,151,0,506750,1608737553,506750,1593437750),(10394,'马格瑞姆的玩具店','Mr  Magorium\'s Wonder Emporium',0,0,0,'CHD.720p.DivX.DTSMA[BDrip]',1,'trans','电影字幕','/简体/繁体/','/SRT/','./files/system/misc/subs/0-9/200904/44548b9a963ab4451c594c115513bb6820080411161327.rar','马格瑞姆的玩具店','',221,267,0,0,0,1,1241016520);"""
    p = parse_sql(sample)
    parsed = p.parse()
    for i in parsed:
        assert len(i)==22,i
def test_read_rar_list():
    with open("data/part02.list.txt",'r') as f:
        for line in read_rar_list(f):
            pass
    assert line == "files/system/misc/subs/0-9/200904/100_Million_Bc20080512195821.rar"


def test_query():
    name_modified = re.sub(r"[\s._-]","%",name)
    pass