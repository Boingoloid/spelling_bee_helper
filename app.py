import json

from flask import Flask 
from flask import request # can remove if don't use
from flask import render_template
from flask import redirect
from flask import url_for
from flask import make_response
from lists.options import DEFAULTS  # grabs list from python file in another folder, notice dot syntax

app = Flask(__name__)

import sys
# sys.path.insert(1, '')
# from SPELLING_BEE_HELPER.python_scripts_app import word_finder

# from application.app.folder.file_1 import func_name
# from python_scripts_app.word_finder import get_letters

#Global Variables
word_found_list = []



def get_letters(available_letters,requierd_letter):
    
    import pandas as pd
    
    
    global word_found_list
    word_found_list = []
    word_found_string = ""

    path = "/Users/matthewacalin/Desktop/Webapps/word-finder-script/english-words/words_alpha.txt"
    path_export = "/Users/matthewacalin/Desktop/Book1.xlsx"
    word_df = pd.DataFrame()
    word_df = pd.read_csv(path, sep=" ", header=None)
    # df = df.drop(columns=df.columns[0], axis=1, inplace=True)
    # df = df.values.tolist()
           
    letters_included = available_letters           
    center_letter = requierd_letter

    word_list = word_df.values.tolist()
    word_list = word_list
    count = 0
    
    
    for word in word_list:
        word = str(word[0]) 

        is_valid_word = True
        contains_center_letter = False 
        is_word_long_enough = True

        # Is the word long enough?
        if len(word) <= 3:
            is_word_long_enough = False  


       
        # Contains Center Letter?
        for letter in word:   
            if letter == center_letter: 
                contains_center_letter = True

                    
        # Are all the letters valid?
 
            if (str(letter) not in str(available_letters)) and (str(letter) not in str(requierd_letter)):
                # print(letter)
                # print(available_letters)
                
                is_valid_word = False 
            
            
            
        # print(word)
        # print("is_word_long_enough: " + str(is_word_long_enough))
        # print("contains_center_letter: " + str(contains_center_letter))
        # print ("is_valid_word: " + str(is_valid_word))      
        
        if (contains_center_letter == True) and (is_word_long_enough == True) and (is_valid_word == True):
                word_found_list.append(word)
    
    word_found_string = " ".join(str(word_found_list))                    
    print("found_words_count")               
    print(len(word_found_list))                
    print(word_found_string)
         
    return word_found_string





















@app.route('/')
def letterEntry():
    return render_template('home/letter-entry-form.html')

@app.route('/', methods=['POST'])
def letterReturn():
    response = make_response(redirect(url_for('letterEntry')))
    letters = request.form['letters']
    requiered_letters = request.form['required-letters']
    
    # print(type(letters))
    # print(type(requiered_letters[0]))    
    # print(letters)
    # print(requiered_letters[0])  
    
    
    # print("form variables")
    # print(json.dumps(dict(request.form.items())))
    # return letters
    return get_letters(letters, requiered_letters)
    # print("return string")
    # print(return_string)
    # print(type(return_string))
    # return return_string
    #return letters + requierd_letters






## Getting other types from url and covering floats and ints
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1':num1, 'num2':num2}
    return render_template("home/add.html", **context) #putting ** means there can be any number of arguments, instead of assigning variables one by one
    # return render_template("home/add.html", num1=num1, num2=num2)




def get_saved_data_in_cookie():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/save', methods=['GET'])
def formStart():
    data = get_saved_data_in_cookie()
    context = data
    return render_template("home/form.html", **context)

@app.route('/save', methods=['POST'])
def save():
    # import pdb
    # pdb.set_trace()
    response = make_response(redirect(url_for('formLanding')))
    data = get_saved_data_in_cookie()
    data.update(dict(request.form.items()))
    # print("printing data in cookie, save form page")
    # print(data)
    response.set_cookie('character', json.dumps(data)) #cast as dict, from tuple pulled from items
    return response


app.run(port=5101,debug=True) #if debug true will reload every change



# -----------------------  REFERENCE

# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files


## Entering a variable in query with request global package. 
# def index(name="Treehouse"): #sets name default value
#     name = request.args.get('name', name) #if argument is there, assign to name. Args is like a dictionary
#     return "Hello from {}".format(name)


## Return raw html 
# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     #return '{} + {} = {}'.format(num1, num2, num1 + num2)
#     return """
#         <!doctype html>
#         <html>
#         <head><title>Adding!</title></head>
#         <body>
#         <h1>{} + {}  = {}</h1>
#         </body>
#         </html>
#     """.format(num1, num2, num1 + num2)



# from flask import redirect,url_for,render_template,request

# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return render_template('index.html')
#     return render_template('index.html')

# if __name__ == '__main__':
#     #DEBUG is SET to TRUE. CHANGE FOR PROD
#     app.run(port=5000,debug=True)

    # # Export to Summary Analysis file for company. Note, excel file must already exist for this script    
    # def exportData(dataframe, sheet_name):
    #     with pd.ExcelWriter(path_export, engine = "openpyxl", mode='a',if_sheet_exists="replace", date_format='mm/dd/yyyy', datetime_format='mm/dd/yyyy') as writer:
    #         workBook = writer.book
    #         try:
    #             workBook.remove(workBook[sheet_name])
    #         except:
    #             print("worksheet doesn't exist")
    #         finally:
    #             dataframe.to_excel(writer, sheet_name=sheet_name)
    #             print("data saved to: " + sheet_name)
    # exportData(word_df,"words")