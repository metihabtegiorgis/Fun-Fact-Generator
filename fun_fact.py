import json 
import requests 
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def fun_fact_gen(_):

    #new session
    clear()

    #image of the icon
    put_html("<p align=""left""><h2><img src=""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpOyUl-R9-_l98wKHrV-TULPuB0PGjJeaTgUE6R_HSQg&s"" width=""5%"">  \ Fun Fact Generator</h2></p>")

    #url for data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    #using GET request
    response = requests.request("GET",url)

    #load request into json file
    data = json.loads(response.text)

    #since only the text is needed, extract and use
    fact = data['text']

    #imporve apperance of fact
    style(put_text(fact), 'color:blue; font-size: 30px') 

    #regenerate option
    put_buttons( 
        [dict(label='Click me', value='outline-success',  
              color='outline-success')], onclick=fun_fact_gen)
    



if __name__ == '__main__': 

    # Put a heading "Fun Fact Generator" 
    put_html("<p align=""left""><h2><img src=""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpOyUl-R9-_l98wKHrV-TULPuB0PGjJeaTgUE6R_HSQg&s")
    # hold the session for long time 
    put_buttons( 
        [dict(label='Click me', value='outline-success',  
              color='outline-success')], onclick=fun_fact_gen)   
hold() 