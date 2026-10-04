import numpy as np
import pandas as pd

# %% [markdown]
# Since Python has a lot of in-build packages and modules, we will go deeper
# in it within this exercise.

# %% [markdown]
# #### Numpy basics

# %%
point_a = [1, 2, 3]  # create a 3x1 list
one_d_point = np.array(point_a)  # Cast it to np.array-datatype

# %%
# Create a point containts two single point
two_d_point = np.array([one_d_point, [-1, -2.5, 3]])
print(two_d_point)

# %% [markdown]
# An ndarray is defined by the number of dimensions, the size of each
# dimension and the type of data it holds. Check the number and size of
# dimensions of an ndarray with the shape attribute:

# %%
print(two_d_point.shape)

# %% [markdown]
# The *two_d_point* is two dimensional with 3 items in each dimension. The
# overall size is obtained by using *size*.

# %%
print(two_d_point.size)

# %% [markdown]
# To display the data type within the numpy array, you can use the *dtype*
# method:

# %%
print(two_d_point.dtype)

# %% [markdown]
# Numpy has a lot of in-build functions to create arrays in often used shapes
# such as ones, eye, ...

# %%
print(np.identity(3))  # Identitiy, I or often E

# %%
print(
    np.eye(
        N=3,  # Number of rows
        M=4,  # Number of columns
        k=1,  # Start index of the diagonal
        dtype=int,
    )
)  # define data type

# %%
print(np.ones(10))  # array of length 10 with 1 column, consists of ones

# %%
print(np.zeros([2, 3]))  # array of length 3 with 2 column, consists of zeros

# %% [markdown]
# #### Indexing and Slicing
# Indexing numpy arrays are identical to indexing and accessing lists

# %%
my_array = np.arange(1, 6)
print(my_array[2])  # Get my_array-value at second index

# %%
print(
    my_array[2:]
)  # Get my_array-values at second index till the end. This is called slicing

# %%
print(my_array[::-1])  # Slice backwards

# %% [markdown]
# The same methodology is applied to higher dimensions

# %%
my_two_d_array = np.array([my_array, my_array + 5, my_array + 10])
print(my_two_d_array)

# %%
print(my_two_d_array[1, 3])  # row index 1, column index 3

# %%
print(my_two_d_array[1:, 3:])  # Slicing is also in higher dimensions available

# %% [markdown]
# #### Reshaping
# Reshaping is often used to bring the data from form a into form b. The data
# is identical, only the arrangement differs.

# %%
# The keyword "newshape=" is deprecated since numpy 2.1, so the shape is
# passed positionally (works with every numpy version).
print(
    np.reshape(my_two_d_array[1:, 3:], (1, 4))  # Input array to reshape
)  # output shape

# %%
print(my_two_d_array.flatten())  # Brings an multidimensional array into shape of 1d
print(
    my_two_d_array.ravel()
)  # Brings an multidimensional array into shape of 1d (without copy them)
assert np.allclose(my_two_d_array.flatten(), my_two_d_array.ravel())

# %%
print(my_two_d_array.T)  # Transpose the array often used

# %%
print(np.transpose(my_two_d_array))  # Transpose the array often used

# %%
print(np.flipud(my_two_d_array))  # Flip the array in row-direction

# %%
print(np.fliplr(my_two_d_array))  # Flip the array in column-direction

# %%
print(
    np.concatenate(
        (
            my_two_d_array,
            np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]]),
        ),  # Arrays to join
        axis=1,
    )
)

# %% [markdown]
# #### Array operations

# %%
print(my_two_d_array + 100)  # Add 100 elementwise
print(np.add(my_two_d_array, 100))  # Also adds 100 elementwise to array

# %%
print(my_two_d_array - 100)  # Subtract 100 elementwise
print(np.subtract(my_two_d_array, 100))  # Also subtracts 100 elementwise to array

# %%
print(my_two_d_array * 5)  # Multiplies array by 5, elementwise
print(np.multiply(my_two_d_array, 5))  # Also multiplies elementwise

# %%
print(my_two_d_array * my_two_d_array)

# %%
print(my_two_d_array @ my_two_d_array.T)

# %%
print(my_two_d_array**2)  # Squares elementwise
print(np.power(my_two_d_array, 2))  # Also squares elementwise

# %%
print(my_two_d_array / 5)  # Divides array by 5, elementwise
print(np.divide(my_two_d_array, 5))  # Also divides elementwise

# %%
print(my_two_d_array.mean())  # Determining the mean
print(np.mean(my_two_d_array))

# %%
print(np.mean(my_two_d_array, axis=1))  # Determines the mean row-wise

# %%
print(np.std(my_two_d_array))  # Determines the standard deviation

# %% [markdown]
# There are much more in-build functions available such as sum, log, dot, ...

# %% [markdown]
# #### 1.3.2.1 Pandas Series
# Pandas Series are similar to numpy ndarrays. The main difference is, that
# you can use custom index labels and apply operations based on that.
import pandas as pd

# %%
my_series = pd.Series(data=[2, 3, 5, 4], index=["a", "b", "c", "d"])  # Data  # Indexes
print(my_series)

# %% [markdown]
# You can simply convert a dictionary into pd.Series

# %%
my_series_from_dict = pd.Series({"x": 2, "a": 4, "y": 4.01, "µ": 45})

# %% [markdown]
# Accessing the items of the series is similar to an dict

# %%
print(my_series_from_dict["a"])

# %%
# Numeric positions need .iloc: plain [-1] on a labelled Series is deprecated
# in pandas 2 and raises a KeyError in pandas 3.
print(my_series_from_dict.iloc[-1])

# %%
print(my_series[1:])  # Slicing is also possible

# %% [markdown]
# You can use numpy functions directly on pandas Series.

# %%
print(np.mean(my_series))

# %% [markdown]
# #### Pandas DataFrame
# A Pandas DataFrame is a two-dimensional table with labeled columns that can
# hold each totally different data such as strings, lists, scalars, ... .
# pd.DataFrame are very similar to SQL database. You can image it as
# in-memory-database.

# %%
test_data = {
    "name": ["Georg", "Donald", "Siegfried"],
    "age": np.array([60, 65, 24]),
    "weight": (75, 123, 101),
    "height": pd.Series([1.81, 1.95, 1.47], index=["Georg", "Donald", "Siegfried"]),
    "siblings": 1,
    "gender": "M",
}

# %%
df = pd.DataFrame(test_data)  # Convert the dictionary to DataFrame

# %%
print(df.head(1))

# %% [markdown]
# Using pd.Series with index will result in an automatically given index
# inside the DataFrame. If we do not use index in the above example, we get
# the index in an ordered way.

# %%
test_data_wo_series = {
    "name": ["Georg", "Donald", "Siegfried"],
    "age": np.array([60, 65, 24]),
    "weight": (75, 123, 101),
    "height": [1.81, 1.95, 1.47],
    "siblings": 1,
    "gender": "M",
}

# %%
df = pd.DataFrame(test_data_wo_series)
print(df)

# %% [markdown]
# You can also provide custom row labels. This makes it much easier to sort
# and find the data you are looking for

# %%
df2 = pd.DataFrame(test_data_wo_series, index=test_data["name"])

print(df2)

# %% [markdown]
# ##### Dealing with DataFrame content
# A DataFrame behaves like a dictionary of Series and thus, you can use a key
# to get the data. An alternative is the so-called dot-operator.

# %%
print(df["weight"])

# %%
print(df.weight)

# %% [markdown]
# To get the values without index just append .values

# %%
print(df.weight.values.tolist())

# %% [markdown]
# You can add columns if they are the same length. Just adding values without
# further information require the identical length. Just parsing list of 2
# elements will result in an error.

# %%
df2["IQ"] = [105, 26, 115]

# %%
print(df2)

# %% [markdown]
# When inserting Series into DataFrame, unmatched values are filled with NaN
# (compare left join in SQL)

# %%
df2["Zip code"] = pd.Series(["87435", "87437"], index=["Georg", "Siegfried"])

print(df2)

# %%
print(df2.loc["Donald", "IQ"])  # loc = location, using string as key

# %%
print(df2.iloc[1, 6])  # iloc = index location, using int/index as key

# %% [markdown]
# Selecting row by boolean index is often used. Prepare and provide a boolean
# index obtained from different conditions is often usefull and comes from an
# good structured algorithmn design.

# %%
boolean_index = [False, True, True]

print(df2[boolean_index])

# %%
boolean_index = df2["age"] > 25

# %%
print(df2[boolean_index])

# %%
print(df2[(df2["age"] > 25) & (df2["IQ"] > 50)])

# %%
