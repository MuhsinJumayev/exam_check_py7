from fastapi import FastAPI

app = FastAPI()

# @app.get('/hello/')
# def hello():
#     return {'hello':'world'}

news_data = [
    {"id": '1', "title": 'news 1'},
    {"id": '2', "title": 'news 2'},
    {"id": '3', "title": 'news 3'},
    {"id": '4', "title": 'news 4'},
    {"id": '5', "title": 'news 5'},
    {"id": '6', "title": 'news 6'},
    {"id": '7', "title": 'news 7'},
    {"id": '8', "title": 'news 8'},
]

@app.get('/news/')
def news(limit: int = None, search: str = None): # query parameter
    """
    SELECT * FROM news;
    """
    
    if search:
        data = list(filter(lambda item: search in item['title'], news_data))
    else:
        data = news_data
        
    return data[:limit]


@app.get('/news/{pk}')
def news_(pk):
    """
    SELECT * FROM news
    WHERE news.id = pk;
    """
    
    return {"result": list(filter(lambda item: pk == item['id'], news_data))[0]}