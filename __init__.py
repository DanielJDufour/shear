import argparse

BACKTICK = "`"
BACK_SLASH = "\\"
FORWARD_SLASH ="/"
SINGLE_QUOTE = "'"
DOUBLE_QUOTE = '"'
TRIPLE_SINGLE_QUOTE = SINGLE_QUOTE * 3
TRIPLE_DOUBLE_QUOTE = DOUBLE_QUOTE * 3
BYTE_MARKER = "b'"

DEFAULTS = [
    ( SINGLE_QUOTE, SINGLE_QUOTE ),
    ( DOUBLE_QUOTE, DOUBLE_QUOTE ),
    ( BACKTICK, BACKTICK ),
    ( TRIPLE_SINGLE_QUOTE, TRIPLE_SINGLE_QUOTE ),
    ( TRIPLE_DOUBLE_QUOTE, TRIPLE_DOUBLE_QUOTE ),
    ( BACK_SLASH + SINGLE_QUOTE, BACK_SLASH + SINGLE_QUOTE ),
    ( BACK_SLASH + DOUBLE_QUOTE, BACK_SLASH + DOUBLE_QUOTE ),
    ( BACK_SLASH + BACKTICK, BACK_SLASH + BACKTICK ),
    ( BYTE_MARKER, SINGLE_QUOTE )
]

def shear(value, chars=DEFAULTS, debug=False):

    if value is None: return

    for i in range(5):
        sheared = False
        for start, end in chars:
            if value.startswith(start) and value.endswith(end):
                value = value[len(start):-len(end)]
                sheared = True
        if not sheared:
            break

    return value

if __name__ == "__main__":
    # execute only if run as a script
    parser = argparse.ArgumentParser()
    parser.add_argument('value')
    parser.add_argument('-c', '--chars')
    parser.add_argument('-d', '--debug', choices=["", "true", "TRUE", "True"])
    args = parser.parse_args()

    chars = shear(args.chars).split(',') if isinstance(args.chars, str) else None
    debug = shear(args.debug) if isinstance(args.debug, str) else False

    if not isinstance(args.value, str):
        raise Exception("[shear] you did not pass in a string to shear")

    result = shear(args.value, chars=chars, debug=debug)

    print(result, end='')
