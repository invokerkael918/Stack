class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minstack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.stack.append(number)
        if len(self.minstack) == 0:
            self.minstack.append(number)
        else:
            self.minstack.append(min(number, self.minstack[-1]))

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        ret = self.stack[-1]
        del (self.stack[-1], self.minstack[-1])
        return ret

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.minstack[-1]
