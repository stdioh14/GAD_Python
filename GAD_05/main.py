import math


class Fractie:
    def __init__(self, numarator, numitor):
        self._numarator = numarator
        self._numitor = numitor

    def __str__(self):
        return "{}/{}".format(self._numarator, self._numitor)

    def __add__(self, other):
        numarator = self._numarator * other.numitor + other.numarator * self._numitor
        numitor = self._numitor * other.numitor

        gcd = math.gcd(numarator, numitor)

        return Fractie(int(numarator / gcd), int(numitor / gcd))

    def __neg__(self):
        return Fractie(-self._numarator, self._numitor)

    def __sub__(self, other):
        return self + (-other)

    def inverse(self):
        return Fractie(self._numitor, self._numarator)

    @property
    def numarator(self):
        return self._numarator

    @property
    def numitor(self):
        return self._numitor

    @numarator.setter
    def numarator(self, numarator):
        self._numarator = numarator

    @numitor.setter
    def numitor(self, numitor):
        self._numitor = numitor


if __name__ == "__main__":
    print("127/256 + 65/256 =", Fractie(127, 256) + Fractie(65, 256))
    print("129/256 - 1/256 =", Fractie(129, 256) - Fractie(1, 256))
    print("inverse =", Fractie(1234, 5678).inverse())
