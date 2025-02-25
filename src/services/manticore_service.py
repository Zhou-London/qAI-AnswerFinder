"""
Service of manticore service
Re-encapsulation of Database operations
"""

from config.manticore_config import manticore_agent


class Agent:

    def __init__(self):
        pass

    def add(self, title: str, question: str, answer: str):
        manticore_agent.index_api.insert(
            {
                "table": "QAs",
                "doc": {"title": title, "question": question, "answer": answer},
            }
        )
