import web

urls = (
    '/', 'mongo.controllers.mongo.Delete',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()