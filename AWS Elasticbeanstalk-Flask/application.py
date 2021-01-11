from flask import Flask


def get_response(username = "World"):
    return '<p>Hello %s!</p>\n' % username

header_text = ''' <html>EB Flask Test<body>'''
instructions = ''' '''
footer_text = '</body>\n</html>'

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text + get_response() + instructions + footer_text))
application.add_url_rule('/<username>', 'hello', (lambda username:  header_text + get_response(username) + footer_text))

if __name__ == "__main__":
   application.debug = True
   application.run()


def square(num):
      result = num ** 2
      return result
square(3)

def square(num): 
    return num ** 2  
square(3)

def square(num): return num ** 2  
square(3)

square = lambda num: num ** 2  
square(3)