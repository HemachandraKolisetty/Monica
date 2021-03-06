from random import choice
from templates.button import ButtonTemplate
from templates.text import TextTemplate
import sys,os
import config,json


def process(action,parameter):
    output ={}
    try:
        with open(config.QUOTES_SOURCE_FILE) as quotes_file:
            quotes = json.load(quotes_file)
            quotes_list = quotes['quotes']
        quote = choice(quotes_list)
        template = ButtonTemplate(text=quote)
        template.add_postback(title='One more!',payload='more!quote')
        output['action'] = action
        output['success'] = True
        output['output'] = template.get_message()
    except Exception as E:
        print E
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print exc_type, fname, exc_tb.tb_lineno
        error_message = 'I couldn\'t find any Quote '
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Tell me a Quote'
        error_message += '\n  - I\'m demotivated'
        error_message += '\n  - I want a quote'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output

if __name__ == '__main__':
    print process('quote','parameter')