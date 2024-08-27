import cv2
import numpy as np
import random

# 定义图片大小
image_size = (768, 1024)

# 定义颜色范围 (B, G, R)
color_range = [(0, 0, 255)]  # 蓝色, 绿色, 红色
background_range = [(255, 255, 255)]  # 浅灰, 白色, 深灰
bud_color = (0, 0, 255)  # 芽点的颜色（棕色）


# 生成 10 张图片
for i in range(10):
    # 随机选择背景颜色
    background_color = random.choice(background_range)
    
    # 创建一个填充背景色的图像
    image = np.full((image_size[0], image_size[1], 3), background_color, dtype=np.uint8)

    # 随机生成 6 到 10 个矩形
    num_rectangles = random.randint(6, 10)
    
    for _ in range(num_rectangles):
        # 随机选择矩形颜色
        color = random.choice(color_range)
        
        # 设置长宽比为 20:1
        width = min(random.randint(10, image_size[0] // 5), 50)  # 宽度范围
        height = width // 12  # 高度根据长宽比计算

        # 确保宽度和高度大于 0
        if width <= 0 or height <= 0:
            continue
        
        # 随机生成矩形的顶点坐标
        x = random.randint(0, image_size[1] - width)
        y = random.randint(0, image_size[0] - height)
        angle = random.randint(0, 360)

        # 创建旋转矩形
        rect = ((x + width // 2, y + height // 2), (width, height), angle)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        
        # 在图像上绘制旋转后的矩形
        cv2.drawContours(image, [box], 0, color, thickness=-1)  # thickness=-1 填充矩形

               # 在茎的左右两侧添加芽点（小圆圈）
        for side in range(2):  # 0 表示左侧, 1 表示右侧
            num_buds = random.randint(1, 2)
            for _ in range(num_buds):
                max_radius = max(height // 2,5)  # 芽点最大半径不超过茎的高度的一半
                radius = random.randint(max(2, max_radius // 2), max_radius)
                
                # 计算芽点中心点，确保芽点贴在茎的边缘
                offsetX = random.randint(-max_radius, width-max_radius)
                offsetY = random.randint(0, max_radius)
                
                # 计算芽点的中心位置
                dx = int(np.cos(np.radians(angle)) * offsetX + np.sin(np.radians(angle)) * offsetY)
                dy = int(np.sin(np.radians(angle)) * offsetX + np.cos(np.radians(angle)) * offsetY)
                
                bud_center = (int(rect[0][0] - dx), int(rect[0][1] + dy))
                
                # 绘制连接到茎上的芽点
                cv2.circle(image, bud_center, radius, bud_color, thickness=-1)


    # 保存图像到文件
    filename = f'samples/rectangle_image_{i+1}.png'
    cv2.imwrite(filename, image)

    print(f'Saved: {filename}')