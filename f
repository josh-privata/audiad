exec(open('command.py').read())
c=Command()
c.recreate_index()
c.push_db_to_index()
