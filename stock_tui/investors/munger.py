# investors/munger.py

from quantitative import QuantitativeAnalysis

class MungerInvestor:
    @staticmethod
    def check_requirements(ticker_symbol):
        # Fetch stock data using QuantitativeAnalysis
        analysis = QuantitativeAnalysis(ticker_symbol)

        # Define criteria based on Munger's investing philosophy
        criteria = {}

        # Munger's criteria thresholds
        criteria['operating_margin'] = analysis.get_operating_margin() and analysis.get_operating_margin() >= 0.20
        criteria['price_to_book'] = analysis.get_price_to_book() and analysis.get_price_to_book() <= 3
        criteria['debt_to_equity'] = analysis.get_debt_to_equity() and analysis.get_debt_to_equity() < 0.5
        criteria['roe'] = analysis.get_roe() and analysis.get_roe() >= 0.15
        criteria['free_cash_flow'] = analysis.get_free_cash_flow() and analysis.get_free_cash_flow() > 0

        # Count how many tests pass
        total_passed = sum(1 for passed in criteria.values() if passed)

        # For example, require at least 3 out of 5 tests to pass
        passes = total_passed >= 3

        return passes, criteria
