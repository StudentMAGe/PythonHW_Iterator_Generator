class IteratorEnhancedRange:
    
    def __init__(self, *args):
    #Arguments are: start (default = 0), end (no default, required argument), step (default = 1)
        self.args = args
        for arg in args:
            if not (type(arg) == int or type(arg) == float):
                raise Exception("Arguments must be numeric")
        if len(args) == 1:
            self.start = 0
            self.end = self.args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = 1
        elif len (args) == 3:
            if self.args[2] == 0:
                raise Exception("Unable to range with step = 0")
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]
        else:
            raise Exception("IteratorEnhancedRange requires at least one, but no more than three arguments")
        self.startediter = False

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step/abs(self.step))*self.start >= (self.step/abs(self.step))*self.end:
            raise StopIteration
        else:
            if self.startediter is False:
                self.startediter = True
                return self.start
            else:
                if (self.step/abs(self.step))*(self.start + self.step) >= (self.step/abs(self.step))*self.end:
                    raise StopIteration
                else:
                    self.start += self.step
                    return self.start

    def __call__(self):
        return self


class GeneratorEnhancedRange:
    
    def __init__(self, *args):
    #Arguments are: start (default = 0), end (no default, required argument), step (default = 1)
        self.args = args
        for arg in args:
            if not (type(arg) == int or type(arg) == float):
                raise Exception("Arguments must be numeric")
        if len(args) == 1:
            self.start = 0
            self.end = self.args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = 1
        elif len (args) == 3:
            if self.args[2] == 0:
                raise Exception("Unable to range with step = 0")
            self.start = self.args[0]
            self.end = self.args[1]
            self.step = self.args[2]
        else:
            raise Exception("GeneratorEnhancedRange requires at least one, but no more than three arguments")
        self.startediter = False

    def __iter__(self):
        return GeneratorEnhancedRange.gener(self)

    def gener(self):
        if (self.step/abs(self.step))*self.start < (self.step/abs(self.step))*self.end:
            if self.startediter is False:
                self.startediter = True
                yield self.start
            else:
                while (self.step/abs(self.step))*(self.start + self.step) < (self.step/abs(self.step))*self.end:
                    self.start += self.step
                    yield self.start

    def __call__(self):
        return self


