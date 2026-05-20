# Bulk data ingestion with DuckDB in Golang using. Threat Intelligence use case.


In this article, I demonstrate how to use the Appender feature to insert large amounts of data into duck using Golang.

The Appender enables extremely fast bulk inserts (ms for +100K IP addresses).

In order to illustrate this feature, I'll use a Threat-Intelligence use case where we store IP addresses from blocklist into DuckDB.

For this matter I will use the [DataShieldIpv4](https://raw.githubusercontent.com/duggytuxy/Data-Shield_IPv4_Blocklist/refs/heads/main/prod_data-shield_ipv4_blocklist.txt) IP blocklist maintained by [Laurent Minne](https://github.com/duggytuxy).

Which contains over 100k IPv4 addresses identified as malicious.

# Tutorial

## Database setup

First of all, you should create a golang project and install duckDB.
```bash
go mod init insert_bulk_data
go get github.com/duckdb/duckdb-go/v2
touch main.go
``` 

Then, in your main.go file, create the duckDB database.

```go
func main() {
	// Create the database
	var db string = "database.db"

	conn, err := sql.Open("duckdb", db)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()
}
```

Create the table where the IP addresses will be stored with the following SQL query.
```go
...

// Create the table ip_blocklist
_, err = conn.Exec(`CREATE TABLE IF NOT EXISTS ip_blocklist(
			id INTEGER PRIMARY KEY,
			ip VARCHAR)`)
if err != nil {
	fmt.Printf("Error while creating the table: %s\n", err)
	return
}
	
```

Now that our database is setup, we can get the IPs from blocklist.

## Request the blocklist

Let's create a simple HTTP client and get the IPs.
```go
func RequestBlocklist() ([]byte, error) {
	var ipList string = "https://cdn.jsdelivr.net/gh/duggytuxy/Data-Shield_IPv4_Blocklist@refs/heads/main/prod_data-shield_ipv4_blocklist.txt"

    client := &http.Client{Timeout: time.Second * 10,}

    req, err := http.NewRequest(http.MethodGet, ipList, nil)
    if err != nil {
        return nil, err
    }

    resp, err := client.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }
	return body, nil
}
```

## IP parsing

As we want to avoid any inconvenience, we are going to parse every IP addresses that we are getting from our source.
Let's use the `net` library with the `net.IP` struct and the `net.ParseIP()` function.

```go
func ParseIPs(body []byte) []net.IP {
	var parsedUrls []net.IP

	content := strings.SplitSeq(string(body), "\n")
	for ip := range content {
		parsedUrls = append(parsedUrls, net.ParseIP(ip))
	}

	return parsedUrls
}
```

Here we take the body page from our request, we split it to get every IP addresses and we parse each of them.

**NOTE**: in this case we are reading the body assuming there are only IPs. By parsing IP addresses, failures can be minimize. But that's not enough. In practice we should parse the body properly. For instance, if there is two columns of data instead of one. The script here is effective but keep in mind that this will not match every case.

## Bulk data insertion

Finally, let's insert our parsed data into the ip_blocklist table with the Appender.

In order to call the DuckDB Appender API, we have to provide a DuckDB connection from the `duckdb` library.

The `Appender`function inserts a slice of parsed IP addresses. It takes, as parameters, a context, the dsn, the name fo the table and the data.

```go
func Appender(ctx context.Context, db string, tbl string, data []net.IP) error {
	connector, err := duckdb.NewConnector(db, nil)
	if err != nil {
		return err
	}
	conn, err := connector.Connect(ctx)
	if err != nil {
		return err
	}
	defer conn.Close()
...
```

The connection is now established with the connector, we can call the Appender API.
```go
...
	appender, err := duckdb.NewAppenderFromConn(conn, "", tbl)
	if err != nil {
		return err
	}
	defer appender.Close()

	for i, url := range data {
		err = appender.AppendRow(i, url.String())
		if err != nil {
			return err
		}
	}

	return nil
``` 

We loop over each IP, we convert them into `string` and the `AppendRow()` function make the magic happens.

## End of the script and print ip_blocklist table

Before running the script, let's create a simple `ReadTable` function so we can see from our eyes the result

```go
func ReadTable(conn *sql.DB) ([]string, error) {
	rows, err := conn.Query("SELECT ip FROM ip_blocklist")
	if err != nil {
		return nil, err
	}

	var (
		ip string
		ips []string
	)

	for rows.Next() {
		err = rows.Scan(&ip)
		if err != nil {
			return nil, err
		}
		ips = append(ips, ip)
	}

	if err = rows.Err(); err != nil {
		return nil, err
	}

	return ips, nil
}
``` 

We use the following query: `SELECT id, ip FROM ip_blocklist`. Then we loop over each row using Scan() function to extract the IP addresses which are appanded to a slice returned at the end of the function.

Finally we can complete the main() function with all the functions we have made.
```go
...
	// request the blocklist from our source
	body, err := RequestBlocklist()
	if err != nil {
		fmt.Println(err)
	}


	// parse each urls
	parsedUrls := ParseIPs(body)


	// insert data
	var ctx context.Context = context.Background()
	err = Appender(ctx, db, "ip_blocklist", parsedUrls)
	if err != nil {
		fmt.Printf("Error while parsing: %s\n", err)
		return
	}


	read database
	ips, err := ReadTable(conn)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(ips)
	}
}
```

Now the script is ready to be compiled and runned.
```go 
go build -o bulk_data.o main.go 
./bulk_data.o
```

The execution time heavily depends on your network download speed. Let's create benchmarks to better see which step is taking the most time.

## Benchmark

With the `time` library, you can wrap every function with a start value and an elapsed value.
```go
Now the script is ready to be compiled and runned.
```go 
go build -o bulk_data.o main.go 
./bulk_data.o
```go
	startRequest := time.Now()
	// request the blocklist from our source
	body, err := RequestBlocklist()
	if err != nil {
		fmt.Println(err)
	}
	elapsedRequest := time.Since(startRequest)


	startParse := time.Now()
	// parse each urls
	parsedUrls := ParseIPs(body)
	elapsedParse := time.Since(startParse)

	
	start := time.Now()
	// insert data
	var ctx context.Context = context.Background()
	err = Appender(ctx, db, "ip_blocklist", parsedUrls)
	if err != nil {
		fmt.Printf("Error while parsing: %s\n", err)
		return
	}
	elapsed := time.Since(start)


	// read database
	// ips, err := ReadTable(conn)
	// if err != nil {
	// 	fmt.Println(err)
	// } else {
	// 	fmt.Println(ips)
	// }

	fmt.Println("Execution time for RequestBlocklist(): ", elapsedRequest)
	fmt.Println("Execution time for ParseIPs(): ", elapsedParse)
	fmt.Println("Execution time for Appender(): ", elapsed)
```

Here, we focus specifically on execution time, so we removed the database read step from the benchmark.

After several runs, these are the observed results:
| Function | Time |
| --- | --- |
| RequestBlocklist() |  10.000647917s |
| ParseIPs() | 27.464µs |
| Appender() | 2.709261ms |

As mentioned earlier, the overall execution time is largely dominated by the RequestBlocklist() function and therefore heavily depends on network download speed.


# Conclusion

In this blog post, we explored how to use the Appender() DuckDB API to efficiently insert bulk data into a database.

We applied this approach to a Threat Intelligence use case by downloading the DataShieldIpv4 blocklist maintained by Laurent Minne.

Finally, we added benchmarks using Go’s time package and observed that the Appender() function can insert more than 100,000 IP addresses in approximately 2.5 ms.

In future work, this database could be used to correlate Zeek logs or other data sources such as PCAP files. It could also serve as a distribution backend for IP reputation feeds consumed by security platforms including SIEMs, IDS/IPS solutions, and firewalls.
