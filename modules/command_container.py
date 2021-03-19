from modules.command_list import command_list

class CommandContainer:
    def __init__(self, command, inputs):
        self.cmd = command
        self.inp = inputs
    
    def run(self):
        func = command_list()
        run_command = getattr(func, self.cmd)
        return run_command(self.inp)

def command_container(*kwargs):
    return CommandContainer(*kwargs)