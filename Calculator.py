


class Calc:
    add = ['plus','add']
    sub = ['minus','subtract']
    div = ['divide', 'divided by','over']
    mult = ['times', 'multiply','multiplied by']
    pow = ['to the power of', 'raised to', 'raised to the power of']
    
    all = add+sub+div+mult+pow

    
    def __fadd(x,y):
        return x+y
    
    def __fsub(x,y):
        return x-y
    def __fdiv(x,y):
        return x/y
    def __fmult(x,y):
        return x*y
    def __fpow(x,y):
        return x**y

    converterTextFunc = {'add': __fadd, 'sub': __fsub, 'div': __fdiv, 'mult': __fmult, 'pow': __fpow}
    converterTextList = {'add': add, 'sub': sub, 'div': div, 'mult': mult, 'pow':pow}
    

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
        op = ''

        cmd = cmd.lower()
        #check if any operation keywords are in sentence
        contain = False
        for item in self.all:
            if item in cmd:
                contain=True
                #there probably is an easier way to determine what operation it is...
                if item in self.add:
                    op = 'add'
                elif item in self.sub:
                    op = 'sub'
                elif item in self.div:
                    op = 'div'
                elif item in self.mult:
                    op = 'mult'
                elif item in self.pow:
                    op = 'pow'
                break

        #if it cant find any then exit
        if not contain:
            return "Error: Calculator Could Not Understand"
        #remove starter words
        if (cmd.startswith('what is') or cmd.startswith('what\'s')):
            cmd = cmd[cmd.find('s')+2:] # remove up to s and one more for the space after the word


        
        for item in self.converterTextList[op]:
            if item in cmd:
                cmd = cmd.split(item)
                break
        return str(self.converterTextFunc[op](float(cmd[0]),float(cmd[1])))

        # #addition NOW OUTDATED BECAUSE I FOUND A WAY TO DO ALL OPERATIONS INSTEAD OF EACH INDIVIDUALLY
        # for item in self.add:
        #     if item in cmd:
        #         #slice before the keyword and after to get numbers
        #         cmd = cmd.split(item)
        #         break
        # return (str(float(cmd[0])+float(cmd[1])))







calc = Calc()
print(calc.fromString("What is 3 TO THE POWER OF 3.9"))