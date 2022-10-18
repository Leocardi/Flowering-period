import os
import pyecharts.options as opts
from pyecharts.charts import Bar
import os.path
import xml.dom.minidom
import xml.etree.cElementTree as et
from scipy.ndimage import measurements


path = "C:/Users/liuli/Desktop/YOLOv5/yolov5-master/Annotations"
files = os.listdir(path)
s = []

square_list = []
side_list = []


# =============================================================================
# extensional filename
# =============================================================================
def file_extension(path):
    return os.path.splitext(path)[1]


for xmlFile in files:
    if not os.path.isdir(xmlFile):
        if file_extension(xmlFile) == '.xml':
            print(os.path.join(path, xmlFile))
            tree = et.parse(os.path.join(path, xmlFile))
            root = tree.getroot()
            filename = root.find('filename').text
            #            print("filename is", path + '/' + xmlFile)
            for Object in root.findall('object'):
                #                name=Object.find('name').text
                #                print("Object name is ", name)
                bndbox = Object.find('bndbox')
                xmin = bndbox.find('xmin').text
                ymin = bndbox.find('ymin').text
                xmax = bndbox.find('xmax').text
                ymax = bndbox.find('ymax').text
                square = (int(ymax) - int(ymin)) * (int(xmax) - int(xmin))
                square_list.append(square)
                #                print(xmin,ymin,xmax,ymax)
                print(square)

# print("square is ", square_list)

# =============================================================================
# 画出直方图
# =============================================================================
num = 1000  # 最大面积
histogram1 = measurements.histogram(square_list, 1, num, 100)  # 直方图
histogram1 = list(map(int, histogram1))  # 转换成 int 格式
print("histogram is ", histogram1)
x_vals = [str(num / 100), str(num / 100 * 2), str(num / 100 * 3), str(num / 100 * 4), str(num / 100 * 5), str(num / 100 * 6), str(num / 100 * 7), str(num / 100 * 8), str(num / 100 * 9), str(num / 100 * 10),
         str(num / 100 * 11), str(num / 100 * 12), str(num / 100 * 13), str(num / 100 * 14), str(num / 100 * 15), str(num / 100 * 16), str(num / 100 * 17), str(num / 100 * 18), str(num / 100 * 19), str(num / 100 * 20),
         str(num / 100 * 21), str(num / 100 * 22), str(num / 100 * 23), str(num / 100 * 24), str(num / 100 * 25), str(num / 100 * 26), str(num / 100 * 27), str(num / 100 * 28), str(num / 100 * 29), str(num / 100 * 30),
         str(num / 100 * 31), str(num / 100 * 32), str(num / 100 * 33), str(num / 100 * 34), str(num / 100 * 35), str(num / 100 * 36), str(num / 100 * 37), str(num / 100 * 38), str(num / 100 * 39), str(num / 100 * 40),
         str(num / 100 * 41), str(num / 100 * 42), str(num / 100 * 43), str(num / 100 * 44), str(num / 100 * 45), str(num / 100 * 46), str(num / 100 * 47), str(num / 100 * 48), str(num / 100 * 49), str(num / 100 * 50),
         str(num / 100 * 51), str(num / 100 * 52), str(num / 100 * 53), str(num / 100 * 54), str(num / 100 * 55), str(num / 100 * 56), str(num / 100 * 57), str(num / 100 * 58), str(num / 100 * 59), str(num / 100 * 60),
         str(num / 100 * 61), str(num / 100 * 62), str(num / 100 * 63), str(num / 100 * 64), str(num / 100 * 65), str(num / 100 * 66), str(num / 100 * 67), str(num / 100 * 68), str(num / 100 * 69), str(num / 100 * 70),
         str(num / 100 * 71), str(num / 100 * 72), str(num / 100 * 73), str(num / 100 * 74), str(num / 100 * 75), str(num / 100 * 76), str(num / 100 * 77), str(num / 100 * 78), str(num / 100 * 79), str(num / 100 * 80),
         str(num / 100 * 81), str(num / 100 * 82), str(num / 100 * 83), str(num / 100 * 84), str(num / 100 * 85), str(num / 100 * 86), str(num / 100 * 87), str(num / 100 * 88), str(num / 100 * 89), str(num / 100 * 90),
         str(num / 100 * 91), str(num / 100 * 92), str(num / 100 * 93), str(num / 100 * 94), str(num / 100 * 95), str(num / 100 * 96), str(num / 100 * 97), str(num / 100 * 98), str(num / 100 * 99), str(num / 100 * 100)]
bar = (
    Bar()
    .add_xaxis(x_vals)
    .add_yaxis('',histogram1)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False, font_size=24),
                         )
    .set_global_opts(title_opts=opts.TitleOpts(title='标注目标尺寸分布', pos_left = '45%',),
                         xaxis_opts=opts.AxisOpts(name='所占像素面积'),
                         yaxis_opts=opts.AxisOpts(name='数量'))
)
bar.render('柱状图.html')


# bar = Bar("目标面积直方图")
# bar = Bar("标注目标尺寸分布" , title_pos="center")
# bar.use_theme("light")
# bar.add("数目",
#         [str(num / 100), str(num / 100 * 2), str(num / 100 * 3), str(num / 100 * 4), str(num / 100 * 5), str(num / 100 * 6), str(num / 100 * 7), str(num / 100 * 8), str(num / 100 * 9), str(num / 100 * 10),
#          str(num / 100 * 11), str(num / 100 * 12), str(num / 100 * 13), str(num / 100 * 14), str(num / 100 * 15), str(num / 100 * 16), str(num / 100 * 17), str(num / 100 * 18), str(num / 100 * 19), str(num / 100 * 20),
#          str(num / 100 * 21), str(num / 100 * 22), str(num / 100 * 23), str(num / 100 * 24), str(num / 100 * 25), str(num / 100 * 26), str(num / 100 * 27), str(num / 100 * 28), str(num / 100 * 29), str(num / 100 * 30),
#          str(num / 100 * 31), str(num / 100 * 32), str(num / 100 * 33), str(num / 100 * 34), str(num / 100 * 35), str(num / 100 * 36), str(num / 100 * 37), str(num / 100 * 38), str(num / 100 * 39), str(num / 100 * 40),
#          str(num / 100 * 41), str(num / 100 * 42), str(num / 100 * 43), str(num / 100 * 44), str(num / 100 * 45), str(num / 100 * 46), str(num / 100 * 47), str(num / 100 * 48), str(num / 100 * 49), str(num / 100 * 50),
#          str(num / 100 * 51), str(num / 100 * 52), str(num / 100 * 53), str(num / 100 * 54), str(num / 100 * 55), str(num / 100 * 56), str(num / 100 * 57), str(num / 100 * 58), str(num / 100 * 59), str(num / 100 * 60),
#          str(num / 100 * 61), str(num / 100 * 62), str(num / 100 * 63), str(num / 100 * 64), str(num / 100 * 65), str(num / 100 * 66), str(num / 100 * 67), str(num / 100 * 68), str(num / 100 * 69), str(num / 100 * 70),
#          str(num / 100 * 71), str(num / 100 * 72), str(num / 100 * 73), str(num / 100 * 74), str(num / 100 * 75), str(num / 100 * 76), str(num / 100 * 77), str(num / 100 * 78), str(num / 100 * 79), str(num / 100 * 80),
#          str(num / 100 * 81), str(num / 100 * 82), str(num / 100 * 83), str(num / 100 * 84), str(num / 100 * 85), str(num / 100 * 86), str(num / 100 * 87), str(num / 100 * 88), str(num / 100 * 89), str(num / 100 * 90),
#          str(num / 100 * 91), str(num / 100 * 92), str(num / 100 * 93), str(num / 100 * 94), str(num / 100 * 95), str(num / 100 * 96), str(num / 100 * 97), str(num / 100 * 98), str(num / 100 * 99), str(num / 100 * 100),],
#         histogram1, is_more_utils=True)
# bar.render(r"C:/Users/liuli/Desktop/YOLOv5/yolov5-master/Annotations/second_chart.html")  # generate HTML file
