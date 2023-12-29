import pandas as pd
import numpy as np
import os

def create_sqlite_db():
    ...

def profilling_report():
    ...


def create_directory_if_not_exists(directory_path):
    """
    Create a directory if it does not exist.

    Parameters:
    - directory_path (str): Path of the directory to be created.

    Returns:
    - None
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    else:
        print(f"Directory '{directory_path}' already exists.")


def analysis_aggragtions(data):
    """Aggregates the given data based on product_code.

    Args:
        - data (DataFrame): Input data

    Returns:
        - DataFrame: Aggregated data
    """
    result = (data
            .groupby('product_code')
            .agg(
                    open_stock_sum=("open_stock", "sum"),
                    alocated_inventory_sum=("alocated_inventory", "sum"),
                    damaged_inventory_sum=("damaged_inventory", "sum"),
                    total_inventory_sum=("total_inventory", "sum"),
                    total_inventory_std=("total_inventory", np.std),
                    total_inventory_mean=("total_inventory", 'mean'),
                    price_per_unit_first=("price_per_unit", "first"),
                    total_price_sum=("total_price", "sum"),
                    total_price_std=("total_price", np.std),
                    total_price_mean=("total_price", 'mean')
                ).reset_index())
    return result
    
def compute_scores(data,scores_conf):
    """Computes scores of ABC and XYZ analysis for the given data.

    Args:
        - data (DataFrame): Input data
        - abc_column (str): Column name for ABC computation
        - xyz_column (str): Column name for XYZ computation

    Returns:
        - DataFrame: Data with scores computed
    """

    abc_column = scores_conf.get('ABC_column')
    xyz_column = scores_conf.get('XYZ_column')
    
    data = data.sort_values(by=abc_column, ascending=False)
    data['cumulative_percentage'] = (data[abc_column].cumsum() / data[abc_column].sum()) * 100
    data['CV'] = data[xyz_column] / data[xyz_column].mean()
    return data

def bucketing(data,conf):
    """Bins the data based on specified configurations.

    Args:
        - data (DataFrame): Input data
        - conf (list): List of dictionaries containing binning configurations
    Returns:
        - DataFrame: Data with bucketed columns added
    """
    for ele in conf:
        bucketed_col = ele.get('new_col')
        original_col = ele.get('original_col')
        bins_list = ele.get('bins')
        labels_names = ele.get('labels')
        data[bucketed_col] = pd.cut(data[original_col], bins=bins_list, labels=labels_names)
    return data



if __name__ == "__main__":
    data = pd.read_excel("C:\\Users\\Dell\\Downloads\\Inventory data.xlsx")
    aggragted = analysis_aggragtions(data)
    scores_conf = {'ABC_column':'total_price_sum','XYZ_column':'total_inventory_sum'}
    bucket_conf = [
        {'original_col':'cumulative_percentage','new_col':'ABC_category','bins':[0, 80, 95, 100],'labels':['A', 'B', 'C']},
        {'original_col':'CV','new_col':'XYZ_category','bins':[-float('inf'), 0.4, 0.7, float('inf')],'labels':['X', 'Y', 'Z']}
        ]
    interim_df = compute_scores(aggragted,scores_conf)
    final_result = bucketing(interim_df,bucket_conf).reset_index(drop=True)
    presentation_path = 'data/presentation'
    create_directory_if_not_exists(presentation_path)
    final_result.to_excel(f"{presentation_path}/results.xlsx")
