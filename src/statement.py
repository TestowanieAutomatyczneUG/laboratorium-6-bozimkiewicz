import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount/100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


class StatementTest(unittest.TestCase):
    def test_empty_performances(self):
        self.assertEqual('Statement for BigCo\nAmount owed is $0.00\nYou earned 0 credits\n',
                         statement({"customer": "BigCo", "performances": []}, {}))

    def test_comedy_audience_less_equal_20(self):
        self.assertEqual('Statement for BigCo\n As You Like It: $360.00 (20 seats)\nAmount owed is $360.00\nYou earned 4 credits\n',
                         statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 20}]},
                                   {"as-like": {"type": "comedy", "name": "As You Like It"}}))

    def test_comedy_audience_more_than_20(self):
        self.assertEqual('Statement for BigCo\n As You Like It: $468.00 (21 seats)\nAmount owed is $468.00\nYou earned 4 credits\n',
                         statement({"customer": "BigCo", "performances": [{"playID": "as-like", "audience": 21}]},
                                   {"as-like": {"type": "comedy", "name": "As You Like It"}}))

    def test_tragedy_audience_less_equal_30(self):
        self.assertEqual('Statement for BigCo\n Hamlet: $400.00 (30 seats)\nAmount owed is $400.00\nYou earned 0 credits\n',
                         statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 30}]},
                                   {"hamlet": {"type": "tragedy", "name": "Hamlet"}}))

    def test_tragedy_audience_more_than_30(self):
        self.assertEqual('Statement for BigCo\n Hamlet: $450.00 (35 seats)\nAmount owed is $450.00\nYou earned 5 credits\n',
                         statement({"customer": "BigCo", "performances": [{"playID": "hamlet", "audience": 35}]},
                                   {"hamlet": {"type": "tragedy", "name": "Hamlet"}}))

    def test_play_type_unknown_error(self):
        self.assertRaises(ValueError, statement, {"customer": "BigCo", "performances": [{"playID": "as-like"}]}, {"as-like": {"type": "Different"}})

    def test_performance_empty(self):
        self.assertRaises(KeyError, statement, {"customer": "BigCo"}, {})

    def test_customer_empty(self):
        self.assertRaises(KeyError, statement, {}, {"hamlet": {"type": "tragedy", "name": "Hamlet"}})
