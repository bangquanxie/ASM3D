# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ammf/protos/mini_batch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ammf/protos/mini_batch.proto',
  package='ammf.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x61mmf/protos/mini_batch.proto\x12\x0b\x61mmf.protos\"\x96\x01\n\x0fMiniBatchConfig\x12\x19\n\x11\x64\x65nsity_threshold\x18\x01 \x02(\x05\x12\x31\n\tp1_config\x18\x02 \x02(\x0b\x32\x1e.ammf.protos.MiniBatchp1Config\x12\x35\n\x0b\x61mmf_config\x18\x03 \x02(\x0b\x32 .ammf.protos.MiniBatchammfConfig\"h\n\x16MiniBatchIouThresholds\x12\x12\n\nneg_iou_lo\x18\x03 \x02(\x02\x12\x12\n\nneg_iou_hi\x18\x04 \x02(\x02\x12\x12\n\npos_iou_lo\x18\x05 \x02(\x02\x12\x12\n\npos_iou_hi\x18\x06 \x02(\x02\"\xbc\x01\n\x11MiniBatchp1Config\x12@\n\x11iou_2d_thresholds\x18\x01 \x01(\x0b\x32#.ammf.protos.MiniBatchIouThresholdsH\x00\x12@\n\x11iou_3d_thresholds\x18\x02 \x01(\x0b\x32#.ammf.protos.MiniBatchIouThresholdsH\x00\x12\x17\n\x0fmini_batch_size\x18\x03 \x02(\x05\x42\n\n\x08iou_type\"n\n\x13MiniBatchammfConfig\x12>\n\x11iou_2d_thresholds\x18\x01 \x02(\x0b\x32#.ammf.protos.MiniBatchIouThresholds\x12\x17\n\x0fmini_batch_size\x18\x02 \x02(\x05')
)




_MINIBATCHCONFIG = _descriptor.Descriptor(
  name='MiniBatchConfig',
  full_name='ammf.protos.MiniBatchConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='density_threshold', full_name='ammf.protos.MiniBatchConfig.density_threshold', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p1_config', full_name='ammf.protos.MiniBatchConfig.p1_config', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ammf_config', full_name='ammf.protos.MiniBatchConfig.ammf_config', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=196,
)


_MINIBATCHIOUTHRESHOLDS = _descriptor.Descriptor(
  name='MiniBatchIouThresholds',
  full_name='ammf.protos.MiniBatchIouThresholds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neg_iou_lo', full_name='ammf.protos.MiniBatchIouThresholds.neg_iou_lo', index=0,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neg_iou_hi', full_name='ammf.protos.MiniBatchIouThresholds.neg_iou_hi', index=1,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_iou_lo', full_name='ammf.protos.MiniBatchIouThresholds.pos_iou_lo', index=2,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_iou_hi', full_name='ammf.protos.MiniBatchIouThresholds.pos_iou_hi', index=3,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=302,
)


_MINIBATCHP1CONFIG = _descriptor.Descriptor(
  name='MiniBatchp1Config',
  full_name='ammf.protos.MiniBatchp1Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iou_2d_thresholds', full_name='ammf.protos.MiniBatchp1Config.iou_2d_thresholds', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iou_3d_thresholds', full_name='ammf.protos.MiniBatchp1Config.iou_3d_thresholds', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mini_batch_size', full_name='ammf.protos.MiniBatchp1Config.mini_batch_size', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='iou_type', full_name='ammf.protos.MiniBatchp1Config.iou_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=305,
  serialized_end=493,
)


_MINIBATCHAMMFCONFIG = _descriptor.Descriptor(
  name='MiniBatchammfConfig',
  full_name='ammf.protos.MiniBatchammfConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='iou_2d_thresholds', full_name='ammf.protos.MiniBatchammfConfig.iou_2d_thresholds', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mini_batch_size', full_name='ammf.protos.MiniBatchammfConfig.mini_batch_size', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=605,
)

_MINIBATCHCONFIG.fields_by_name['p1_config'].message_type = _MINIBATCHP1CONFIG
_MINIBATCHCONFIG.fields_by_name['ammf_config'].message_type = _MINIBATCHAMMFCONFIG
_MINIBATCHP1CONFIG.fields_by_name['iou_2d_thresholds'].message_type = _MINIBATCHIOUTHRESHOLDS
_MINIBATCHP1CONFIG.fields_by_name['iou_3d_thresholds'].message_type = _MINIBATCHIOUTHRESHOLDS
_MINIBATCHP1CONFIG.oneofs_by_name['iou_type'].fields.append(
  _MINIBATCHP1CONFIG.fields_by_name['iou_2d_thresholds'])
_MINIBATCHP1CONFIG.fields_by_name['iou_2d_thresholds'].containing_oneof = _MINIBATCHP1CONFIG.oneofs_by_name['iou_type']
_MINIBATCHP1CONFIG.oneofs_by_name['iou_type'].fields.append(
  _MINIBATCHP1CONFIG.fields_by_name['iou_3d_thresholds'])
_MINIBATCHP1CONFIG.fields_by_name['iou_3d_thresholds'].containing_oneof = _MINIBATCHP1CONFIG.oneofs_by_name['iou_type']
_MINIBATCHAMMFCONFIG.fields_by_name['iou_2d_thresholds'].message_type = _MINIBATCHIOUTHRESHOLDS
DESCRIPTOR.message_types_by_name['MiniBatchConfig'] = _MINIBATCHCONFIG
DESCRIPTOR.message_types_by_name['MiniBatchIouThresholds'] = _MINIBATCHIOUTHRESHOLDS
DESCRIPTOR.message_types_by_name['MiniBatchp1Config'] = _MINIBATCHP1CONFIG
DESCRIPTOR.message_types_by_name['MiniBatchammfConfig'] = _MINIBATCHAMMFCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MiniBatchConfig = _reflection.GeneratedProtocolMessageType('MiniBatchConfig', (_message.Message,), dict(
  DESCRIPTOR = _MINIBATCHCONFIG,
  __module__ = 'ammf.protos.mini_batch_pb2'
  # @@protoc_insertion_point(class_scope:ammf.protos.MiniBatchConfig)
  ))
_sym_db.RegisterMessage(MiniBatchConfig)

MiniBatchIouThresholds = _reflection.GeneratedProtocolMessageType('MiniBatchIouThresholds', (_message.Message,), dict(
  DESCRIPTOR = _MINIBATCHIOUTHRESHOLDS,
  __module__ = 'ammf.protos.mini_batch_pb2'
  # @@protoc_insertion_point(class_scope:ammf.protos.MiniBatchIouThresholds)
  ))
_sym_db.RegisterMessage(MiniBatchIouThresholds)

MiniBatchp1Config = _reflection.GeneratedProtocolMessageType('MiniBatchp1Config', (_message.Message,), dict(
  DESCRIPTOR = _MINIBATCHP1CONFIG,
  __module__ = 'ammf.protos.mini_batch_pb2'
  # @@protoc_insertion_point(class_scope:ammf.protos.MiniBatchp1Config)
  ))
_sym_db.RegisterMessage(MiniBatchp1Config)

MiniBatchammfConfig = _reflection.GeneratedProtocolMessageType('MiniBatchammfConfig', (_message.Message,), dict(
  DESCRIPTOR = _MINIBATCHAMMFCONFIG,
  __module__ = 'ammf.protos.mini_batch_pb2'
  # @@protoc_insertion_point(class_scope:ammf.protos.MiniBatchammfConfig)
  ))
_sym_db.RegisterMessage(MiniBatchammfConfig)


# @@protoc_insertion_point(module_scope)
