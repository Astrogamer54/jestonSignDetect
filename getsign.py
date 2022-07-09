import jetson.inference
import jetson.utils
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("inp", type=str, default="")
parser.add_argument("out", type=str, default="output.png")
parser.add_argument("--network", type=str, default="googlenet")
parser.add_argument("--camera", type=str, default="0")
parser.add_argument("--width", type=int, default=1280)
parser.add_argument("--height", type=int, default=720)

try:
	opt = parser.parse_known_args()[0]
except:
	print("Parser Error")
	sys.exit(0)

net = jetson.inference.imageNet(opt.network, sys.argv)

inp = jetson.utils.videoSource(opt.inp, argv=sys.argv)
out = jetson.utils.videoOutput(opt.out, argv=sys.argv)
font = jetson.utils.cudaFont()

while True:
	img = inp.Capture()
	class_id, confidence = net.Classify(img)
	class_desc = net.GetClassDesc(class_id)
	font.OverlayText(img, img.width, img.height, "Detected {:s} with {:05.2f}% confidence,".format(class_desc,confidence * 100), 5, 5, font.White, font.Gray40)
	out.Render(img)
	print(class_desc)
	print(confidence*100)
	if not inp.IsStreaming() or not out.IsStreaming():
		break

	


