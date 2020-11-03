# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

hat1 = prob_calculator.Hat(yellow=3, blue=2, green=6)

print(hat1.contents)
print(hat1.draw(5))

hat = prob_calculator.Hat(blue=3,red=2,green=6)
probability = prob_calculator.experiment(hat=hat, 
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=2000)
print(probability)
# Run unit tests automatically
main(module='test_module', exit=False)

