import datetime
import csv

class Markdown:
    def __init__(self):
        self.f = open('text.txt','w')

    def output_doc(self,Doc):

        Doc.output_data()

class Doc:
    def __init__(self,attributes):
        self.attributes = attributes

    def output_data(self):
        for attribute in attributes:
            attribute.output_data()


class Table:
    def __init__(self,name):
        self.name = name
        self.f_in = open(self.name,'r')
        self.f_out = open('table_out.txt','w')

    def output_data(self):
        self.output_head()
        self.output_body()
        self.file_end()

    def data_read(self):
        reader = csv.reader(self.f_in)

        return reader

    def file_end(self):
        self.f_in.close()
        self.f_out.close()

    def output_head(self):
        reader = self.data_read()
        header = next(reader)
        l = []
        for head in header:
            l.append("|")
            l.append(head)

        #print(l)

        for i in l:
            print(i,end="")
        print("\n")

        print(l)

        s = ' '.join(l)
        #print(s)
        self.f_out.write(s)
        self.f_out.write('\n')




    def output_body(self):
        reader = self.data_read()
        l = [[]]
        for row in reader:
            tmp = []
            for r in row:
                tmp.append("|")
                tmp.append(r)
            l.append(tmp)

        del l[0]

        # for i in l:
        #     for j in i:
        #         print(j,end="")
        #     print("\n")

        for i in l:
            print(i)
            s = ' '.join(i)
            self.f_out.write(s)
            self.f_out.write('\n')





if __name__ == '__main__':

    doc = Markdown()

    name = "samle.csv"
    doc.output_doc(Table(name))
