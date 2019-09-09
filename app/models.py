class Review:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response

class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,url,category):
        self.id =id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Articles:
    '''
    Articles class
    '''
    def __init__(self,id,image,description,articlesSource,author,timePublished):
        self.id=id
        self.image=image
        self.description=description
        self.articlesSource=articlesSource
        self.timePublished=timePublished
        self.author=author

        