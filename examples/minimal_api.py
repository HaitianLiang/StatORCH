import numpy as np
from statorch.tools.quantification import emq
p=np.array([[.8,.2],[.4,.6],[.3,.7]])
print(emq(p,np.array([.5,.5])))
