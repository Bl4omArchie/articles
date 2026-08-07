# Threat Intelligence operating center - part 2

# Data enrichment with MaxMind database

In the last tutorial we saw how to ingest bulk data with DuckDB in Golang with the Appender API. Now that we have a database full of IP addresses from the [DataShieldIpv4](https://raw.githubusercontent.com/duggytuxy/Data-Shield_IPv4_Blocklist/refs/heads/main/prod_data-shield_ipv4_blocklist.txt), one cool thing will be to geo-locate them. 

These are the intelligence we want to gather for each IP address for this tutorial.
| Category | Data collected |
| :---: | :---: |
| Identity | IP (ipv4)|
| DNS | domain names per IP |
| GeoLocation | city and country |
| Ping | rtt (min, max, avg, std), is alive |


Let's start geo-locating IP addresses from the DataShieldIpv4 blocklist and get additionnal infos.


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

