# oop_inheritance.py
# An example of basic inheritance

class SwimmingRock():
    ...  # stuff from earlier

# This type of object can inherit all properties and abilities of SwimmingRock!
class TalkingSwimmingRock(SwimmingRock):

    # However, you must call the __init__ method of the parent class.
    def __init__(self):
        super().__init__()
