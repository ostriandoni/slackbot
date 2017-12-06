import csv

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

    def leaderboard(self):
        data = []
        with open('score.csv','r') as input_file:
            reader = csv.reader(input_file)
            reader.next() # skip header

            for line in reader:
                data.append(tuple(line))

        data = sorted(data, key=lambda tup: int(tup[1]), reverse=True)[:10]

        with open('top10.csv','w') as output_file:
            csv.writer(output_file).writerows(data)

        f = open('top10.csv','r')
        message = f.read()
        f.close()

        return "Top 10 Leaderboard:\n" + message
