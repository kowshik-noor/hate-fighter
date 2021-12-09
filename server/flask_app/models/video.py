from flask_app.config.mysqlconnection import connectToMySQL

class Video: 
    def __init__ (self, data):
        self.video_id = data['video_id']
        self.title = data['title']
        self.channel_name = data['channel_name']
        self.dislikes = data['dislikes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # self.info = {
        #     "video_id" : data["video_id"],
        #     "title" : data["title"],
        #     "channel_name" : data["channel_name"],
        #     "dislikes": data["dislikes"],
        #     "created_at": data["created_at"],
        #     "updated_at": data["updated_at"]
        # }

    # returns a random video from the database
    @classmethod
    def random_video(cls):
        pass

    # returns a video with the given video id
    # i will need this because an insert method will only return the id of the inserted
    # document. not the object 
    @classmethod
    def show_video(cls, data):
        query = "SELECT * FROM videos WHERE video_id = %(video_id)s;"
        result = connectToMySQL('hate-fighter').query_db(query, data)

        return cls(result[0])

    @classmethod
    def create_video(cls, data):
        query = "INSERT INTO videos (video_id, title, channel_name, dislikes) VALUES (%(video_id)s, %(title)s, %(channel_name)s, %(dislikes)s);"
        connectToMySQL('hate-fighter').query_db(query, data)