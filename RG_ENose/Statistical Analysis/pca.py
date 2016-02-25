from scipy.stats import f
from sklearn.decomposition import PCA
import numpy

def pca(data, scl, n_components, plot=1):
    """Compute PCA"""

    m, n = data.shape
    pca = PCA()
    pca.fit(data)
    scores = pca.transform(data)[:, :n_components]
    loads = pca.components_[:n_components, :]
    var100 = pca.explained_variance_ratio_ * 100
    ssq = numpy.array(zip(range(1, m + 1), pca.explained_variance_, var100,
          numpy.cumsum(var100)))
    res = numpy.sum((data - numpy.dot(scores, loads)) ** 2, 1)
    q = 0
    tsq = (n_components * (m - 1) / (m - n_components)) * f.isf(0.05, n_components, 
           min(300, m - n_components)) if m != n_components else 0
    tsqs = numpy.sum(numpy.dot(scores, numpy.linalg.inv(numpy.diag(
           ssq[:n_components, 1] ** 0.5))) ** 2,
           1) if n_components > 1 else scores ** 2 / ssq[0, 1]

    return [scores, loads.T, ssq, res, q, tsq, tsqs]
