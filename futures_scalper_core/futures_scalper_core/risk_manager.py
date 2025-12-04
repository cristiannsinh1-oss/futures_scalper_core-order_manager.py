class RiskManager:
    def __init__(self, max_loss_percent=1.0, take_profit_percent=0.4):
        self.max_loss_percent = max_loss_percent
        self.take_profit_percent = take_profit_percent

    def calculate_position_size(self, balance: float, price: float):
        return round((balance * 0.02) / price, 3)

    def check_exit_conditions(self, entry_price: float, current_price: float):
        change = ((current_price - entry_price) / entry_price) * 100

        if change <= -self.max_loss_percent:
            return "STOP_LOSS"

        if change >= self.take_profit_percent:
            return "TAKE_PROFIT"

        return None
