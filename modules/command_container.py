from modules.command_list import command_list

class CommandContainer:
    def __init__(self, command, inputs, discord_client):
        self.cmd = command
        self.inp = inputs
        self.client = discord_client
    
    def run(self):
        func = command_list(input_message = self.inp, client = self.client)
        run_command = getattr(func, self.cmd)
        return run_command()

def command_container(*args):
    return CommandContainer(*args)