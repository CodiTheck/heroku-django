import sys
import traceback
from rest_framework.views import exception_handler
from rest_framework.response import Response
from . import ERRO


def strerr(tbobj):
    """ Fonction of Error tracked printing """
    msg = "\n";
    # msg += ''.join([' ' for _ in ERRO]) + "\t%16s %8s %64s\n" % ("FILE NAME", "LINENO", "MODULE/FUNCTION",);
    for tb in tbobj:
        msg += ERRO + "\t%16s %8d %64s\n" % (tb.name, tb.lineno, tb.filename,);
    return msg;


def api_exc_handler(exc, context):
    """ Program that is executed when an exception is raised
    in current processing.
    """
    response = exception_handler(exc, context);

    # get traceback error
    exc_type, exc_value, exc_traceback = sys.exc_info();
    tb = traceback.extract_tb(exc_traceback);
    if response is not None:
        return response;
    else:
        # exec_list = str(exc).split('DETAIL: ');
        # return Response({'error_message': exec_list[-1]}, status=400);
        print(strerr(tb));
        print(ERRO + f"{exc}");
        return Response({'error_message': (0xFF, list(exc.args))}, status=503);



