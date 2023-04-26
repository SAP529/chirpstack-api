# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/gateway.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/chirpstack-api/as_pb/external/api/gateway.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\x30\x63hirpstack-api/as_pb/external/api/frameLog.proto\"\xfd\x03\n\x07Gateway\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\"\n\x08location\x18\x04 \x01(\x0b\x32\x10.common.Location\x12\'\n\x0forganization_id\x18\x05 \x01(\x03R\x0eorganizationID\x12\x19\n\x11\x64iscovery_enabled\x18\x06 \x01(\x08\x12*\n\x11network_server_id\x18\x07 \x01(\x03R\x0fnetworkServerID\x12,\n\x12gateway_profile_id\x18\x08 \x01(\tR\x10gatewayProfileID\x12!\n\x06\x62oards\x18\t \x03(\x0b\x32\x11.api.GatewayBoard\x12$\n\x04tags\x18\n \x03(\x0b\x32\x16.api.Gateway.TagsEntry\x12,\n\x08metadata\x18\x0b \x03(\x0b\x32\x1a.api.Gateway.MetadataEntry\x12,\n\x12service_profile_id\x18\x0c \x01(\tR\x10serviceProfileID\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"C\n\x0cGatewayBoard\x12\x17\n\x07\x66pga_id\x18\x01 \x01(\tR\x06\x66pgaID\x12\x1a\n\x12\x66ine_timestamp_key\x18\x02 \x01(\t\"5\n\x14\x43reateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"\x1f\n\x11GetGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xf8\x01\n\x12GetGatewayResponse\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfirst_seen_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\"\n\x14\x44\x65leteGatewayRequest\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\'GenerateGatewayClientCertificateRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\"\x8e\x01\n(GenerateGatewayClientCertificateResponse\x12\x10\n\x08tls_cert\x18\x01 \x01(\t\x12\x0f\n\x07tls_key\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61_cert\x18\x03 \x01(\t\x12.\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"l\n\x12ListGatewayRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\'\n\x0forganization_id\x18\x03 \x01(\x03R\x0eorganizationID\x12\x0e\n\x06search\x18\x04 \x01(\t\"\x9b\x03\n\x0fGatewayListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rfirst_seen_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0clast_seen_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x0forganization_id\x18\x06 \x01(\x03R\x0eorganizationID\x12*\n\x11network_server_id\x18\x07 \x01(\x03R\x0fnetworkServerID\x12\"\n\x08location\x18\n \x01(\x0b\x32\x10.common.Location\x12\x1b\n\x13network_server_name\x18\x0b \x01(\t\"P\n\x13ListGatewayResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\x03\x12$\n\x06result\x18\x02 \x03(\x0b\x32\x14.api.GatewayListItem\"5\n\x14UpdateGatewayRequest\x12\x1d\n\x07gateway\x18\x01 \x01(\x0b\x32\x0c.api.Gateway\"\xad\n\n\x0cGatewayStats\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13rx_packets_received\x18\x02 \x01(\x05\x12\x33\n\x16rx_packets_received_ok\x18\x03 \x01(\x05R\x13rxPacketsReceivedOK\x12\x1b\n\x13tx_packets_received\x18\x04 \x01(\x05\x12\x1a\n\x12tx_packets_emitted\x18\x05 \x01(\x05\x12N\n\x18tx_packets_per_frequency\x18\x06 \x03(\x0b\x32,.api.GatewayStats.TxPacketsPerFrequencyEntry\x12N\n\x18rx_packets_per_frequency\x18\x07 \x03(\x0b\x32,.api.GatewayStats.RxPacketsPerFrequencyEntry\x12@\n\x11tx_packets_per_dr\x18\x08 \x03(\x0b\x32%.api.GatewayStats.TxPacketsPerDrEntry\x12@\n\x11rx_packets_per_dr\x18\t \x03(\x0b\x32%.api.GatewayStats.RxPacketsPerDrEntry\x12H\n\x15tx_packets_per_status\x18\n \x03(\x0b\x32).api.GatewayStats.TxPacketsPerStatusEntry\x12\x36\n\x0b\x63onn_status\x18\x0b \x03(\x0b\x32!.api.GatewayStats.ConnStatusEntry\x12\x13\n\x0bstats_count\x18\x0c \x01(\x05\x12O\n\x18rx_frequency_utilization\x18\r \x03(\x0b\x32-.api.GatewayStats.RxFrequencyUtilizationEntry\x12O\n\x18tx_frequency_utilization\x18\x0e \x03(\x0b\x32-.api.GatewayStats.TxFrequencyUtilizationEntry\x12\x16\n\x0eup_bytes_count\x18\x0f \x01(\x02\x12\x18\n\x10\x64own_bytes_count\x18\x10 \x01(\x02\x1a<\n\x1aTxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a<\n\x1aRxPacketsPerFrequencyEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13TxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x35\n\x13RxPacketsPerDrEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x39\n\x17TxPacketsPerStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x31\n\x0f\x43onnStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a=\n\x1bRxFrequencyUtilizationEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a=\n\x1bTxFrequencyUtilizationEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\xb1\x01\n\x16GetGatewayStatsRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\x12\x10\n\x08interval\x18\x02 \x01(\t\x12\x33\n\x0fstart_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rend_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x17GetGatewayStatsResponse\x12!\n\x06result\x18\x01 \x03(\x0b\x32\x11.api.GatewayStats\"\x87\x01\n\x06PingRX\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x19\n\x08lora_snr\x18\x03 \x01(\x01R\x07loRaSNR\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x06 \x01(\x01\"3\n\x12GetLastPingRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"\x8a\x01\n\x13GetLastPingResponse\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tfrequency\x18\x02 \x01(\r\x12\n\n\x02\x64r\x18\x03 \x01(\r\x12$\n\x07ping_rx\x18\x04 \x03(\x0b\x32\x0b.api.PingRXR\x06pingRX\">\n\x1dStreamGatewayFrameLogsRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"\x87\x01\n\x1eStreamGatewayFrameLogsResponse\x12+\n\x0cuplink_frame\x18\x01 \x01(\x0b\x32\x13.api.UplinkFrameLogH\x00\x12/\n\x0e\x64ownlink_frame\x18\x02 \x01(\x0b\x32\x15.api.DownlinkFrameLogH\x00\x42\x07\n\x05\x66rame\">\n\x1dStreamGatewayEventLogsRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"\xa0\x01\n\x1eStreamGatewayEventLogsResponse\x12\x0c\n\x04type\x18\x01 \x01(\t\x12!\n\x0cpayload_json\x18\x02 \x01(\tR\x0bpayloadJSON\x12\x30\n\x0cpublished_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\tstream_id\x18\x04 \x01(\tR\x08streamID\"8\n\x17GetGatewayStatusRequest\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\"I\n\x18GetGatewayStatusResponse\x12\x1d\n\ngateway_id\x18\x01 \x01(\tR\tgatewayID\x12\x0e\n\x06status\x18\x02 \x01(\t2\xf0\t\n\x0eGatewayService\x12U\n\x06\x43reate\x12\x19.api.CreateGatewayRequest\x1a\x16.google.protobuf.Empty\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/api/gateways:\x01*\x12R\n\x03Get\x12\x16.api.GetGatewayRequest\x1a\x17.api.GetGatewayResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/api/gateways/{id}\x12\x62\n\x06Update\x12\x19.api.UpdateGatewayRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\x1a\x1a/api/gateways/{gateway.id}:\x01*\x12W\n\x06\x44\x65lete\x12\x19.api.DeleteGatewayRequest\x1a\x16.google.protobuf.Empty\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/api/gateways/{id}\x12P\n\x04List\x12\x17.api.ListGatewayRequest\x1a\x18.api.ListGatewayResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/api/gateways\x12o\n\x08GetStats\x12\x1b.api.GetGatewayStatsRequest\x1a\x1c.api.GetGatewayStatsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /api/gateways/{gateway_id}/stats\x12o\n\x0bGetLastPing\x12\x17.api.GetLastPingRequest\x1a\x18.api.GetLastPingResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/api/gateways/{gateway_id}/pings/last\x12\xb8\x01\n GenerateGatewayClientCertificate\x12,.api.GenerateGatewayClientCertificateRequest\x1a-.api.GenerateGatewayClientCertificateResponse\"7\x82\xd3\xe4\x93\x02\x31\"//api/gateways/{gateway_id}/generate-certificate\x12\x87\x01\n\x0fStreamFrameLogs\x12\".api.StreamGatewayFrameLogsRequest\x1a#.api.StreamGatewayFrameLogsResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/gateways/{gateway_id}/frames0\x01\x12\x87\x01\n\x0fStreamEventLogs\x12\".api.StreamGatewayEventLogsRequest\x1a#.api.StreamGatewayEventLogsResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/gateways/{gateway_id}/events0\x01\x12s\n\tGetStatus\x12\x1c.api.GetGatewayStatusRequest\x1a\x1d.api.GetGatewayStatusResponse\")\x82\xd3\xe4\x93\x02#\x12!/api/gateways/{gateway_id}/statusBk\n!io.chirpstack.api.as.external.apiB\x0cGatewayProtoP\x01Z6github.com/SAP529/chirpstack-api/go/v4/as/external/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.as_pb.external.api.gateway_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.chirpstack.api.as.external.apiB\014GatewayProtoP\001Z6github.com/SAP529/chirpstack-api/go/v4/as/external/api'
  _GATEWAY_TAGSENTRY._options = None
  _GATEWAY_TAGSENTRY._serialized_options = b'8\001'
  _GATEWAY_METADATAENTRY._options = None
  _GATEWAY_METADATAENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._options = None
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._options = None
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_CONNSTATUSENTRY._options = None
  _GATEWAYSTATS_CONNSTATUSENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_RXFREQUENCYUTILIZATIONENTRY._options = None
  _GATEWAYSTATS_RXFREQUENCYUTILIZATIONENTRY._serialized_options = b'8\001'
  _GATEWAYSTATS_TXFREQUENCYUTILIZATIONENTRY._options = None
  _GATEWAYSTATS_TXFREQUENCYUTILIZATIONENTRY._serialized_options = b'8\001'
  _GATEWAYSERVICE.methods_by_name['Create']._options = None
  _GATEWAYSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\022\"\r/api/gateways:\001*'
  _GATEWAYSERVICE.methods_by_name['Get']._options = None
  _GATEWAYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\024\022\022/api/gateways/{id}'
  _GATEWAYSERVICE.methods_by_name['Update']._options = None
  _GATEWAYSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\037\032\032/api/gateways/{gateway.id}:\001*'
  _GATEWAYSERVICE.methods_by_name['Delete']._options = None
  _GATEWAYSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\024*\022/api/gateways/{id}'
  _GATEWAYSERVICE.methods_by_name['List']._options = None
  _GATEWAYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\017\022\r/api/gateways'
  _GATEWAYSERVICE.methods_by_name['GetStats']._options = None
  _GATEWAYSERVICE.methods_by_name['GetStats']._serialized_options = b'\202\323\344\223\002\"\022 /api/gateways/{gateway_id}/stats'
  _GATEWAYSERVICE.methods_by_name['GetLastPing']._options = None
  _GATEWAYSERVICE.methods_by_name['GetLastPing']._serialized_options = b'\202\323\344\223\002\'\022%/api/gateways/{gateway_id}/pings/last'
  _GATEWAYSERVICE.methods_by_name['GenerateGatewayClientCertificate']._options = None
  _GATEWAYSERVICE.methods_by_name['GenerateGatewayClientCertificate']._serialized_options = b'\202\323\344\223\0021\"//api/gateways/{gateway_id}/generate-certificate'
  _GATEWAYSERVICE.methods_by_name['StreamFrameLogs']._options = None
  _GATEWAYSERVICE.methods_by_name['StreamFrameLogs']._serialized_options = b'\202\323\344\223\002#\022!/api/gateways/{gateway_id}/frames'
  _GATEWAYSERVICE.methods_by_name['StreamEventLogs']._options = None
  _GATEWAYSERVICE.methods_by_name['StreamEventLogs']._serialized_options = b'\202\323\344\223\002#\022!/api/gateways/{gateway_id}/events'
  _GATEWAYSERVICE.methods_by_name['GetStatus']._options = None
  _GATEWAYSERVICE.methods_by_name['GetStatus']._serialized_options = b'\202\323\344\223\002#\022!/api/gateways/{gateway_id}/status'
  _GATEWAY._serialized_start=235
  _GATEWAY._serialized_end=744
  _GATEWAY_TAGSENTRY._serialized_start=652
  _GATEWAY_TAGSENTRY._serialized_end=695
  _GATEWAY_METADATAENTRY._serialized_start=697
  _GATEWAY_METADATAENTRY._serialized_end=744
  _GATEWAYBOARD._serialized_start=746
  _GATEWAYBOARD._serialized_end=813
  _CREATEGATEWAYREQUEST._serialized_start=815
  _CREATEGATEWAYREQUEST._serialized_end=868
  _GETGATEWAYREQUEST._serialized_start=870
  _GETGATEWAYREQUEST._serialized_end=901
  _GETGATEWAYRESPONSE._serialized_start=904
  _GETGATEWAYRESPONSE._serialized_end=1152
  _DELETEGATEWAYREQUEST._serialized_start=1154
  _DELETEGATEWAYREQUEST._serialized_end=1188
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_start=1190
  _GENERATEGATEWAYCLIENTCERTIFICATEREQUEST._serialized_end=1251
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_start=1254
  _GENERATEGATEWAYCLIENTCERTIFICATERESPONSE._serialized_end=1396
  _LISTGATEWAYREQUEST._serialized_start=1398
  _LISTGATEWAYREQUEST._serialized_end=1506
  _GATEWAYLISTITEM._serialized_start=1509
  _GATEWAYLISTITEM._serialized_end=1920
  _LISTGATEWAYRESPONSE._serialized_start=1922
  _LISTGATEWAYRESPONSE._serialized_end=2002
  _UPDATEGATEWAYREQUEST._serialized_start=2004
  _UPDATEGATEWAYREQUEST._serialized_end=2057
  _GATEWAYSTATS._serialized_start=2060
  _GATEWAYSTATS._serialized_end=3385
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_start=2917
  _GATEWAYSTATS_TXPACKETSPERFREQUENCYENTRY._serialized_end=2977
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_start=2979
  _GATEWAYSTATS_RXPACKETSPERFREQUENCYENTRY._serialized_end=3039
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_start=3041
  _GATEWAYSTATS_TXPACKETSPERDRENTRY._serialized_end=3094
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_start=3096
  _GATEWAYSTATS_RXPACKETSPERDRENTRY._serialized_end=3149
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_start=3151
  _GATEWAYSTATS_TXPACKETSPERSTATUSENTRY._serialized_end=3208
  _GATEWAYSTATS_CONNSTATUSENTRY._serialized_start=3210
  _GATEWAYSTATS_CONNSTATUSENTRY._serialized_end=3259
  _GATEWAYSTATS_RXFREQUENCYUTILIZATIONENTRY._serialized_start=3261
  _GATEWAYSTATS_RXFREQUENCYUTILIZATIONENTRY._serialized_end=3322
  _GATEWAYSTATS_TXFREQUENCYUTILIZATIONENTRY._serialized_start=3324
  _GATEWAYSTATS_TXFREQUENCYUTILIZATIONENTRY._serialized_end=3385
  _GETGATEWAYSTATSREQUEST._serialized_start=3388
  _GETGATEWAYSTATSREQUEST._serialized_end=3565
  _GETGATEWAYSTATSRESPONSE._serialized_start=3567
  _GETGATEWAYSTATSRESPONSE._serialized_end=3627
  _PINGRX._serialized_start=3630
  _PINGRX._serialized_end=3765
  _GETLASTPINGREQUEST._serialized_start=3767
  _GETLASTPINGREQUEST._serialized_end=3818
  _GETLASTPINGRESPONSE._serialized_start=3821
  _GETLASTPINGRESPONSE._serialized_end=3959
  _STREAMGATEWAYFRAMELOGSREQUEST._serialized_start=3961
  _STREAMGATEWAYFRAMELOGSREQUEST._serialized_end=4023
  _STREAMGATEWAYFRAMELOGSRESPONSE._serialized_start=4026
  _STREAMGATEWAYFRAMELOGSRESPONSE._serialized_end=4161
  _STREAMGATEWAYEVENTLOGSREQUEST._serialized_start=4163
  _STREAMGATEWAYEVENTLOGSREQUEST._serialized_end=4225
  _STREAMGATEWAYEVENTLOGSRESPONSE._serialized_start=4228
  _STREAMGATEWAYEVENTLOGSRESPONSE._serialized_end=4388
  _GETGATEWAYSTATUSREQUEST._serialized_start=4390
  _GETGATEWAYSTATUSREQUEST._serialized_end=4446
  _GETGATEWAYSTATUSRESPONSE._serialized_start=4448
  _GETGATEWAYSTATUSRESPONSE._serialized_end=4521
  _GATEWAYSERVICE._serialized_start=4524
  _GATEWAYSERVICE._serialized_end=5788
# @@protoc_insertion_point(module_scope)
