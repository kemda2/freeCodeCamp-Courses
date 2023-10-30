# # String değerleri int'e çevirirken rakam olursa çevrilemeyeceği için dönüşürse dönüştür dönüşmezse -1 olarak çıkar diyoruz.

# astr = "Hello Bob" 
# try:
#     istr = int(astr) 
# except: 
#     istr = -1

# print("First", istr)

# astr = "123" 
# try:
#     istr = int(astr) 
# except: 
#     istr = -1

# print("Second", istr)

####################################################################################################

# astr = 'Bob'
# try:
#     print('Hello') 
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1
# print('Done', istr)

####################################################################################################

# rawstr = input("Enter a number: ") 
# try:
#     ival = int(rawstr) 
# except:
#     ival = -1

# if ival > 0 :
#     print('Nice work') 
# else:
#     print('Not a number')
    
####################################################################################################

# big = max('Hello world') 
# print(big)
# tiny = min('Hello World') 
# print(tiny)

####################################################################################################

# print(0 == 0.0)
# print(0 is 0.0) # Is hem değer hem de türün aynı olmasını bekler.
# print(0 is 0)

####################################################################################################

# text = open("text.txt")
# print(text)

####################################################################################################

# text = open('text.txt') 
# count = 0 
# for line in text: 
#     count += 1
# print('Line Count:', count)

####################################################################################################

# text = open('text.txt') 
# inp = text.read() 

# print(len(inp))
# print(inp[:21])

####################################################################################################

# text = open('text.txt')  
# for line in text:
#     line = line.rstrip()
#     if line.startswith('K'): 
#         print(line)

####################################################################################################

# text = open('text.txt')  
# for line in text:
#     line = line.rstrip()
#     if not "oglu" in line: 
#         continue
#     print(line)

####################################################################################################

# fname = input("Enter the file") 
# try:
#     text = open(fname) 
# except:
#     quit()

# count = 0

# for line in text:
#     if line.startswith('K'):
#         count += 1
# print('There were', count, 'subject lines in', fname)

####################################################################################################

# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c) 

####################################################################################################

# print(help([]))

####################################################################################################

# stuff = list()
# stuff.append('book') 
# stuff.append(99) 
# print(stuff)

# stuff.append('cookie') 
# print(stuff)

####################################################################################################

# total = 0
# count = 0
# while True:
#     inp = input('Entar a nunber: ') 
#     if inp == 'done' : break 
#     value = float(inp) 
    
#     total += value 
#     count += 1

# average = total / count 
# print('Average:', average)



# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float (inp)
#     numlist.append(value)
    
# average = sum(numlist) / len (numlist)
# print ("Average: ", average)

####################################################################################################

# line = 'A lot                                            of spaces'
# etc = line.split() 
# print(etc)

# line = 'first;second;third' 
# thing = line.split() 
# print(thing)
# print(len(thing))

# thing = line.split(';') 
# print(thing)
# print(len(thing))

####################################################################################################

# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# print(purse['candy'])
# purse['candy'] = purse['candy'] + 2 
# print(purse)

####################################################################################################

# lst = list() 
# lst.append(21) 
# lst.append(183) 
# print(lst)
# lst[0] = 23 
# print(lst)

# ddd = dict() 
# ddd['age'] = 21 
# ddd['course'] = 182 
# print(ddd)
# ddd['age'] = 23
# print(ddd)

####################################################################################################

# ccc = dict() 
# ccc['csev'] = 1 
# ccc['cwen'] = 1 
# print(ccc)
# ccc['cwen'] += 1
# print(ccc)

####################################################################################################

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] 
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else :
#         counts[name] += 1

# print(counts)


# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen'] 

# for name in names:
#     counts[name] = counts.get(name,0) + 1
# print(counts)

####################################################################################################

# counts = {'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))

####################################################################################################

# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

# counts = dict()
# print('Enter a line of text:') 
# line = input('')

# words = line.split()

# print('Words: ', words)
# print('Counting...') 
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Counts', counts)

####################################################################################################

# counts = {'chuck' : 1 , 'fred' : 42, 'jan': 100} 
# for key in counts:
#     print(key, counts[key])

####################################################################################################

# jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}  

# print(list(jjj))
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())




# jjj = {'chuck' : 1, 'fred' : 42, 'jan': 100}  

# for a,b in jjj.items():
#     print(a,b)

####################################################################################################

# name = input('Enter file:')
# handle = open(name)
# counts = dict()
# for line in handle:
#     words = line.split() 
#     for word in words: 
#         counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None 

# for word,count in counts.items():
#     if bigcount is None or count > bigcount: 
#         bigword = word 
#         bigcount = count

# print(bigword, bigcount)

####################################################################################################

# x = ('Glann', 'Sally', 'Joseph') 
# print(x[2])

# y = ( 1, 9, 2 ) 
# print(y)

# print(max(y))

# for i in y:
#     print(i)



# x = [9, 8, 7] 
# x[2] = 6 
# print(x)



# (x, y) = (4, 'fred') 
# print(y) 
# (a, b) = (99, 98) 
# print(a)

####################################################################################################

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k,v) in d.items(): 
#     print(k, v)

# tups = d.items() 
# print(tups)

####################################################################################################

# print((0, 1, 2) < (5, 1, 2))
# print((0, 1, 3) < (0, 1, 2))
# print((0, 1, 2000000) < (0, 3, 4))
# print(('Jones', 'Sally') < ('Jones', 'Sam'))
# print(('Jones', 'Sally') > ('Adams', 'Sam'))

####################################################################################################

# d = {"a" : 10, "b" : 1, "c" : 22} 

# print(d.items())

# print(sorted(d.items()))



# d = {'b':1, 'a':10, 'c':22} 

# for k, v in d.items():
#     print(k, v)

# t = sorted(d.items()) 
# print(t)

# for k, v in sorted(d.items()):
#     print(k, v)


# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
# for k, v in c.items(): 
#     tmp.append((v,k))

# print(tmp)

# tmp = sorted(tmp, reverse=True) 
# print(tmp)

####################################################################################################

# fhand = open('Guide.txt') 
# counts = dict() 
# for line in fhand:
#     words = line.split() 
#     for word in words:
#         counts[word] = counts.get(word, 0) +1
# lst = list()
# for key, val in counts.items(): 
#     newtup = (val, key) 
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# for val, key in lst[:10] : 
#     print(key, val)

####################################################################################################

# c = {'a':10, 'b':1, 'c':22}
# print(sorted([(v,k) for k,v in c.items()]))

####################################################################################################

# ^ bir satırın başını inceler 
# $ satırın sonunu inceler  
# . herhangi bir karakteri inceler 
# \s boşlukları inceler 
# \S boşluk olmayan karakterleri inceler 
# * bir karakteri 0 veya daha fazla kez tekrarlar 
# *? mümkün olduğunca eşleşen karakteri 0 veya daha fazla kez tekrarlar 
# + karakteri 1 veya daha fazla kez tekrarlar 
# +? mümkün olduğunca eşleşen karakteri 1 veya daha fazla kez tekrarlar 

# import re olmadan kullanılamaz

####################################################################################################

# hand = open('Guide.txt') 
# for line in hand:
#     line = line.rstrip()
#     if line.find('import') >= 0: 
#         print(line)

# import re
# hand = open('Guide.txt') 
# for line in hand:
#     line = line.rstrip()
#     if re.search('^import', line): # ^ yüzünden ile başlayanları arıyor.
#         print(line)

####################################################################################################

# import re
# x = "My 2 favorite numbers are 19 and 42"
# y = re.findall ('[0-9]+' ,x) 
# print(y)



# import re
# x = "My 2 favorite numbers are 19 and 42"
# y = re.findall('[AEIOU]+',x) 
# print(y)



# import re
# x = 'From: Using the : character'
# y = re.findall('^F.+:', x)
# print (y)


# import re
# x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('\S+@\S+', x)
# print (y)

# y = re.findall('From (\S+@\S+)',x) 
# print(y)



# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)



# import re
# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos = data.find('@')
# print (atpos)
# sppos = data.find(' ', atpos)
# print(sppos)
# host = data [atpos+1 : sppos]
# print(host)

# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words = data.split()
# email = words[1]
# pieces = email.split('@') 
# print(pieces[1])



# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008' 
# y = re.findall('@([^ ]*)',lin) 

# print(y)

# import re
# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008' 
# y = re.findall('^From .*@([^ ]*)',lin) 
# print(y)

####################################################################################################

# import re	
# hand = open('mbox-short.txt') 

# numlist = list() 

# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) 
#     if len(stuff) != 1 : continue 
#     num = float(stuff[0]) 
#     numlist.append(num) 
#     print ('Maximum: ', max (numlist))

####################################################################################################

# import re
# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+',x)
# print(y)

####################################################################################################

# import Socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# mysock.connect( ('data.pr4e.org', 80) )

####################################################################################################

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() 
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# mysock.close()

####################################################################################################

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
# for line in fhand:
#     print(line.decode().strip())

####################################################################################################

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm') 
# for line in fhand:
#     print(line.decode().strip())

####################################################################################################

# import urllib.request, urllib.parse, urllib.error 
# from bs4 import BeautifulSoup
# url = input('Enter - ') 
# html = urllib.request.urlopen(url).read() 
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the another tags 
# # enter http://www.dr-chuck.com/page1.htm
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

####################################################################################################

# import xml.etree.ElementTree as ET
# data = '''<person>
#     <name>Chuck</name>
#     <phone type="intl"> 
#         +1 734 303 4456
#     </phone>
#     <email hide="yes"/>
# </person>'''
# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attr:',tree.find('email').get('hide'))

####################################################################################################

# import xml.etree.ElementTree as ET
# input = '''<stuff> 
#     <users>
#         <user x="2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x="7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst)) 
# for item in lst:
#     print('Name', item.find('name').text) 
#     print('Id', item.find('id').text) 
#     print('Attribute', item.get("x"))

####################################################################################################

# import json 
# data = '''{
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#     }, 
#     "email" : { 
#     "hide" : "yes"
#     }
# }'''
# info = json.loads(data)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])

####################################################################################################

# import json
# data = '''
#   [
#     { "id" : "001",
#       "x" : "2",
#      "name" : "Quincy"
#     } ,
#     { "id" : "009",
#       "x" : "7",
#       "name" : "Mrugesh"
#     }
#   ]
# '''
# info = json.loads(data)
# print(info[1]['name'])

####################################################################################################

# {"status": "OK", 
#  "results": [ 
#      { "geometry": { 
#          "location_type": "APPROXIMATE", 
#          "location": { 
#              "lat": 42.2808256,
#                 "Ing": -83.7430378
#          }
#      }, 
#       "address_components": [ 
#         { "long_name": "Ann Arbor", 
#          "types": [ "locality", 
#                    "political" 
#                    ], 
#          "short_name": "Ann Arbor" 
#         } 
#         ] ,
#       "formatted_address": "Ann Arbor, MI, USA", 
#       "types": [ "locality", "political" ] 
#       } 
#   ] 
#  }
                                                                                                                                                        
####################################################################################################

# import urllib.request, urllib.parse, urllib.error 
# import json
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# while True:
#     address = input('Enter location: ') 
#     if len(address) < 1: break
#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url) 
#     uh = urllib.request.urlopen(url) 
#     data = uh.read().decode() 
#     print('Retrieved', len(data), 'characters')
    
#     try:
#         js = json.loads(data) 
#     except:
#         js = None
        
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data) 
#         continue
#     lat = js["results"][0]["geometry"]["location"]["lat"] 
#     lng = js["results"][0]["geometry"]["location"]["lng"] 
#     print('lat', lat, 'Ing', lng) 
    
#     location = js['results'][0]['formatted_address'] 
#     print(location)

####################################################################################################

# import urllib.request, urllib.parse, urllib.error
# import twurl
# import json

# TWITTER_URL = 'https://api.twiteer.com/1.1/friends/list.json'
# while True:
#     print(' ')

#     acct = input('Enter Twitter Account: ')
#     if (len(acct)<1): break
#     url = twurl.augment(TWITTER_URL, {'screen name':acct, count:5})
#     print('Retrieving', url)
#     connection = urllib.request.urlopen(url)
#     data = connection.read().decode()
#     headers = dict(connection.getheaders())
#     print('Remaining', headers['x-rate-limit-remaining'])
#     js = json.loads(data)
#     print(json.dumps(js, indent=4))
#     for i in js['users']:
#         print(u['screen_name'])
#         s = u['status']['text']
#         print('    ',s[:50])

####################################################################################################

# class PartyAnimal:
#     x = 0
#     def __init__(self):
#         print('I am constructed')
#     def party(self) : 
#         self.x = self.x + 1 
#         print('So far',self.x)
#     def __del__(self):
#         print('I am destructed', self.x)
# an = PartyAnimal() 
# an.party() 
# an.party() 
# an = 42 
# print('an contains', an)

####################################################################################################

# class PartyAnimal: 
#     x = 0 
#     name = "" 
#     def __init__ (self, z) :
#         self.name = z 
#         print(self.name,"constructed")
#     def party(self) : 
#         self.x = self.x + 1 
#         print(self.name,"party count",self.x)

# s = PartyAnimal("Sally")
# s.party()
# j = PartyAnimal("Jim") 
# j.party() 
# s.party ()

####################################################################################################

# class PartyAnimal: 
#     x = 0 
#     name = "" 
#     def __init__(self, nam) :
#         self.name = nam 
#         print(self.name,"constructed")
    
#     def party(self): 
#         self.x = self.x + 1 
#         print(self.name,"party count",self.x)

# class FootballFan(PartyAnimal):
#     points = 0
#     def touchdown(self):
#         self.points = self.points + 7
#         self.party()
#         print(self.name,"points",self.points)

# s = PartyAnimal("Sally") 
# s.party()
# j = FootballFan("Jim")
# j.party()
# j.touchdown()

####################################################################################################

# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
# DELETE FROM Users WHERE email='ted@umich.edu’
# UPDATE Users SET name='Charles' WHERE email-csev@umich.edu'
# SELECT * FROM Users
# SELECT * FROM Users WHERE email='csev@umich.edu'
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name DESC

####################################################################################################

# import sqlite3

# conn = sqlite3.connect('music.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Tracks')
# cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# conn.close()



# import sqlite3

# conn = sqlite3.connect('music.sqlite')
# cur = conn.cursor()

# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
#     ('Thunderstruck', 20))
# cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
#     ('My Way', 15))
# conn.commit()

# print('Tracks:')
# cur.execute('SELECT title, plays FROM Tracks')
# for row in cur:
#      print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

# cur.close()



# import sqlite3

# conn = sqlite3.connect('friends.sqlite')
# cur = conn.cursor()

# cur.execute('SELECT * FROM People')
# count = 0
# print('People:')
# for row in cur:
#     if count < 5: print(row)
#     count = count + 1
# print(count, 'rows.')

# cur.execute('SELECT * FROM Follows')
# count = 0
# print('Follows:')
# for row in cur:
#     if count < 5: print(row)
#     count = count + 1
# print(count, 'rows.')

# cur.execute('''SELECT * FROM Follows JOIN People
#             ON Follows.to_id = People.id
#             WHERE Follows.from_id = 2''')
# count = 0
# print('Connections for id=2:')
# for row in cur:
#     if count < 5: print(row)
#     count = count + 1
# print(count, 'rows.')

# cur.close()

####################################################################################################

# Chapter 15

# CREATE TABLE Album ( 
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
#                     artist_id INTEGER, 
#                     title TEXT
# )
# CREATE TABLE Track ( 
#                     id INTEGER NOT NULL PRIMARY KEY
#                     AUTOINCREMENT UNIQUE, 
#                     title TEXT, 
#                     album_id INTEGER, 
#                     genre_id INTEGER, 
#                     Ion INTEGER, rating INTEGER, count INTEGER )

# select Album.title, Artist.name from Album join Artist on Album.artistjd = Artist id

# select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id

# SELECT Track.title, Track.genre_id, Genre.id, Genre.name FROM Track JOIN Genre

# select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id

# select Track.title, Artist.name, Album.title, Genre.name from Track join Genre join Album join Artist on Track.genre_id = Genre.id and Track.album_id = Album.id and Album.artist_id = Artist.id

####################################################################################################

# CREATE TABLE User ( 
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
#                     name TEXT UNIQUE, 
#                     email TEXT);

# CREATE TABLE Course ( 
#                      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
#                      title TEXT UNIQUE );

# CREATE TABLE Member (	
#                     user_id     integer,	
#                     course_id   INTEGER, 
#                     role	    INTEGER,
#                     PRIMARY KEY (user_id, course_id) );

# INSERT INTO User (name, email) VALUES	(’Jane’, ’jane@tsugi.org’);
# INSERT INTO User (name, email) VALUES	('Ed’, 'ed@tsugi.org');
# INSERT INTO User (name, email) VALUES	('Sue', 'sue@tsugi.org');
# INSERT INTO Course (title) VALUES ('Python');
# INSERT INTO Course (title) VALUES ('SQL');
# INSERT INTO Course (title) VALUES ('PHP');

# INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1) ;
# INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0) ;
# INSERT INTO Member (user id, course id, role) VALUES (3, 1, 0) ;

# INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0) ;
# INSERT INTO Member (user id, course id, role) VALUES (2, 2, 1) ;
# INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
# INSERT INTO Member (user id, course id, role) VALUES (3, 3, 0);



####################################################################################################

# def arithmetic_arranger(problems, bools=False):
#     # Check the number of problems
#     if len(problems) > 5:
#         return "Error: Too many problems."
    
#     first = []
#     second = []
#     operator = []

#     for x in problems:
#         pieces = x.split()
#         first.append(pieces[0])
#         operator.append(pieces[1])
#         second.append(pieces[2])

#     # Check for * or /
#     if "*" in operator or "/" in operator:
#         return "Error: Operator must be '+' or '-'."

#     # Check the digits
#     for i in range(len(first)):
#         if not (first[i].isdigit() and second[i].isdigit()):
#             return "Error: Numbers must only contain digits."

#     # Check the length
#     for i in range(len(first)):
#         if len(first[i]) > 4 or len(second[i]) > 4:
#             return "Error: Numbers cannot be more than four digits."

#     first_line = []
#     second_line = []
#     third_line = []
#     fourth_line = []

#     for i in range(len(first)):
#         if len(first[i]) > len(second[i]):
#             first_line.append(" "*2 + first[i])
#         else:
#             first_line.append(" "*(len(second[i]) - len(first[i]) + 2) + first[i])

#     for i in range(len(second)):
#         if len(second[i]) > len(first[i]):
#             second_line.append(operator[i] + " " + second[i])
#         else:
#             second_line.append(operator[i] + " "*(len(first[i]) - len(second[i]) + 1) + second[i])

#     for i in range(len(first)):
#         third_line.append("-"*(max(len(first[i]), len(second[i])) + 2))

#     if bools:
#         for i in range(len(first)):
#             if operator[i] == "+":
#                 ans = str(int(first[i]) + int(second[i]))
#             else:
#                 ans = str(int(first[i]) - int(second[i]))

#             if len(ans) > max(len(first[i]), len(second[i])):
#                 fourth_line.append(" " + ans)
#             else:
#                 fourth_line.append(" "*(max(len(first[i]), len(second[i])) - len(ans) + 2) + ans)
#         arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
#     else:
#         arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
#     return arranged_problems
        
        
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

####################################################################################################

# class Category:

#   def __init__(self, category):
#     self.category = category
#     self.ledger = []


#   def __str__(self):
#     s = self.category.center(30, "*") + "\n"

#     for item in self.ledger:
#       temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
#       s += temp + "\n"

#     s += "Total: " + str(self.get_balance())
#     return s

#   def deposit(self, amount, description=""):
#     temp = {}
#     temp['amount'] = amount
#     temp['description'] = description
#     self.ledger.append(temp)


#   def withdraw(self, amount, description=""):
#     if self.check_funds(amount):
#       temp = {}
#       temp['amount'] = 0 - amount
#       temp['description'] = description
#       self.ledger.append(temp)
#       return True
#     return False


#   def get_balance(self):
#     balance = 0
#     for item in self.ledger:
#       balance += item['amount']
#     return balance


#   def transfer(self, amount, budget_cat):
#     if self.check_funds(amount):
#       self.withdraw(amount, "Transfer to " + budget_cat.category)
#       budget_cat.deposit(amount, "Transfer from " + self.category)
#       return True
#     return False


#   def check_funds(self, amount):
#     if amount > self.get_balance():
#       return False
#     return True


# def create_spend_chart(categories):
#   spend = []
#   for category in categories:
#     temp = 0
#     for item in category.ledger:
#       if item['amount'] < 0:
#         temp += abs(item['amount'])
#     spend.append(temp)
  
#   total = sum(spend)
#   percentage = [i/total * 100 for i in spend]

#   s = "Percentage spent by category"
#   for i in range(100, -1, -10):
#     s += "\n" + str(i).rjust(3) + "|"
#     for j in percentage:
#       if j > i:
#         s += " o "
#       else:
#         s += "   "
#     # Spaces
#     s += " "
#   s += "\n    ----------"

#   cat_length = []
#   for category in categories:
#     cat_length.append(len(category.category))
#   max_length = max(cat_length)

#   for i in range(max_length):
#     s += "\n    "
#     for j in range(len(categories)):
#       if i < cat_length[j]:
#         s += " " + categories[j].category[i] + " "
#       else:
#         s += "   "
#     # Spaces
#     s += " "

#   return s

####################################################################################################

# class Rectangle:

#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   def __str__(self):
#     return "Rectangle(width=" + str(self.width) + \
#            ", height=" + str(self.height) + ")"

#   def set_width(self, width):
#     self.width = width

#   def set_height(self, height):
#     self.height = height

#   def get_area(self):
#     return self.width * self.height

#   def get_perimeter(self):
#     return 2 * (self.width + self.height)

#   def get_diagonal(self):
#     return (self.width ** 2 + self.height ** 2) ** .5

#   def get_picture(self):
#     if self.width > 50 or self.height > 50:
#       return "Too big for picture."
#     rectangle = ("*" * self.width + "\n") * self.height
#     return rectangle

#   def get_amount_inside(self, shape):
#     max_width = self.width // shape.width
#     max_height = self.height // shape.height
#     return max_width * max_height


# class Square(Rectangle):

#   def __init__(self, length):
#     super().__init__(length, length)

#   def __str__(self):
#     return "Square(side=" + str(self.width) + ")"

#   def set_side(self, side):
#     self.width = side
#     self.height = side

#   def set_width(self, side):
#     self.width = side
#     self.height = side

#   def set_height(self, side):
#     self.width = side
#     self.height = side

####################################################################################################

# import copy
# import random
# # Consider using the modules imported above.

# class Hat:

#   def __init__(self, **kwargs):
#     self.contents = []
#     for key, value in kwargs.items():
#       for _ in range(value):
#         self.contents.append(key)

#   def draw(self, number):
#     if number > len(self.contents):
#       return self.contents
#     balls = []
#     for _ in range(number):
#       choice = random.randrange(len(self.contents))
#       balls.append(self.contents.pop(choice))
#     return balls

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

#   expected_no_of_balls = []
#   for key in expected_balls:
#       expected_no_of_balls.append(expected_balls[key])
#   successes = 0

#   for _ in range(num_experiments):
#     new_hat = copy.deepcopy(hat)
#     balls = new_hat.draw(num_balls_drawn)

#     no_of_balls = []
#     for key in expected_balls:
#       no_of_balls.append(balls.count(key))

#     if no_of_balls >= expected_no_of_balls:
#       successes += 1

#   return successes/num_experiments

####################################################################################################

# def arithmetic_arranger(islemler, secim=False):
  
#   birinci = list()
#   isaret = list()
#   ikinci = list()
    
#   # islemler 5'ten fazlaysa hata ver 
#   if len(islemler) > 5:
#     return "Error: Too many problems."
  
#   # islemleri ayır
#   for islem in islemler:
#     # islemi bol
#     ayrilmis_islem = islem.split()
    
#     # listeleri hazırla
#     birinci.append(ayrilmis_islem[0])
#     isaret.append(ayrilmis_islem[1])
#     ikinci.append(ayrilmis_islem[2])

  
      
#   # Kontrollere başla
#   for i in range(len(birinci)):
    
#     # Yalnızca sayı içeriyor mu diye kontrol et
#     if not (birinci[i].isdigit() and ikinci[i].isdigit()):
#       return "Error: Numbers must only contain digits."

#     # islemler'deki sayılar 4'ten büyükse hata ver
#     if len(birinci[i]) > 4 or len(ikinci[i]) > 4:
#       return "Error: Numbers cannot be more than four digits."
    
#     # islemler çarpma veya bölmeyse hata ver
#     if isaret[i] == "*" or isaret[i] == "/":
#       return "Error: Operator must be '+' or '-'."
        
#   s1 = list()
#   s2 = list()
#   s3 = list()
#   s4 = list()
        
#   for i in range(len(birinci)):
#     if len(birinci[i]) > len(ikinci[i]):
#       s1.append(" "*2 + birinci[i])
#     else:
#       s1.append(" " * (len(ikinci[i]) - len(birinci[i]) + 2) + birinci[i])

#   for i in range(len(ikinci)):
#     if len(ikinci[i]) > len(birinci[i]):
#       s2.append(isaret[i] + " " +ikinci[i])
#     else:
#       s2.append(isaret[i] + " " * (len(birinci[i])-len(ikinci[i])+1) + ikinci[i])
  
#   for i in range(len(birinci)):
#     s3.append("-" * (max(len(birinci[i]),len(ikinci[i])) + 2))        

#   if secim == True:
#     for i in range(len(birinci)):
#       if isaret[i] == "+":
#         sonuc = str(int(birinci[i]) + int(ikinci[i]))
#       elif isaret[i] == "-":
#         sonuc = str(int(birinci[i]) - int(ikinci[i]))  

#       mak = max(len(birinci[i]), len(ikinci[i]))
  
      
      
#       if len(sonuc) > mak:
#         s4.append(" " * (len(sonuc)-mak) + sonuc)
#       else:
#         s4.append(" " * (mak + 2 - len(sonuc)) + sonuc)
      
#     arranged_problems = "    ".join(s1) + "\n" + "    ".join(s2) + "\n" + "    ".join(s3) + "\n" + "    ".join(s4)
#   else:
#     arranged_problems = "    ".join(s1) + "\n" + "    ".join(s2) + "\n" + "    ".join(s3) 
    
#   return arranged_problems

# print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True))

####################################################################################################

# def add_time(start, duration, weekday = ""):

# # haftanın başlangıç günü verileni küçük harfe çevirerek çalışacak.
# # eğer diğer güne geçerse kaç gün geçtiğine göre bildirimde bulunacak
  
#   cur_h_m, cur_h_type = start.split()
#   cur_h, cur_m = cur_h_m.split(":")
  
#   dur_h, dur_m = duration.split(":")
  
#   #cur_h_type
#   #cur_h
#   #cur_m
#   #dur_h
#   #dur_m
  
#   cur_h_i = int(cur_h) 
#   cur_m_i = int(cur_m)
#   dur_h_i = int(dur_h)
#   dur_m_i = int(dur_m)
  
#   day_count = 0
      
#   for i in range(dur_m_i):
#     cur_m_i += 1
#     dur_m_i -= 1
#     if cur_m_i == 60:
#       cur_m_i = 0
#       cur_h_i += 1
#       if cur_h_i == 13:
#         cur_h_i = 1
#       if cur_h_i == 12:
#         if cur_h_type == "AM":
#           cur_h_type = "PM"
#         else:
#           cur_h_type = "AM"
#           day_count += 1
        
  
#   for i in range(dur_h_i):
#     cur_h_i += 1
#     dur_h_i -= 1
#     if cur_h_i == 13:
#         cur_h_i = 1
#     if cur_h_i == 12:
#       if cur_h_type == "AM":
#         cur_h_type = "PM"
#       else:
#         cur_h_type = "AM"
#         day_count += 1
        
#   new_day_name = ""
#   days_dict = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
#   if weekday != "": 
#     day_num = days_dict[weekday.lower()]
#     new_day_num = day_num + day_count
#     new_day_num = new_day_num % 7
#     if new_day_num == 0:
#         new_day_num = 7
#     for k,v in days_dict.items():
#       if v == new_day_num:
#         new_day_name = k 
#     if day_count == 0:
#       new_time = "{}:{} {}, {}".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title())
#     elif day_count == 1:
#       new_time = "{}:{} {}, {} (next day)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title())
#     else:
#       new_time = "{}:{} {}, {} ({} days later)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title(),day_count)
#   else:
#     if day_count == 0:
#       new_time = "{}:{} {}".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type)
#     elif day_count == 1:
#       new_time = "{}:{} {} (next day)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,)
#     else:
#       new_time = "{}:{} {} ({} days later)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type, day_count)
  
#   return new_time

  
  
  
#   a = "{}:{:02d} {} ({} days later)".format(new_hour,new_minute,new_hour_type,new_day)
    
#   print(a)
#   print(new_hour, new_minute, new_day, sep=" ; ")
 
  
  
#   return new_time
  
# print(add_time("3:00 PM", "3:10"))
# # Returns: 6:10 PM

# print(add_time("11:30 AM", "2:32", "Monday"))
# # Returns: 2:02 PM, Monday

# print(add_time("11:43 AM", "00:20"))
# # Returns: 12:03 PM

# print(add_time("10:10 PM", "3:30"))
# # Returns: 1:40 AM (next day)

# print(add_time("11:43 PM", "24:20", "tueSday"))
# # Returns: 12:03 AM, Thursday (2 days later)

# print(add_time("6:30 PM", "205:12"))
# # Returns: 7:42 AM (9 days later)

# print(add_time("3:30 PM", "2:12"))
# # "5:42 PM"
# print(add_time("11:55 AM", "3:12"))
# # "3:07 PM"
# print(add_time("9:15 PM", "5:30"))
# # "2:45 AM (next day)"
# print(add_time("11:40 AM", "0:25"))
# # "12:05 PM"
# print(add_time("2:59 AM", "24:00"))
# # "2:59 AM (next day)"
# print(add_time("11:59 PM", "24:05"))
# # "12:04 AM (2 days later)"
# print(add_time("8:16 PM", "466:02"))
# # "6:18 AM (20 days later)"
# print(add_time("5:01 AM", "0:00"))
# # "5:01 AM"
# print(add_time("3:30 PM", "2:12", "Monday"))
# # "5:42 PM, Monday"
# print(add_time("2:59 AM", "24:00", "saturDay"))
# # "2:59 AM, Sunday (next day)"
# print(add_time("11:59 PM", "24:05", "Wednesday"))
# # "12:04 AM, Friday (2 days later)"
# print(add_time("8:16 PM", "466:02", "tuesday"))
# # "6:18 AM, Monday (20 days later)"

####################################################################################################

# class Category:
#     def __init__(self,isim):
#         self.isim = isim
#         self.ledger = []
          
    
#     def deposit(self,amount,description=""):
#         arttirma_dict = {"amount": amount,"description": description}
#         self.ledger.append(arttirma_dict)
    
#     def withdraw(self,amount,description=''):
#         if self.check_funds(amount):
#             amount *= -1
#             eksiltme_dict = {"amount": amount, "description": description}
#             self.ledger.append(eksiltme_dict)
#             return True
#         else:
#             return False
          
#     def get_balance(self):
#         bakiye = 0
#         for x in self.ledger:
#             bakiye += x["amount"]
#         return bakiye
    
#     def transfer(self, amount, hedef):
#         if self.withdraw(amount,"Transfer to {}".format(hedef.isim)):
#             hedef.deposit(amount, "Transfer from {}".format(self.isim))
#             return True
#         else:
#             return False
     
#     def check_funds(self,amount):
#         if self.get_balance() >= amount:
#             return True
#         return False
    
#     def __str__(self):
#         a = int((30 - len(self.isim))/2)
#         text = "*" * a + self.isim + "*" * (30 - a - len(self.isim)) + "\n"
        
#         for x in self.ledger:
#             text += "{:<23}{:7.2f}".format(x["description"][:23], x["amount"]) + "\n"
#         text += "Total: " + str(self.get_balance())
#         return text

# def create_spend_chart(kategoriler):

#     toplam_harcama = []
#     isim_max = 0
#     for kategori in kategoriler:
#         ara_toplam = 0
#         for x in kategori.ledger:
#             if x["amount"] < 0:
#                 ara_toplam += abs(x["amount"])
        
#         if isim_max < len(kategori.isim):
#             isim_max = len(kategori.isim)
        
#         toplam_harcama.append(ara_toplam) 

#     toplam = sum(toplam_harcama)    
#     oranlar = [(x*100)/toplam for x in toplam_harcama]

#     oranlar = [round(x,2) for x in oranlar]
    
#     chart = "Percentage spent by category"
#     for satir in range(100, -1, -10):
#         chart += "\n" + str(satir).rjust(3) + "|"
#         for kategori_oran in oranlar:
#             if satir <= kategori_oran:
#                 chart += " o "
#             else:
#                 chart += "   "
#         chart += " "

#     chart += "\n    ----------"
    
#     for i in range(isim_max):
#         chart += "\n    "
#         for j in range(len(kategoriler)):
#             if i < len(kategoriler[j].isim):
#                 chart += " " + kategoriler[j].isim[i] + " "
#             else:
#                 chart += "   "
#         chart += " "

#     return chart
    
# Food = Category("Food")
# Clothing = Category("Clothing")
# Auto = Category("Auto")

# Food.deposit(1000,"initial deposit")
# Food.withdraw(10.15,"groceries")
# Food.withdraw(15.89,"restaurant and more food")
# Food.transfer(50,Clothing)
# Clothing.withdraw(25.55)

# print(Food)
# print(Clothing)
# print(Auto)

# create_spend_chart([Food,Clothing,Auto]) 
    
            
####################################################################################################

# class Rectangle:
#   def __init__(self,width,height):
#     self.width = width
#     self.height = height
#     self.name = "Rectangle"
  
#   def set_width(self,new_width):
#       self.width = new_width
  
#   def set_height(self,new_height):
#       self.height = new_height
      
#   def get_area(self):
#     return self.width * self.height
    
#   def get_perimeter(self):
#     return 2 * (self.width + self.height)
    
#   def get_diagonal(self):
#     return (self.width ** 2 + self.width ** 2) ** .5
    
#   def get_picture(self):
#     if self.width > 50 or self.height > 50:
#         return "Too big for picture."
#     else:
#         metin = ""
        
#         for i in range(self.height):
#             metin += "*" * self.width + "\n"
#         return metin

#   def __str__(self):
#     return "Rectangle(width={}, height={})".format(self.width,self.height)
  
#   def get_amount_inside(self,obj):
#     a = self.width // obj.width
#     b = self.height // obj.height
#     return a * b

# class Square(Rectangle):
#   def __init__(self,side):
#     self.width = side
#     self.height = side
#     self.name = "Square"
  
#   def set_side(self,side):
#     self.width = side
#     self.height = side
  
#   def __str__(self):
#     return "Square(side={})".format(self.width)

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))

####################################################################################################

# import copy
# import random
# # Consider using the modules imported above.

# class Hat:
  
#   def __init__(self,**kwargs):
#     self.contents = []
        
#     for k,v in kwargs.items():
#       for i in range(v):
#         self.contents.append(k) 
  
#   def draw(self, rep):
    
#     if rep > len(self.contents):
#       return self.contents
    
#     those_balls = []
#     for i in range(rep):
#       eleman = random.randrange(len(self.contents))
#       those_balls.append(self.contents.pop(eleman))
    
#     return those_balls


# def experiment(hat,expected_balls,num_balls_drawn,num_experiments):

#   olasilik = 0
#   beklenen = []
  

#   for i in range(num_experiments):
#     yedek = copy.deepcopy(hat)
#     cekilen = yedek.draw(num_balls_drawn)
    
#     for k in expected_balls:
#       beklenen.append(k)
    
#     cek_dict = {}
#     for j in cekilen:
#       cek_dict[j] = cek_dict.get(j,0) + 1  
    
#     sayim = 0
    
#     for k in beklenen:
#       if k in cek_dict and expected_balls[k] <= cek_dict[k]:
#           sayim += 1 
    
#     if sayim == len(beklenen):
#       olasilik += 1
  
#   olasilik /= num_experiments   
#   return olasilik
      



# hat = Hat(black=6, red=4, green=3)

# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=5,
#                   num_experiments=2000)

# print(probability)


####################################################################################################
