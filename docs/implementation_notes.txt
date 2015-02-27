# Algorithms for bin packing

## Online algorithms

These can run without a pre-set list of items.

### Next Fit

Put items in the current bin until one doesn't fit, then move on to a new bin. Simple and efficient in terms of time complexity, but not great in terms of space.

### First Fit

Put an item into the first bin that will hold it, keeping bins open.

### Best Fit

Put an item into the bin with the least available space that can still hold it.

### Worst Fit

Put an item into the bin with the most available space.

## Off-line algorithms

Off-line algorithms have a pre-set list of items, allowing further optimizations. Typically this means sorting the list in descending order. Each online algorithm <X> has an off-line counterpart <X> Decreasing.
