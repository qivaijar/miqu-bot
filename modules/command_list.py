# use yaml to load all the required strings to be sent
import yaml

# read text list yaml
with open('text_list.yaml', 'r') as f:
    text_list = yaml.load(f, Loader=yaml.FullLoader)

class CommandList:

    def mqhelp(*args):
        command_string = "message.channel.send(\"" + text_list['mqhelp_strings'][0] + "\")"
        return command_string

def command_list(*kwargs):
    return CommandList(*kwargs)