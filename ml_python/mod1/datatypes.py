""" Tuple

Definition: Tuples are ordered sequences of elements, which can be of different data types such as strings, integers, or floats. They are immutable, meaning once created, their contents cannot be changed. """

ratings = (5, 3.5, "Excellent", True)

print("\nTuple f_element: ", ratings[0]) # 5

""" Lists

Definition: Lists are ordered collections of elements, which can be modified (mutable). Lists can contain mixed data types and can be nested. """

my_list = [1, "apple", 3.5, True]

print("\nList f_element: ", my_list[0])


""" Dictionaries

- Unlike lists, which use integer indexes, dictionaries use keys and values.
- Keys are similar to indexes but can be of any immutable data type (e.g., strings, numbers).
- Values can be of any data type (mutable or immutable) and can be duplicated. """

songs = {
  "backburner": "niki",
  "multo": "cup of joe",
  "alipin": "shamrock"
}

print("\nDictionary:")
print(songs["backburner"])
print(songs["multo"])


""" Sets

- Unlike lists and tuples, sets are *unordered* and do not record element position.
- Sets only contain *unique* elements, meaning no duplicates. """

my_list = [1, 2, 2, 3]
my_set = set(my_list)  # Result: {1, 2, 3}
