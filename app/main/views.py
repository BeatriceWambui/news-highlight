from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles
from ..models import Review
from .forms import ReviewForm
#views 
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular news
    popular_news = get_news('sources')

    title = 'Home- Welcome to our News Highlight Website'
    search_news = request.args.get('news_query')

    return render_template('index.html', title = title, popular = popular_news)

@main.route('/news/<id>')
def news(id):
    '''
    View news page function that returns the news highlights page and its data
    '''
    news = get_articles(id)
    title = 'You are viewing articles'
    return render_template('news.html', title = title, news = news)
@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)
@main.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)