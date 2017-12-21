import command
import csv

class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()

        if events and len(events) > 0:
            for event in events:
                print (event)

                if ('channel' in event and 'text' in event and event.get('type') == 'message'):
                    channel = event['channel']
                    text = event['text']
                    from_user = event['user']
                    link = 'Haydar receives 1 point from Jeff. He now has 10 points.'

                    if 'thanks <@' in text.lower() and link not in text: # if say thanks and mention some user
                        mentioned_user = text.split('@', 1)[-1].replace('>', '')
                        mentioned_user = mentioned_user[0:9]
                        status = self.command.is_available(from_user)

                        if status:
                            points = int(self.command.get_karma_by_user_id(mentioned_user, False)) + 1
                            self.command.update_karma_points(mentioned_user, points)
                            self.command.update_karma_remaining(from_user)
                            reply = self.command.get_user_name_by_user_id(mentioned_user) + ' receives 1 point from ' + self.command.get_user_name_by_user_id(from_user) + '. He now has ' + str(points) + ' points.'
                        else:
                            reply = 'Sorry, there is nothing left karma to give'

                        self.bot.slack_client.api_call('chat.postMessage', channel=channel, text=reply, as_user=True)
                    elif 'karma' in text.lower() and channel.startswith('D') and 'bot_id' not in event: # if say karma in direct message
                        print ("Received message: " + text + " in channel: " + channel + " from user: " + from_user)
                        response = self.command.get_karma_by_user_id(from_user, True)
                        self.bot.slack_client.api_call("chat.postMessage", channel=channel, text='Your karma is equal to ' + response, as_user=True)
                    else:
                        self.parse_event(event)

    def parse_event(self, event):
        if event and 'text' in event and self.bot.bot_id in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])

    def handle_event(self, user, command, channel):
        if command and channel:
            print ("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handle_command(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
