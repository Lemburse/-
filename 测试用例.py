from predeal import predeal
import os
predeal = predeal()
for filename in os.listdir('G:\gpu-train-hongtou\\test'):
    #i = random.randint(0,3)

    path = os.path.join('G:\gpu-train-hongtou\\test',filename)
    predeal.addNoise(path,'gaussian')
    predeal.color2black(path)

    predeal.rotate(path,90)
