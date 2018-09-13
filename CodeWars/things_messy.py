class Thing(object):
    def __init__(self, name, plural = False):
        self.name = name[:-1 if plural else None]
        if 'desc' not in dir(self):
            self.desc = {'is_'+name.lower()[:-1 if plural else None]:True}
        self.is_a = IsA(self, True)
        self.is_not_a = IsA(self, False)
        self.is_the = IsThe(self)
        self.being_the = IsThe(self)
        self.has = lambda num: HasSome(self, num)
        self.having = self.has
        self.can = Can(self)
    
    def __getattr__(self, attr):
        name = self.name
        if attr in self.desc:
            return self.desc[attr]
        else:
            print('undefined')
            
class IsA(Thing):
    def __init__(self, parent, boo):
        self.thing = parent
        self.boo = boo
    
    def __getattr__(self, method):
        self.thing.desc ={**self.thing.desc, 'is_a_'+method:self.boo}

class IsThe(Thing):
    def __init__(self, parent):
        self.thing = parent
        self.is_the_desc = {}
    
    def __getattr__(self, method): #method = parent_of.joe
        return ThingOf(self.thing, method)
        
class ThingOf(object):
    def __init__(self, parent, method_name):
         self.thing_of_desc = {'thing':parent,'name':method_name}
    def __getattr__(self, relative):
        if relative in self.thing_of_desc:
            return self.thing_of_desc[relative]
        print('calling ThingOf\'s getattr on',relative)
        self.thing.desc = {**self.thing.desc, self.name:relative}
        
class HasSome(object):
    def __init__(self, thing, num):
        self.num = num
        self.thing = thing
        
    def __getattr__(self, method):
        item = tuple((Thing(method, True) for i in range(self.num))) if self.num>1 else Thing(method)
        tuple_thing = type('tuple_Thing', (tuple,), {'having':self.thing.has, 'each':Each(item)})
        if isinstance(item,tuple): item = tuple_thing(item)
        self.thing.desc = {**self.thing.desc, method: item}
        return item

class Each(Thing):
    def __init__(self, things):
        self.things = things
        self.being_the = EachBeing(self.things)
        self.and_the = self.being_the
    
    def having(self, num):
        return EachHaving(num, self.things)
        
    
class EachBeing(Thing):
    def __init__(self, things):
        self.things = things
        
    def __getattr__(self, attribute):
        return EachBeingAttr(self.things, attribute)

class EachBeingAttr:
    def __init__(self, things, attr):
        self.things = things
        self.attr = attr
    
    def __getattr__(self, value):
        for thing in self.things:
            thing.desc = {**thing.desc, self.attr: value}
        return Each(self.things)
    
class EachHaving(Thing):
    def __init__(self, num, things):
        self.things = things
        self.num = num
        
    def __getattr__(self, method):
        for thing in self.things:
            thing.has(self.num).__getattr__(method)
            tuple_thing = type('tuple_Thing', (tuple,), {'each':Each(tuple(thing.__getattr__(method) for thing in self.things))})
        return tuple_thing().each
        
class Can(Thing):
    def __init__(self, thing):
        self.thing = thing
    
    def can_do(self, method, past=''):
        #.can.verb(method, past='')
        #decorate method so it repeats when called on empty
        def decorator(func):
            def decorated(*args, **kwargs):
                func.__globals__['name'] = self.thing.name
                if past:
                    if past in self.thing.desc:
                        self.thing.desc[past].append(func(*args, **kwargs))
                    else:
                        self.thing.desc = {**self.thing.desc, past: [func(*args, **kwargs)]}
                return func(*args, **kwargs)
            return decorated 
    
        self.thing.desc = {**self.thing.desc, self.verb: decorator(method)}
        
    def __getattr__(self, verb):  
        self.verb = verb
        return self.can_do
    
