import jetson.inference
import jetson.utils
import argparse
import sys
import threading
import time
import Servo


# parse the command line

para_LEMON = ['Lemon.py', '--model=./jetson-inference/python/training/detection/ssd/models/lemon/lemon3.onnx', '--class_labels=./jetson-inference/python/training/detection/ssd/models/lemon/labels.txt', '--input_blob=input_0', '--output_cvg=scores', '--output_bbox=boxes', '--camera=/dev/video0', '--width=640', '--height=480']

parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 
is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]



try:
    opt = parser.parse_known_args()[0]
except:
    print("")
    parser.print_help()
    sys.exit(0)


# load the object detection network
net = jetson.inference.detectNet(opt.network, para_LEMON, opt.threshold)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=para_LEMON)
output = jetson.utils.videoOutput(opt.output_URI, argv=para_LEMON+is_headless)

good = threading.Event()
bad = threading.Event()
detect_event = threading.Event()

# Int Arm:
servo.initArm()

def get_lemon():
    while True:
        if good.is_set():
            # print("good")
            # time.sleep(0.5)
            # time.sleep(0)
            servo.move_to_good_box()


        elif bad.is_set():
            # print("bad")
            # time.sleep(0.5)
            servo.move_to_bad_box()
        else:
            servo.initArm()
        

thr = threading.Thread(target = get_lemon, daemon = True)
thr.start()


while True:
    # capture the next image
    img = input.Capture()

    # detect objects in the image (with overlay)
    detections = net.Detect(img, overlay=opt.overlay)

    if len(detections) == 0:
       good.clear()
       bad.clear()

    else:
        for detection in detections:
            good.clear()
            bad.clear()
            if net.GetClassDesc(detection.ClassID) == 'good':
                good.set()
                bad.clear()

            elif net.GetClassDesc(detection.ClassID) == 'bad':
                bad.set()
                good.clear()
        # render the image
    output.Render(img)

    if not input.IsStreaming() or not output.IsStreaming():
        break
