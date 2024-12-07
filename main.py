import sys
from create_sql.query import subtitle_find


if __name__ =="__main__":
    query = sys.argv[1]

    for sub in subtitle_find(query):
        if sub.subtitle is not None:
            print(sub.subtitle.cnname,sub.subtitle.enname,sub.subtitle.filename)
            print("\t",sub.volume, sub.file_path)
        else:
            *_,filename = sub.file_path.split("/")
            print(filename)
            print("\t", sub.volume, sub.file_path)