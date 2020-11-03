import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    contents = []

    for color, amount in kwargs.items():
      for i in range(amount):
        contents.append(color)
    
    self.contents = contents

  def draw(self, n_balls):
    if len(self.contents) >= n_balls:
      balls = random.sample(self.contents, n_balls)
      [self.contents.remove(ball) for ball in balls]
      return balls
    else:
      return self.contents
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0

  for i in range(num_experiments): 
    initial_contents = copy.copy(hat.contents)

    draw = hat.draw(num_balls_drawn)
    hat.contents = initial_contents

    draw_count = {}
    for ball in draw:
      if ball not in draw_count:
        draw_count[ball] = 1
      else:
        draw_count[ball] += 1

    sample_vs_expected = []
    for ball in expected_balls:
      if draw_count.get(ball, 0) >= expected_balls[ball]:
        sample_vs_expected.append(True)
      else:
        sample_vs_expected.append(False)
    
    if all(sample_vs_expected):
      success += 1
    
    
    
  probability = success / num_experiments
  return probability


