import math

class SentiAnalyzer:

    # Make the method signature to accept "sentidata" and "word"
    def __init__(self):
        print('This is a senti analyzer')

    def probWordPositiveAndNegative(self, sentidata, word, idxWord):
        pointedWord = word[idxWord]
        reviews = [int(float(row[-1])) for row in sentidata] # 리뷰 198개가 주어졌다. 주어진 198개의 리뷰가 pos인지 neg인지 알려주는 마지막 column 값 198개를 reviews에 list로 저장한다.
        occurrence = [int(float(row[idxWord])) for row in sentidata] # ?

        # Calculate the number of positive review occurrence with the pointed word, and assign the calculated value to 'positive'
        # positive review이면서 동시에 그 word가 나온 review의 개수
        positive = 0
        for i in range(len(occurrence)):
            positive = positive + occurrence[i] * reviews[i] # first blank
            # review에 idxword가 포함되어 있으면서 positive인 review의 개수를 계산하여 그 개수를 positive에 assign

        # Calculate the number of positive reviews from the entire review set
        numPositiveReviews = sum(reviews) # second blank
        # If we sum up all the ones at column 28625 of sentidata.csv then thats the number of the positive reviews. since positive is 1 neg is 0.
        # 전체 review 중 positive인 모든 review의 개수를 numPositiveRevies에  assign

        # Calculate the number of negative review occurrence with the pointed word, and assign the calculated value to 'negative'
        negative = 0
        for i in range(len(occurrence)):
            negative = negative + negative + occurrence[i] * (1 - reviews[i]) # third blank
            # one minus zero becomes one and one minus one becomes zero. so negative becomes one.
            # review에 idxword가 포함되어 있으면서 negative인 review의 개수를 계산하여 그 개수를 negative에 assign

        rowCount = len(sentidata)
        positiveProb = float(positive) / float(numPositiveReviews)
        negativeProb = float(negative) / float(rowCount - numPositiveReviews)

        if positiveProb == 0:
            positiveProb = 0.00001
        if negativeProb == 0:
            negativeProb = 0.00001
        return pointedWord, positiveProb, negativeProb

    def probPositiveAndNegative(self, sentidata):
        positive = sum([int(float(row[-1])) for row in sentidata])
        numReviews = len(sentidata)
        negative = numReviews - positive
        positiveProb = float(positive) / float(numReviews)
        negativeProb = float(negative) / float(numReviews)
        return positiveProb, negativeProb

    def findUsedWords(self, sentidata, word, idx):
        # Return the index of the used words in 'idx'th review
        temp = [int(float(x)) for x in sentidata[idx][:-1]]
        idxUsedWords = [index for index, value in enumerate(temp) if value == 1]
        # Return the actual words in 'idx'th review
        usedWords = [word[idx] for idx in idxUsedWords]
        return idxUsedWords, usedWords

    def runAnalysis(self, sentidata, word, idxReview):
        probLogPositive = 0
        probLogNegative = 0
        idxUsedWords, usedWords = self.findUsedWords(sentidata, word, idxReview)

        # Make a for-loop to run from the first word to the last word
        for i in range(len(idxUsedWords)): # blank
            # get the first word from the used word set
            idxWord = idxUsedWords[i]
            # calculate the word's probability to be positive or negative
            pointedWord, positive, negative = self.probWordPositiveAndNegative(sentidata, word, idxWord)
            probLogPositive += math.log(positive)
            probLogNegative += math.log(negative)

        positiveProb1, negativeProb1 = self.probPositiveAndNegative(sentidata)
        # In log dimension ordinary multiplication becomes adding.
        # In log dimension adding is equal to multiplication in ordinary domain.
        # e.g. 0.1 * 0.1 = 0.01, 0.01 * 0.1 = 0.001 -> 0.삼십개의영1은 컴퓨터에서 zero. -> numerical error -> this is the reason why we take log dimension.
        probLogPositive += math.log(positiveProb1)
        probLogNegative += math.log(negativeProb1)

        if probLogPositive > probLogNegative:
            sentiment = 'Positive'
            print('Positive')
        else:
            sentiment = 'Negative'
            print('Negative')

        return probLogPositive, probLogNegative, sentiment

# these are for the video lecture.


# Sentiment Analysis are very popular these days.

# We can identify bad reviews.
# And We can use those to improve our product by fixing those complains.

# classification task
# We are going to use numbers to distinguish pos and neg product reviews.
# How can we turn these articles in numbers?
# We can create a vector and solve the above problem. e.g. <1,0,0,1>, <I, cool, Lcd, >
# numerical representation of this text. ------> called bag of words


# RECALL conditional probability

# At th end of the day we are going to put some text at 'E' of P(H bar E)
# and calculate the probablity of being pos or neg.

# Many Words slide's formular is our final formular of our numberical part.
# You dont have to understand the final formular not yet.
# 다음주에도 Sentiment A.를 이어서 할건데 excercise 하다보면 우리가 뭐를 하는건지 이해할 수 있을 것이다.


# SentiData.csv 파일을 열어라.
# 0과 1이 많이 보일 것이다.
# Dataset 슬라이드의 디스크립션을 보시오.
# 28625 : final column


# seven blanks


# comments are the things that what i want you to do.

# Occurance means that whether that word is being poped up or not. 1 or 0 for each review.

# Before you try to fill in those blanks please read through this code.
# and then start to fill out those blanks.

# word.csv
#   Row : 28624 words
# sentidata.csv
#   Row : 198 product reviews
#   Col :
#   - 0-28624 : whether the review contains a certain word(1) or not(0)
#   - 28625 : wheter the review is positive(1) or not(0)



# 다섯번째 column은 다섯번째 단어가 그 리뷰에 나왔는지 나오지 않았는지를 0 또는 1로 표시한다. 나왔으면 1이고 아니면 0이다.

# We are college students. So We are going to deal with difficult things.