from flask import render_template, redirect
from app import app
from app.push_post import Push_post

listOfPosts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
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
            'body': form.p_text.data})
        listOfPosts.reverse()
        return redirect('/index')
    return render_template('push_text.html', form=form)