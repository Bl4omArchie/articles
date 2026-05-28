# Convert csv to parquet using Dask (python)

Using the dask framework.

**1- Single csv to parquet**

```python
dd.read_csv("dataset.csv")
```


**2- Multiple csv to parquet**

```python
dd.read_csv("*.csv")
```

**3- Optimization : break parquet into partitions + compression**

```python
dd.read_csv("*.csv", blocksize=25e6, compression="zstd")
```

**4- Map the parquet partition to its original dataset**

```python
results = {}

# Read every csv
csv_files = [src] if redwing.is_file() else list[redwing.glob("*.csv"))

# Store every parquet partition with the following format : csv_name_part_n.parquet
for csv_file in csv_files:
    name = csv_file.stem

    df = dd.read_csv(csv_file, blocksize=25e6, assume_missing=True)
    df.to_parquet(dst, compression="zstd", name_function=lambda i: f"{name}_part_{i}.parquet")

    parts = sorted(str(p) for p in dst.glob(f"{name}_*.parquet"))
    results[name] = parts

# return a dict with the following struct : {"path/to/csv_name.csv": [path/to/part1.parquet, path/to/part2.parquet, ...]}
return results
```

**5- Write a parquet file from specific columns**

```python
df = dd.read_csv('dataset.csv', usecols=['col1', 'col2', 'col3'])
df[['col1']].to_parquet('parquet_col1/', write_index=False)
df[['col2']].to_parquet('parquet_col2/', write_index=False)
```