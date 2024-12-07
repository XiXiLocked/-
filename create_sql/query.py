import re
import sqlite3
from dataclasses  import dataclass
from .create_sqlite import SQLITE_FILE

@dataclass
class Subtitle:
    id:int
    cnname:str
    enname:str
    resourceid:int
    season:int
    episode:int
    segment:str
    segment_num:int
    source:str
    category:str
    lang:str
    format:str
    file:str
    filename:str
    remark:str
    view:int
    downloads:int
    comments:int
    updater:int
    updatetime:int
    operator:int
    dateline:int

@dataclass
class Query_result:
    subtitle:Subtitle
    volume:str
    file_path:str

def query_from_Table_subtitle(con, query):
    sql_find= r"select * from subtitle where  cnname like ? or enname like ? or segment like ? or file like ? or filename like ?;"
    sql_rar = r"select * from subtitle_in_rar where file like ?;"
    result_collection = []
    for i in con.execute(sql_find,(f"%{query}%",)*5):
        sub = Subtitle(*i)
        query_file = sub.file
        if query_file:
            if query_file.startswith(r'./'):
                query_file = query_file[2:]
            result = con.execute(sql_rar,(f"%{query_file}%",)).fetchone()
            if result:
                file, rar_file= result
                result_collection.append(Query_result(sub,rar_file,file))
            else:
                result_collection.append(Query_result(sub,"",""))
        else :
                result_collection.append(Query_result(sub,"",""))
            
    return result_collection


def query_from_Table_subtitle_in_rar(con, query):
    sql_find = r"select * from subtitle_in_rar where file like ?;"
    result_collection = []
    for i in con.execute(sql_find,(f"%{query}%",)):
        file, rar_file= i
        result_collection.append(Query_result(None,rar_file,file))
    return result_collection


          

def subtitle_find(query_name, sqlite_file = SQLITE_FILE):
    query_modified = re.sub(r"[\s._-]","%",query_name)
    query_modified = re.sub(r'%+', '%', query_modified)
    
    result_collection = []
    with sqlite3.connect(sqlite_file) as con:
        result_from_subtitle = query_from_Table_subtitle(con,query_modified)
        result_from_subtitle_in_rar = query_from_Table_subtitle_in_rar(con,query_modified)
        result_collection.extend(result_from_subtitle)
        result_collection.extend(result_from_subtitle_in_rar)
    return result_collection
            
            



if __name__ =="__main__":
    # subtitle_find("非常人贩")
    # subtitle_find("Knew")
    # for sub in subtitle_find("Hawk"):
    import sys
    query = sys.argv[1]

    for sub in subtitle_find(query):
        if sub.subtitle is not None:
            print(sub.subtitle.cnname,sub.subtitle.enname,"\t",sub.volume)
        else:
            *_,filename = sub.file_path.split("/")
            print(filename,"\t", sub.volume)