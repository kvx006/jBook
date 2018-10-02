# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'/home/tsuki/Downloads/ipagp.ttf', size=14)

plt.bar([1, 2], [5, 10], 0.25)
plt.bar([1.25, 2.25], [4, 8], 0.25, color='darkorange')
plt.xlim((0.75, 2.75))
plt.ylim((0, 12))
plt.ylabel(u'軸ラベルはfontproperties=fp', fontproperties=fp)
plt.xticks([1.25, 2.25], [u'目盛りは', 'fontproperties=fp'], fontproperties=fp)
plt.title(u'タイトルはfontproperties=fp', fontproperties=fp)
plt.text(2.125, 10, u'テキストは\nfontproperties=fp', fontproperties=fp,
         ha='center')
plt.annotate(u'アノテーションは\nfontproperties=fp', xy=(1.125, 5), xytext=(1.3, 8),
             fontproperties=fp, arrowprops=dict(facecolor='k', shrink=0.05))
plt.legend([u'凡例は', 'prop=fp'], prop=fp, loc='upper left')
# plt.show()
plt.savefig('fontproperties.png', bbox_inches='tight')
plt.close()
