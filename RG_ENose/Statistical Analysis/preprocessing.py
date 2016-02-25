import numpy

def parameters(data, model, n_cols):
    """Preprocessing for parameters"""

    G = 1 / data
    n = G.shape[1]

    if model in {1, 3}:
        G_temp = numpy.max(G, 0) - numpy.min (G, 0)
    elif model in {2, 4}:
        G_temp = G[-1] - G[0]

    if model == 3:
        G_temp /= numpy.max(G)
    elif model == 4:
        G_temp /= G[-1]

    data_out = G_temp.reshape(n/n_cols, n_cols)

    return data_out

def normalize(data, model):
    """Normalization"""

    formulas = {1: lambda x: (x - numpy.mean(x, 0)) / numpy.std(x, 0, ddof=1),
                2: lambda x: x - numpy.mean(x, 0),
                3: lambda x: (x - numpy.min(x)) / numpy.max(x)}

    if model in formulas:
        data_out = formulas.get(model)(data)
    else:
        data_out = data

    return data_out
