import pyWhat.regex_identifier


def export_cli(text):
    ident = pyWhat.regex_identifier.RegexIdentifier()
    return ident.check(text)

