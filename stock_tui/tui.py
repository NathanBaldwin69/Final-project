import curses
from investors.buffett import BuffettInvestor
from investors.munger import MungerInvestor
from investors.lynch import PeterLynchInvestor

INVESTOR_CLASSES = {
    'Buffett': BuffettInvestor,
    'Munger': MungerInvestor,
    'Peter Lynch': PeterLynchInvestor,
}

def display_header(window, message):
    window.clear()
    window.addstr(0, 0, message)
    window.refresh()

def get_investor_choice(window):
    options = list(INVESTOR_CLASSES.keys()) + ["All (Buffett, Munger, Peter Lynch)"]
    window.addstr(2, 0, "Select an investor for stock evaluation:")
    for i, name in enumerate(options, 1):
        window.addstr(2 + i, 0, f"{i}. {name}")
    window.refresh()

    choice = window.getch()
    if choice in [ord(str(i)) for i in range(1, len(INVESTOR_CLASSES) + 1)]:
        return [list(INVESTOR_CLASSES.keys())[choice - ord('1')]]
    elif choice == ord(str(len(options))):  # Option for 'All'
        return list(INVESTOR_CLASSES.keys())
    else:
        return []

def get_ticker_input(window):
    window.addstr(7, 0, "Enter ticker symbol: ")
    window.refresh()

    window.move(8, 0)
    ticker = ""

    while True:
        char = window.getch()
        if char == 10:  # Enter
            break
        elif char == 27:  # ESC
            return ""
        elif char in (263, 127):  # Backspace
            ticker = ticker[:-1]
            window.move(8, 0)
            window.clrtoeol()
            window.addstr(8, 0, ticker)
        else:
            ticker += chr(char)
            window.addstr(8, len(ticker) - 1, chr(char))
        window.refresh()

    return ticker.upper()

def get_analysis_mode(window):
    window.clear()
    window.addstr(2, 0, "Select analysis mode:")
    window.addstr(3, 0, "1. Single stock (detailed criteria)")
    window.addstr(4, 0, "2. Multiple stocks (summary only)")
    window.refresh()

    choice = window.getch()
    if choice == ord('1'):
        return 'single'
    elif choice == ord('2'):
        return 'multi'
    else:
        return ''

def display_results(window, ticker_symbol, investor_results):
    def wait_and_clear():
        window.addstr(curses.LINES - 1, 0, "Press any key to continue...")
        window.refresh()
        window.getch()
        window.clear()

    window.clear()
    line_index = 2
    window.addstr(0, 0, f"Results for {ticker_symbol}:\n\n")

    max_lines = curses.LINES - 2

    for name, results in investor_results.items():
        criteria = results['criteria']
        passes = results['passes']

        if len(investor_results) == 1:
            window.addstr(line_index, 0, f"{name} Results:")
            line_index += 1
            window.addstr(line_index, 0, f"Overall: {'PASS' if passes else 'FAIL'}")
            line_index += 1
            for key, passed in criteria.items():
                window.addstr(line_index, 0, f" - {key}: {'PASS' if passed else 'FAIL'}")
                line_index += 1
                if line_index >= max_lines:
                    wait_and_clear()
                    line_index = 2
        else:
            passed_tests = sum(criteria.values())
            total_tests = len(criteria)
            window.addstr(line_index, 0, f"{name} Summary: Passed {passed_tests} of {total_tests} tests")
            line_index += 1
            if line_index >= max_lines:
                wait_and_clear()
                line_index = 2

    window.refresh()

def main(stdscr):
    curses.curs_set(0)
    display_header(stdscr, "Stock Evaluation TUI")

    selected = get_investor_choice(stdscr)
    if not selected:
        stdscr.addstr(10, 0, "Invalid choice! Please select a valid option.")
        stdscr.refresh()
        stdscr.getch()
        return

    mode = get_analysis_mode(stdscr)
    if not mode:
        stdscr.addstr(10, 0, "Invalid analysis mode selected. Exiting...")
        stdscr.refresh()
        stdscr.getch()
        return

    if mode == 'single':
        ticker = get_ticker_input(stdscr)
        if not ticker:
            stdscr.addstr(10, 0, "No ticker symbol entered. Exiting...")
            stdscr.refresh()
            stdscr.getch()
            return

        investor_results = {}
        for name in selected:
            cls = INVESTOR_CLASSES[name]
            passed, criteria = cls.check_requirements(ticker)
            investor_results[name] = {"passes": passed, "criteria": criteria}

        display_results(stdscr, ticker, investor_results)

    elif mode == 'multi':
        tickers = []
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Enter ticker symbol (or press ENTER to finish): ")
            stdscr.refresh()
            ticker = get_ticker_input(stdscr)
            if not ticker:
                break
            tickers.append(ticker)

        stdscr.clear()
        line_index = 0
        max_lines = curses.LINES - 2

        for ticker in tickers:
            stdscr.addstr(line_index, 0, f"{ticker}:")
            line_index += 1

            for name in selected:
                cls = INVESTOR_CLASSES[name]
                passed, criteria = cls.check_requirements(ticker)
                summary = f"{name}: {'PASS' if passed else 'FAIL'} ({sum(criteria.values())}/{len(criteria)})"
                stdscr.addstr(line_index, 2, summary)
                line_index += 1

            line_index += 1

            if line_index >= max_lines:
                stdscr.addstr(curses.LINES - 1, 0, "Press any key to continue...")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
                line_index = 0

        stdscr.refresh()

    stdscr.addstr(curses.LINES - 1, 0, "Press any key to exit.")
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
