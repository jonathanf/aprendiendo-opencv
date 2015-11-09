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
#

import cv2
import random

videopath = 'capture/video'
camera = 0

def capturefromcamera():
    cap = cv2.VideoCapture(0)
    framecount = 0
    control = 10
    while True:
        ret, frame = cap.read()
        framecount += 1
        # Random image tranform
        if framecount % 10 == 0:
            control = random.randint(1, 10)
        if control < 2:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
        elif control < 4:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif control < 6:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
        elif control < 8:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        else:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        # Display the resulting frame
        framename = 'frame%s' % int(control / 2) or 1
        cv2.imshow(framename, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def saveinfile():
    return

def capturefromfile():
    return

capturefromcamera()



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: