# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cprotos.proto\x12\x06protos\"\xaf\x01\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12!\n\x05genre\x18\x04 \x01(\x0e\x32\x12.protos.Book.Genre\x12\x17\n\x0fpublishing_year\x18\x05 \x01(\x05\">\n\x05Genre\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x46ICTION\x10\x01\x12\x0f\n\x0bNON_FICTION\x10\x02\x12\n\n\x06POETRY\x10\x03\"\xae\x01\n\rInventoryItem\x12\x18\n\x10inventory_number\x18\x01 \x01(\x05\x12\x1c\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x0c.protos.BookH\x00\x12,\n\x06status\x18\x03 \x01(\x0e\x32\x1c.protos.InventoryItem.Status\"/\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tAVAILABLE\x10\x01\x12\t\n\x05TAKEN\x10\x02\x42\x06\n\x04item\"!\n\x0b\x42ookRequest\x12\x12\n\nISBNTOFIND\x18\x01 \x01(\t\"%\n\x12\x43reateBookResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2x\n\x10InventoryService\x12\x36\n\nCreateBook\x12\x0c.protos.Book\x1a\x1a.protos.CreateBookResponse\x12,\n\x07GetBook\x12\x13.protos.BookRequest\x1a\x0c.protos.Bookb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=25
  _BOOK._serialized_end=200
  _BOOK_GENRE._serialized_start=138
  _BOOK_GENRE._serialized_end=200
  _INVENTORYITEM._serialized_start=203
  _INVENTORYITEM._serialized_end=377
  _INVENTORYITEM_STATUS._serialized_start=322
  _INVENTORYITEM_STATUS._serialized_end=369
  _BOOKREQUEST._serialized_start=379
  _BOOKREQUEST._serialized_end=412
  _CREATEBOOKRESPONSE._serialized_start=414
  _CREATEBOOKRESPONSE._serialized_end=451
  _INVENTORYSERVICE._serialized_start=453
  _INVENTORYSERVICE._serialized_end=573
# @@protoc_insertion_point(module_scope)