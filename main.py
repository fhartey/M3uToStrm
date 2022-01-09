import os
from pathlib import Path
import requests



UserUrl = input("Enter your M3u Url: ")
UserDir = input("Enter your DIR: ")
import requests

r = requests.get(UserUrl)
content = r.content
content = r.content.decode("utf8")



# check for special charters in the name if there all change them to spaces
def EdgeCases(FileName):
    if FileName.find('/') != -1:
      FileName = [' ' if x=='/' 
                        else x for x in FileName]
      FileName = "".join(FileName)
    return FileName

def CreateStrmFiles(FileName, link):
    #Directory = "./Example/"
    FileName =   UserDir + EdgeCases(FileName) + ".strm"
    Path(FileName).touch()
    print(link, file=open(FileName, "a"))

def CreateStrmTvshowFiles():
    print("Hello")

# use this function to get the movie name and link after done formating the m3u
def ParseEquals(content, title):
    
    for counter, item in enumerate(content.split('movie-name=')):
        print(item.split('\n')[0])
        CreateStrmFiles(item.split('\n')[0], item.split('\n')[1])

def ParseEqualsTvShows(content, title):
    for counter, item in enumerate(content.split('movie-name=')):
        print(item.split('\n')[0].split('S'))


def ParseNames(content):

    for coutner, item in enumerate(content.split(",")):

        if item.find('#EXTM3U') == -1:
          print(coutner)
          print(item.split('\n')[0])
          print(item.split('\n')[1])
          print(item.split('\n')[0], file=open("output.txt", "a"))
          print(item.split('\n')[1], file=open("output.txt", "a"))

def FormatInput(content):
    newlist = ''
    for coutner, item in enumerate(content.split('\n')):
        if item.find('#EXTM3U') == -1 and item.find('https') == -1:

            index = item.find(',')
            item = item[:index] + 'movie-name=' + item[index + 1:]

        newlist +=  os.linesep + item
    return newlist



#Movies
newlist = FormatInput(content)
print(newlist)
ParseEquals(newlist, "movie-name=")


