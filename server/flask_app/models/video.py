from flask_app.config.mysqlconnection import connectToMySQL

class Video: 
    def __init__ (self, data):
        self.video_id = data['video_id']
        self.title = data['title']
        self.channel_name = data['channel_name']
        self.dislikes = data['dislikes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # returns a random video from the database
    @classmethod
    def random_video(cls):
        query = "SELECT * FROM videos ORDER BY RAND() LIMIT 1;"
        result = connectToMySQL('hate-fighter').query_db(query)
        return cls(result[0])

    # returns a video with the given video id
    @classmethod
    def show_video(cls, data):
        query = "SELECT * FROM videos WHERE video_id = %(video_id)s;"
        result = connectToMySQL('hate-fighter').query_db(query, data)

        if len(result) > 0:
            return cls(result[0])
        else:
            return False

    # inserts a video into the database if its ID is not in the db
    @classmethod
    def create_video(cls, data):
        if not cls.show_video({'video_id': data['video_id']}):
            query = "INSERT INTO videos (video_id, title, channel_name, dislikes) VALUES (%(video_id)s, %(title)s, %(channel_name)s, %(dislikes)s);"
            connectToMySQL('hate-fighter').query_db(query, data)
            return
        else:
            # if the video id exists in the db, update the row with the latest info
            cls.update_video(data)
            return

    # updates a video with a given id
    @classmethod
    def update_video(cls, data):
        query = "UPDATE videos SET title=%(title)s, channel_name=%(channel_name)s, dislikes=%(dislikes)s, updated_at=NOW() WHERE video_id=%(video_id)s;"
        connectToMySQL('hate-fighter').query_db(query, data)