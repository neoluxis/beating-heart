import numpy as np

canvas_width = 600
canvas_height = 600
world_width = 0.05
world_heigth = 0.05

# 中间心的参数
points = None
fixed_point_size = 20000
fixed_scale_range = (4, 4.3)
min_scale = np.array([1.0, 1.0, 1.0]) * 0.9
max_scale = np.array([1.0, 1.0, 1.0]) * 0.9
min_heart_scale = -15
max_heart_scale = 16

# 外围随机心参数
random_point_szie = 7000
random_scale_range = (3.5, 3.9)
random_point_maxvar = 0.2

# 心算法参数
mid_point_ignore = 0.93

# 相机参数
camera_close_plane = 0.1
camera_position = np.array([0.0, -2.0, 0.0])

# 点的颜色
hue = 0.92
color_strength = 255

# 常用向量缓存
zero_scale = np.array([0.0, 0.0, 0.0])
unit_scale = np.array([1.0, 1.0, 1.0])
color_white = np.array([255, 255, 255])
axis_y = np.array([0.0, 1.0, 0.0])

# 渲染缓存
render_buffer = np.empty((canvas_width, canvas_height, 3), dtype=int)
strength_buffer = np.empty((canvas_width, canvas_height), dtype=float)

# 随机点文件缓存
points_file = "./cache/temp.txt"

# 渲染结果
total_frames = 30
output_dir = "./cache/frames"

# 格式
image_fmt = "jpg"
