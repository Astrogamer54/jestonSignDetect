# jetsonSignDetect

A prototype program to detect speed limit signs. Images are drawings of speed limit signs so it will not work in the real world. Model has accuracy of 94% for me. 

![sign](https://github.com/Astrogamer54/jetsonSignDetect/blob/main/demoimages/sign.png)
![sign1](https://github.com/Astrogamer54/jetsonSignDetect/blob/main/demoimages/sign1.png)
![sign2](https://github.com/Astrogamer54/jetsonSignDetect/blob/main/demoimages/sign2.png)

## How to run

### Clone repo
`git clone https://github.com/Astrogamer54/jetsonSignDetect.git`
`cd jetsonSignDetect`

### Unpack images
```mkdir data/traffic_signs/TEST && tar -xvzf data/traffic_signs/TEST.tar.gz -C data/traffic_signs/TEST
tar -xvzf traffic_signs.tar.gz -C data/traffic_signs/```


### Run train.py
```python3 train.py -b 8 --epochs CHANGETHISTOHOWMANYEPOCHESYOUWANT -j 2

###set env
```NET=models/traffic_signs
DATASET=data/traffic_signs```

### Run imageNet
`python3 getsign.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/TEST/60/200.jpg.jpg sign.png`
