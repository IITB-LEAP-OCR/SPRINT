# TEDS-for-table-structure

TEDS helps to know the edit distance between the two tree structure. For similarity between two html, we needs TEDS score, but while we only require to check the structure of the html not tree. We have slightly different approaches.

Requirements:
```
pip3 install bs4
pip3 install tqdm
pip3 install lxml
pip3 install distance
pip3 install apted
```

In order to calculate TEDS score of two html, one is actual and other is predicted. Place two html as a string in ```examples.py```. Then, run following command.

```
python3 teds.py 
```

--- 

For Table Structure TEDS score:
```
teds = TEDS()
teds.evaluate(y_pred_html,y_true_html, True)
```

For Whole HTML TEDS score:
```
teds = TEDS()
teds.evaluate(y_pred_html,y_true_html, True)
```