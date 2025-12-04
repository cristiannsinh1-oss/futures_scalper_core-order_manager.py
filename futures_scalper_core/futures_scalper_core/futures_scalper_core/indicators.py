import pandas as pd

class Indicators:
    @staticmethod
    def rsi(series: pd.Series, period=14):
        delta = series.diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]

    @staticmethod
    def sma(series: pd.Series, period=14):
        return series.rolling(window=period).mean().iloc[-1]
