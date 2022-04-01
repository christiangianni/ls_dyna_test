from lasso.dyna import Binout
from lasso.dyna import D3plot, ArrayType, FilterType
d3plot = D3plot(r"C:\Users\gianni\Downloads\lsdyna\d3plot",
                state_array_filter=["node_displacement"],
                buffered_reading=True,
                state_filter={0, -1})

d3plot.plot()