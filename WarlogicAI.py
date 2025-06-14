########################################################################################################################
print("###############################################################################################################")
print("Setting up imports")
print("###############################################################################################################")
########################################################################################################################
# 0- Intsall modules
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c
# !pip install google_spreadsheet
# !pip install google-auth-oauthlib
# !pip install pandas
# !pip install google
# !pip install google-api-python-client

# 1- Import modules
########## Loading Exiting libraries ##########
##https://www.tensorflow.org/api_docs/python/tf/keras/Sequential
import tensorflow as tf
import numpy as np
# Load Keras' ResNet50 model that was pre-trained against the ImageNet database

##oops##ImageRecognitionModel = tf.keras.applications.resnet50.ResNet50()

import pandas as pd
from pytz import unicode
#######from sklearn.preprocessing import MinMaxScaler

#import os
import shutil

#from __future__ import print_function
from pathlib import Path
import imghdr
import random
import this
import sys
print(sys.path)
import inspect, re
from datetime import datetime
import pandas as pd
import googleapiclient
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pyke import knowledge_engine
import sys
import math


#https://www.tensorflow.org/tutorials/images/classification
import matplotlib.pyplot as plt
##import numpy as np
#pip install pillow
import PIL
##import tensorflow as tf

##oops##from tensorflow import keras
##oops##from tensorflow.keras import layers
##oops##from tensorflow.keras.models import Sequential
import pathlib

########################################################################################################################
print("###############################################################################################################")
print("Setting up global functions")
print("###############################################################################################################")
########################################################################################################################
### usage function

########################################################################################################################
print("###############################################################################################################")
print("Setting up global variables")
print("###############################################################################################################")
########################################################################################################################
if True:
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    print("Skipping sample files download")
    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
else:
    dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
    data_dir = tf.keras.utils.get_file('flower_photos.tar', origin=dataset_url, extract=True)

data_dir = "C:\\Users\\khaxa\\Desktop\\Ex_Files_Building_Deep_Learning_Apps\\Exercise Files\\03\\images"
data_dir = pathlib.Path(data_dir).with_suffix('')
#"C:\\Users\\khaxa\\Desktop\\Ex_Files_Building_Deep_Learning_Apps\\Exercise Files\\03\\images" #



# 3- Golbal variables
# dictionary of models
dictionary = [{'model_name': 'WarLogic Family',
              'type': 'Exper System (E.S.)',
              'make': 'PyKE',
              'developer': 'Khaled',
              'available': True,
              'useful': True,
              'complete': 0.50,
              'objective': 'Find out relationships between archetypes. Advise strategies for Ranks, Team Morales, and Battle plans.',
              'program_reference': '',
              'inputs': '',
              'returns': '',
              'depends_on': ''
              },
              {'model_name': 'ResNet50',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': 'opensource',
               'available': True,
               'useful': False,
               'complete': 1.00,
               'objective': 'Identify images. it is not very useful in the case of action figures.',
               'program_reference': '',
               'inputs': 'War chronicles campaigns',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': '',
               'type': 'genetic algorithms (G.A.)',
               'make': 'PyGAD',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'Create and evaluate new generations of skill and default values',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Archetype Model 1',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the archetype.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Archetype Model 2',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the archetype.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Vendor Model 1',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the vendor.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Vendor Model 2',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the vendor.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Universe Model 1',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the vendor.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Universe Model 2',
               'type': 'Neural Network (N.N.)',
               'make': 'tensorflow',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the vendor.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               },
              {'model_name': 'Identify Character Model 1',
               'type': 'Search Engine',
               'make': 'google image search',
               'developer': '',
               'available': False,
               'useful': False,
               'complete': 0.00,
               'objective': 'read an action figure image and tries to identify the vendor.',
               'program_reference': '',
               'inputs': '',
               'returns': '',
               'depends_on': ''
               }
              ]

AllSkills = []
AllCompanies = []
AllArchtypes = ['Elephant health', 'Horse Health', 'Camel Health', 'wildcat Health', 'Bear Health', 'Dog Health',
                'Dragon Health', 'Eagle Health', 'Boar Health', 'Unicorn Health', 'Hydra Health', 'Lion Health',
                'Yak Health', 'Cannon health 30', 'Car Health', 'Truck Health', 'small walker Health', 'Walker Health 160',
                'Amphebian health', 'Boat duribility', 'Buggy durability', 'Motorcycle durability', 'APC health',
                'large tank health', 'Transport Chopper Health', 'fighter chopper health', 'Jeep Durability',
                'fighter jet health', 'Plane health', 'spaceship health', 'speeder health', 'star fighter health',
                'X-Wing health points', 'Drone durability', 'Fairy health', 'Halfling health', 'Gnome Health',
                'Nanomited-human health', 'Xenoling health', 'Twi Health', 'Tognath health', 'Mutant Health',
                'Human Health', 'Alien Health', 'cyborg health', 'Dinosaur health', 'Centaur Health', 'Dwarf Health',
                'ogre Health', 'Goblin Health', 'Minotaur Health', 'Orc Health', 'Clone health (human)', 'Iron Golem Health',
                'Ghast Health', 'Minecraft player Health', 'Undead health', 'Enderman health', 'Creeper Health',
                'robot health', 'Mermaid health', 'Droid health', 'Elf health', 'Storage box', 'Building health',
                'Cottage Durability 640', 'landing pad Durability', 'Bunker Durability 2560', 'Castle Durability 5120',
                'Bridge durability', 'Landing runway duribility', 'Unidentified health']

#icons and symbols dictionary
name_symbol_dictionary = {
    ### Applies to skills only
    'RnD': '1.1',
    'group or combo': '||',
    'comment': '{}',
    'impact': '!',
    'range': '@',
    'expansion': '*',
    'penalty': '&',
    'probability': '$',
    'cost': '%',
    'number': '#',
    ### Applies to skills and units
    'name': '()',
    'description': '//',
    'wikiURL': '<>',
    'jpegURL': '[]',
    ### Applies to categories
    'effectiveness': '~',
    'strategy': ':',
    'control': '^',
    'move': '>',
    'offense': '}',
    'defense': '[',
    'category': '?',
    'subcategory': '??',
    ### Applies to interaction between units and skills
    'used_iterations': '(#)',
    'remaining_iterations': ')#(',
    'unit-number': '-',
    'cos1_cost2_totalcost': '+',
    'reserved': '=',
    'skill_enabled': '(_)',
    'Health': '[[[',
    'IQ': '^^^',
    'Kills': '}}}',
    'TTL': ':::',
    'Elevation or Depth': '>>>',
    ### Applies to units only
    'Integration': '1.2',
    'Unit enabled': ';',
    'Battles': ',,,',
    'Veteran points': '...',
    ### Applies to phases only
    'Defense phase': '[[',
    'Control phase': '^^',
    'Offense phase': '}}',
    'Strategy phase': '::',
    'Movement phase': '>>'
    # 'reserved':'`',
    # 'reserved':''',
}


########################################################################################################################
print("###############################################################################################################")
print("Defining Classes")
print("###############################################################################################################")
########################################################################################################################


################################################### Unit ##############################################################
class Unit:
    _UnitClass = "Unit class. a unit is any individual soldier, vehicle, building, or actor of any kind"

    def __init__(self, *args, **kwargs):
        print("==================================================================\n")
        self.companyFile = kwargs.get('companyFile')
        self.name = kwargs.get('name')  if kwargs.get('name') is not None else "No_Name"
        self.number = kwargs.get('')
        self.loreURL = kwargs.get('')
        self.imageURL = kwargs.get('')
        self.descriptionURL = kwargs.get('')
        self.Health = kwargs.get('')
        self.IQ = kwargs.get('')
        self.Kills = kwargs.get('')
        self.Veteran = kwargs.get('')
        self.points = kwargs.get('')
        self.TTL = kwargs.get('')
        self.Elevation_or_Depth = kwargs.get('')
        self.Battles = kwargs.get('')
        self.Unit = kwargs.get('')
        self.enabled = kwargs.get('')
        self.SkillReferences = kwargs.get('')
        self.image_destination = 'images\\' + '_'  + str(self.number) + '_' + str(self.name) + '.jpg'


    def downloadImage(self, _identityArray, _uniqueFileName):
        #
        #anaconda
        #conda activate py37
        #pip install requests
        #https://stackoverflow.com/questions/30229231/python-save-image-from-url
        import requests
        img_data = requests.get(self.imageURL).content
        for race in _identityArray:
            strippedname = str(self.name).rstrip()  # some manual name inputs might have \r\n in them which breaks the file name while writing to desk.
            image_destination = 'images\\'+self.number+'_'+str(_uniqueFileName)+'_'+strippedname+'___'+str(race)+'___.jpg'
            print("]]]]]]]]]]]]]]]]]]]]]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", image_destination)
            #with open('images\image_name.jpg', 'wb') as handler:
            with open(image_destination, 'wb') as handler:
                handler.write(img_data)

    def identifyImage(self):
        # Load the image file, resizing it to 224x224 pixels (required by this model)
        # img = image.load_img("bay.jpg", target_size=(224, 224))
        # pip install pillow >>> in py37 anaconda env
        # img = tf.keras.preprocessing.image.load_img("bay.jpg", target_size=(224, 224))
        image_destination = 'images\\' + self.number + '_' + self.name + '.jpg'
        img = tf.keras.preprocessing.image.load_img(image_destination, target_size=(224, 224))

        # Convert the image to a numpy array
        imgArray = tf.keras.preprocessing.image.img_to_array(img)

        # Add a forth dimension since Keras expects a list of images
        imgArray = np.expand_dims(imgArray, axis=0)

        # Scale the input image to the range used in the trained network
        # x = resnet50.preprocess_input(x)
        # https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/preprocess_input
        # tf.keras.applications.mobilenet.preprocess_input(x)
        # imgArray = tf.keras.applications.mobilenet.preprocess_input(imgArray)
        # https://github.com/ovh/ai-training-examples/blob/main/notebooks/computer-vision/image-classification/tensorflow/resnet50/notebook-resnet-transfer-learning-image-classification.ipynb
        # tensorflow.keras.applications.resnet50 import preprocess_input
        imgArray = tf.keras.applications.resnet50.preprocess_input(imgArray)

        # Run the image through the deep neural network to make a prediction
        # predictions = model.predict(x)
        predictions3 = ImageRecognitionModel.predict(imgArray)

        # Look up the names of the predicted classes. Index zero is the results for the first image.
        # predicted_classes = resnet50.decode_predictions(predictions, top=9)
        # https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet50/decode_predictions
        predicted_classes = tf.keras.applications.resnet50.decode_predictions(predictions3, top=10)

        print("This is an image of:")

        for imagenet_id, name, likelihood in predicted_classes[0]:
            print(" - {}: {:2f} likelihood".format(name, likelihood))



################################################### Skill ##############################################################
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
    #    2- Do dumps in side files that can only be read with shells like vi.
    #    3- save debugs and traces
    _skillClass = "This is a variable that should not be changed. This will always represent the breakdown and functionality of a skill."

    # def __init__(self, name, group, description, comment, \
    #             wikiURL, jpegURL, category, subcategory, \
    #             penalty, number, impact, reach, expansion):
    # https://stackoverflow.com/questions/13710631/is-there-shorthand-for-returning-a-default-value-if-none-in-python
    # https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-implement-multiple-constructors

    def __init__(self, *args, **kwargs):
        print("==================================================================\nSkill addition: OOP Object oriented Python Class definition with flexible argument passing.")
        self.name = kwargs.get('name')
        self.group = kwargs.get('group')
        self.description = kwargs.get('description')
        self.comment = kwargs.get('comment') if kwargs.get('comment') is not None else "No Comment"
        self.wikiURL = kwargs.get('wikiURL')
        self.jpegURL = kwargs.get('jpegURL')
        self.category = kwargs.get('category')
        self.subcategory = kwargs.get('subcategory')
        #self.penalty =  0.00
        self.penalty = kwargs.get('penalty') if kwargs.get('penalty') is not None else 1.00
        #self.impact = kwargs.get('impact')
        self.cost = None
        self.probability = 1.00
        self.number = kwargs.get('number') if kwargs.get('number') is not None else 20
        self.impact = kwargs.get('impact') if kwargs.get('impact') is not None else 1.00
        self.reach = kwargs.get('reach') if kwargs.get('reach') is not None else 1.00
        self.expansion = kwargs.get('expansion') if kwargs.get('expansion') is not None else 1.00
        self.effectiveness = None
        self.calculateCost()
        self.attrs = vars(self)

        print("Skill addition: Cost is ", self.cost)

    def getProbability(self):
        # https://note.nkmk.me/en/python-type-isinstance/
        if type(self.number) is str:
            self.number = 20
        print("Skill addition: #", self.number)
        num = 1
        num = int(self.number)
        if num == None or self.number == 0:
            # or self.number < 1:
            self.number = 1
        elif num >= 20:
            self.number = 20
        elif num < 20 and num > 1:
            self.number = int(self.number)  # int integer casting
        else:
            self.number = 20

        if self.subcategory == None and self.category == None:
            print("Skill addition: We do not know either yet so we will go with 100%")
            return 1.00
        elif self.subcategory == None and self.category != None:
            print("Skill addition: We only know the category, look it up")
            prop = categoryDicionary(self.category)
            if prop == None:
                print("Skill addition: if you cannot find the category, return 1.00")
                return 1.00
            elif prop != None:
                print("Skill addition: if you can find the category, return it in float")
                return float(prop)
            else:
                print("Skill addition: anything else, return 1.00")
                return 1.00
        else:
            print("Skill addition: anything else, return 1.00")
            return 1.00

    def calculateCost(self):
        self.probability = self.getProbability()
        if False:
            print("Skill addition: probability.......", type(self.probability))
            print("Skill addition: number.............", type(self.number))
            print("Skill addition: penalty.............", self.penalty)
        power = 1
        try:  # try to do this
            power = name_symbol_dictionary['RnD']
            if False:
                print("Skill addition: RnD power is: ", power)
        except NameError:  # if you get this error show this message
            print("Skill addition: Could not look up RnD power..")
            power = 0
        except:  # if you any other error print this message
            print("Skill addition: Undefined exception trying to lookup RnD power")
            power = 0
        else:  # if you dont get any errors, do something dependant on the previous task
            if False:
                print("Skill addition: No reported errors while trying to look up RnD power")
            self.cost = ( float(self.impact) + float(self.reach) + float(self.expansion)) * (float(self.probability) * float(self.number)) + float(self.penalty)
            #float(self.penalty) +

            print("Skill addition: Cost of new skill ", self.name, " is ", self.cost, "$")
        finally:  # and in all cases do the following
            if self.cost == None:
                self.cost = 1000000
        return self.cost

    def showSkillAttributes(self):
        try:
            record = ', '.join("%s: %s" % item for item in self.attrs.items())
            if False:
                print("Skill addition: Record: ", record  )
        except:
            if False:
                print("Skill addition: something happened")


#############################################Database retriever ########################################################
class GoogleRetriever():
    def __init__(self, *args, **kwargs):
        print("==================================================================")
        self.scope = [kwargs.get('scope')] if kwargs.get('scope') is not None else ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.file = kwargs.get('file') if kwargs.get('file') is not None else "1ArmVkHAETavtG2G4RJOVtD0O7aHcD-Mw5_hnf3zDPdw"
        self.cellrange = kwargs.get('cellrange') if kwargs.get('cellrange') is not None else 'Skills!A2:O990'
        self.secret = kwargs.get('secret') if kwargs.get('secret') is not None else 'client_secret_438937642705-hee3p5cnh2eq4t4fnc30kco72igikpg6.apps.googleusercontent.com.json'
        self.values = []
        self.rows = kwargs.get('rows') if kwargs.get('rows') is not None else '1191'
        self.identityArray = []

    # 4- Define retriever
    def retrieve(self):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """

        # 3- Connect to data stores, databases, files
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        # The ID and range of a sample spreadsheet.
        #SAMPLE_SPREADSHEET_ID = "1ArmVkHAETavtG2G4RJOVtD0O7aHcD-Mw5_hnf3zDPdw"
        ##SAMPLE_SPREADSHEET_ID="1rbsL0aLE3E5FxIVjMIHvc-oWb8baYvR0oZVW5Kx20uM"
        #SAMPLE_RANGE_NAME = 'Skills!A2:O990'
        #SAMPLE_RANGE_NAME = self.cellrange

        #Open WL browser
        ## 
