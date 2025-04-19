# stocks/quantitative.py

import yfinance as yf

class QuantitativeAnalysis:
    def __init__(self, ticker_symbol):
        """
        Initialize by fetching stock data from Yahoo Finance.
        """
        ticker = yf.Ticker(ticker_symbol)
        self.info = ticker.info

    # Getter methods for stock data
    def get_roe(self):
        """Get return on equity (ROE)"""
        return self.info.get('returnOnEquity')

    def get_debt_to_equity(self):
        """Get debt-to-equity ratio"""
        return self.info.get('debtToEquity')

    def get_profit_margin(self):
        """Get profit margin"""
        return self.info.get('profitMargins')

    def get_eps_growth(self):
        """Get earnings per share (EPS) growth"""
        return self.info.get('earningsQuarterlyGrowth')

    def get_forward_pe(self):
        """Get forward price-to-earnings (PE) ratio"""
        return self.info.get('forwardPE')

    def get_sgr(self):
        """Get sustainable growth rate (SGR)"""
        roe = self.get_roe()
        payout_ratio = self.info.get('payoutRatio')
        if roe is None or payout_ratio is None:
            return None
        return roe * (1 - payout_ratio)

    # Munger criteria checks
    def get_operating_margin(self):
        """Get operating margin"""
        return self.info.get('operatingMargins')

    def get_price_to_book(self):
        """Get price-to-book ratio"""
        return self.info.get('priceToBook')

    def get_free_cash_flow(self):
        """Get free cash flow"""
        return self.info.get('freeCashflow')

    # Peter Lynch specific checks
    def get_five_year_eps_growth(self):
        """Get 5-year annualized EPS growth"""
        return self.info.get('fiveYearAvgDividendYield')

    def get_eps_stability(self):
        """Get EPS stability (year-over-year fluctuation)"""
        return self.info.get('earningsQuarterlyGrowth')

    def get_peg_ratio(self):
        """Get PEG ratio"""
        return self.info.get('pegRatio')

    def get_peg_y(self):
        """Get Dividend-Adjusted PEG (PEGY)"""
        dividend_yield = self.get_dividend_yield()
        pe_ratio = self.get_forward_pe()
        eps_growth = self.get_eps_growth()
    
        if None in (dividend_yield, pe_ratio, eps_growth) or pe_ratio == 0:
            return None

        return (eps_growth + dividend_yield) / pe_ratio

    def get_net_cash_per_share(self):
        """Get net cash per share"""
        return self.info.get('netCashPerShare')

    def get_dividend_yield(self):
        """Get dividend yield"""
        return self.info.get('dividendYield')

    def get_payout_ratio(self):
        """Get payout ratio"""
        return self.info.get('payoutRatio')

    def get_inventory_turnover(self):
        """Get inventory turnover"""
        return self.info.get('inventoryTurnover')

    def get_inventory_growth_vs_sales_growth(self):
        """Get inventory growth vs. sales growth"""
        return self.info.get('inventoryGrowth')

    def get_sales_growth(self):
        """Get sales growth"""
        return self.info.get('revenueGrowth')
