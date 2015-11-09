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
        framename = 'frame%s' % int(control / 3) or 1

        # Flipping
        if framecount % 4 == 0:
            img = cv2.flip(img, 0)
        # Transpose
        if framecount % 3 == 0:
            cv2.transpose(img)
        cv2.imshow(framename, img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def saveinfile():
    cap = cv2.VideoCapture(0)

    #Define the codec and create ViweoWriter object
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('capture/video/capture.avi', fourcc, 20.0, (640, 480))
    while True:
        ret, frame = cap.read()
        if ret:
            flipcode = random.randint(-10, 10)
            frame = cv2.flip(frame, flipcode)

            # write flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    return

def capturefromfile():
    cap = cv2.VideoCapture('capture/video/capture.avi')

    while True:
        ret, frame = cap.read()
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame,'Jonathan',(10,180), font, 4,(255,255,255),2,cv2.cv.CV_INTER_LINEAR)

        cv2.imshow('readfile', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print
print "===================="
print " Choose one option: "
print "===================="
print

op = raw_input("(camera|save|file): ")
if op == 'camera':
    capturefromcamera()
elif op == 'save':
    saveinfile()
elif op == 'file':
    capturefromfile()
else:
    print 'Oops!!'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: