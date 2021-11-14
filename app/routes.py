from flask import render_template, redirect
from app import app
from app.push_post import Push_post
from app.listOfPosts import listOfPosts


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Все записи', posts=listOfPosts)

@app.route('/push_post', methods=['GET', 'POST'])
def newpost():
    form=Push_post()
    if form.validate_on_submit():
        
        listOfPosts.reverse()
        listOfPosts.append({'author': {'username': form.username.data},
            'body': form.p_text.data,'num':''+str(len(listOfPosts)+1)})
        listOfPosts.reverse()
        return redirect('/index')
    return render_template('push_text.html', form=form)

@app.route('/post/<numofpost>')
def viewPost(numofpost):
    p1=listOfPosts[len(listOfPosts)-int(numofpost)]
    return render_template('post.html', post=p1)

