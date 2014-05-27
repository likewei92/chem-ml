import numpy as np

def perm_matx(C,perm):
    nx,ny = C.shape
    C[:,:] = C[perm,:]
    C[:,:] = C[:,perm]
    return C

def randomize_C(C,metd,sigma=0):
    nx,ny = C.shape
    assert(nx == ny)
    if metd == 1:
        return np.sort(np.linalg.eigvalsh(C))[::-1]
    elif metd == 2:
        perm = zip(*sorted(zip(range(nx),np.linalg.norm(C,axis=1)),key=lambda z:z[1]))[0]
        return perm_matx(C,perm)
    elif metd == 3:
        perm = zip(*sorted(zip(range(nx),np.random.normal(0,sigma,nx) + np.linalg.norm(C,axis=1)),key=lambda z:z[1]))[0]
        return perm_matx(C,perm)
    else:
        raise Exception("Invalid method")

if __name__ == '__main__':
    # p_test = np.array([1,0,2])
    # C_test = np.array([[1,0,2],[0,1,3],[2,3,1]])
    # print C_test
    # print perm_matx(C_test,p_test)
    # print randomize_C(np.random.rand(10,10),2)