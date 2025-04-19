# investors/peter_lynch.py

from stocks.quantitative import QuantitativeAnalysis

class PeterLynchInvestor:
    @staticmethod
    def check_requirements(ticker_symbol):
        # Fetch stock data
        analysis = QuantitativeAnalysis(ticker_symbol)

        # Define criteria using quantitative analysis methods
        criteria = {}

        # Peter Lynch's criteria thresholds
        # Earnings Analysis
        criteria['eps_growth'] = analysis.get_five_year_eps_growth() and analysis.get_five_year_eps_growth() >= 0.10
        criteria['eps_stability'] = analysis.get_eps_stability() and analysis.get_eps_stability() < 0.20

        # Valuation Metrics
        criteria['peg_ratio'] = analysis.get_peg_ratio() and analysis.get_peg_ratio() < 1
        criteria['peg_y'] = analysis.get_peg_y() and analysis.get_peg_y() >= 1

        # Balance Sheet Strength
        criteria['debt_to_equity'] = analysis.get_debt_to_equity() and analysis.get_debt_to_equity() < 0.5
        criteria['net_cash_per_share'] = analysis.get_net_cash_per_share() and analysis.get_net_cash_per_share() > 0

        # Dividend Metrics
        criteria['dividend_yield'] = analysis.get_dividend_yield() and analysis.get_dividend_yield() >= 0.02
        criteria['payout_ratio'] = analysis.get_payout_ratio() and analysis.get_payout_ratio() < 0.6

        # Operational Efficiency
        criteria['inventory_growth_vs_sales_growth'] = analysis.get_inventory_growth_vs_sales_growth() and analysis.get_inventory_growth_vs_sales_growth() < analysis.get_sales_growth()
        criteria['inventory_turnover'] = analysis.get_inventory_turnover() and analysis.get_inventory_turnover() > 6

        # Count how many criteria passed
        total_passed = sum(1 for v in criteria.values() if v)

        # For Peter Lynch, require at least 6 of the 9 criteria to pass
        passes = total_passed >= 6

        return passes, criteria
