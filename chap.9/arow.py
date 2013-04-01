class AROW:
    def __init__(self, num_features, r=0.1):
        self.num_features = num_features
        self.r = r
        self.means = [0.0 for i in range(num_features)]
        self.covariances = [1.0 for i in range(num_features)]

    def margin(self, features):
        result = 0.0

        for i in range(self.num_features):
            result += self.means[i] * features[i]

        return result

    def predict(self, features):
        return self.margin(features) > 0

    def update(self, features, label):
        m = self.margin(features)
        if label * m >= 1:
            return False

        confidence = 0.0
        for i in range(self.num_features):
            value = features[i]
            confidence += self.covariances[i] * value * value

        beta = 1.0 / (confidence + self.r)
        alpha = label * (1.0 - label * m) * beta

        for i in range(self.num_features):
            value = features[i]
            v = self.covariances[i] * value
            self.means[i] += alpha * v
            self.covariances[i] -= beta * v * v

        return True
