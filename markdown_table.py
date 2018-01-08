import datetime
import csv

class Doc:
    def output_doc(self,doctype):
        doctype.output_data()

class Markdown:
    def __init__(self,name):
        self.name = name

    def output_data(self):
        self.output_head()
        # self.output_body()
        # self.output_end()

    def data_read(self):
        dataname = self.name

        with open(dataname,'r') as f:
            reader = csv.reader(f)
            header = next(reader)

        return header

    def output_head(self):
        header = self.data_read()
        s_h = " | "
        l = []
        for head in header:
            l.append("|")
            l.append(head)
        # l.append("|")

        for i in l:
            print(i,end="")


if __name__ == '__main__':

    doc = Doc()

    name = "samle.csv"
    doc.output_doc(Markdown(name))
