# investors/buffett.py

from stocks.quantitative import QuantitativeAnalysis

class BuffettInvestor:
    @staticmethod
    def check_requirements(ticker_symbol):
        # Fetch stock data
        analysis = QuantitativeAnalysis(ticker_symbol)

        # Define criteria using quantitative analysis methods
        criteria = {}

        # Buffett's criteria thresholds
        criteria['roe'] = analysis.get_roe() and analysis.get_roe() >= 0.15
        criteria['debt_to_equity'] = analysis.get_debt_to_equity() and analysis.get_debt_to_equity() < 0.5
        criteria['profit_margin'] = analysis.get_profit_margin() and analysis.get_profit_margin() >= 0.1
        criteria['eps_growth'] = analysis.get_eps_growth() and analysis.get_eps_growth() >= 0.1
        criteria['forward_pe'] = analysis.get_forward_pe() and analysis.get_forward_pe() <= 15
        criteria['sgr'] = analysis.get_sgr() and analysis.get_sgr() >= 0.10

        # Count how many criteria passed
        total_passed = sum(1 for v in criteria.values() if v)

        # The company passes if at least 4 of 6 criteria are met
        passes = total_passed >= 4

        return passes, criteria
