class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)

    for record in records:
        if record.record_id == record.parent_id and record.record_id != 0:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id > len(records) - 1:
            raise ValueError("Record id is invalid or out of order.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

    nodes = {record.record_id: Node(record.record_id) for record in records}
    for record in records:
        if record.record_id:
            nodes[record.parent_id].children.append(nodes[record.record_id])

    return nodes.get(0)
