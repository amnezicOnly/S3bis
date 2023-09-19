# `algo_py` directory

Will contain all "modules" (.py) needed for algo classes

## Utilisation

To import the module `xxx.py`

    from algo_py import xxx


- either the file containing the import is in the same directory as `algo_py`
- either the directory containing `algo_py` has been added to the "Python path" (recommended)

## Graphviz to display trees (and later graphs)

How to use the `tree.dot` and `treeasbin.dot` functions?

#### Online

- Copy the result of `print(tree.dot(T))` here: [https://dreampuf.github.io/GraphvizOnline](https://dreampuf.github.io/GraphvizOnline)

#### Console
Install Graphviz:
- ubuntu:
	```bash
	sudo apt-get graphviz
	```
- windows: [use this installation procedure](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224)

You can now create image files:
- save the result of your `dot` function in a file (`tree.dot`in the example below)
- run `dot`:
   - for instance under Ubuntu
        ```bash
        dot tree.dot -Tpng > tree.png
        ```
        creates `tree.png`: 
        
        ![`tree.png`](tree.png) 

#### IPython
Using the `display` functions in `tree.py` and `treeasbin.py` with IPython (spyder, jupyter..)
- install the Graphviz Python module

  In Python console:
	```Python
	pip install Graphviz
	```

- try `tree.display(T)` 
