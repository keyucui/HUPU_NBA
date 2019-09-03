#encoding=utf-8

from PIL import Image
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba as jb
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

def simpleWordCloud(text="好"):
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    mask = np.array(Image.open("lebron.jpg"))
    wcd = WordCloud(background_color=None, repeat=True, max_words=500, height=480, width=854,
                    max_font_size=100, colormap="Reds", mask=mask, mode="RGBA")
    text = "我是真的喜欢你啊，喜欢"
    ss = " ".join(jb.lcut(text))
    wcd.generate(ss)
    wcd.to_image()
    wcd.to_file("hupu1.png")

if __name__=='__main__':
    simpleWordCloud()
    # plt.plot([1,2], [3,4])
    # plt.title('我爱你')
    # plt.show()
