from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

# this code is adapted from https://github.com/miguelgrinberg/Flask-SocketIO-Chat<Paste>

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' joined'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' left'}, room=room)

@socketio.on('timer', namespace='/chat')
def text(message):
    """Sent by a client when the timer is updated.
    The timer is update for all people in the room."""
    room = session.get('room')
    emit('timerupdate', {'msg': message}, room=room)
