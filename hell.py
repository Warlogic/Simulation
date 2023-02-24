# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import print_function
import this
import sys
print(sys.path)

#!pip install google
from datetime import datetime


#https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c
#!pip install google_spreadsheet
#!pip install google-auth-oauthlib
#!pip install pandas
import pandas as pd
import googleapiclient
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
#!pip install google-api-python-client
from google.auth.transport.requests import Request
import os
import pickle

#insall modules
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

#Add to Spyder PATH
#C:\Users\khaxa\.spyder-py3 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\python311.zip 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\Lib 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\DLLs 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\Lib\site-packages 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\Lib\site-packages\win32 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\Lib\site-packages\win32\lib 
#C:\Users\khaxa\AppData\Local\Programs\Python\Python311\Lib\site-packages\Pythonwin


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
#SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID="1ArmVkHAETavtG2G4RJOVtD0O7aHcD-Mw5_hnf3zDPdw"
SAMPLE_RANGE_NAME='Skills!A2:O990'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    #https://developers.google.com/sheets/api/quickstart/python
    #https://console.cloud.google.com/getting-started?pli=1
    #https://developers.google.com/sheets/api/quickstart/python?authuser=3%3A
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(\
            'client_secret_23118429738-rt17k8bhl138qi3t9j0jop81d2prqk9h.apps.googleusercontent.com.json', \
                SCOPES)
            #'client_secret_23118429738-83l1bn1dir1v8isnjuicmingd4blofvv.apps.googleusercontent.com.json',
            
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        loop20 =30
        for row in values:
            loop20 = loop20 -1
            if loop20 <1:
                continue
            elif row[0] == "Metadata":
                next
            else:
            # Print columns A and E, which correspond to indices 0 and 4.
                print((row[0],row[1],row[3],row[4],row[5], row[6], row[7], row[8], row[9], row[10]))
                newSkill = Skill( group = row[0], \
                                  name  = row[1], \
                                  category = row[4], \
                                  subcategory = row[3], \
                                  penalty = row[6], \
                                  number = row[10], \
                                  impact = row[7], \
                                  reach = row[8], \
                                  expansion = row[9])
                
    except HttpError as err:
        print(err)








print("###################################################")
xn= 16   #integer
xf=16.1  #float
xs ="Warlogic"
xb = False
print ("string: ", xs, "is type: ", type(xs))
print ("Number: ", xn, "is type: ", type(xn))
print ("Number: ", xf, "is type: ", type(xf))
print ("Boolean: ", xb, "is type: ", type(xb))

print("###################################################")
print ("[lists] elements are not unique, \
       their order matters when comparing, \
       lists takes boolean, integers, strings, sets,\
       tuples, dictionaries, objects, and other lists, \
       and is variable in size, can append to it.\
       Weird consumption of range().")
actionFigure = [[11,123,45],[True,False],\
                ["hasbro","lightsabre","force"],\
                ["centimeters",9.3,True],\
                 range(10,100,5)   ]
length = len(actionFigure)
print(actionFigure)
print(actionFigure[3])
print(length)
actionFigure.append({1,'f',True})
actionFigure.append((2,"t",False))
actionFigure.append({'name':'Luke Skylwalker', 'job':'jedi'})
print(actionFigure)
print("list comprehension: turn sequence into Circumferences 2*pi*radius = 2*3.14*radius ~=6radius")
radiuses=[1,2,3,4,5,6,7,8,9]
effectiveExplosionCircumferences = [6*radius for radius in radiuses if radius < 7]
print (effectiveExplosionCircumferences)

WarlogicSkillEquation = "(( Impac + reach + EXPANSION ) * (probability * number ) + penalty ) ^ RnD"
WarlogicSkillEquationList = WarlogicSkillEquation.split()
print(WarlogicSkillEquationList)
def disect (equation):
    return equation.replace("\(", " ").lower()
print("Function chaining >>>>>>. ",[disect(word) for word in WarlogicSkillEquation.split()] )
    
print("###################################################")

print ("{Sets} elements are unique, \
       their order does NOT matter when comparing, \
       They take booleans but do not digest them :), \
       sets takes integers, strings, tuples\
       and is variable in size, can append to it.")
newfigure={1,'fff',True,'ggggggggggg', 1, 'ff', 'ff', (1,2) }
print(newfigure)
print(len(newfigure))
newfigure.add('dddddd')
print(newfigure)
print(len(newfigure))

print("###################################################")
print("(tuples) are like lists \
      but you cannot add items to it after creating them.\
      And they consume all types.\
      redundancy is OK, and order matters,\
      When used in reurns they can be without brackets")
oldfigure = ("d",'d',1,3,False,(4,5,6),[7,8,9],{10,23},{'name':'Luke Skylwalker', 'job':'jedi'})
print(oldfigure)

print("###################################################")
print("Ranges are like a numeric list of numbers,\
      you can choose begining, end and step")
x = range(3, 20, 5)
for n in x:
  print(n)

print("###################################################")
#https://www.w3schools.com/python/ref_func_map.asp
def myfunc(a, b):
  return a + "------" + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print("###################################################")
print("{'dict':'ionaries'} are lookup tables \
      you can append after creation.\
      And they consume all types.\
      ...")
dictionary ={'name':'khaled',
             'job':'game developer',
             'collection':2000,
             'available':True,
             'favourite figures':[100, 123, 343]
             }
print(len(dictionary))
print(dictionary['name'])
print(dictionary)

veterans = [["Brother Sevito",	9],
["Intercessors Primaris Lieutenant Naviaz",	7],
["Heavy Bolter 1",	8],
["Marine 1 red",	7],
["Marine 2 no helmet",	8],
["Marine 3",	7],
["Marine 4",	7],
["Heavy Bolter 2",	7],
["Skull Drone 1",	1],
["Skull drone 2",	2],
["Sentinal 1",	2],
["Sentinal 2",	2],
["Sentinal 0",	2],
["Veteran Imperial fists",	7]]

HallOfFame1 = {item[0]:item[1] for item in veterans }
HallOfFame2 = {key:value for key, value in veterans }
HallOfFame3 = list(HallOfFame2.items()) #cast to list 
HallOfFame4 = [{"Name":key, "Level":value} for key, value in HallOfFame2.items()]
print("Dictionary comprehension")
print(HallOfFame1)
print(HallOfFame2)
print(HallOfFame3)
print(HallOfFame4)

VeteranCredts = []

print("###################################################")

print("Logic operation True==True                 is: ", True==True)
print("Logic operation True!=True                 is: ", True!=True)
print("Logic operation True and True              is: ", True and True)
print("Logic operation not(False or False)        is: ", not(False or False))
print("Logic operation 11 in (1,2,3,4)            is: ", 11 in (1,2,3,4))
print("Logic operation not('cat' in 'my pet cat') is: ", not('cat' in 'my pet cat'))
print("###################################################")

print("be careful with floats")
print((1.2-1.0))
print(round((1.2-1.0),2))
print(int('100',2))  #100 string in base 2

from decimal import Decimal, getcontext
print(getcontext())
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))
print(bool(''))
print(bool({}))
print(bool())
print(bool([]))
print("xxxx")
print("###################################################")


print("_______________________________\n\
operator    int        str     \n\
+           add     concatinate\n\
-         subtract             \n\
*         multiply             \n\
**        power                \n\
/                              \n\
%                              \n\
*x        pointer , ref        \n\
**x       pointer pointer      \n\
int() float() str() casting    \n\
==                             \n\
<=                             \n\
>=                             \n\
>                              \n\
<                              \n\
!=                             \n\
and                            \n\
or                             \n\
not                            \n\
in                             \n\
xor doesnt exit in this form   \n\
# shift >> << & |              \n\
# Random   , primes            \n\
# slice list[begin:end:+-step] \n\
# poiters and references       \n\
turnary  Y if Z > Q else X     \n\
while, pass, break, continue   \n\
For pass break continue else    \n\
None, NULL?                    \n\
                               \n\
                               \n\
_______________________________\n\
")

name_symbol_dictionary = {
    'RnD':'1.1',
    'Integration':'1.2',
    'group':'',
    'name':'',
    'comment':'',
    'description':'',
    'wikiURL':'',
    'jpegURL':'',
    'impact':'!',
    'range':'@',
    'expansion':'*',
    'penalty':'&',
    'probability':'$',
    'cost':'%',
    'number':'#',
    'effectiveness':'~',
    'strategy':':',
    'control':'^',
    'move':'>',
    'offense':'}',
    'defense':'[',
    'category':'/',
    'subcategory':'//',
    'reserved':']',
    'reserved':'{',
    'reserved':'(',
    'reserved':')',
    'reserved':'-',
    'reserved':'+',
    'reserved':'=',
    'reserved':'_',
    'reserved':';',
    'reserved':'<',
    'reserved':'(*)',
    'reserved':')*(',
    'reserved':'|',
    'reserved':'.',
    'reserved':',',
    'reserved':'?',
    'reserved':'|'
    #'reserved':'/',
    #'reserved':'`',
    #'reserved':''',

    }

def getprimes(upto):
    print("local variables in prime function   ",locals())
    print("global variables outside prime function   ",globals())
    for number in range(2, upto):
        found_factors = False
        for factor in range(2, int(number**0.5) + 1):
            if number % factor == 0:
                found_factors = True
                break
        else:
            print(f'{number} is prime')
        #else is cleaner and more pythonic than:    
        if not found_factors:
            print(f'{number} is prime!')

getprimes(30)

print("variables as functions")
print(getprimes.__code__.co_varnames)
print(getprimes.__code__.co_code)

def painting(af):
    return "red"

actionFigure = 50
procedure = [getprimes, print, painting]
for func in procedure:
    result = func(actionFigure)
print(result)

print("lambda one time function on the fly")
r=(lambda x: x+10)(3)
print(r)


AllSkills =[]

categoryDicionary ={
    'Offense':'0.25',
    'Defense':'1.00',
    'Control':'0.50',
    'Strategy':'2.00',
    'Movement':'0.30',
    'Machine health':'101',
    'Animal health':'101',
    'Race health':'101',
    'repair':'38',
    'healing':'32',
    'Miracle':'29',
    'Automatic Regeneration':'20',
    'Detector':'51',
    'food':'14',
    'energy':'19',
    'Morph':'4',
    'Dive':'5',
    'Dig':'3',
    'Air':'13',
    'Land':'17',
    'Desert fittings':'0',
    'Snow fittings':'0',
    'Mudd fittings':'0',
    'Jungle fittings':'0',
    'Storm fittings':'0',
    'Blizzard fittings':'0',
    'Highsea fittings':'0',
    'Gravity transport':'0',
    'all':'62',
    'nothing':'0',
    'sea':'15',
    'space':'11',
    'Bolter':'39',
    'Explosive':'39',
    'Biological':'33',
    'Blaster':'3',
    'Melee':'1',
    'Dropbomb':'1',
    'handgun':'2',
    'Submachine gun':'5',
    'Machine gun':'5',
    'Rifle':'5',
    'Battle Rifle':'5',
    'Assault rifle':'5',
    'Hand to hand':'1',
    'Laser':'10',
    'RangelessExplosives':'1',
    'plasma':'21',
    'Accuray or Rapid fire':'18',
    'Precision':'14',
    'Rapid fire':'22',
    'Sonic':'0',
    'projectile':'8',
    'Snipe':'30',
    'precision(D20)':'77',
    'Remote Explosive':'50',
    'nanomite':'23',
    'Fire':'17',
    'Chemical or Gas':'33',
    'WMD':'0',
    'uranium':'14',
    'Actionable':'23',
    'Manipulation':'41',
    'Obstacle':'576',
    'Reinforcement':'203',
    'Administrative':'0',
    'Countermeasure':'57',
    'Vulnerability':'49',
    'morale':'22',
    'type':'0',
    'Universe':'0',
    'Vendor':'0',
    'Information':'54',
    'Limited use':'0',
    'every other time use':'0',
    'Reverse morale':'0',
    'WIP':'0',
    'Rule':'0',
    }

    

class Skill:
    # Defense in depth (Defensive programming):
    # A- Input handling 
    #    1 put default values for variables in case the caller does not specify.
    #    2 handle multiple use cases: 
    #        a specific correct range
    #        Out of range
    #        Cast to proper expected type
    #        also Double check the type of variables on input
    # B- handle exceptions
    # C- protect varialble setting that should only be calculated localy
    #    1- invoke update and calculate localy if possible
    #    2- protect getting/reading variables that should only be read by friendly classes
    #     _ underscore to protect variables https://stackoverflow.com/questions/6338867/friending-classes-in-python
    # D- Be careful what you log. 
    #    1- Encode it first.
    #    2- Do dumps in side file sthat can only be read with shells like vi.
    #    3- save debugs and traces
    
    #def __init__(self, name, group, description, comment, \
    #             wikiURL, jpegURL, category, subcategory, \
    #             penalty, number, impact, reach, expansion):
    #https://stackoverflow.com/questions/13710631/is-there-shorthand-for-returning-a-default-value-if-none-in-python
    #https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-implement-multiple-constructors
    
    def __init__(self, *args, **kwargs):
        print("OOP Object oriented Python Class difinition with flexible argument passing.")
        self.name=kwargs.get('name')
        self.group=kwargs.get('group')
        self.description=kwargs.get('description')
        self.comment=kwargs.get('comment') if kwargs.get('comment') is not None else "No Comment"  
        self.wikiURL=kwargs.get('wikiURL')
        self.jpegURL=kwargs.get('jpegURL')
        self.category=kwargs.get('category')
        self.subcategory=kwargs.get('subcategory')
        self.penalty=kwargs.get('penalty') if kwargs.get('number') is not None else 0.00
        self.impact=kwargs.get('impact')
        self.cost=None
        self.probability=1.00
        self.number=kwargs.get('number') if kwargs.get('number') is not None else 20
        self.impact=kwargs.get('impact') if kwargs.get('impact') is not None else 1.00
        self.reach=kwargs.get('reach') if kwargs.get('reach') is not None else 1.00
        self.expansion=kwargs.get('expansion') if kwargs.get('expansion') is not None else 1.00
        self.effectiveness=None
        self.calculateCost()
        self.attrs = vars(self)
        
        print(self.cost)
        

    def getProbability(self):
       #https://note.nkmk.me/en/python-type-isinstance/
       if type(self.number) is str:
          self.number=20
       print(self.number)
       num = 1
       num = int(self.number)
       if num == None or self.number == 0 :
           #or self.number < 1:
           self.number = 1 
       elif num >= 20:
           self.number =20 
       elif num <20 and num >1:
           self.number = int(self.number) #int integer casting
       else:
           self.number = 20

       if self.subcategory == None and self.category == None:
          print("We do not know either yet so we will go with 100%") 
          return 1.00
       elif self.subcategory == None and self.category != None:
           print("We only know the category, look it up") 
           prop = categoryDicionary(self.category)
           if prop == None:
               print("if you cannot find the category, return 1.00")
               return 1.00
           elif prop != None:
               print("if you can find the category, return it in float")
               return float(prop)
           else:
               print("anything else, return 1.00")
               return 1.00
       else:
           print("anything else, return 1.00")
           return 1.00
          
    def calculateCost(self):
        self.probability=self.getProbability()
        print(".probab.......", type(self.probability))
        print(".number.............", type(self.number))
        print(".penalt.............", self.penalty)
        power=1 
        try: #try to do this
            power = name_symbol_dictionary['RnD']
            print("RnD power is: ", power)
        except NameError: #if you get this error show this message
            print("Could not look up RnD power..")
            power=0
        except: # if you any other error print this message
            print("Undefined exception trying to lookup RnD power")
            power=0
        else: #if you dont get any errors, do something dependant on the previous task
            print("No reported errors while tring to look up RnD power")
            self.cost = (float(self.penalty) + \
                    (float(self.probability) * float(self.number) ) * \
                        float(self.impact + self.reach + self.expansion) ) 
            print("Cost of new skill ",self.name," is ", self.cost,"$")
        finally: #and in all cases do the following
            if self.cost == None:
                self.cost = 1000000
        return self.cost
     
    def showSkillAttributes(self):
        try:
            print(', '.join("%s: %s" % item for item in self.attrs.items()))
        except:
            print("something happened")    




skill1 = Skill(group = "jedi combo", name = "green light sabre")
print(skill1.name)
print(skill1.group)
skill1.showSkillAttributes()
print("----------------------------------")
skill2 = Skill(name = "sklill2")
print(skill2.name)
print(skill2.group)


#skillsSheet="https://docs.google.com/spreadsheets/d/1ArmVkHAETavtG2G4RJOVtD0O7aHcD-Mw5_hnf3zDPdw/edit#gid=1"

main()









#subcategory with implicit rules and defaults.
##
#meta data and template and default skills
#global rules with battle configurable defaults.
##
##

class strategy(Skill):
	pass

class control(Skill):
	pass

class move(Skill):
	pass

class offense(Skill):
	pass

class defense(Skill):
	pass        

class Unit:
    def __init__(self, uname):
        self.name=uname
        self.skills=[]

    def addSkill(self,newSkill):
        self.skills.append(newSkill)

class group():
	def __init__(self):
		#self.Name = statement()
		#self.Description = statement()
		self.Cost = 0
		self.List = []

	def getCost(self):
		totalCost = 0
		for s in self.List:
			totalCost += s.getCost()
		return totalCost

	def anounceUpgrade(self):
		print("Adding item to a group")

	def upgrade(self, item):
		self.anounceUpgrade()
		length = len(self.List)
		print (length)
		self.List.append(item)



class team(group):
	def anounceUpgrade(self):
		print("Adding unit to a team")

class squad(group):
	def anounceUpgrade(self):
		print("Adding team to a battle")

        
class Platoon(group):
    def __init__(self, pname):
        self.name=pname
        self.units=[]

class Field:
    def __init__(self, fname):
        self.name=fname
        self.terrain=[]
        
class Battle:
    def __init__(self, bname,fname):
        self.name=bname
        self.players=[]
        self.platoons=[]
        self.field=Field(fname)
        
class WarChronicle:
    def __init__(self, name):
        self.name=name
        self.battles=[]
        self.hallOfFame=[]
        
snakeeyes=Unit('Snake Eyes')
snakeeyes.skills.append('ssssss')


myList = [1,2,3,4,5]
print([2*item for item in myList])
print(myList)

myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
print(filteredList)







"""
https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
https://www.freecodecamp.org/news/time-complexity-of-algorithms/#:~:text=When%20we%20analyse%20an%20algorithm,are%20the%20number%20of%20operations).
https://stackoverflow.com/questions/9252891/big-o-what-is-the-complexity-of-summing-a-series-of-n-numbers
Name	     Big O
Constant	 O(c)
Logarithmic	 O(log(n))      Binary search (sorting is required) nlog2n
Linear	     O(n)           Linear search
Log Linear	 O(nlog(n))     Quick Sort
SumNumSeq     (n²+n)/2       Not linear, still quadratic, yet half in worst case scenario. 
Quadratic	 O(n²)          Selection Sort
Cubic	     O(n³)
Polynomial   O(n^p)
Exponential	 O(2ⁿ)
Factorial    O(n!) ~ O(nⁿ)          Travelling salesperson

"""
##########################################################
arr=[4, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # list
l=arr.__len__()
print("N is (",l,")")
##########################################################
def quadratic_algo(items):
    steps=0
    for item in items:
        for item2 in items:
            steps=steps+1
    return steps
O=quadratic_algo(arr)
print("quadratic_algo has complexity if O(",O,")")
##########################################################
def interview_algo(items, target):
    steps=0
    complements=[]
    for item in items:
        #print(item)
        for c in complements:
            steps=steps+1
            #print("item: ", item, "   complement: " , c, "    steps:", steps)
            if item == c:
                return steps
        complements.append(target-item)
    return steps
O=interview_algo(arr,100)
print("interview _algo has complexity if O(",O,")")
##########################################################
def constant_algo(items):
    result = items[0] * items[3]+10000
    return result
O=constant_algo(arr)
print("constant_algo has complexity if O(",O,")")
##########################################################
def linear_algo(items):
    steps=0
    for item in items:
        #print(item)
        steps=steps+1
    return steps
O=linear_algo(arr)
print("linear_algo has complexity if O(",O,")")

