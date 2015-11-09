# -*- coding: utf-8 -*-
#    Copyright (C) 2015  Jonathan Finlay <jfinlay@riseup.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import cv2

def show_cv2():
    img = cv2.imread('img/tpp.jpg', 0)
    cv2.imshow('tpp', img)
    k = cv2.waitKey(0)
    while k != 27:
        k = cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_matplot():
    from matplotlib import pyplot as plt
    img = cv2.imread('img/tpp.jpg', 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

op = raw_input("Show method (cv|mp): ")
if op == 'cv':
    show_cv2()
elif op == 'mp':
    show_matplot()
else:
    print "Unknow method"

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
