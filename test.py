import cv2
import numpy as np
import random

canvasWidth, canvasHeight = 2048, 1536
for j in range(10):
    image = np.full((canvasHeight, canvasWidth, 3),(255,255,255), dtype=np.uint8)
    for i in range(20):
        angel = random.randint(-180,180)
        width = random.randint(60,140)
        height = width // 12
        rectCenter = (random.randint(width,canvasWidth-width), random.randint(height,canvasHeight-height))
        cv2.rectangle(image,(rectCenter[0] - int(width/2),rectCenter[1] - int(height/2)),(rectCenter[0]+ int(width/2),rectCenter[1] + int(height/2)),(0,255,0),-1)
        for _ in random.choice([[1], [1, 2]]):
            bud_radius= random.randint(int(height*0.5),int(height*0.8))
            bud_y = rectCenter[1]+random.randint(0,int(height/2))
            if(_%2==0):
                bud_y = rectCenter[1]-random.randint(0,int(height/2))
            cv2.circle(image, (rectCenter[0] + random.randint(int(-width/2), int(width/2)) ,bud_y),bud_radius, (0,200,0), thickness=-1)
        rot_mat = cv2.getRotationMatrix2D((int(canvasWidth/2),int(canvasHeight/2)), angel, 1)
        image = cv2.warpAffine(image, rot_mat, image.shape[1::-1], borderValue=(255,255,255),flags=cv2.INTER_LANCZOS4)

    filename = f'samples/plant_tissue_simulation_{1+j}.png'
    cv2.imwrite(filename, image)
    print(f'Saved: {filename}')