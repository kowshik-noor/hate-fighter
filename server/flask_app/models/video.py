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