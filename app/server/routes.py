from flask import session, redirect, url_for, render_template, request, flash
from . import main
from .forms import LoginForm, TimerForm
from app.server.database import db_session
from app.server.models import ChatSession


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    chatroom = ChatSession.query.filter(ChatSession.name == room)

    # initialize the chat session if it doesn't already exist
    if chatroom.first() is None:
        chatsession = ChatSession(name=room, admin=name)
        db_session.add(chatsession)
        db_session.commit()

    # get the chat session data
    chatroom = ChatSession.query.filter(ChatSession.name == room).first()
    timer = TimerForm()
    session['timer'] = timer.data
    session['num'] = -1

    form_data = dict(admin=chatroom.admin,
                     name=name,
                     room=chatroom.name,
                     timer=session['timer'],
                     num=session['num'])

    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', form=form_data)


def get_session_data():
    # get the chat session data
    name = session.get('name', '')
    room = session.get('room', '')
    chatroom = ChatSession.query.filter(ChatSession.name == room).first()
    form_data = dict(admin=chatroom.admin,
                     name=name,
                     room=chatroom.name,
                     timer=session['timer'],
                     num=session['num'])
    return form_data


@main.route("/chat/timer/", methods=['GET', 'POST'])
def timer():
    """
    end point for starting the PH timer
    """
    if request.method == 'POST':
        # send text to screen to indicate that the timer has started.
        flash('Timer Started')

    # get session data and pass it back to the template
    data = get_session_data()

    # redirect to the mytimer function 
    return redirect(url_for('main.mytimer', num=25*60, form=data))


@main.route('/<int:num>h', methods=['POST'])
def hours(num):
    return redirect(url_for('main.mytimer', num=num*3600))


@main.route('/chat', methods=['POST'])
def stop():
    data = get_session_data()
    return render_template('chat.html',
                           form=data)


@main.route('/chat', methods=['POST'])
def kill():
    # place holder for killing the chat room
    print('kill chat room')
    return render_template('chat.html', form=get_session_data())


@main.route('/<int:num>s')
@main.route('/<int:num>')
def mytimer(num):
    form = get_session_data()
    return render_template('chat.html',
                           form=form,
                           num=num)
