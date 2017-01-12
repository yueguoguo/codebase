import pandas as pd


def get_nominal_integer_dict(nominal_vals):
    d = {}
    for val in nominal_vals:
        if val not in d:
            current_max = max(d.values()) if len(d) > 0 else -1
            d[val] = current_max+1
    return d


def convert_to_integer(srs):
    d = get_nominal_integer_dict(srs)
    return srs.map(lambda x: d[x])


def categorical_to_numeric(df):
    """
    Convert categorical columns to numeric and leave numeric columns
    as they are
    :param df: dataframe
    :return: dataframe with only numerical values
    """
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column.dtype == 'object':
            ret[column_name] = convert_to_integer(column)
        else:
            ret[column_name] = column
    return ret


if __name__ == "__main__":

    df = pd.DataFrame({'letters':['a','b','c'],
                       'numbers':[1,2,3]})
    print("Example of conversion from categorical to numeric")
    df_numeric = categorical_to_numeric(df)
    print(df_numeric)

