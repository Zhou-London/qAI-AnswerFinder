"""
Service of manticore service
Re-encapsulation of Database operations
"""

from configure.manticore_config import manticore_agent

# Configure table name
TABLE_NAME = "qas"


class Agent:

    def __init__(self):
        pass

    def check_status(self):
        if manticore_agent:
            return True
        else:
            return False

    # Add data to this table
    def add(self, title: str, question: str, answer: str):

        response = manticore_agent.index_api.insert(
            {
                "table": TABLE_NAME,
                "doc": {"title": title, "question": question, "answer": answer},
            }
        )

        return response

    # Search data from this table
    def search(self, text: str):

        response = manticore_agent.search_api.search(
            {
                "table": TABLE_NAME,
                "query": {"query_string": f"@question {text}"},
                "highlight": {"fields": {"tag": {}}},
            }
        )

        return response

    # Delete data using "title"
    def delete(self, text: str):

        response = manticore_agent.index_api.delete(
            {"table": TABLE_NAME, "query": {"match": {"title": text}}}
        )

        return response


manticore_service = Agent()
