# LearningML
A code repo for learning ML (deep learning, NLP, etc)

perf compare:

- GTX1650 vs Tesla V100  
https://askgeek.io/en/gpus/vs/NVIDIA_GeForce-GTX-1650-vs-NVIDIA_Tesla-V100-PCIe-32-GB

|  | my desktop | brian's cluster |
| --- | --- | --- |
| seq2seq.ipynb (pytorch) |24'13''|8'59''|
| CPU | i7 9700 (8 thread) (8 core) | E5-2698 v4 (80 thread) (2 x 20 core x 2 thread) |
| memory | 16GB | 504GB |
| gpu | GTX1650 GDDR6 TU117-A | Tesla V100-SXM2-32GB x 8 |
| gpu-memory | 4GB GDDR6 | 32GB HBM2 x 8 |

- brian's cluster:
```
Epoch 0 / 16
Current Time = 08:05:03
Epoch 1 / 16
Current Time = 08:05:58
Epoch 2 / 16
Current Time = 08:06:36
Epoch 3 / 16
Current Time = 08:07:08
Epoch 4 / 16
Current Time = 08:07:41
Epoch 5 / 16
Current Time = 08:08:14
Epoch 6 / 16
Current Time = 08:08:48
Epoch 7 / 16
Current Time = 08:09:19
Epoch 8 / 16
Current Time = 08:09:50
Epoch 9 / 16
Current Time = 08:10:22
Epoch 10 / 16
Current Time = 08:10:53
Epoch 11 / 16
Current Time = 08:11:25
Epoch 12 / 16
Current Time = 08:11:57
Epoch 13 / 16
Current Time = 08:12:28
Epoch 14 / 16
Current Time = 08:12:59
Epoch 15 / 16
Current Time = 08:13:30
Current Time = 08:14:02
```

- my cluster:
```
Epoch 0 / 16
Current Time = 15:01:55
Epoch 1 / 16
Current Time = 15:03:25
Epoch 2 / 16
Current Time = 15:04:56
Epoch 3 / 16
Current Time = 15:06:27
Epoch 4 / 16
Current Time = 15:07:57
Epoch 5 / 16
Current Time = 15:09:29
Epoch 6 / 16
Current Time = 15:11:00
Epoch 7 / 16
Current Time = 15:12:30
Epoch 8 / 16
Current Time = 15:14:01
Epoch 9 / 16
Current Time = 15:15:32
Epoch 10 / 16
Current Time = 15:17:02
Epoch 11 / 16
Current Time = 15:18:33
Epoch 12 / 16
Current Time = 15:20:04
Epoch 13 / 16
Current Time = 15:21:35
Epoch 14 / 16
Current Time = 15:23:06
Epoch 15 / 16
Current Time = 15:24:37
Current Time = 15:26:08
```