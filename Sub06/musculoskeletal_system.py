class MusculoskeletalSystem:
  # Constructor
  def __init__(self, bones: int, skeletal_muscles: int):
    self.bones = bones
    self.skeletal_muscles = skeletal_muscles

    
    def check_move(self):
      if (self.bones >= 206 and self.skeletal_muscles >= 600):
        self.move = True
      else:
        self.move = False
      return self.move
