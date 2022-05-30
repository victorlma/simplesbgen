#!/usr/bin/env python
import os
from datetime import datetime

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

class Msg:

    MsgBoxDiv = '<div class="msgbox pborder">\n<p><span class="hg emph"> '
    MsgBoxSays = ' says: </span>\n'
    MsgBoxP = '<p>\n'
    MsgBoxDate = '<p class="date">\n'
    MsgBoxPe = '</p>\n'
    MsgBoxDive = '</div>\n'

    def __init__(self, file):
        self.file_path = file
        self.sender = ""
        self.paragraphs = [""]
        self.true_date = ""
        self.date = "" 
        self._setup()

    def __repr__(self):
        return "<Msg:{}..., Sender:{}, Date:{}>".format(self.paragraphs[0][0:5], self.sender, self.date[0:3])
    def __str__(self):
        return "{}\n{}\n{}\n".format(self.date, self.sender, "\n".join(self.paragraphs))

    def _setup(self):
        with open(self.file_path, "r") as f:
            paragraph_num = 0
            for line in f:
                if line == "\n":
                    if self.true_date and self.sender:
                        paragraph_num += 1
                        self.paragraphs.append("")
                    continue
                elif line.split()[0] in DAYS and self.true_date == "":
                    self.true_date = line
                    self.date = self.true_date[0:11] + self.true_date[-5:]
                elif line[0:2] == "[[":
                    self.sender = line[2:-3]
                else:
                    self.paragraphs[paragraph_num] += line
                    

    def to_html(self):
        html = '{}{}{}{}'.format(Msg.MsgBoxDiv, self.sender,Msg.MsgBoxSays,self.paragraphs[0],Msg.MsgBoxPe)
        if len(self.paragraphs) > 1:
            for par in self.paragraphs[1:]:
                html += '{}{}{}'.format(Msg.MsgBoxP, par, Msg.MsgBoxPe)

        html += '{}{}{}{}'.format(Msg.MsgBoxDate,self.date, Msg.MsgBoxPe, Msg.MsgBoxDive)

        return html

    

if __name__ == "__main__":
    
    msgs = []
    
    for r, dir, files in os.walk("msgs"):
        for file in files:
            msgs.append(Msg(os.path.join(r,file)))

    print(msgs[0].date)
    msgs.sort(reverse=True ,key = lambda msgdate: datetime.strptime(msgdate.true_date,"%a %b %d %I:%M:%S %p %z %Y\n"))

    combined_html = ""

    for msg in msgs:
        combined_html += (msg.to_html() + "\n")

    with open("template.html", "r") as f1:
        with open("index.html", "w") as f2:
            for line in f1:
                if line.strip() == "{{ msgs }}":
                    f2.write(combined_html)
                else:
                    f2.write(line)

