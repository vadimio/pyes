#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Method(object):
  GET = 0
  PUT = 1
  POST = 2
  DELETE = 3
  HEAD = 4
  OPTIONS = 5

  _VALUES_TO_NAMES = {
    0: "GET",
    1: "PUT",
    2: "POST",
    3: "DELETE",
    4: "HEAD",
    5: "OPTIONS",
  }

  _NAMES_TO_VALUES = {
    "GET": 0,
    "PUT": 1,
    "POST": 2,
    "DELETE": 3,
    "HEAD": 4,
    "OPTIONS": 5,
  }

class Status(object):
  CONTINUE = 100
  SWITCHING_PROTOCOLS = 101
  OK = 200
  CREATED = 201
  ACCEPTED = 202
  NON_AUTHORITATIVE_INFORMATION = 203
  NO_CONTENT = 204
  RESET_CONTENT = 205
  PARTIAL_CONTENT = 206
  MULTI_STATUS = 207
  MULTIPLE_CHOICES = 300
  MOVED_PERMANENTLY = 301
  FOUND = 302
  SEE_OTHER = 303
  NOT_MODIFIED = 304
  USE_PROXY = 305
  TEMPORARY_REDIRECT = 307
  BAD_REQUEST = 400
  UNAUTHORIZED = 401
  PAYMENT_REQUIRED = 402
  FORBIDDEN = 403
  NOT_FOUND = 404
  METHOD_NOT_ALLOWED = 405
  NOT_ACCEPTABLE = 406
  PROXY_AUTHENTICATION = 407
  REQUEST_TIMEOUT = 408
  CONFLICT = 409
  GONE = 410
  LENGTH_REQUIRED = 411
  PRECONDITION_FAILED = 412
  REQUEST_ENTITY_TOO_LARGE = 413
  REQUEST_URI_TOO_LONG = 414
  UNSUPPORTED_MEDIA_TYPE = 415
  REQUESTED_RANGE_NOT_SATISFIED = 416
  EXPECTATION_FAILED = 417
  UNPROCESSABLE_ENTITY = 422
  LOCKED = 423
  FAILED_DEPENDENCY = 424
  INTERNAL_SERVER_ERROR = 500
  NOT_IMPLEMENTED = 501
  BAD_GATEWAY = 502
  SERVICE_UNAVAILABLE = 503
  GATEWAY_TIMEOUT = 504
  INSUFFICIENT_STORAGE = 506

  _VALUES_TO_NAMES = {
    100: "CONTINUE",
    101: "SWITCHING_PROTOCOLS",
    200: "OK",
    201: "CREATED",
    202: "ACCEPTED",
    203: "NON_AUTHORITATIVE_INFORMATION",
    204: "NO_CONTENT",
    205: "RESET_CONTENT",
    206: "PARTIAL_CONTENT",
    207: "MULTI_STATUS",
    300: "MULTIPLE_CHOICES",
    301: "MOVED_PERMANENTLY",
    302: "FOUND",
    303: "SEE_OTHER",
    304: "NOT_MODIFIED",
    305: "USE_PROXY",
    307: "TEMPORARY_REDIRECT",
    400: "BAD_REQUEST",
    401: "UNAUTHORIZED",
    402: "PAYMENT_REQUIRED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    405: "METHOD_NOT_ALLOWED",
    406: "NOT_ACCEPTABLE",
    407: "PROXY_AUTHENTICATION",
    408: "REQUEST_TIMEOUT",
    409: "CONFLICT",
    410: "GONE",
    411: "LENGTH_REQUIRED",
    412: "PRECONDITION_FAILED",
    413: "REQUEST_ENTITY_TOO_LARGE",
    414: "REQUEST_URI_TOO_LONG",
    415: "UNSUPPORTED_MEDIA_TYPE",
    416: "REQUESTED_RANGE_NOT_SATISFIED",
    417: "EXPECTATION_FAILED",
    422: "UNPROCESSABLE_ENTITY",
    423: "LOCKED",
    424: "FAILED_DEPENDENCY",
    500: "INTERNAL_SERVER_ERROR",
    501: "NOT_IMPLEMENTED",
    502: "BAD_GATEWAY",
    503: "SERVICE_UNAVAILABLE",
    504: "GATEWAY_TIMEOUT",
    506: "INSUFFICIENT_STORAGE",
  }

  _NAMES_TO_VALUES = {
    "CONTINUE": 100,
    "SWITCHING_PROTOCOLS": 101,
    "OK": 200,
    "CREATED": 201,
    "ACCEPTED": 202,
    "NON_AUTHORITATIVE_INFORMATION": 203,
    "NO_CONTENT": 204,
    "RESET_CONTENT": 205,
    "PARTIAL_CONTENT": 206,
    "MULTI_STATUS": 207,
    "MULTIPLE_CHOICES": 300,
    "MOVED_PERMANENTLY": 301,
    "FOUND": 302,
    "SEE_OTHER": 303,
    "NOT_MODIFIED": 304,
    "USE_PROXY": 305,
    "TEMPORARY_REDIRECT": 307,
    "BAD_REQUEST": 400,
    "UNAUTHORIZED": 401,
    "PAYMENT_REQUIRED": 402,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "METHOD_NOT_ALLOWED": 405,
    "NOT_ACCEPTABLE": 406,
    "PROXY_AUTHENTICATION": 407,
    "REQUEST_TIMEOUT": 408,
    "CONFLICT": 409,
    "GONE": 410,
    "LENGTH_REQUIRED": 411,
    "PRECONDITION_FAILED": 412,
    "REQUEST_ENTITY_TOO_LARGE": 413,
    "REQUEST_URI_TOO_LONG": 414,
    "UNSUPPORTED_MEDIA_TYPE": 415,
    "REQUESTED_RANGE_NOT_SATISFIED": 416,
    "EXPECTATION_FAILED": 417,
    "UNPROCESSABLE_ENTITY": 422,
    "LOCKED": 423,
    "FAILED_DEPENDENCY": 424,
    "INTERNAL_SERVER_ERROR": 500,
    "NOT_IMPLEMENTED": 501,
    "BAD_GATEWAY": 502,
    "SERVICE_UNAVAILABLE": 503,
    "GATEWAY_TIMEOUT": 504,
    "INSUFFICIENT_STORAGE": 506,
  }

class RestRequest(object):
  """
  Attributes:
   - method
   - uri
   - params
   - headers
   - body
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'method', None, None, ), # 1
    (2, TType.STRING, 'uri', None, None, ), # 2
    (3, TType.MAP, 'params', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'headers', (TType.STRING,None,TType.STRING,None), None, ), # 4
    (5, TType.STRING, 'body', None, None, ), # 5
  )

  def __init__(self, method=None, uri=None, params=None, headers=None, body=None,):
    self.method = method
    self.uri = uri
    self.params = params
    self.headers = headers
    self.body = body

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.method = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.uri = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.params = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin() 
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.params[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.headers = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = iprot.readString();
            self.headers[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.body = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RestRequest')
    if self.method != None:
      oprot.writeFieldBegin('method', TType.I32, 1)
      oprot.writeI32(self.method)
      oprot.writeFieldEnd()
    if self.uri != None:
      oprot.writeFieldBegin('uri', TType.STRING, 2)
      oprot.writeString(self.uri)
      oprot.writeFieldEnd()
    if self.params != None:
      oprot.writeFieldBegin('params', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.params))
      for kiter14,viter15 in self.params.items():
        oprot.writeString(kiter14)
        oprot.writeString(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.headers != None:
      oprot.writeFieldBegin('headers', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.headers))
      for kiter16,viter17 in self.headers.items():
        oprot.writeString(kiter16)
        oprot.writeString(viter17)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.body != None:
      oprot.writeFieldBegin('body', TType.STRING, 5)
      oprot.writeString(self.body)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RestResponse(object):
  """
  Attributes:
   - status
   - headers
   - body
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'status', None, None, ), # 1
    (2, TType.MAP, 'headers', (TType.STRING,None,TType.STRING,None), None, ), # 2
    (3, TType.STRING, 'body', None, None, ), # 3
  )

  def __init__(self, status=None, headers=None, body=None,):
    self.status = status
    self.headers = headers
    self.body = body

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.status = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.headers = {}
          (_ktype19, _vtype20, _size18 ) = iprot.readMapBegin() 
          for _i22 in xrange(_size18):
            _key23 = iprot.readString();
            _val24 = iprot.readString();
            self.headers[_key23] = _val24
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.body = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RestResponse')
    if self.status != None:
      oprot.writeFieldBegin('status', TType.I32, 1)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.headers != None:
      oprot.writeFieldBegin('headers', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.headers))
      for kiter25,viter26 in self.headers.items():
        oprot.writeString(kiter25)
        oprot.writeString(viter26)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.body != None:
      oprot.writeFieldBegin('body', TType.STRING, 3)
      oprot.writeString(self.body)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

