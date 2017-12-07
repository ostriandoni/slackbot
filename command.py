import csv
import pandas as pd

class Command(object):
    def __init__(self):
        self.commands = { 
            "jump" : self.jump,
            "help" : self.help,
            "leaderboard" : self.leaderboard
        }

    def handle_command(self, user, command):
        response = "<@" + user + ">: "

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()

        return response

    def jump(self):
        return "Kris Kross will make you jump jump"

    def help(self):
        response = "Currently I support the following commands:\r\n"

        for command in self.commands:
            response += command + "\r\n"

        return response

    def get_user_data(self, exclude_first_col):
        data = []
        with open('user.csv','r') as input_file:
            reader = csv.reader(input_file)
            reader.next() # skip header

            if exclude_first_col:
                user_data = [el[1:] for el in map(tuple, reader)]
            else:
                user_data = [el for el in map(tuple, reader)]

        if exclude_first_col:
            return sorted(user_data, key=lambda tup: int(tup[1]), reverse=True)[:10] # get top 10 karma points
        else:
            return sorted(user_data, key=lambda tup: int(tup[2]), reverse=True)

    def leaderboard(self):
        with open('top10.csv','w') as output_file:
            csv.writer(output_file).writerows(self.get_user_data(True)) # create view of top 10 karma points

        f = open('top10.csv','r')
        message = f.read()
        f.close()

        return "Top 10 Leaderboard:\n" + message

    def get_karma_by_user_id(self, user):
        item = [item for item in self.get_user_data(False) if item[0] == user]

        if item:
            return item[0][2]
        else:
            return "There is no user with ID " + user

    def get_user_name_by_user_id(self, user):
        item = [item for item in self.get_user_data(False) if item[0] == user]

        if item:
            return item[0][1]
        else:
            return "There is no user with ID " + user

    def update_karma(self, user, karma):
        df = pd.read_csv("user.csv")
        df.loc[df["uid"] == user, "score"] = karma
        df.to_csv("user.csv", index=False)

