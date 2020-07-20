import web
import app
import ssl
import pymongo
from pymongo import MongoClient

render = web.template.render("mongo/views/")

class Delete:
    def GET(self):
        client = MongoClient("mongodb://testdb:test@first-shard-00-00.azha6.mongodb.net:27017,first-shard-00-01.azha6.mongodb.net:27017,first-shard-00-02.azha6.mongodb.net:27017/<Escuela>?ssl=true&replicaSet=atlas-m76lu5-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.get_database('Escuela')
        Alumnos_collection=db.Alumnos
        contenedor=list(Alumnos_collection.find())
        tam=Alumnos_collection.count()
        return render.delete(contenedor,tam)
    def POST(self):
        print("entrando a metdo form POST")
        try:
            valor_borrar=web.input()
            print("el id a borrar es")
            print(valor_borrar)
            client = MongoClient("mongodb://testdb:test@first-shard-00-00.azha6.mongodb.net:27017,first-shard-00-01.azha6.mongodb.net:27017,first-shard-00-02.azha6.mongodb.net:27017/<Escuela>?ssl=true&replicaSet=atlas-m76lu5-shard-0&authSource=admin&retryWrites=true&w=majority")
            db = client.get_database('Escuela')
            Alumnos_collection=db.Alumnos
            print("antes de borrar hay:")
            contador=Alumnos_collection.count()
            print(contador)
            borrar=valor_borrar.borrar
            print(borrar)
            Alumnos_collection.delete_one({'_id':str(borrar)})
            contenedor=list(Alumnos_collection.find())
            tam=Alumnos_collection.count()
            print("despues de borrar hay:")
            print(tam)
            return render.delete(contenedor,tam)
        except Exception as error:
            return "Error" +str(error)




