# Handwriting Digits - Easy or hard? An IBM DIV HACKS Project

## Introduction
This project is specifically designed for the [DIV HACKS for Columbia University](https://cu-divhacks.github.io/) on April 14, 2018.

### Note to participants
If you are not clear about any particular concept as discussed below, please ask your technical mentors to help you. You can do the programming using whatever programming language you are comfortable with, be it Python, R, Matlab, JAVA, or C/C++. 

## Motivation

Handwriting recognition is a well-studied subject in computer vision and has found wide applications in our daily life (such as sorting USPS mails by zip codes). 

One of the most known datasets is the [MNIST dataset of handwritten digits](http://yann.lecun.com/exdb/mnist/), which has a training set of 60,000 examples, and a test set of 10,000 examples. 

Below is an example of some digits from the MNIST dataset.

![alt text](http://theanets.readthedocs.io/en/stable/_images/mnist-digits-small.png "MNIST image examples")

In this DIV HACKS project, we will be doing something different from most typical MNIST digital recognition tasks (where the goal is to recognize the ten digits from 0 to 9).

Instead, we are given the same MNIST dataset, but additionally, we are also given recognition results from some 21 machine learning (ML) algorithms implemented by various people (called ALG1, ALG2, …, ALG21). In other words, for each digit in the MINIST dataset, we have 21 results from the 21 ML algorithms: a value of 1 means that the corresponding ML algorithm has correctly recognized the digit, and a value of 0 means that the corresponding ML algorithm did not recognize the digit correctly.

Same as MNIST dataset, we have such results for both the [training dataset](https://github.com/JinjunXiong/divhacks/blob/master/MNIST_train.csv) and the [test dataset](https://github.com/JinjunXiong/divhacks/blob/master/MNIST_test.csv). The recognition results are given as CSV (comma separated value) format as follows, where the ID is the sequence ID of the MNIST digit in the MNIST dataset, the Label is the supposed MNIST digit, and ALG1 to ALG 21 indicate the prediction values from those corresponding ML algorithms.

Obviously, different implementations of these ML algorithms will have different predictive power in recognize those digits.

## Goals

Here is our hypothesis: some handwriting digits are inherently easier to recognize than others – this can be indicated by how easily a digit can be correctly predicted by those 21 ML algorithms. If a digit can be easily recognized by most ML algorithms, it is probably safe to assume that the digit is easy to recognize. If a digit can NOT be recognized correctly by most ML algorithms, it is probably safe to assume that the digit is HARD to recognize.

Our DIV HACK goal is to design a binary classifier for these handwriting digits so that we can correctly predict if a digit is easy or hard to recognize. (Note that we are not asking you to recognize the digit itself.)

## Tasks

### Required tasks (must do)

Here are a few tasks that you must do:

1. You’ll first need to generate the EASY or HARD labels for each digits based on the 21 ML algorithms prediction values. To do so, you need to calculate the percentage of times the prediction is correct, i.e., **PC** = (# of correct predictions) / 21. You will also choose a threshold value (**T**) to convert that PC number into an EASY or HARD label. For example, let’s say we pick the threshold to be T = 50%, then if there are more cases of a digit are predicted correct than wrong, we can mark that digit as an “EASY” label. Otherwise, that image is marked as a “HARD” label.  (You will later experiment with different threshold values.) You will need to generate the EASY or HARD labels for both the training dataset and the test dataset. 

2. Explore the dataset and report your findings using either data or plots to answer the following question: among 0 – 9, which digits are easier to predict than others? What could be the reasons in your opinion?

3. Design and implement a binary classifier (EASY or HARD) for all MNIST training data using the above so-obtained labeled data -- while using the 10K test data for testing. Report your training and test accuracy. Please remember to use the validation set from your training data to tune your classifier as needed.


### Advanced tasks (optional)

Here are a few more tasks that you can challenge yourself: 

4. Separate the dataset per digit (i.e., separate data into 10 groups based on digit 0 to 9). Design and implement a binary classifier for each digit group to predict it’s EASY or HARD to be recognized. Using the corresponding test data set for testing. Report your training and test accuracy for each digit group. Report your findings using either data or plots to answer the following question: for each digit, what makes one handwriting easy to be recognized and what makes one handwriting hard to be recognized? What would be your explanation for your findings?

5. Change threshold value **T** as shown in step (1) to get different ways of generate the EASY or HARD labels, and repeat the above steps. Do you observe any differences in your earlier findings? How would you explain your findings?

### Even more advanced tasks (optional)

Here are a few more things that you could do if you want to really challenge yourself

6. Build a web page frontend (hosted on your local machine) to display various findings from your results above. The quality of the web page and visualization should help to convey your message.

7. Deploy the web page frontend to the [IBM Bluemix cloud](https://console.bluemix.net/catalog/) (using the free account) and let everyone else from the world to see your beautiful DIV HACKS results.  


