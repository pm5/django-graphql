from unittest import TestCase
from unittest.mock import MagicMock

from graphqlengine.query import QueryEngine

class QueryEngineTest(TestCase):

    def testQuery(self):
        engine = QueryEngine()
        User = MagicMock()
        engine.addModel('user', User)
        engine.query("""
            {
                user(id: 4) {
                    name
                }
            }
        """)
        User.assert_called_with(id = 4)
