#!/usr/bin/env python3
import polars as pl
import sys


def capitalize_names(input_csv, output_csv, column_idx):
    df = pl.read_csv(input_csv)
    if column_idx < 0 or column_idx >= len(df.columns):
        print(f"Error: column_index {column_idx} is out of range.")
        sys.exit(1)
    column_name = df.columns[column_idx]
    df = df.with_columns(
        pl.col(column_name).apply(lambda x: x.title() if isinstance(x, str) else x).alias(column_name)
    )
    df.write_csv(output_csv)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py input.csv output.csv column_index")
        sys.exit(1)
    INPUT_FILE, OUTPUT_FILE, COLUMN_INDEX = sys.argv[1], sys.argv[2], int(sys.argv[3])
    capitalize_names(INPUT_FILE, OUTPUT_FILE, COLUMN_INDEX)
