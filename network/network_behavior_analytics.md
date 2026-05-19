# Network behavior analytics

This document enumerate data and technic useful in network behavior analysis.


# Raw packet fields

Useful packet fields for each layer (OSI model) 

| L2          | L3                  | L4              | L7                     |
| ----------- | ------------------- | --------------- | ---------------------- |
| MAC src/dst | IP src/dst          | TCP flags       | DNS query/response     |
| EtherType   | TTL / Hop limit     | Seq/Ack numbers | TLS SNI                |
| VLAN ID     | DSCP / ECN          | Window size     | JA3 / JA4 fingerprints |
| MPLS        | Fragmentation flags | Retransmissions | HTTP headers           |
| MPLS labels | IP options          | UDP length      | User-Agent             |
|             |                     | ICMP type/code  | QUIC parameters        |
|             |                     |                 | SSH fingerprints       |




# Features

Useful features you can compute or aggregate/join.

| To compute                                       | To aggregate | To join             |
| ------------------------------------------------ | ------------ | ------------------- |
| IAT                                              | per flow     | threat intelligence |
| idle / active time                               | per protocol | several log files   |
| burst analysis                                   | time window  |                     |
| bulk transfer                                    |              |                     |
| flow statistics (bytes/sec, flow duration, etc.) |              |                     |



# Definitions

- Flow: a sequence of packets sharing the same tuple (src_ip, dst_ip, src_port, dst_port, protocol) during a given time interval.

- IAT (inter-arrival time): the elapsed time between two consecutive packets in a flow. We usually compute data such as the average of a flow IAT, the standard deviation or the min and max IAT of a flow.

- Subflow:  an exchange of packets in a flow, where the inter-arrival time between the packets is less than subflow_max_iat. If the inter-arrival time between two packets is larger than subflow_max_iat, then the current subflow is terminated and a new subflow starts.

- Bulk Transmission: a continuous transmission of at least bulk_min_length data packets (packets carrying payload) from either the source or the destination. A bulk transmission is terminated if the other side transmits a data packet or if the inter-arrival time between two packets is larger than the bulk bulk_timeout. If at the termination the bulk flow has not seen more than bulk_min_length, then that bulk flow is discarded.

- Active and Idle Time: a flow is considered to be active if a successive packet arrives in less than active_timeout. If no packet is seen after active_timeout, then the flow is considered to have been idle during that period.
