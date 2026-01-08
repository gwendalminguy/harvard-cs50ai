# Analysis

This model has been trained on 13 different versions with these fixed parameters:

- Epochs: 10
- Test Size: 0.4
- Categories: 43

And the following parameters adjusted differently for each version:

- number of convolutional and pooling layers
- number and size of filters for convolutional layers
- pool size for pooling layers
- number and size of hidden layers
- dropout value

The best results were given by the VERSION 13, with the following configuration:

- 3 convolutional layers of 32 filters each with a kernel matrix of dimension 3 x 3
- 1 pooling layer with a dimension of 3 x 3
- 1 flattening layer
- 1 hidden layer of 128 units
- no dropout layer

This version gave the following results:

- 98.73% accuracy
- 5.74% loss


## VERSION 01

CONFIGURATION:
- Convolutional Layer:
	- Filters: 16
	- Kernel Matrix: 5 x 5
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9110
- Loss: 0.9852


## VERSION 02

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 5 x 5
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9213
- Loss: 0.5619


## VERSION 03

CONFIGURATION:
- Convolutional Layer:
	- Filters: 64
	- Kernel Matrix: 5 x 5
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9206
- Loss: 0.5909


## VERSION 04

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9343
- Loss: 0.5630


## VERSION 05

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 4 x 4
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9112
- Loss: 0.3845


## VERSION 06

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.1
- Output Layer

RESULTS:
- Accuracy: 0.5783
- Loss: 1.5613


## VERSION 07

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 64
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.0542
- Loss: 3.4968


## VERSION 08

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 256
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9261
- Loss: 0.5276


## VERSION 09

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.8970
- Loss: 0.4568


## VERSION 10

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 2 x 2
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.25
- Output Layer

RESULTS:
- Accuracy: 0.3943
- Loss: 2.0793


## VERSION 11

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 3 x 3
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9215
- Loss: 0.3912


## VERSION 12

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 3 x 3
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9528
- Loss: 0.2477


## VERSION 13

CONFIGURATION:
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Convolutional Layer:
	- Filters: 32
	- Kernel Matrix: 3 x 3
- Pooling Layer:
	- Pool Size: 3 x 3
- Flattening Layer
- Hidden Layer:
	- Units: 128
- Dropout Layer:
	- Dropout: 0.0
- Output Layer

RESULTS:
- Accuracy: 0.9873
- Loss: 0.0574
