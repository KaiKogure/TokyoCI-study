#!/usr/bin/env python

import advancedclassify
import arow


def classify_and_validate_dp(name, dataset):
    avgs = advancedclassify.lineartrain(dataset)
    correct_count = 0.0
    for row in dataset:
        res = advancedclassify.dpclassify(row.data, avgs)
        if res == row.match:
            correct_count += 1
    accuracy = correct_count / len(dataset)
    print "[%s] correct: %d/%d, accuracy: %f" % (name, correct_count,
                                                 len(dataset), accuracy)


def classify_and_validate_arow(dataset):
    num_features = len(dataset[0].data)
    arow_model = arow.AROW(num_features)

    # train
    for row in dataset:
        label = row.match
        if label == 0:
            label = -1
        arow_model.update(row.data, label)

    # verify
    correct_count = 0.0
    for row in dataset:
        label = row.match
        if label == 0:
            label = False
        else:
            label = True
        actual = arow_model.predict(row.data)
        if actual == label:
            correct_count += 1

    accuracy = correct_count / len(dataset)
    print "[%s] correct: %d/%d, accuracy: %f" % ("AROW", correct_count,
                                                 len(dataset), accuracy)


# load and scaling data
agesonly = advancedclassify.loadmatch('agesonly.csv', allnum=True)
numericalset = advancedclassify.loadnumerical('matchmaker.csv')
scaledset, scalef = advancedclassify.scaledata(numericalset)

# show agematch distribution
#advancedclassify.plotagematches(agesonly)
#advancedclassify.plotagematches(numericalset)

# agesonly.csv linear classification
classify_and_validate_dp("agesonly", agesonly)

# matchmaker.csv linear classification
classify_and_validate_dp("matchmaker", numericalset)
classify_and_validate_dp("scaled matchmaker", scaledset)
classify_and_validate_arow(scaledset)
