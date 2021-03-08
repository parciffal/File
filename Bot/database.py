import csv
import config


class DataConnector:
    filename = config.FILENAME
    
    def writeHeaders(self):
        headers = ['name', 'id', 'status']
        with open(self.filename, 'a', newline = '') as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames=columns)
            writer.writeheaders()

    def add_user(self, username, user_id, status: bool):
        users = self.get_all_ids()
        stat = False
        for id in users:
            if str(user_id) == str(id):
                count = True
        if count == False:
            with open(self.filename, 'a', newline="") as file:
                columns = ["name", "id", "status"]
                writer = csv.DictWriter(file, fieldnames=columns)
                user = {"name": username, "id": user_id, "status": status}
                writer.writerow(user)

    def get_all_ids(self):
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            userlist = []
            for row in reader:
                userlist.append(row["id"])
            return userlist

    def id_cheaker(self, new_user_id):
        user_id = self.get_all_ids()
        is_user = False
        for id in user_id:
            if new_user_id == id:
                is_user = True
        return is_user

    def remove(self, user_id):
        lines = list()
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if str(user_id) == str(row['id']):
                    continue
                else:
                    dick = {"name": row['name'], "id": row['id'], "status": row['status']}
                    lines.append(dick)

        with open(self.filename, 'w') as file:
            columns = ["name", "id", "status"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'], "id": row['id'], "status": row['status']}
                writer.writerow(user)

    def make_userActive(self, user_id):
        lines = list()
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if user_id == row['id']:
                    dick = {"name": row['name'], "id": row['id'], "status": True}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'], "id": row['id'], "status": row['status']}
                    lines.append(dick)
            file.close()

        with open(self.filename, 'w') as file:
            columns = ["name", "id", "status"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'], "id": row['id'], "status": row['status']}
                writer.writerow(user)
            file.close()


    def make_userNotActive(self, user_id):
        lines = list()
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if user_id == row['id']:
                    dick = {"name": row['name'], "id": row['id'], "status": False}
                    lines.append(dick)
                else:
                    dick = {"name": row['name'], "id": row['id'], "status": row['status']}
                    lines.append(dick)
            file.close()

        with open(self.filename, 'w') as file:
            columns = ["name", "id", "status"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for row in lines:
                user = {"name": row['name'], "id": row['id'], "status": row['status']}
                writer.writerow(user)
            file.close()
