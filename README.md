## Learning Multithreading in Python 🐍

Multithreading is an advanced topic in all programming languages.
In this tutorial I'm going to implement some examples to have better understanding of multithreading programming.

### What is multithreading?

### What is GIL?

### So we don't have multithreading in Python?

### List of examples:
- **🔹Example 1**: running two function in concurrent manner
    - **✅ Description:** Suppose we have two functions **f** and **g**. These functions return some integer value at the end of their
long running. What we want to do is running these two function simultaneously instead of running first f and then g. 
- **🔹Example 2**: using concurrent.futures package
    - **✅ Description:** There is a module named concurrent.features provide an integrated interface for working with
    multithreading and multiprocessing. It seems is better to use this module because of its integrated interface.
