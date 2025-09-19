from dataclasses import dataclass
from typing import Any

NODE, EDGE, ATTR = range(3)

VALIDATION = {
    NODE: {"len": 2, "msg": "Node is malformed"},
    EDGE: {"len": 3, "msg": "Edge is malformed"},
    ATTR: {"len": 2, "msg": "Attribute is malformed"},
}


@dataclass(eq=True, frozen=False)
class Node:
    name: Any
    attrs: dict[Any:Any]


@dataclass(eq=True, frozen=False)
class Edge:
    src: Any
    dst: Any
    attrs: dict[Any:Any]


class Graph:
    def __init__(self, data: list = None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if not data:
            return

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

        for item in data:
            self._process_item(item)

    def _process_item(self, item):

        if len(item) < 3:
            raise TypeError("Graph item incomplete")

        type_ = item[0]
        if type_ not in (NODE, EDGE, ATTR):
            raise ValueError("Unknown item")

        action = {
            NODE: self._add_node,
            EDGE: self._add_edge,
            ATTR: self._add_attr,
        }
        
        itemdata = item[1:]
        self._test_len(type_, len(itemdata))
        action[type_](itemdata)

    def _test_len(self, type, itemsize):
        if VALIDATION[type]["len"] != itemsize:
            raise ValueError(VALIDATION[type]["msg"])

    def _add_node(self, itemdata):
        name, attrs = itemdata
        self.nodes.append(Node(name, attrs))

    def _add_edge(self, itemdata):
        src, dst, attrs = itemdata
        self.edges.append(Edge(src, dst, attrs))

    def _add_attr(self, itemdata):
        key, value = itemdata
        self.attrs[key] = value
