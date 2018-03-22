#!/usr/bin/env python
from app import create_app, socketio
#import sqlite3
#import os
from app.server.database import init_db

app = create_app(debug=True)


#def build_db(dbpath):
#
#    if not os.path.exists(dbpath):
#
#        # build session database
#        conn = sqlite3.connect(dbpath)
#        c = conn.cursor()
#
#        # Create table
#        c.execute('''CREATE TABLE chatrooms
#                             (room text, admin text, created text)''')
#
#        # Save (commit) the changes
#        conn.commit()
#        conn.close()

if __name__ == '__main__':
#    build_db('session.db')
    init_db()
    socketio.run(app)
