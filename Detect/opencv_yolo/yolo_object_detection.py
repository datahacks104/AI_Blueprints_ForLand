import cv2
import numpy as np
import glob
import random
import os
from PIL import Image



sizes = {}
def detect_land(images_path, base_dir):
    global getlength, getwidth
    path = os.path.join(base_dir,'opencv_yolo')
    weights = os.path.join(path,"yolov3_training_last.weights")
    cfg = os.path.join(path, "yolov3_testing.cfg")

    # Load Yolo
    net = cv2.dnn.readNet(weights, cfg)

    # Name custom object
    classes = ["Land"]

    # Images path
    images_path = glob.glob(os.path.join(images_path, '*'))



    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Insert here the path of your images
    random.shuffle(images_path)
    # loop through all the images
    for img_path in images_path:
        # Loading image
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=0.25, fy=0.25)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    # Object detected
                    print(class_id)
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                width1=w+x
                height1=h+y
                lable2="length= " + str(width1) + " and " + "width= " + str(height1)
                color = colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 4)
                cv2.putText(img, lable2, (x, y + 30), font, 3, color, 3)

                getlength = width1
                getwidth = height1


        cv2.imwrite(img_path, img)

        im = Image.open(img_path)
        if 'dpi' in im.info:
            dpiX, dpiY = im.info['dpi']
        else:
            dpiX, dpiY = [96, 96]
        width_in = float(im.size[0])/float(dpiX)
        height_in = float(im.size[1])/float(dpiY)

        size = (width_in, height_in)

        sizes[img_path] = sizes
def returning_width():
    return getwidth
def returning_length():
    return getlength


