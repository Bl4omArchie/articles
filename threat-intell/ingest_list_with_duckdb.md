# Threat Intelligence operating center - part 1

# Three method to ingest large amount of data using DuckDB and Golang

In this tutorial, you will learn several ways to ingest efficiently data list into DuckDB.


# Pre-requistes

The only pre-requiste for this tutorial is to install DuckDB. You can install the python package, or whathever language suits you, and also the command line interface (CLI) which I recommend for this tutorial as I will use it too.
[DuckDB Installation page](https://duckdb.org/install/?platform=linux&environment=cli)

To install the cli:
```bash
curl https://install.duckdb.org | sh
```

# Method 1: direct file ingestion

The first method is the simplest. Giving a list of IP, let's say the [DataShieldIpv4](https://raw.githubusercontent.com/duggytuxy/Data-Shield_IPv4_Blocklist/refs/heads/main/prod_data-shield_ipv4_blocklist.txt) IP blocklist, we want to ingest every IP into DuckDB.

First, download the Ip blocklist and then enter DuckDB from the cli.

```bash
wget https://raw.githubusercontent.com/duggytuxy/Data-Shield_IPv4_Blocklist/refs/heads/main/prod_data-shield_ipv4_blocklist.txt
duckdb
```

Now let's read our IP blocklist using the read_csv() function. As the blocklist is a single-column, single-value text file, using `read_csv()` is still coherent. A CSV file is essentially a text file organized into columns, and in this case there is simply one column.

```bash
memory D select * from read_csv("/path/to/prod_data-shield_ipv4_blocklist.txt", header = False);
```

In our terminal we can now see the blocklist IP ingested into our freshly created database.
Here, the data is only store in memory. If you want to save the data, you should first create a database.

```bash
CREATE TABLE datashield AS
SELECT * FROM from read_csv("/path/to/prod_data-shield_ipv4_blocklist.txt", header = False);
```

# Method 2: pre-treatement before saving

In the first method the data is immediatly saved into our database which is convenient for us but yet a bit rush.
In order to verify the data integrity, we first want to parse each of our IPs. This way, we're are garantee to deal with the expected data.
Also, some list may contains headers with comments. This way, we can avoid them properly.

To do so, let's make a golang script that does the following:
- download the IP blocklist
- parse each IP
- save the data using 

# Method 3: the appender API