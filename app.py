class App:
    def __getattr__(self, name):
        if str(name) not in self.__dict__:
            print('[*]auto import app.' + name)
            self.__dict__[name] = __import__(name)
            self.__dict__[name].app = self
            return self.__dict__[name]

app = App()
app.core.run()
