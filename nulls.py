def find_nulls(dataset):
    import pandas as pd
    import numpy as np
    Names = dataset.columns.values
    number = np.linspace(1, len(Names), len(Names))
    #cols = np.array([])
    j = 0
    k = 0
    for i in Names:
        name = Names[k]
        col_num = number[k]
        check_col = pd.isnull(dataset[name])
        k +=1
        if check_col[j] != False:
            print('Column in position',col_num,'.\n Header ""%s"" has Missing Values!' %name)
            #np.concatenate(cols)
        else:
            j += 1
    return






