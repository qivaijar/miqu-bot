# import required libraries
import yaml

# read text list yaml
with open('text_list.yaml', 'r') as f:
    text_list = yaml.load(f, Loader=yaml.FullLoader)

class CommandList:

    def __init__(self, input_message, client):
        self.inp = input_message
        self.client = client

    def mqhelp(*args):
        command_string = "message.channel.send(\"" + text_list['mqhelp_strings'][0] + "\")"
        return command_string
    
    def mqpl(self):
        print(self.client)
        print(self.inp)
        return 0 


def command_list(input_message, client):
    return CommandList(input_message, client)

