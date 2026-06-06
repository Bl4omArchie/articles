import dask.dataframe as dd
from pathlib import Path

def warm_up():
    df = dd.read_csv("hikari.csv")
    print(df.head)


def convert_parquet():
    df = dd.read_csv("hikari.csv")
    df.to_parquet("output/")
    
    df_parquet = dd.read_parquet("output/")
    print(df_parquet.head)


def wildcard():
    df = dd.read_csv("*.csv")
    df.to_parquet("output/")
    
    df_parquet = dd.read_parquet("output/")
    print(df_parquet.head)


def compression():
    df = dd.read_csv("hikari.csv")
    df.to_parquet("output/", compression="zstd")
    
    df_parquet = dd.read_parquet("output/")
    print(df_parquet.head())


def map():
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
    

def column():
    df = dd.read_csv('hikari.csv', usecols=["traffic_category", "Label"])
    df.to_parquet('parquet_col/', write_index=False)
    
    df_parquet = dd.read_parquet("parquet_col/")
    print(df_parquet.head())
    

if __name__ == "__main__":
    column()
