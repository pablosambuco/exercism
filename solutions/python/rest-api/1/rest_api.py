import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        try:
            if payload:
                payload = json.loads(payload)

            if url == "/users":
                users = self.database["users"]
                if payload:
                    users = [user for user in users if user["name"] in payload["users"]]

                return json.dumps({"users": users})
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid payload"})

    def post(self, url, payload=None):
        try:
            if payload:
                payload = json.loads(payload)

            if url == "/add":
                data = {
                    "name": payload["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0,
                }
                self.database["users"].append(data)
                return json.dumps(data)

            elif url == "/iou":
                giver = payload["lender"]
                taker = payload["borrower"]
                amount = float(payload["amount"])

                for user in self.database["users"]:
                    if user["name"] == giver:
                        self._settle(user, "+", amount, taker, "owes", "owed_by")
                    if user["name"] == taker:
                        self._settle(user, "-", amount, giver, "owed_by", "owes")

                return self.get("/users", json.dumps({"users": [giver, taker]}))
        except json.JSONDecodeError:
            return json.dumps({"error": "Invalid payload"})

    @staticmethod
    def _settle(user, operation, amount, other, key1, key2):
        if operation == "+":
            user["balance"] += amount
        else:
            user["balance"] -= amount

        if other in user[key1]:
            if user[key1][other] > amount:
                user[key1][other] -= amount
                amount = 0
                if other in user[key2]:
                    user[key2].pop(other)
            else:
                amount -= user[key1][other]
                user[key1].pop(other)
        if amount:
            user[key2][other] = user[key2].get(other, 0) + amount
