import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

values_10dc=[(0, 6962.790697674419), (500, 7086.677908937606), (1000, 6922.314049586776), (1500, 6976.372712146422), (2000, 7058.823529411764), (2500, 6922.314049586776), (3000, 7142.954159592529), (3500, 6908.910891089108), (4000, 7142.954159592529), (4500, 7031.155778894472), (5000, 7114.720812182741), (5500, 7142.954159592529), (6000, 7003.672787979967), (6500, 6895.551894563426), (7000, 6949.253731343283), (7500, 7100.675675675676), (8000, 6908.910891089108), (8500, 7058.823529411764), (9000, 7044.96644295302), (9500, 6882.236842105263), (10000, 6855.737704918033), (10500, 7142.954159592529), (11000, 7086.677908937606), (11500, 7100.675675675676), (12000, 7017.391304347826), (12500, 6922.314049586776), (13000, 7017.391304347826), (13500, 7044.96644295302), (14000, 6868.96551724138), (14500, 6868.96551724138), (15000, 7031.155778894472), (15500, 6922.314049586776), (16000, 6842.553191489362), (16500, 7086.677908937606), (17000, 6976.372712146422), (17500, 6989.999999999999), (18000, 6829.411764705882), (18500, 6949.253731343283), (19000, 7044.96644295302), (19500, 7031.155778894472), (20000, 6935.761589403974), (20500, 7003.672787979967), (21000, 6962.790697674419), (21500, 6764.343598055106), (22000, 6803.257328990228), (22500, 7003.672787979967), (23000, 6790.243902439024), (23500, 6908.910891089108), (24000, 7017.391304347826), (24500, 6962.790697674419), (25000, 6829.411764705882), (25500, 6764.343598055106), (26000, 6976.372712146422), (26500, 6976.372712146422), (27000, 6738.610662358644), (27500, 6803.257328990228), (28000, 7058.823529411764), (28500, 7031.155778894472), (29000, 6908.910891089108), (29500, 6908.910891089108), (30000, 7031.155778894472), (30500, 6764.343598055106), (31000, 6777.272727272727), (31500, 6751.456310679611), (32000, 6700.32154340836), (32500, 6935.761589403974), (33000, 6949.253731343283), (33500, 6842.553191489362), (34000, 6949.253731343283), (34500, 6962.790697674419), (35000, 6777.272727272727), (35500, 6842.553191489362), (36000, 6935.761589403974), (36500, 6829.411764705882), (37000, 6751.456310679611), (37500, 6989.999999999999), (38000, 6764.343598055106), (38500, 6949.253731343283), (39000, 6725.806451612902), (39500, 6895.551894563426), (40000, 6725.806451612902), (40500, 6751.456310679611), (41000, 6803.257328990228), (41500, 6935.761589403974), (42000, 6976.372712146422), (42500, 6764.343598055106), (43000, 6842.553191489362), (43500, 6908.910891089108), (44000, 6764.343598055106), (44500, 6842.553191489362), (45000, 6725.806451612902), (45500, 6700.32154340836), (46000, 6908.910891089108), (46500, 6675.000000000001), (47000, 6976.372712146422), (47500, 6842.553191489362), (48000, 6675.000000000001), (48500, 6882.236842105263), (49000, 6949.253731343283), (49500, 6713.04347826087)]
values_50dc=[(0, 6624.840764331209), (500, 6816.313213703101), (1000, 6816.313213703101), (1500, 6624.840764331209), (2000, 6855.737704918033), (2500, 6725.806451612902), (3000, 6790.243902439024), (3500, 6713.04347826087), (4000, 6624.840764331209), (4500, 6713.04347826087), (5000, 6725.806451612902), (5500, 6725.806451612902), (6000, 6803.257328990228), (6500, 6514.285714285715), (7000, 6637.32057416268), (7500, 6502.19435736677), (8000, 6502.19435736677), (8500, 6514.285714285715), (9000, 6430.434782608696), (9500, 6675.000000000001), (10000, 6430.434782608696), (10500, 6600.0), (11000, 6587.638668779715), (11500, 6383.333333333332), (12000, 6313.761467889908), (12500, 6466.146645865836), (13000, 6442.301710730948), (13500, 6490.140845070422), (14000, 6502.19435736677), (14500, 6502.19435736677), (15000, 6371.648690292758), (15500, 6290.853658536585), (16000, 6371.648690292758), (16500, 6279.45205479452), (17000, 6200.602409638554), (17500, 6371.648690292758), (18000, 6256.752655538696), (18500, 6156.287425149699), (19000, 6145.291479820629), (19500, 6234.190620272315), (20000, 6279.45205479452), (20500, 6112.5), (21000, 6245.454545454545), (21500, 6047.787610619468), (22000, 6178.378378378379), (22500, 6112.5), (23000, 6090.80118694362), (23500, 6222.960725075528), (24000, 6101.634472511143), (24500, 6256.752655538696), (25000, 6005.278592375367), (25500, 6167.316341829085), (26000, 6167.316341829085), (26500, 6047.787610619468), (27000, 6112.5), (27500, 6167.316341829085), (28000, 6145.291479820629), (28500, 6189.473684210527), (29000, 5963.26530612245), (29500, 6112.5), (30000, 6167.316341829085), (30500, 6123.397913561848), (31000, 6167.316341829085), (31500, 5963.26530612245), (32000, 5942.441860465115), (32500, 5994.729136163982), (33000, 6058.493353028065), (33500, 6090.80118694362), (34000, 5932.075471698114), (34500, 5880.691642651297), (35000, 6047.787610619468), (35500, 5901.156069364162), (36000, 6047.787610619468), (36500, 5963.26530612245), (37000, 6037.113402061856), (37500, 5901.156069364162), (38000, 5880.691642651297), (38500, 5860.344827586207), (39000, 5860.344827586207), (39500, 6005.278592375367), (40000, 6058.493353028065), (40500, 5901.156069364162), (41000, 6037.113402061856), (41500, 6026.470588235294), (42000, 5942.441860465115), (42500, 5880.691642651297), (43000, 5901.156069364162), (43500, 6026.470588235294), (44000, 6047.787610619468), (44500, 5932.075471698114), (45000, 5890.909090909091), (45500, 6026.470588235294), (46000, 6015.859030837006), (46500, 5820.0), (47000, 5994.729136163982), (47500, 5809.985734664765), (48000, 5901.156069364162), (48500, 5994.729136163982), (49000, 5952.838427947599), (49500, 5952.838427947599)]
values_100dc=[(0, 6908.910891089108), (500, 6855.737704918033), (1000, 6700.32154340836), (1500, 6624.840764331209), (2000, 6895.551894563426), (2500, 6624.840764331209), (3000, 6764.343598055106), (3500, 6868.96551724138), (4000, 6816.313213703101), (4500, 6612.400635930049), (5000, 6751.456310679611), (5500, 6637.32057416268), (6000, 6575.316455696203), (6500, 6502.19435736677), (7000, 6600.0), (7500, 6575.316455696203), (8000, 6466.146645865836), (8500, 6371.648690292758), (9000, 6454.205607476635), (9500, 6268.085106382978), (10000, 6200.602409638554), (10500, 6256.752655538696), (11000, 6178.378378378379), (11500, 6112.5), (12000, 6200.602409638554), (12500, 6234.190620272315), (13000, 6134.328358208955), (13500, 6134.328358208955), (14000, 5963.26530612245), (14500, 5963.26530612245), (15000, 5973.722627737225), (15500, 5963.26530612245), (16000, 6080.0), (16500, 5911.432706222866), (17000, 5800.0), (17500, 5942.441860465115), (18000, 5973.722627737225), (18500, 5942.441860465115), (19000, 5740.677966101694), (19500, 5840.114613180516), (20000, 5890.909090909091), (20500, 5663.128491620112), (21000, 5840.114613180516), (21500, 5780.113636363637), (22000, 5770.212765957447), (22500, 5587.292817679558), (23000, 5663.128491620112), (23500, 5568.595041322315), (24000, 5721.12676056338), (24500, 5624.999999999999), (25000, 5624.999999999999), (25500, 5606.094182825485), (26000, 5624.999999999999), (26500, 5559.284731774415), (27000, 5624.999999999999), (27500, 5513.114754098361), (28000, 5568.595041322315), (28500, 5540.740740740741), (29000, 5587.292817679558), (29500, 5431.578947368421), (30000, 5458.536585365854), (30500, 5440.54054054054), (31000, 5503.956343792634), (31500, 5404.83870967742), (32000, 5440.54054054054), (32500, 5360.747663551401), (33000, 5334.574468085107), (33500, 5395.973154362416), (34000, 5282.849604221636), (34500, 5360.747663551401), (35000, 5467.571234735413), (35500, 5440.54054054054), (36000, 5369.518716577539), (36500, 5282.849604221636), (37000, 5369.518716577539), (37500, 5300.0), (38000, 5300.0), (38500, 5282.849604221636), (39000, 5265.78947368421), (39500, 5231.937172774869), (40000, 5369.518716577539), (40500, 5300.0), (41000, 5274.308300395256), (41500, 5334.574468085107), (42000, 5223.529411764705), (42500, 5325.896414342629), (43000, 5325.896414342629), (43500, 5282.849604221636), (44000, 5265.78947368421), (44500, 5300.0), (45000, 5308.609271523179), (45500, 5265.78947368421), (46000, 5148.837209302326), (46500, 5291.413474240422), (47000, 5291.413474240422), (47500, 5223.529411764705), (48000, 5116.195372750643), (48500, 5198.437500000001), (49000, 5132.474226804125), (49500, 5198.437500000001)]
values_temperature=[(0, 6935.761589403974), (500, 7017.391304347826), (1000, 7185.665529010239), (1500, 7017.391304347826), (2000, 7031.155778894472), (2500, 7072.727272727273), (3000, 6962.790697674419), (3500, 6989.999999999999), (4000, 7058.823529411764), (4500, 6829.411764705882), (5000, 6829.411764705882), (5500, 6829.411764705882), (6000, 7017.391304347826), (6500, 6962.790697674419), (7000, 6989.999999999999), (7500, 6976.372712146422), (8000, 7058.823529411764), (8500, 6922.314049586776), (9000, 6751.456310679611), (9500, 6816.313213703101), (10000, 6751.456310679611), (10500, 6777.272727272727), (11000, 6725.806451612902), (11500, 6764.343598055106), (12000, 6855.737704918033), (12500, 6989.999999999999), (13000, 6908.910891089108), (13500, 6816.313213703101), (14000, 6751.456310679611), (14500, 6649.840255591055), (15000, 6725.806451612902), (15500, 6868.96551724138), (16000, 6725.806451612902), (16500, 6662.4), (17000, 6649.840255591055), (17500, 6725.806451612902), (18000, 6882.236842105263), (18500, 6868.96551724138), (19000, 6895.551894563426), (19500, 6895.551894563426), (20000, 6725.806451612902), (20500, 6777.272727272727), (21000, 6790.243902439024), (21500, 6882.236842105263), (22000, 6738.610662358644), (22500, 6725.806451612902), (23000, 6738.610662358644), (23500, 6738.610662358644), (24000, 6575.316455696203), (24500, 6687.640449438202), (25000, 6563.033175355449), (25500, 6550.788643533122), (26000, 6842.553191489362), (26500, 6738.610662358644), (27000, 6624.840764331209), (27500, 6662.4), (28000, 6803.257328990228), (28500, 6575.316455696203), (29000, 6675.000000000001), (29500, 6816.313213703101), (30000, 6538.582677165355), (30500, 6751.456310679611), (31000, 6700.32154340836), (31500, 6675.000000000001), (32000, 6700.32154340836), (32500, 6675.000000000001), (33000, 6751.456310679611), (33500, 6764.343598055106), (34000, 6490.140845070422), (34500, 6751.456310679611), (35000, 6502.19435736677), (35500, 6502.19435736677), (36000, 6713.04347826087), (36500, 6526.415094339623), (37000, 6700.32154340836), (37500, 6675.000000000001), (38000, 6764.343598055106), (38500, 6700.32154340836), (39000, 6662.4), (39500, 6550.788643533122), (40000, 6649.840255591055), (40500, 6738.610662358644), (41000, 6738.610662358644), (41500, 6675.000000000001), (42000, 6600.0), (42500, 6612.400635930049), (43000, 6563.033175355449), (43500, 6675.000000000001), (44000, 6649.840255591055), (44500, 6526.415094339623), (45000, 6738.610662358644), (45500, 6587.638668779715), (46000, 6563.033175355449), (46500, 6612.400635930049), (47000, 6550.788643533122), (47500, 6764.343598055106), (48000, 6550.788643533122), (48500, 6575.316455696203), (49000, 6738.610662358644), (49500, 6649.840255591055)]


x_coord_10 = [coord[0] for coord in values_10dc]
y_coord_10 = [coord[1] for coord in values_10dc]
plt.plot(x_coord_10, y_coord_10, label='10%') 
#plt.show()

x_coord_50 = [coord[0] for coord in values_50dc]
y_coord_50 = [coord[1] for coord in values_50dc]

plt.plot(x_coord_50, y_coord_50, label='50%') 

x_coord_100 = [coord[0] for coord in values_100dc]
y_coord_100 = [coord[1] for coord in values_100dc]

plt.plot(x_coord_100, y_coord_100, label='100%')

x_coord_temp = [coord[0] for coord in values_temperature]
y_coord_temp = [coord[1] for coord in values_temperature]
plt.plot(x_coord_temp,y_coord_temp, label='temperature')


plt.legend(loc='upper right')
plt.show()






