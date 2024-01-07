# Sidewinder
This is an extension which provides an intuitive Gradio GUI for the pytube library package.
The script abstracts the underlying commands and method calls that would otherwise be required to use this tool.
## Installation
Firstly, ensure that you have the necessary dependencies.
```python
pip install pytube
pip install gradio
pip install nest_asyncio
```
Secondly, you will need to modify line 10 of sidewinder.py and add your own individual filepath where the content is saved.
```
file_path = "C:/Users/Adder/Documents/Container"
```
Lastly, run sidewinder with
```
python sidewinder.py
```
The program will check for updates in the dependencies and then launch the Gradio GUI in your web browser. The user interface should be relatively straightforward. 
