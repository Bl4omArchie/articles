# Threat-Intelligence with DuckDB (part 2)

# Data Enrichment with MaxMind

In the last tutorial we saw how to ingest bulk data with DuckDB in Golang with the Appender API. Now that we have a database full of IP addresses from the [DataShieldIpv4](https://raw.githubusercontent.com/duggytuxy/Data-Shield_IPv4_Blocklist/refs/heads/main/prod_data-shield_ipv4_blocklist.txt), one cool thing will be enrich our database with additional data like geo-location, ASN, dns etc. 

In this tutorial, we will gather the following intelligence for each IP address:
- City
- Country
- ASN
- DNS
- IsAlive
- PingStatistics

# Table of contents
1. [Database setup](#database-setup)
2. [Request DataShieldIpv4](#request-datashieldipv4)
3. [IP addresses parsing](#ip-addresses-parsing)
4. [Bulk data insertion](#bulk-data-insertion)
5. [Read table and end of script](#read-table-and-end-of-script)
6. [Benchmark](#benchmark)
6. [Conclusion](#conclusion)


# Tutorial

## Code clean up

## MaxMind database setup

## MaxMind DuckDB extension

## Reverse DNS

## Conclusion
