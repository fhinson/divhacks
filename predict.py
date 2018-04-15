import numpy as np
import math
import itertools
import pprint
from matplotlib import pyplot as plt


def load_data(csv_filename):
    array = np.loadtxt(open(csv_filename, "rb"), delimiter=",", skiprows=1, usecols=range(23))
    return array

if __name__ == "__main__":

    train_data = load_data('MNIST_train.csv')
    # test_data = load_data('MNIST_test.csv')

    pc_dataset = [
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
        {
          "ALG1":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG2":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG3":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG4":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG5":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG6":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG7":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG8":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG9":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG10":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG11":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG12":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG13":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG14":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG15":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG16":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG17":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG18":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG19":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG20":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
          "ALG21":
            {
              "total_observed": 0,
              "total_correct": 0,
            },
        },
    ]

    for instance in train_data:
      label = int(instance[1])
      alg = pc_dataset[label]
      alg_id = 1
      for i in range(len(instance)):
        if i > 1:
          alg_id_string = "ALG" + str(alg_id)
          alg_info = alg[alg_id_string]
          alg_info["total_observed"] += 1
          if instance[i] == 1:
            alg_info["total_correct"] += 1
          alg_id += 1



    ############## Test Code ###############
    T = 0.5

    TEST_DIGIT = 4
    alg_set = pc_dataset[TEST_DIGIT]

    best_alg = ""
    best_alg_score = 0

    for alg in alg_set:
      score = alg_set[alg]["total_correct"] / float(alg_set[alg]["total_observed"])
      if score > best_alg_score:
        best_alg = alg

    print best_alg

    best_scores = []

    for i in range(9):
      score_set = []
      alg_set = pc_dataset[i]
      alg_score = 0
      alg_set = pc_dataset[i]
      for alg in alg_set:
        score = alg_set[alg]["total_correct"] / float(alg_set[alg]["total_observed"])
        score_set.append(score)
      best_scores.append(score_set)

    # print best_scores

    ## FOR A GIVEN TEST DIGIT, I'M ABLE TO PREDICT THE BEST ALGORITHM PERFORMANCE FOR THAT DIGIT
