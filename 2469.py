# Convert the Temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        # simple return of the input temp modified for Keliv and Farenheit
        return [(celsius + 273.15), ((celsius * 1.8) + 32)]
