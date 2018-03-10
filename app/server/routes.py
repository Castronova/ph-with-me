from flask import session, redirect, url_for, render_template, request, flash
from . import main
from .forms import LoginForm, TimerForm


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
#    import pdb;pdb.set_trace()
    name = session.get('name', '')
    room = session.get('room', '')
    

    timer = TimerForm()
    session['timer'] = timer.data
    session['num'] = -1 

    form_data = dict(name=name,
                     room=room,
                     timer=session['timer'],
                     num=session['num'])

    if name == '' or room == '':
        return redirect(url_for('.index'))
#    return render_template('chat.html', name=name, room=room, timer=timer)
    return render_template('chat.html', form=form_data)

@main.route("/chat/timer/", methods=['GET', 'POST'])
def timer():

#    import pdb;pdb.set_trace()
    form_data = {}
    if request.method == 'POST':
#        form_data['name'] = session.get('name', '')
#        form_data['room'] = session.get('room', '')
#        form_data['timer'] = session.get('timer', '')
#        session['timer'] = form.timer
        flash('Timer Started')
#    return redirect(url_for('main.chat'))
    return redirect(url_for('main.mytimer', num=25*60))
#    return render_template('chat.html', form=form)

def get_chat_session_data():
    form_data = {}
    form_data['name'] = session.get('name', '')
    form_data['room'] = session.get('room', '')
#    form_data['timer'] = session.get('timer', '')
    return form_data

@main.route('/<int:num>h', methods=['POST'])
def hours(num):
    return redirect(url_for('main.mytimer', num=num*3600))

@main.route('/<int:num>s')
@main.route('/<int:num>')
def mytimer(num):
    form = get_chat_session_data()
    return render_template('chat.html',
                           form=form,
                           num=num)






