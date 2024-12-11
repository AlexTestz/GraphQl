from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
import graphene

app = Flask(__name__)

# Definir un esquema básico de GraphQL
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "Hola, Mundo!"

schema = Schema(query=Query)

# Agregar la vista GraphQL a la ruta y habilitar GraphiQL
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)

