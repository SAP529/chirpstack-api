# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/device.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.as_pb.external.api import frameLog_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_frameLog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.chirpstack-api/as_pb/external/api/device.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\x30\x63hirpstack-api/as_pb/external/api/frameLog.proto\"\x95\x03\n\x06\x44\x65vice\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x0e\x61pplication_id\x18\x03 \x01(\x03R\rapplicationID\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12*\n\x11\x64\x65vice_profile_id\x18\x05 \x01(\tR\x0f\x64\x65viceProfileID\x12\x18\n\x10skip_f_cnt_check\x18\x06 \x01(\x08\x12\x1a\n\x12reference_altitude\x18\x07 \x01(\x01\x12-\n\tvariables\x18\x08 \x03(\x0b\x32\x1a.api.Device.VariablesEntry\x12#\n\x04tags\x18\t \x03(\x0b\x32\x15.api.Device.TagsEntry\x12\x13\n\x0bis_disabled\x18\n \x01(\x08\x1a\x30\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x03\n\x0e\x44\x65viceListItem\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x0e\x61pplication_id\x18\x03 \x01(\x03R\rapplicationID\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12*\n\x11\x64\x65vice_profile_id\x18\x05 \x01(\tR\x0f\x64\x65viceProfileID\x12\x1b\n\x13\x64\x65vice_profile_name\x18\x06 \x01(\t\x12\x1d\n\x15\x64\x65vice_status_battery\x18\x07 \x01(\r\x12\x1c\n\x14\x64\x65vice_status_margin\x18\x08 \x01(\x05\x12+\n#device_status_external_power_source\x18\n \x01(\x08\x12/\n\'device_status_battery_level_unavailable\x18\x0b \x01(\x08\x12#\n\x1b\x64\x65vice_status_battery_level\x18\x0c \x01(\x02\x12<\n\x0clast_seen_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastSeenAt\"\\\n\nDeviceKeys\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x0f\n\x07nwk_key\x18\x02 \x01(\t\x12\x0f\n\x07\x61pp_key\x18\x03 \x01(\t\x12\x13\n\x0bgen_app_key\x18\x04 \x01(\t\"2\n\x13\x43reateDeviceRequest\x12\x1b\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0b.api.Device\"+\n\x10GetDeviceRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"\xcf\x01\n\x11GetDeviceResponse\x12\x1b\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0b.api.Device\x12<\n\x0clast_seen_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastSeenAt\x12\x1d\n\x15\x64\x65vice_status_battery\x18\x06 \x01(\r\x12\x1c\n\x14\x64\x65vice_status_margin\x18\x14 \x01(\x05\x12\"\n\x08location\x18\x15 \x01(\x0b\x32\x10.common.Location\"\xa2\x02\n\x11ListDeviceRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\x12%\n\x0e\x61pplication_id\x18\x03 \x01(\x03R\rapplicationID\x12\x0e\n\x06search\x18\x04 \x01(\t\x12,\n\x12multicast_group_id\x18\x05 \x01(\tR\x10multicastGroupID\x12,\n\x12service_profile_id\x18\x06 \x01(\tR\x10serviceProfileID\x12.\n\x04tags\x18\x07 \x03(\x0b\x32 .api.ListDeviceRequest.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"N\n\x12ListDeviceResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12#\n\x06result\x18\x02 \x03(\x0b\x32\x13.api.DeviceListItem\".\n\x13\x44\x65leteDeviceRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"2\n\x13UpdateDeviceRequest\x12\x1b\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x0b.api.Device\"?\n\x17\x43reateDeviceKeysRequest\x12$\n\x0b\x64\x65vice_keys\x18\x01 \x01(\x0b\x32\x0f.api.DeviceKeys\"/\n\x14GetDeviceKeysRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"=\n\x15GetDeviceKeysResponse\x12$\n\x0b\x64\x65vice_keys\x18\x01 \x01(\x0b\x32\x0f.api.DeviceKeys\"?\n\x17UpdateDeviceKeysRequest\x12$\n\x0b\x64\x65vice_keys\x18\x01 \x01(\x0b\x32\x0f.api.DeviceKeys\"2\n\x17\x44\x65leteDeviceKeysRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"\xd7\x01\n\x10\x44\x65viceActivation\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x10\n\x08\x64\x65v_addr\x18\x02 \x01(\t\x12\x11\n\tapp_s_key\x18\x03 \x01(\t\x12\x15\n\rnwk_s_enc_key\x18\x04 \x01(\t\x12\x17\n\x0fs_nwk_s_int_key\x18\x08 \x01(\t\x12\x17\n\x0f\x66_nwk_s_int_key\x18\t \x01(\t\x12\x10\n\x08\x66_cnt_up\x18\x05 \x01(\r\x12\x14\n\x0cn_f_cnt_down\x18\x06 \x01(\r\x12\x14\n\x0c\x61_f_cnt_down\x18\n \x01(\r\"I\n\x15\x41\x63tivateDeviceRequest\x12\x30\n\x11\x64\x65vice_activation\x18\x01 \x01(\x0b\x32\x15.api.DeviceActivation\"2\n\x17\x44\x65\x61\x63tivateDeviceRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"5\n\x1aGetDeviceActivationRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"O\n\x1bGetDeviceActivationResponse\x12\x30\n\x11\x64\x65vice_activation\x18\x01 \x01(\x0b\x32\x15.api.DeviceActivation\"2\n\x17GetRandomDevAddrRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\",\n\x18GetRandomDevAddrResponse\x12\x10\n\x08\x64\x65v_addr\x18\x01 \x01(\t\"\xd3\x03\n\x0b\x44\x65viceStats\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nrx_packets\x18\x02 \x01(\r\x12\x0f\n\x07gw_rssi\x18\x03 \x01(\x02\x12\x0e\n\x06gw_snr\x18\x04 \x01(\x02\x12M\n\x18rx_packets_per_frequency\x18\x05 \x03(\x0b\x32+.api.DeviceStats.RxPacketsPerFrequencyEntry\x12?\n\x11rx_packets_per_dr\x18\x06 \x03(\x0b\x32$.api.DeviceStats.RxPacketsPerDrEntry\x12,\n\x06\x65rrors\x18\x07 \x03(\x0b\x32\x1c.api.DeviceStats.ErrorsEntry\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13RxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a-\n\x0b\x45rrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\xaa\x01\n\x15GetDeviceStatsRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x10\n\x08interval\x18\x02 \x01(\t\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\":\n\x16GetDeviceStatsResponse\x12 \n\x06result\x18\x01 \x03(\x0b\x32\x10.api.DeviceStats\"7\n\x1cStreamDeviceFrameLogsRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"\x86\x01\n\x1dStreamDeviceFrameLogsResponse\x12+\n\x0cuplink_frame\x18\x01 \x01(\x0b\x32\x13.api.UplinkFrameLogH\x00\x12/\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x15.api.DownlinkFrameLogH\x00\x42\x07\n\x05\x66rame\"7\n\x1cStreamDeviceEventLogsRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"\x9f\x01\n\x1dStreamDeviceEventLogsResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12!\n\x0cpayload_json\x18\x02 \x01(\tR\x0bpayloadJSON\x12\x30\n\x0cpublished_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\tstream_id\x18\x04 \x01(\tR\x08streamID\"3\n\x18\x43learDeviceNoncesRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"1\n\x16GetDeviceStatusRequest\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\"B\n\x17GetDeviceStatusResponse\x12\x17\n\x07\x64\x65v_eui\x18\x01 \x01(\tR\x06\x64\x65vEUI\x12\x0e\n\x06status\x18\x02 \x01(\t2\xd1\x0f\n\rDeviceService\x12S\n\x06\x43reate\x12\x18.api.CreateDeviceRequest\x1a\x16.google.protobuf.Empty\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/api/devices:\x01*\x12T\n\x03Get\x12\x15.api.GetDeviceRequest\x1a\x16.api.GetDeviceResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/api/devices/{dev_eui}\x12M\n\x04List\x12\x16.api.ListDeviceRequest\x1a\x17.api.ListDeviceResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/devices\x12Z\n\x06\x44\x65lete\x12\x18.api.DeleteDeviceRequest\x1a\x16.google.protobuf.Empty\"\x1e\x82\xd3\xe4\x93\x02\x18*\x16/api/devices/{dev_eui}\x12\x64\n\x06Update\x12\x18.api.UpdateDeviceRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\x1a\x1d/api/devices/{device.dev_eui}:\x01*\x12v\n\nCreateKeys\x12\x1c.api.CreateDeviceKeysRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/api/devices/{device_keys.dev_eui}/keys:\x01*\x12\x65\n\x07GetKeys\x12\x19.api.GetDeviceKeysRequest\x1a\x1a.api.GetDeviceKeysResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/devices/{dev_eui}/keys\x12v\n\nUpdateKeys\x12\x1c.api.UpdateDeviceKeysRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\x1a\'/api/devices/{device_keys.dev_eui}/keys:\x01*\x12g\n\nDeleteKeys\x12\x1c.api.DeleteDeviceKeysRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/api/devices/{dev_eui}/keys\x12|\n\x08\x41\x63tivate\x12\x1a.api.ActivateDeviceRequest\x1a\x16.google.protobuf.Empty\"<\x82\xd3\xe4\x93\x02\x36\"1/api/devices/{device_activation.dev_eui}/activate:\x01*\x12m\n\nDeactivate\x12\x1c.api.DeactivateDeviceRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/api/devices/{dev_eui}/activation\x12}\n\rGetActivation\x12\x1f.api.GetDeviceActivationRequest\x1a .api.GetDeviceActivationResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/devices/{dev_eui}/activation\x12\x80\x01\n\x10GetRandomDevAddr\x12\x1c.api.GetRandomDevAddrRequest\x1a\x1d.api.GetRandomDevAddrResponse\"/\x82\xd3\xe4\x93\x02)\"\'/api/devices/{dev_eui}/getRandomDevAddr\x12i\n\x08GetStats\x12\x1a.api.GetDeviceStatsRequest\x1a\x1b.api.GetDeviceStatsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/api/devices/{dev_eui}/stats\x12\x81\x01\n\x0fStreamFrameLogs\x12!.api.StreamDeviceFrameLogsRequest\x1a\".api.StreamDeviceFrameLogsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/devices/{dev_eui}/frames0\x01\x12\x81\x01\n\x0fStreamEventLogs\x12!.api.StreamDeviceEventLogsRequest\x1a\".api.StreamDeviceEventLogsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/devices/{dev_eui}/events0\x01\x12s\n\x11\x43learDeviceNonces\x12\x1d.api.ClearDeviceNoncesRequest\x1a\x16.google.protobuf.Empty\"\'\x82\xd3\xe4\x93\x02!*\x1f/api/devices/{dev_eui}/devnonce\x12m\n\tGetStatus\x12\x1b.api.GetDeviceStatusRequest\x1a\x1c.api.GetDeviceStatusResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/devices/{dev_eui}/statusBj\n!io.chirpstack.api.as.external.apiB\x0b\x44\x65viceProtoP\x01Z6github.com/SAP529/chirpstack-api/go/v4/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.device_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\013DeviceProtoP\001Z6github.com/SAP529/chirpstack-api/go/v4/as/external/api'
  _DEVICE_VARIABLESENTRY._options = None
  _DEVICE_VARIABLESENTRY._serialized_options = b'8\001'
  _DEVICE_TAGSENTRY._options = None
  _DEVICE_TAGSENTRY._serialized_options = b'8\001'
  _LISTDEVICEREQUEST_TAGSENTRY._options = None
  _LISTDEVICEREQUEST_TAGSENTRY._serialized_options = b'8\001'
  _DEVICESTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _DEVICESTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _DEVICESTATS_RXPACKETSPERDRENTRY._options = None
  _DEVICESTATS_RXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _DEVICESTATS_ERRORSENTRY._options = None
  _DEVICESTATS_ERRORSENTRY._serialized_options = b'8\001'
  _DEVICESERVICE.methods_by_name['Create']._options = None
  _DEVICESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\021\"\014/api/devices:\001*'
  _DEVICESERVICE.methods_by_name['Get']._options = None
  _DEVICESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\030\022\026/api/devices/{dev_eui}'
  _DEVICESERVICE.methods_by_name['List']._options = None
  _DEVICESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\016\022\014/api/devices'
  _DEVICESERVICE.methods_by_name['Delete']._options = None
  _DEVICESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\030*\026/api/devices/{dev_eui}'
  _DEVICESERVICE.methods_by_name['Update']._options = None
  _DEVICESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\"\032\035/api/devices/{device.dev_eui}:\001*'
  _DEVICESERVICE.methods_by_name['CreateKeys']._options = None
  _DEVICESERVICE.methods_by_name['CreateKeys']._serialized_options = b'\202\323\344\223\002,\"\'/api/devices/{device_keys.dev_eui}/keys:\001*'
  _DEVICESERVICE.methods_by_name['GetKeys']._options = None
  _DEVICESERVICE.methods_by_name['GetKeys']._serialized_options = b'\202\323\344\223\002\035\022\033/api/devices/{dev_eui}/keys'
  _DEVICESERVICE.methods_by_name['UpdateKeys']._options = None
  _DEVICESERVICE.methods_by_name['UpdateKeys']._serialized_options = b'\202\323\344\223\002,\032\'/api/devices/{device_keys.dev_eui}/keys:\001*'
  _DEVICESERVICE.methods_by_name['DeleteKeys']._options = None
  _DEVICESERVICE.methods_by_name['DeleteKeys']._serialized_options = b'\202\323\344\223\002\035*\033/api/devices/{dev_eui}/keys'
  _DEVICESERVICE.methods_by_name['Activate']._options = None
  _DEVICESERVICE.methods_by_name['Activate']._serialized_options = b'\202\323\344\223\0026\"1/api/devices/{device_activation.dev_eui}/activate:\001*'
  _DEVICESERVICE.methods_by_name['Deactivate']._options = None
  _DEVICESERVICE.methods_by_name['Deactivate']._serialized_options = b'\202\323\344\223\002#*!/api/devices/{dev_eui}/activation'
  _DEVICESERVICE.methods_by_name['GetActivation']._options = None
  _DEVICESERVICE.methods_by_name['GetActivation']._serialized_options = b'\202\323\344\223\002#\022!/api/devices/{dev_eui}/activation'
  _DEVICESERVICE.methods_by_name['GetRandomDevAddr']._options = None
  _DEVICESERVICE.methods_by_name['GetRandomDevAddr']._serialized_options = b'\202\323\344\223\002)\"\'/api/devices/{dev_eui}/getRandomDevAddr'
  _DEVICESERVICE.methods_by_name['GetStats']._options = None
  _DEVICESERVICE.methods_by_name['GetStats']._serialized_options = b'\202\323\344\223\002\036\022\034/api/devices/{dev_eui}/stats'
  _DEVICESERVICE.methods_by_name['StreamFrameLogs']._options = None
  _DEVICESERVICE.methods_by_name['StreamFrameLogs']._serialized_options = b'\202\323\344\223\002\037\022\035/api/devices/{dev_eui}/frames'
  _DEVICESERVICE.methods_by_name['StreamEventLogs']._options = None
  _DEVICESERVICE.methods_by_name['StreamEventLogs']._serialized_options = b'\202\323\344\223\002\037\022\035/api/devices/{dev_eui}/events'
  _DEVICESERVICE.methods_by_name['ClearDeviceNonces']._options = None
  _DEVICESERVICE.methods_by_name['ClearDeviceNonces']._serialized_options = b'\202\323\344\223\002!*\037/api/devices/{dev_eui}/devnonce'
  _DEVICESERVICE.methods_by_name['GetStatus']._options = None
  _DEVICESERVICE.methods_by_name['GetStatus']._serialized_options = b'\202\323\344\223\002\037\022\035/api/devices/{dev_eui}/status'
  _DEVICE._serialized_start=234
  _DEVICE._serialized_end=639
  _DEVICE_VARIABLESENTRY._serialized_start=546
  _DEVICE_VARIABLESENTRY._serialized_end=594
  _DEVICE_TAGSENTRY._serialized_start=596
  _DEVICE_TAGSENTRY._serialized_end=639
  _DEVICELISTITEM._serialized_start=642
  _DEVICELISTITEM._serialized_end=1084
  _DEVICEKEYS._serialized_start=1086
  _DEVICEKEYS._serialized_end=1178
  _CREATEDEVICEREQUEST._serialized_start=1180
  _CREATEDEVICEREQUEST._serialized_end=1230
  _GETDEVICEREQUEST._serialized_start=1232
  _GETDEVICEREQUEST._serialized_end=1275
  _GETDEVICERESPONSE._serialized_start=1278
  _GETDEVICERESPONSE._serialized_end=1485
  _LISTDEVICEREQUEST._serialized_start=1488
  _LISTDEVICEREQUEST._serialized_end=1778
  _LISTDEVICEREQUEST_TAGSENTRY._serialized_start=596
  _LISTDEVICEREQUEST_TAGSENTRY._serialized_end=639
  _LISTDEVICERESPONSE._serialized_start=1780
  _LISTDEVICERESPONSE._serialized_end=1858
  _DELETEDEVICEREQUEST._serialized_start=1860
  _DELETEDEVICEREQUEST._serialized_end=1906
  _UPDATEDEVICEREQUEST._serialized_start=1908
  _UPDATEDEVICEREQUEST._serialized_end=1958
  _CREATEDEVICEKEYSREQUEST._serialized_start=1960
  _CREATEDEVICEKEYSREQUEST._serialized_end=2023
  _GETDEVICEKEYSREQUEST._serialized_start=2025
  _GETDEVICEKEYSREQUEST._serialized_end=2072
  _GETDEVICEKEYSRESPONSE._serialized_start=2074
  _GETDEVICEKEYSRESPONSE._serialized_end=2135
  _UPDATEDEVICEKEYSREQUEST._serialized_start=2137
  _UPDATEDEVICEKEYSREQUEST._serialized_end=2200
  _DELETEDEVICEKEYSREQUEST._serialized_start=2202
  _DELETEDEVICEKEYSREQUEST._serialized_end=2252
  _DEVICEACTIVATION._serialized_start=2255
  _DEVICEACTIVATION._serialized_end=2470
  _ACTIVATEDEVICEREQUEST._serialized_start=2472
  _ACTIVATEDEVICEREQUEST._serialized_end=2545
  _DEACTIVATEDEVICEREQUEST._serialized_start=2547
  _DEACTIVATEDEVICEREQUEST._serialized_end=2597
  _GETDEVICEACTIVATIONREQUEST._serialized_start=2599
  _GETDEVICEACTIVATIONREQUEST._serialized_end=2652
  _GETDEVICEACTIVATIONRESPONSE._serialized_start=2654
  _GETDEVICEACTIVATIONRESPONSE._serialized_end=2733
  _GETRANDOMDEVADDRREQUEST._serialized_start=2735
  _GETRANDOMDEVADDRREQUEST._serialized_end=2785
  _GETRANDOMDEVADDRRESPONSE._serialized_start=2787
  _GETRANDOMDEVADDRRESPONSE._serialized_end=2831
  _DEVICESTATS._serialized_start=2834
  _DEVICESTATS._serialized_end=3301
  _DEVICESTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=3139
  _DEVICESTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=3199
  _DEVICESTATS_RXPACKETSPERDRENTRY._serialized_start=3201
  _DEVICESTATS_RXPACKETSPERDRENTRY._serialized_end=3254
  _DEVICESTATS_ERRORSENTRY._serialized_start=3256
  _DEVICESTATS_ERRORSENTRY._serialized_end=3301
  _GETDEVICESTATSREQUEST._serialized_start=3304
  _GETDEVICESTATSREQUEST._serialized_end=3474
  _GETDEVICESTATSRESPONSE._serialized_start=3476
  _GETDEVICESTATSRESPONSE._serialized_end=3534
  _STREAMDEVICEFRAMELOGSREQUEST._serialized_start=3536
  _STREAMDEVICEFRAMELOGSREQUEST._serialized_end=3591
  _STREAMDEVICEFRAMELOGSRESPONSE._serialized_start=3594
  _STREAMDEVICEFRAMELOGSRESPONSE._serialized_end=3728
  _STREAMDEVICEEVENTLOGSREQUEST._serialized_start=3730
  _STREAMDEVICEEVENTLOGSREQUEST._serialized_end=3785
  _STREAMDEVICEEVENTLOGSRESPONSE._serialized_start=3788
  _STREAMDEVICEEVENTLOGSRESPONSE._serialized_end=3947
  _CLEARDEVICENONCESREQUEST._serialized_start=3949
  _CLEARDEVICENONCESREQUEST._serialized_end=4000
  _GETDEVICESTATUSREQUEST._serialized_start=4002
  _GETDEVICESTATUSREQUEST._serialized_end=4051
  _GETDEVICESTATUSRESPONSE._serialized_start=4053
  _GETDEVICESTATUSRESPONSE._serialized_end=4119
  _DEVICESERVICE._serialized_start=4122
  _DEVICESERVICE._serialized_end=6123
# @@protoc_insertion_point(module_scope)
