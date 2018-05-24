import cv2
import os

dir_list = os.listdir("Videos")
sampling_rate = 4

def sample_file(filename, start_image_name):
  vidcap = cv2.VideoCapture(filename)
  success,image = vidcap.read()
  skip = 0
  count = start_image_name
  success = True
  while success:
    if skip % sampling_rate == 0:
      timestamp = vidcap.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
      cv2.imwrite("Images/frame%d.jpg" % count, image)     # save frame as JPEG file
      print "Saving frame: {} at {}ms".format(count,timestamp) 
      count += 1
    success,image = vidcap.read()
    skip += 1
  return count


image_name = 0
for f in dir_list:
  image_name = sample_file("Videos/" + f, image_name)