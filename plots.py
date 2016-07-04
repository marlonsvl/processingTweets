import matplotlib.pyplot as plt


# data
tags = ('elnino','emergencia','fenómeno','alerta','fenómenoelnino','fenómenodeelnino',
	'fenómenodelnino','fenómeno El Nino','fenómeno del Nino','emergency')
y_pos = (628,2051,68221,901,255,15,145,40981,26924,0)
performance = 3 + 10 * np.random.rand(len(tags))
error = np.random.rand(len(tags))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, tags)
plt.xlabel('Tags')
plt.title('Frequency of each tag')

plt.show()
