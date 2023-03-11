

def get_letters(letters,requiered_letters):
    
   
    word_found_list = []

    import os
    import shutil
    import math
    import pandas as pd
    import numpy as np
    import openpyxl

    path = "/Users/matthewacalin/Desktop/Webapps/word-finder-script/english-words/words_alpha.txt"
    path_export = "/Users/matthewacalin/Desktop/Book1.xlsx"
    word_df = pd.DataFrame()
    word_df = pd.read_csv(path, sep=" ", header=None)
    # df = df.drop(columns=df.columns[0], axis=1, inplace=True)
    # df = df.values.tolist()
        
    # Export to Summary Analysis file for company. Note, excel file must already exist for this script    
    def exportData(dataframe, sheet_name):
        with pd.ExcelWriter(path_export, engine = "openpyxl", mode='a',if_sheet_exists="replace", date_format='mm/dd/yyyy', datetime_format='mm/dd/yyyy') as writer:
            workBook = writer.book
            try:
                workBook.remove(workBook[sheet_name])
            except:
                print("worksheet doesn't exist")
            finally:
                dataframe.to_excel(writer, sheet_name=sheet_name)
                print("data saved to: " + sheet_name)
    # exportData(word_df,"words")
                
    # letters_included = ["l","t","d","u","i","n","a"] 
    letters_included = letters           
    # center_letter = "a"
    center_letter = requiered_letters

    word_list = word_df.values.tolist()
    
    # print(word_list[0:10])
    count = 0
    for word in word_list:
        word = str(word[0])
        if len(word) <= 3:
            continue
    #     print(type(word))
    #     print("Word :" + word)
        is_valid_word = True
        is_valid_letter = True
        contains_center_letter = False
        for letter in word:
            if letter in letters_included:
                is_valid_letter = True
            else:
                is_valid_letter = False
                is_valid_word = False
            if letter == center_letter:
                contains_center_letter = True
        if is_valid_word and contains_center_letter:
            count = count + 1        
            # print("Word:")
            # print(word) 
            type(word)
            # print("count:")
            # print(count)
            # type(count)
            print("Word found")
            print(word)
            word_found_list.append(word[0])
            
            # \word_found_list = word_found_list.(str1.join(s))(word)
    # print("PRINTING WORD FOUND LIST")  
    # print("word_found_list")
    # print(word_found_list)
    # print(type(word_found_list))
    
    word_found_string = ' '.join(map(str, word_found_list))
    # # word_found_string = " ".join(str(word_found_list))
    print("word_found_string")
    print(word_found_string)
    return word_found_string
    # return "Hello Cruel World"            
