#coding:utf8
#命令行高亮/提示等
#
from __future__ import unicode_literals, print_function

def simple():
    from prompt_toolkit import prompt

    text = prompt('Give me some input: ')
    print('You said: %s' % text)


def simple1():
    from prompt_toolkit import PromptSession

    # Create prompt object.
    session = PromptSession()

    # Do multiple input calls.
    text1 = session.prompt("please input text1: ")
    text2 = session.prompt("please input text2: ")
    print("text1: "+text1)
    print("text2: "+text2)


#高亮
def color():
    from pygments.lexers.html import HtmlLexer
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.lexers import PygmentsLexer

    text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer))
    print('You said: %s' % text)


def color0():
    from pygments.lexers.html import HtmlLexer
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.styles import Style
    from prompt_toolkit.lexers import PygmentsLexer

    our_style = Style.from_dict({
        'pygments.comment':   '#888888 bold',
        'pygments.keyword':   '#ff88ff bold',
    })

    text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer),
              style=our_style)

def color1():
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.styles import Style
    
    style = Style.from_dict({
        # User input (default text).
        '':          '#ff0066',
    
        # Prompt.
        'username': '#884444',
        'at':       '#00aa00',
        'colon':    '#0000aa',
        'pound':    '#00aa00',
        'host':     '#00ffff bg:#444400',
        'path':     'ansicyan underline',
    })
    
    message = [
        ('class:username', 'john'),
        ('class:at',       '@'),
        ('class:host',     'localhost'),
        ('class:colon',    ':'),
        ('class:path',     '/user/john'),
        ('class:pound',    '# '),
    ]
    
    text = prompt(message, style=style)


def color2():
    from prompt_toolkit.shortcuts import prompt
    from prompt_toolkit.styles import style_from_pygments_cls, merge_styles
    from prompt_toolkit.lexers import PygmentsLexer
    from prompt_toolkit.styles import Style   
 
    from pygments.styles.tango import TangoStyle
    from pygments.lexers.html import HtmlLexer
    
    our_style = merge_styles([
        style_from_pygments_cls(TangoStyle),
        Style.from_dict({
            'pygments.comment': '#888888 bold',
            'pygments.keyword': '#ff88ff bold',
        })
    ])
    
    text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer),
                  style=our_style)


#自动补全
def auto():
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter

    html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>','</html>', '</body>', '</head>', '</title>'])
    text = prompt('Enter HTML: ', completer=html_completer)
    print('You said: %s' % text)



from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
    
class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        #获取输入的字符串
        text = document.text
        x=len(text)
        yield Completion('completion', start_position=-x)

class MyCustomCompleter1(Completer):
    def get_completions(self, document, complete_event):
        # Display this completion, black on yellow.
        yield Completion('completion1', start_position=-1,
                         style='bg:ansiyellow fg:ansiblack')

        # Underline completion.
        yield Completion('completion2', start_position=-1,
                         style='underline')

        # Specify class name, which will be looked up in the style sheet.
        yield Completion('completion3', start_position=-1,
                         style='class:special-completion')

def auto2():    
    text = prompt('> ', completer=MyCustomCompleter(),complete_while_typing=True)


#自动提示
def auto_suggest():
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import InMemoryHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

    session = PromptSession()

    while True:
        text = session.prompt('> ', auto_suggest=AutoSuggestFromHistory())
        print('You said: %s' % text)


def _default():
    from prompt_toolkit import prompt
    import getpass
    #默认值
    text=prompt('What is your name: ', default='%s' % getpass.getuser())
    #text=prompt('What is your name: ',  mouse_support=True)
    print(text)


"""
validator   有效性检查
prompt('> ',validator=XXX)
"""

###################################
#格式化输出
def my_print():
    
    from prompt_toolkit import print_formatted_text
    from prompt_toolkit.formatted_text import FormattedText
    
    text = FormattedText([
        ('#ff0066', 'Hello'),
        ('', ' '),
        ('#44ff00 italic', 'World'),
    ])
    
    print_formatted_text(text)
###################################
"""
from prompt_toolkit.shortcuts import input_dialog
#对话框
"""

##################################
#进度条



def processbar0():
    from prompt_toolkit.shortcuts import ProgressBar
    import time

    with ProgressBar() as pb:
        for i in pb(range(800)):
            time.sleep(.01)



def processbar1():
    from prompt_toolkit.shortcuts import ProgressBar
    import time

    def some_iterable():
        yield 1
        time.sleep(1)
        yield 1
        time.sleep(1)
        yield 1
        time.sleep(1)
        yield 1
        time.sleep(1)
        yield 1

    with ProgressBar() as pb:
        for i in pb(some_iterable(), total=5):
            time.sleep(.01)





##########异步######################
import asyncio
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

async def my_coroutine():
    
    session = PromptSession()
    while True:
        with patch_stdout():
            result = await session.prompt_async('Say something: ')
        print('You said: %s' % result)

def run_coroutin():
    
    tasks = [my_coroutine() for i in range(3)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print("all done")
    loop.close()


if __name__=="__main__":
    
    #simple()
    #simple1()
    #color()
    #color1()
    #color2()
    #auto()
    #auto1()
    #auto2()
    #_default()
    
    #auto_suggest()
    #my_print()

    #processbar0()
    processbar1()

    #my_coroutine()
    #run_coroutin()
