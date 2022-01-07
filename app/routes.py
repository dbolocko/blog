from flask import render_template, redirect
from app import app
from app.push_post import Push_post
from app.listOfPosts import listOfPosts, nr
import json

def savePosts():
    global listOfPosts
    print(str(listOfPosts))
    y=str(listOfPosts)
    txt_file= open("output.txt","w")
    txt_file.write(y)
    txt_file.close()
    print("save")

def loadPosts():
    global listOfPosts
    listOfPosts = []
    global nr
    nr+=1
    txt_file= open("output.txt","r")
    y=txt_file.read()
    txt_file.close()
    i=0
    while i<len(y):
        print(y)
        print("\n\n"+str(i))
        tempauthor=""
        tempbody=""
        tempnum=""
        #если author is valid то 
        #считываем до первой двойной кавычки, запоминаем и автора, и его длину
        #пропускаем мимо ушей n символов и считываем и запоминаем тело и его длину
        #-/-/- и считываем номер -/=/=
        #сохранить в массив всё что достали
        if(y[:13]=="[{'author': '"):
            i=13
            while y[i]!="'":
                tempauthor+=y[i]
                i+=1
            tempalen=i-13
            i+=12
            while y[i]!="'":
                tempbody+=y[i]
                i+=1
            i+=len("', 'num': '")
            while y[i]!="'":
                tempnum+=y[i]
                i+=1
            listOfPosts.append({'author': tempauthor,'body': tempbody,'num':tempnum})
            y=y[i:]
            i=0
            #очистить содержимое проанализированной части строки
        elif(y[:16]=="'}, {'author': '"):
            i=16
            while y[i]!="'":
                tempauthor+=y[i]
                i+=1
            i+=len("', 'body': '")
            while y[i]!="'":
                tempbody+=y[i]
                i+=1
            i+=len("', 'num': '")
            while y[i]!="'":
                tempnum+=y[i]
                i+=1
            listOfPosts.append({'author': tempauthor,'body': tempbody,'num':tempnum})
            y=y[i:]
            i=0
        else:
            i+=1

@app.route('/')
@app.route('/index')
def index():
    print(len(listOfPosts))
    global nr
    if(nr<1):
        loadPosts()
    return render_template('index.html', title='Все записи', posts=listOfPosts)

@app.route('/push_post', methods=['GET', 'POST'])
def newpost():
    form=Push_post()
    if form.validate_on_submit():
        listOfPosts.reverse()
        listOfPosts.append({'author': form.username.data,
            'body': form.p_text.data,'num':''+str(len(listOfPosts)+1)})
        listOfPosts.reverse()
        savePosts()
        return redirect('/index')
    return render_template('push_text.html', form=form)

@app.route('/post/<numofpost>')
def viewPost(numofpost):
    p1=listOfPosts[len(listOfPosts)-int(numofpost)]
    return render_template('post.html', post=p1)

@app.route('/save')
def savvvee123():
    savePosts()
    return "ok"

@app.route('/load')
def llooaaaddd44():
    loadPosts()
    return str(listOfPosts)