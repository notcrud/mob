from blitzdb import Document, FileBackend

backend = FileBackend('./mob-db')

'''
A user shall have the following attributes: name, email, username/handle, twitter/facebook ID, auth token, karma points, as well
as future references to posts, comments and votes.
'''

class User(Document):
	pass


'''
A post shall have the following attributes: title, content, a reference to the user who posted it, timestamp, a list containing
IDs of comments in chronological order, as well as a list of vote IDs.
'''

class Post(Document):
	pass

'''
A comment shall have the following attributes: content, a reference to the author.
'''

class Comment(Document):
	pass

'''
A vote shall have a reference to the user, and a reference to the post.
'''

class Vote(Document):
	pass


