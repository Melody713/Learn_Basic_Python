from string import Template
#从标准库"String"模块导入Template类
import os

os.chdir('D:\Python\leran_basic_python\yate\yate')

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')
#为函数设置了一个参数resp 并为该参数设置缺省值"text/html"

def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
#打开'templates目录下header.html'文件,并读取其中的内容作为函数的参数

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
#该函数需要提供一个参数the_links,这个参数需要打开templates/footer.html文件,从中获取并替换

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')
#返回表单最前面的HTML,允许调用者指定url和方法

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
#返回表单最末尾的HTML,还允许调用者修改提交按钮的文本

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
#给定一个选单按钮名和值,创建一个按钮

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
#给定一个选项表,该函数会将列表转换为一个HTML无序列表. 每次象Ul元素添加一个Li元素

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>')

# print(include_header('This is a tittle'))
# print(include_footer({'Home':'/index.html', 'Select': '/cgi-bin/select.py'}))
# print(start_form("/cgi-bin/porcess-athlete.py"))
# print(end_form())
# print(end_form("Click to Confirm Your Order"))
#
# for fab in ['John', 'Paul', 'George', 'Ringo']:
#     print(radio_button(fab,fab))
# print(u_list(['Life of Brian', 'Holy Grail']))
# print(header("Welcome to my home on the web",5))
# print(para("Was it worth the wait?"))