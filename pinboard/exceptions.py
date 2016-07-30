# import urllib2
import urllib.error

class PinboardError(Exception):
    pass

class PinboardServerError(urllib.error.HTTPError):
    pass

class PinboardServiceUnavailable(urllib.error.HTTPError):
    pass

class PinboardAuthenticationError(urllib.error.HTTPError):
    pass

class PinboardForbiddenError(urllib.error.HTTPError):
    pass

