#
# def check_crush(pic):
#     total = 0
#     result = []
#     crush = [0] * len(pic)
#     for i in range(len(pic)):
#         if crush[i] == 0:
#             x, y, d, e = pic[i]
#             energe = 0
#             for j in range(i+1, len(pic)):
#                 if crush[j] == 0:
#                     x_, y_, d_, e = pic[j]
#                     if d != d_:
#                         if abs(d - d_) == 1:
#                             if (abs(x - x_) == 1 and y_ == y) or (abs(y - y_) == 1 and x_ == x):
#                                 crush[j] = 1
#                                 crush[i] = 1
#                                 energe += d + d_
#                                 break
#                     if x == x_ and y == y_:
#                         energe += d + d_
#                         crush[j] = 1
#                         crush[i] = 1
#                         break
#             else:
#                 result.append(pic[i])
#             total += energe
#     return result, total