from flask_restful import Resource, reqparse


class Translator(Resource):
    """Receive an valid input and calculate it translation"""

    def __init__(self):
        self.to_roman_dict = {
            "kil": "I",
            "jin": "V",
            "pol": "X",
            "kilow": "L",
            "jij": "C",
            "jinjin": "D",
            "polsx": "M",
        }

        self.to_decimal_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    def _translate_to_roman(self, user_input):
        parsed_input = user_input.split(" ")

        response = [
            self.to_roman_dict.get(kwegonian_text) for kwegonian_text in parsed_input
        ]

        return response

    def _translate_to_decimal(self, roman_numerals):
        def _convert_roman_to_decimal(roman_values):
            total = 0
            for value in range(len(roman_values) - 1):
                if roman_values[value] < roman_values[value + 1]:
                    total -= roman_values[value]
                else:
                    total += roman_values[value]

            total += roman_values[-1]
            return total

        response = [
            self.to_decimal_dict.get(roman_text) for roman_text in roman_numerals
        ]
        total_decimal = _convert_roman_to_decimal(response)
        print(total_decimal)

        return response

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("input", type=str, required=True)
        args = parser.parse_args()

        roman_list = self._translate_to_roman(args.get("input", ""))

        final_translation = self._translate_to_decimal(roman_list)
        return {"status": "200"}
