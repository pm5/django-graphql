from graphql.parser import GraphQLParser

class QueryEngine:
    """
    GraphQL query engine.

    Usage:

        graphql = QueryEngine()
        graphql.addModel('user', user)
        result = graphql.query('''
            {
                user(id: 4) {
                    name
                }
            }
        ''')
        # result = {'user': {'name': 'Mark Zuckerberg'}}
    """
    def __init__(self, **kwargs):
        self._models = {}
        self._parser = GraphQLParser()

    def addModel(self, name, model):
        self._models[name] = model

    def _getAST(self, query):
        return self._parser.parse(query)

    def query(self, query):
        ast = self._getAST(query)
