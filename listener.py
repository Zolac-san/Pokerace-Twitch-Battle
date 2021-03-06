class Listener(object):
    callbacks = {}

    def on(self, event_name, callback):
        

        if event_name not in self.callbacks:
            self.callbacks[event_name] = [callback]
        else:
            self.callbacks[event_name].append(callback)

    def trigger(self, event_name, args = ()):
        #args = (self,*args)
        if self.callbacks is not None and event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback(*args)