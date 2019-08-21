import pandas as pd

def to_latex_table(file_name, df, directory=None, index=False, nr_decimals=2):
    """
    Parameters
    ==========
    file_name : name of table (without .tex)
    df : pandas.DataFrame (object) which has to be rendered to latex
    index : should the index of the DataFrame be shown
    """

    df = df.round(nr_decimals)

    if directory is None:
        with open('{}.tex'.format(file_name), 'w') as tf:
            tf.write(df.to_latex(index=index))
    else:
        with open('{}//{}.tex'.format(directory, file_name), 'w') as tf:
            tf.write(df.to_latex(index=index))

