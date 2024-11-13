# oopexamples.py

# Composition Example
class Mouth():

    def __init__(self, say=''):
        self.say = say
        
    def talk(self):
        return self.say
        
class Desk():

    def __init__(self, mouth=None):
        self.mouth = mouth
        
    def talk(self):
        if isinstance(self.mouth, Mouth): # This object must be of type Mouth
            return self.mouth.talk()
        else:
            return ''
        
        
if __name__ == '__main__':

    desk_mouth = Mouth('thud')
    my_desk = Desk(desk_mouth)
    print(my_desk.talk()) # outputs 'thud'
