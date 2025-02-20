import pandas as pd #加载pandas库，读取并处理数据
import marsilea as ma #加载Marsilea库
import matplotlib #加载matplotlib库用于设置热图渐变色
mat=pd.read_csv("matrix.CSV",index_col=0)
don=pd.read_csv("DON.CSV")
don=don.T
colors = ["#3CB371","white", "#1E90FF"] #设置颜色范围
h=ma.Heatmap(mat, #矩阵数据
             linewidth=1, #热图每个元素边框宽度
             ##自定义设置热图渐变色
             cmap=matplotlib.colors.LinearSegmentedColormap.from_list("my_cmap", colors),
             width=5,
             height=9) ##确定热图的长宽
h.add_right(ma.plotter.Numbers(don[0], color="#F05454")) #给热图右边添加柱状图
h.add_left(ma.plotter.Labels(don.index)) #给热图左边添加标签
##遍历mat的每一行，给热图上部添加折线
for i in range(len(mat)):
    h.add_top(ma.plotter.Point(mat.iloc[i],label=mat.index[i],color="black"))
h.add_legends() ###添加图注
h.render() #展示热图
h.save("matrix.pdf") #保存图片