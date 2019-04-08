import traceback


def exception_traceback_str(e):
    traceback_str = (str(e) + ':' + ''.join(traceback.format_tb(e.__traceback__))).replace('\n', ' ')
    return traceback_str
