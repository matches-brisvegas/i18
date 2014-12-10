
#Notes#

* To get the updated .mo file the process needs to be restart (including ipython)
* fuzzy denotes values in the .po not updated. ie. after an update, these are the string translations that need doing

**extract string literals list from code**
```
cd mjc 
pybabel extract -o i18.pot  .
```

**create initial language set (.po)**
```
cd mjc
pybabel init  -l en_US -i i18.pot  -d locale
```

**update existing language set**
```
cd mjc
pybabel update  -l en_US -i i18.pot  -d locale
```

**compile .po into .mo**
```
cd mjc
pybabel compile -l en_US -d locale
```


