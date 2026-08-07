# Convert csv to parquet using Dask (python)

**Definition:** Parquet is a free and open-source column-oriented data storage format. Implemented using the record-shredding and assembly algorithm, parquet provides high efficiency in data analytics for large dataset.

In this tutorial, we will see different ways to convert a CSV file into parquet format using Dask framework in python.

# Setup

Execute the bash script that will deploy the python environnement en download two CSV dataset.

```bash
chmod +x build-python.sh
./build-python.sh
```

# Tutorial
To improve storage efficiency and read performance
**Warm-up**

First, let's read our CSV with dask.

```python
import dask as dd

df = dd.read_csv("hikari.csv")
print(df.head)
```

**1- Convert csv to parquet**

[Full dask Documentation](https://docs.dask.org/en/stable/generated/dask.dataframe.to_parquet.html)

Now we shall convert our CSV into parquet format
```python
df = dd.read_csv("hikari.csv")
df.to_parquet("output/")

df_parquet = dd.read_parquet("output/")
print(df_parquet.head)
```

Parquet file comes into partition. Meaning you give a folder name and get multiple files. 


**2- Multiple csv to parquet**

Using the wildcard *, you can read several CSV into a single dataframe.

```python
df = dd.read_csv("*.csv")
df.to_parquet("output/")

df_parquet = dd.read_parquet("output/")
print(df_parquet.head)
```

**3- Optimization : enable compression**

To improve storage efficiency and read performance, we will d enable compression.

```python
df = dd.read_csv("*.csv")
df.to_parquet("output/", compression="zstd")

df_parquet = dd.read_parquet("output/")
print(df_parquet.head())
```

**4- Map the parquet partition to its original dataset**

In order to keep tracks of our parquet partition, lets create a map that will keep the initial CSV name binded to our multiple parquet files.

```python
src = Path(".")
dst = Path("output")
dst.mkdir(exist_ok=True)
results = {}

# Read every csv
csv_files = list(src.glob("*.csv"))

# Store every parquet partition with the following format : csv_name_part_n.parquet
for csv_file in csv_files:
    name = csv_file.stem

    df = dd.read_csv(csv_file)
    df.to_parquet(dst, compression="zstd", write_index=False, name_function=lambda i: f"{name}_part_{i}.parquet")

    parts = sorted(str(p) for p in dst.glob(f"{name}_*.parquet"))
    results[name] = parts

print(results)
```

As you can, there is a weird line here:
```py
df.to_parquet(dst, compression="zstd", name_function=lambda i: f"{name}_part_{i}.parquet")
```
In order to give a different name for each partition file, we create a lambda function that defines the name of the file.

**5- Write a parquet file from specific columns**

You can also export only selected columns to reduce memory usage and improve performance on large datasets.

```python
df = dd.read_csv('hikari.csv', usecols=["traffic_category", "Label"])
df.to_parquet('parquet_col/', write_index=False)

df_parquet = dd.read_parquet("parquet_col/")
print(df_parquet.head())
```

# Notes
- pyarrow is currently the recommended Parquet backend for Dask.
- zstd generally provides better compression ratios than snappy, but may use more CPU.
- write_index=False is recommended unless the index is required later.
- Dask works best with partitioned datasets instead of a single large Parquet file.
