from .indicators import Indicators

class Strategy:
    def __init__(self, df):
        self.df = df

    def generate_signal(self):
        rsi = Indicators.rsi(self.df['close'])
        ma_fast = Indicators.sma(self.df['close'], 9)
        ma_slow = Indicators.sma(self.df['close'], 21)

        if rsi < 30 and ma_fast > ma_slow:
            return "BUY"

        if rsi > 70 and ma_fast < ma_slow:
            return "SELL"

        return None
