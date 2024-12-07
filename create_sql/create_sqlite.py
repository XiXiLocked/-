import os
import re
import sqlite3
from . import parse_sql
gpt_modified_CREATE = """CREATE TABLE subtitle (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cnname TEXT NOT NULL,
  enname TEXT DEFAULT NULL,
  resourceid INTEGER NOT NULL DEFAULT 0,
  season INTEGER NOT NULL DEFAULT 0,
  episode INTEGER NOT NULL DEFAULT 0,
  segment TEXT DEFAULT NULL,
  segment_num INTEGER NOT NULL DEFAULT 0,
  source TEXT NOT NULL,
  category TEXT NOT NULL,
  lang TEXT NOT NULL,
  format TEXT NOT NULL,
  file TEXT DEFAULT NULL,
  filename TEXT DEFAULT NULL,
  remark TEXT,
  views INTEGER NOT NULL DEFAULT 0,
  downloads INTEGER NOT NULL DEFAULT 0,
  comments INTEGER NOT NULL DEFAULT 0,
  updater INTEGER NOT NULL DEFAULT 0,
  updatetime INTEGER NOT NULL DEFAULT 0,
  operator INTEGER DEFAULT NULL,
  dateline INTEGER NOT NULL
);

CREATE INDEX idx_resourceid ON subtitle (resourceid);
CREATE INDEX idx_source ON subtitle (source);
CREATE INDEX idx_category ON subtitle (category);
CREATE INDEX idx_segment ON subtitle (segment);

CREATE TABLE subtitle_format_rel (
  subtitleid INTEGER DEFAULT NULL,
  format TEXT DEFAULT NULL,
  CONSTRAINT chk_format CHECK (format IN ('srt', 'ass'))
);

CREATE INDEX idx_subtitle_format ON subtitle_format_rel (subtitleid);

CREATE TABLE subtitle_lang_rel (
  subtitleid INTEGER DEFAULT NULL,
  lang TEXT DEFAULT NULL,
  CONSTRAINT chk_lang CHECK (lang IN ('cn', 'en', 'tw', 'kr', 'jp', 'cnjp', 'cnkr', 'cnen'))
);

CREATE INDEX idx_subtitle_lang ON subtitle_lang_rel (subtitleid);"""

SQLITE_FILE = "rrys_sub.sqlite3"

def read_sql(sql_file):
    DROP = []
    CREATE = []
    INSERT = []
    with open(sql_file,'r') as f:
        s = []
        record = False
        for e,line in enumerate(f):
            if "INSERT INTO" in line:
                INSERT.append(line)
            if "DROP TABLE" in line:
                DROP.append(line)

            if not record and "CREATE TABLE" in line:
                record = True
            if record:
                s.append(line)

            if record and ";" in line:
                record = False
                CREATE.append("".join(s))
                s.clear()
    return {"DROP":DROP,
            "CREATE":CREATE,
            "INSERT":INSERT}
  

def recreate_sql(subsql):
    match read_sql(subsql):
        case {"DROP":DROP,
            "CREATE":CREATE,
            "INSERT":INSERT}:
            with open("create_sql.sql",'w') as f:
                for drop in DROP:
                    f.write(drop)
                    f.write("\n")

                for sql in CREATE:
                    f.write(sql)
                    f.write("\n")
                
                for insert_data in INSERT:
                    f.write(insert_data)
        case _:
            raise ValueError("Not Appropriate Value")

def recreate_sqlite(sql_file):
    with sqlite3.connect(SQLITE_FILE) as con:
        placeholders ="?,"*22 
        sql = "INSERT INTO `subtitle` VALUES ("+placeholders[:-1] +")"
        match read_sql(sql_file):
            case {"DROP":DROP,
                "CREATE":CREATE,
                "INSERT":INSERT}:
                    for drop in DROP:
                        con.execute(drop)
                    for create in CREATE:
                        con.execute(create)
                    for i,insert in enumerate(INSERT):
                        if r"`subtitle`" in insert:
                            values = insert[29:].rstrip().rstrip(";")
                            for line in parse_sql(values).parse():
                            # for line in reparse_insert2(insert):
                                try:
                                    con.execute(sql,[eval(v) if v!="NULL" else None for v in line])
                                    # reparse_insert(insert))
                                except sqlite3.ProgrammingError:
                                    print(line,len(line),"error")
                                    for m in line:
                                        print(m)
                                    raise 
                                except Exception:
                                    print("what happened?")
                                    raise
                        else:
                            con.execute(insert)
            case _:
                pass



def read_rar_list(f):
    start =0
    for i,line in enumerate(f):
        if i==7:
            m = re.match(r"(-+\s+){4}",line)
            start = m.end()
        elif i<7:
            continue
        else:
            if line.startswith("-"):
                break
            else:
                if not line.startswith(r"    ..A.... "):
                    continue
                yield line[start:].strip()


def make_rar_sqlite():
    part_list = [(f"data/part{i:02d}.list.txt", 
                 f"字幕备份.part{i:02d}.rar") for i in range(1,11)]
    sqls = [
        "DROP TABLE IF EXISTS `subtitle_in_rar`; ",
"""CREATE TABLE `subtitle_in_rar` (
   file TEXT DEFAULT NULL,
   rar_file TEXT DEFAULT NULL
);""",
       
    ]
    sql_insert =  "INSERT INTO `subtitle_in_rar` VALUES (?,?);"
    with sqlite3.connect(SQLITE_FILE) as con:
        for sql in sqls:
            con.execute(sql)
        
        for file,no in part_list:
            with open(file,'r') as f:
                for fn in read_rar_list(f):
                    con.execute(sql_insert,(fn,no))


if __name__ == "__main__":
    # main()

    # recreate_sql("data/SUB.sql")
    # recreate_sqlite("create_sql1.sql")
    # make_rar_sqlite()

    pass