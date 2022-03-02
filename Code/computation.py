# This function is to calculate weighted average return of the portfolio
def wavg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return np.nan


def ts_reg(factor_matrix, test_assets, RF, table):
    import statsmodels.api as sm
    import pandas as pd
    X = sm.add_constant(factor_matrix)
    const_value = list()
    t_value = list()
    rsquared_adj_value = list()
    risidual_matrix = pd.DataFrame()
    # Loop to perform regression
    # Note that we should deduct RF from the portfolio return to get the excess return
    for i in range(len(test_assets.columns)):
        y= test_assets.iloc[:,i]-RF
        model = sm.OLS(y, X)
        results = model.fit()
        const_value.append(results.params.tolist()[0])
        t_value.append(results.tvalues.tolist()[0])
        rsquared_adj_value.append(results.rsquared_adj)
        if i == 0:
            risidual_matrix = pd.DataFrame(results.resid,columns=[i])
        else:
            risidual_matrix=risidual_matrix.join(pd.DataFrame(results.resid,columns=[i]))
    # convert result into dataframe
    alpha = r'$\alpha^{FF}$' if factor_matrix.columns.tolist() == ['smb','hml','mktrf'] else r'$\alpha$'
    ts_result = {alpha: const_value, r'$[t]$': t_value, r'$R^2_{adj}$': rsquared_adj_value, 'test_assets_name': test_assets.columns}
    ts_result = pd.DataFrame.from_dict(ts_result, orient='index')
    ts_result.columns = ts_result.loc['test_assets_name',:]
    ts_result = ts_result.drop(['test_assets_name'])
    ts_result.columns = table.columns
    table = pd.concat([table, ts_result.loc[[alpha]]*1200])
    table = pd.concat([table, ts_result.loc[[r'$[t]$']]])
    return table.astype(float).round(2)

def make_owt(pvwret, _ff, sorting_bin):
    import pandas as pd
    import numpy as np
    pvwret = pd.merge(pvwret,_ff,on='jdate',how='left')
    pvwret = pvwret.rename(columns={1:'Low', sorting_bin: 'High', 'date':'L-H'})
    pvwret['L-H'] = pvwret['Low'] - pvwret['High'] 

    col_name = pvwret.columns.tolist()[1:sorting_bin+2]
    ow_table = pd.DataFrame(columns= col_name)
    # calculate average
    for col in pvwret.iloc[:,1:sorting_bin+1].columns:
        pvwret[col] = pvwret[col]-pvwret['rf']
    ow_table.loc[r'$r^S$',:] = pvwret.iloc[:,1:sorting_bin+2].mean()*1200

    # manually calculate the t stats for the estimated mean of excess return, using the sample std/sqrt(num) as the estimated std for the mean
    num = pvwret.iloc[:,1:sorting_bin+2].shape[0] 
    ow_table.loc[r'$[t]$',:] = pvwret.iloc[:,1:sorting_bin+2].mean()/pvwret.iloc[:,1:sorting_bin+2].std()*np.sqrt(num)
    # calculate alpha from ts_reg and concat to the table
    ow_table = ts_reg(pvwret[['mktrf']], pvwret.iloc[:,1:sorting_bin+2], 0, ow_table)
    ow_table = ts_reg(pvwret[['smb','hml','mktrf']], pvwret.iloc[:,1:sorting_bin+2], 0, ow_table)
    # using 10 portfolios to calcuate their average alpha
    ow_table['MAE'] = abs(ow_table.iloc[:,0:-1]).mean(axis=1).round(2)
    ow_table.iloc[[0,1,3,5],-1] = ''
    return ow_table