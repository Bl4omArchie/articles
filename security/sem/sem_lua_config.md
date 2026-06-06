# Snort Easy Manual

Welcome to ESM. This document will guide through the installation of Snort and its configuration.


## Configuration file


### Configure snort

The Snort project has made an interesting choice to configure its software. It uses Lua script language to dynamically configure variables.

Those variables can modify Snort behavior but also allow you to write rules.

For instance, the $HOME_NET variable defines the range of your network.

Here is an example of the default snort config file :
```lua
HOME_NET = "192.168.0.0"
EXTERNAL_NET = !HOME_NET
```


### What is Lua ?

Lua is a very ligthweigth script language that can easily be integrated in various language such as C, C++, Golang and more. [Wikipédia](https://en.wikipedia.org/wiki/Lua).

Here, I describe a few basic notions you must know in order to read a snort config file.

#### Data type

| Type     | Description                              | Example                         |
|----------|------------------------------------------|----------------------------------|
| number   | Integer or floating-point value          | x = 42 ; y = 3.14               |
| boolean  | Logical true / false                     | flag = true                     |
| string   | Text (immutable sequence of bytes)       | s = "hello"                     |
| userdata | External variable from C                 | u = some_c_binding_object       |
| thread   | Coroutine (cooperative execution unit)   | t = coroutine.create(function() end) |
| nil      | Absence of value                         | x = nil                         |


#### Data structure

In lua there is only one data structure: table. With a table you can defines an array, a dictionnary, a linked list, a queue, a stack. Pretty much everything.

```lua
array = {'a', 'b', 1, 2}
dict = {'a': 1, 'b': 2}
```

More example [here](https://www.tutorialspoint.com/lua/lua_inserting_elements_into_lists.htm)


#### 5 things to know:
- lua is dynamically typed
- indexing starts at 1 (not 0)
- variables are global by default (you must defines local keyword beside a variable)
- the syntax is nearly the same as python
- functions behave like variables


Conclusion: learning the basic of Lua is recommended to understand snort configuration.