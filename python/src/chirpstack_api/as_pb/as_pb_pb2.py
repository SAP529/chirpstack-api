# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/as_pb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n chirpstack-api/as_pb/as_pb.proto\x12\x02\x61s\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"S\n\x17\x44\x65viceActivationContext\x12\x10\n\x08\x64\x65v_addr\x18\x01 \x01(\x0c\x12&\n\tapp_s_key\x18\x02 \x01(\x0b\x32\x13.common.KeyEnvelope\"\xa2\x02\n\x17HandleUplinkDataRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x10\n\x08join_eui\x18\x02 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x03 \x01(\r\x12\x0e\n\x06\x66_port\x18\x04 \x01(\r\x12\x0b\n\x03\x61\x64r\x18\x05 \x01(\x08\x12\n\n\x02\x64r\x18\x06 \x01(\r\x12!\n\x07tx_info\x18\x07 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x08 \x03(\x0b\x32\x10.gw.UplinkRXInfo\x12\x0c\n\x04\x64\x61ta\x18\t \x01(\x0c\x12>\n\x19\x64\x65vice_activation_context\x18\n \x01(\x0b\x32\x1b.as.DeviceActivationContext\x12\x18\n\x10\x63onfirmed_uplink\x18\x0b \x01(\x08\"\x88\x01\n\x1eHandleProprietaryUplinkRequest\x12\x13\n\x0bmac_payload\x18\x01 \x01(\x0c\x12\x0b\n\x03mic\x18\x02 \x01(\x0c\x12!\n\x07tx_info\x18\x03 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x04 \x03(\x0b\x32\x10.gw.UplinkRXInfo\"`\n\x12HandleErrorRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x1b\n\x04type\x18\x03 \x01(\x0e\x32\r.as.ErrorType\x12\r\n\x05\x65rror\x18\x04 \x01(\t\x12\r\n\x05\x66_cnt\x18\x05 \x01(\r\"P\n\x18HandleDownlinkACKRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x14\n\x0c\x61\x63knowledged\x18\x03 \x01(\x08\"\xa3\x01\n\x16SetDeviceStatusRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62\x61ttery\x18\x02 \x01(\r\x12\x0e\n\x06margin\x18\x03 \x01(\x05\x12\x1d\n\x15\x65xternal_power_source\x18\x04 \x01(\x08\x12!\n\x19\x62\x61ttery_level_unavailable\x18\x05 \x01(\x08\x12\x15\n\rbattery_level\x18\x06 \x01(\x02\"c\n\x18SetDeviceLocationRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\"\n\x08location\x18\x02 \x01(\x0b\x32\x10.common.Location\x12\x12\n\nuplink_ids\x18\x03 \x03(\x0c\"\xc4\x08\n\x19HandleGatewayStatsRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\x0c\x12\x10\n\x08stats_id\x18\x02 \x01(\x0c\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x08location\x18\x04 \x01(\x0b\x32\x10.common.Location\x12\x1b\n\x13rx_packets_received\x18\x05 \x01(\r\x12\x1e\n\x16rx_packets_received_ok\x18\x06 \x01(\r\x12\x1b\n\x13tx_packets_received\x18\x07 \x01(\r\x12\x1a\n\x12tx_packets_emitted\x18\x08 \x01(\r\x12=\n\x08metadata\x18\t \x03(\x0b\x32+.as.HandleGatewayStatsRequest.MetadataEntry\x12Z\n\x18tx_packets_per_frequency\x18\n \x03(\x0b\x32\x38.as.HandleGatewayStatsRequest.TxPacketsPerFrequencyEntry\x12Z\n\x18rx_packets_per_frequency\x18\x0b \x03(\x0b\x32\x38.as.HandleGatewayStatsRequest.RxPacketsPerFrequencyEntry\x12L\n\x11tx_packets_per_dr\x18\x0c \x03(\x0b\x32\x31.as.HandleGatewayStatsRequest.TxPacketsPerDrEntry\x12L\n\x11rx_packets_per_dr\x18\r \x03(\x0b\x32\x31.as.HandleGatewayStatsRequest.RxPacketsPerDrEntry\x12T\n\x15tx_packets_per_status\x18\x0e \x03(\x0b\x32\x35.as.HandleGatewayStatsRequest.TxPacketsPerStatusEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13TxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13RxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"m\n\x12HandleTxAckRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x12\n\ngateway_id\x18\x03 \x01(\x0c\x12#\n\x07tx_info\x18\x04 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\"\x87\x01\n ReEncryptDeviceQueueItemsRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\x0c\x12\x10\n\x08\x64\x65v_addr\x18\x02 \x01(\x0c\x12\x13\n\x0b\x66_cnt_start\x18\x03 \x01(\r\x12+\n\x05items\x18\x04 \x03(\x0b\x32\x1c.as.ReEncryptDeviceQueueItem\"R\n!ReEncryptDeviceQueueItemsResponse\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.as.ReEncryptedDeviceQueueItem\"a\n\x18ReEncryptDeviceQueueItem\x12\x13\n\x0b\x66rm_payload\x18\x01 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x0e\n\x06\x66_port\x18\x03 \x01(\r\x12\x11\n\tconfirmed\x18\x04 \x01(\x08\"c\n\x1aReEncryptedDeviceQueueItem\x12\x13\n\x0b\x66rm_payload\x18\x01 \x01(\x0c\x12\r\n\x05\x66_cnt\x18\x02 \x01(\r\x12\x0e\n\x06\x66_port\x18\x03 \x01(\r\x12\x11\n\tconfirmed\x18\x04 \x01(\x08\"\x9a\x01\n\x16HandleConnStateRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\x0cR\tgatewayID\x12\x18\n\x05state\x18\x02 \x01(\x0e\x32\t.gw.State\x12\x10\n\x08stats_id\x18\x03 \x01(\x0c\x12\x13\n\x0bis_retained\x18\x04 \x01(\x08\" \n\x05State\x12\x0b\n\x07OFFLINE\x10\x00\x12\n\n\x06ONLINE\x10\x01*\x1c\n\x08RXWindow\x12\x07\n\x03RX1\x10\x00\x12\x07\n\x03RX2\x10\x01*\xbb\x01\n\tErrorType\x12\x0b\n\x07GENERIC\x10\x00\x12\x08\n\x04OTAA\x10\x01\x12\x16\n\x12\x44\x41TA_UP_FCNT_RESET\x10\x02\x12\x0f\n\x0b\x44\x41TA_UP_MIC\x10\x03\x12\x1a\n\x16\x44\x45VICE_QUEUE_ITEM_SIZE\x10\x04\x12\x1a\n\x16\x44\x45VICE_QUEUE_ITEM_FCNT\x10\x05\x12\x1f\n\x1b\x44\x41TA_UP_FCNT_RETRANSMISSION\x10\x06\x12\x15\n\x11\x44\x41TA_DOWN_GATEWAY\x10\x07\x32\xae\x06\n\x18\x41pplicationServerService\x12I\n\x10HandleUplinkData\x12\x1b.as.HandleUplinkDataRequest\x1a\x16.google.protobuf.Empty\"\x00\x12W\n\x17HandleProprietaryUplink\x12\".as.HandleProprietaryUplinkRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x0bHandleError\x12\x16.as.HandleErrorRequest\x1a\x16.google.protobuf.Empty\"\x00\x12K\n\x11HandleDownlinkACK\x12\x1c.as.HandleDownlinkACKRequest\x1a\x16.google.protobuf.Empty\"\x00\x12M\n\x12HandleGatewayStats\x12\x1d.as.HandleGatewayStatsRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x0bHandleTxAck\x12\x16.as.HandleTxAckRequest\x1a\x16.google.protobuf.Empty\"\x00\x12G\n\x0fSetDeviceStatus\x12\x1a.as.SetDeviceStatusRequest\x1a\x16.google.protobuf.Empty\"\x00\x12K\n\x11SetDeviceLocation\x12\x1c.as.SetDeviceLocationRequest\x1a\x16.google.protobuf.Empty\"\x00\x12j\n\x19ReEncryptDeviceQueueItems\x12$.as.ReEncryptDeviceQueueItemsRequest\x1a%.as.ReEncryptDeviceQueueItemsResponse\"\x00\x12N\n\x16HandleGatewayConnStats\x12\x1a.as.HandleConnStateRequest\x1a\x16.google.protobuf.Empty\"\x00\x42[\n\x14io.chirpstack.api.asB\x16\x41pplicationServerProtoP\x01Z)github.com/SAP529/chirpstack-api/go/v4/asb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.as_pb_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.chirpstack.api.asB\026ApplicationServerProtoP\001Z)github.com/SAP529/chirpstack-api/go/v4/as'
  _HANDLEGATEWAYSTATSREQUEST_METADATAENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERFREQUENCYENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERFREQUENCYENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERDRENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERDRENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERSTATUSENTRY._options = None
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _RXWINDOW._serialized_start=2915
  _RXWINDOW._serialized_end=2943
  _ERRORTYPE._serialized_start=2946
  _ERRORTYPE._serialized_end=3133
  _DEVICEACTIVATIONCONTEXT._serialized_start=166
  _DEVICEACTIVATIONCONTEXT._serialized_end=249
  _HANDLEUPLINKDATAREQUEST._serialized_start=252
  _HANDLEUPLINKDATAREQUEST._serialized_end=542
  _HANDLEPROPRIETARYUPLINKREQUEST._serialized_start=545
  _HANDLEPROPRIETARYUPLINKREQUEST._serialized_end=681
  _HANDLEERRORREQUEST._serialized_start=683
  _HANDLEERRORREQUEST._serialized_end=779
  _HANDLEDOWNLINKACKREQUEST._serialized_start=781
  _HANDLEDOWNLINKACKREQUEST._serialized_end=861
  _SETDEVICESTATUSREQUEST._serialized_start=864
  _SETDEVICESTATUSREQUEST._serialized_end=1027
  _SETDEVICELOCATIONREQUEST._serialized_start=1029
  _SETDEVICELOCATIONREQUEST._serialized_end=1128
  _HANDLEGATEWAYSTATSREQUEST._serialized_start=1131
  _HANDLEGATEWAYSTATSREQUEST._serialized_end=2223
  _HANDLEGATEWAYSTATSREQUEST_METADATAENTRY._serialized_start=1883
  _HANDLEGATEWAYSTATSREQUEST_METADATAENTRY._serialized_end=1930
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERFREQUENCYENTRY._serialized_start=1932
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERFREQUENCYENTRY._serialized_end=1992
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERFREQUENCYENTRY._serialized_start=1994
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERFREQUENCYENTRY._serialized_end=2054
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERDRENTRY._serialized_start=2056
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERDRENTRY._serialized_end=2109
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERDRENTRY._serialized_start=2111
  _HANDLEGATEWAYSTATSREQUEST_RXPACKETSPERDRENTRY._serialized_end=2164
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERSTATUSENTRY._serialized_start=2166
  _HANDLEGATEWAYSTATSREQUEST_TXPACKETSPERSTATUSENTRY._serialized_end=2223
  _HANDLETXACKREQUEST._serialized_start=2225
  _HANDLETXACKREQUEST._serialized_end=2334
  _REENCRYPTDEVICEQUEUEITEMSREQUEST._serialized_start=2337
  _REENCRYPTDEVICEQUEUEITEMSREQUEST._serialized_end=2472
  _REENCRYPTDEVICEQUEUEITEMSRESPONSE._serialized_start=2474
  _REENCRYPTDEVICEQUEUEITEMSRESPONSE._serialized_end=2556
  _REENCRYPTDEVICEQUEUEITEM._serialized_start=2558
  _REENCRYPTDEVICEQUEUEITEM._serialized_end=2655
  _REENCRYPTEDDEVICEQUEUEITEM._serialized_start=2657
  _REENCRYPTEDDEVICEQUEUEITEM._serialized_end=2756
  _HANDLECONNSTATEREQUEST._serialized_start=2759
  _HANDLECONNSTATEREQUEST._serialized_end=2913
  _HANDLECONNSTATEREQUEST_STATE._serialized_start=2881
  _HANDLECONNSTATEREQUEST_STATE._serialized_end=2913
  _APPLICATIONSERVERSERVICE._serialized_start=3136
  _APPLICATIONSERVERSERVICE._serialized_end=3950
# @@protoc_insertion_point(module_scope)
