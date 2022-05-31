from operator import contains


class Calc:
    add = ['plus','add']
    sub = ['minus','subtract']
    div = ['divide', 'divided by','over']
    mult = ['times', 'multiply','multiplied by']
    pow = ['to the power of']
    all = add+sub+div+mult+pow

    """
    Tim's current approach:
    just handle basic operations
    only handles 2 numbers
    eg. 5 times 2
    cannot handle 5 times 2 times 1


    side notes:
        if I want to do a full implementation of longer calculations the current approach wont work...
        eg. 5 + 3 * 2 - 10
        I would probably need a priority queue to handle bedmas?
        and probably some data structure to represent expressions...
    """
    def fromString(self, cmd):

        cmd = cmd.lower()
        #check if any operation keywords are in sentence
        contain = False
        for item in self.all:
            if item in cmd:
                contain=True
                break
        #if it cant find any then exit
        if not contain:
            return "Error: Calculator Could Not Understand"
        #remove starter words
        if (cmd.startswith('what is') or cmd.startswith('what\'s')):
            cmd = cmd[cmd.find('s')+2:] # remove up to s and one more for the space after the word
            print(cmd)

        for item in self.add:
            if item in cmd:
                #slice before the keyword and after to get numbers
                return






calc = Calc()
print(calc.fromString("What is 3 plus 3"))