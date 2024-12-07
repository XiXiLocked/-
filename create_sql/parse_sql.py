class parse_sql:
    """
    用来解析以 "INSERT INTO `subtitle` VALUES "开头的插入sql
    的values 部分，处理引号和转义。
    """
    def __init__(self, sql):
        self.sql = sql
        self.collection = None
        self.next = 0

    def parse(self):
        if self.collection is not None:
            return self.collection

        self.next = 0
        collection = []
        
        while self.next< len(self.sql):
            c = self.sql[self.next]
            if c.isspace() or c==",":
                self.next+=1
            elif c=="(":
                collection.append(self.parse_p())
            else:
                self.next+=1

        self.collection = collection
        return self.collection

    def parse_p(self):
        quotes ="\"\'"
        item = []
        self.next +=1
        c = self.sql[self.next]
        while c != ')':
            if c.isspace(): 
                self.next +=1
            elif c==",":
                self.next +=1
            else :
                if c.isnumeric():
                    item.append(self.parse_n())
                elif c in quotes:
                    item.append(self.parse_quote(c))
                elif c=="N":
                    item.append(self.parse_null())
                else:
                    self.next +=1
            c = self.sql[self.next]
        return item
    
    def parse_n(self):
        start = self.next
        c = self.sql[self.next]
        while c.isnumeric():
            self.next +=1
            c = self.sql[self.next]
        return self.sql[start:self.next]
    
    def parse_quote(self, quote):
        start = self.next
        self.next +=1
        while True:
            c = self.sql[self.next]
            if c=='\\':
                self.next +=2
            elif c != quote:
                self.next +=1
            else :
                self.next +=1
                return self.sql[start: self.next]
    def parse_null(self):
        if self.next+3< len(self.sql):
            self.next+=4
            return "NULL"
        else:
            raise ValueError(self.next)


