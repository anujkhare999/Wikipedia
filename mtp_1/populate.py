import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mtp_1.settings')
import django
django.setup()

from imageDuplicates.models import Question,Choice

file1=open('anuj.txt','r')
lines=file1.readlines()

file2=open('anuj2.txt','r')
lines2=file2.readlines()

def add_topic(line):
    data=line.split(',')
    t=Question.objects.get_or_create(question_text=data[0],link=data[1])[0]
    t.save()
    return t

def add_topic2(line):
    data=line.split(',')
    t=Question.objects.get_or_create(question_text=data[0])[0]
    t.save()
    return t

def populate(N):
    for line in lines:
        top = add_topic(line)

def populate2(N):
    for line in lines2:
        dat=line.split(',')
        top = add_topic2(dat[0])
        choice=Choice.objects.get_or_create(question=top,choice_text=dat[1],votes=0,types=dat[2])

if __name__=='__main__':
    populate(len(lines))
    populate2(len(lines2))        