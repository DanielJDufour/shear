<div align="center">
	<div>
		<img width="500" height="500" src="shear.png" alt="shear logo">
	</div>
</div>

# features
:package: &nbsp; works great out of the box  
:scissors: &nbsp; removes regular quotes like `"` and `'`  
:snake: &nbsp; removes python quotes like `'''` and `"""`  
:zap: &nbsp; removes JavaScript quotes like `` ` ``

# install
`pipenv install shear` or `pip3 install shear`

# usage
## python
```python
from shear import shear

name = "`Daniel`"

sheared_name = shear(name)
# sheared_name is Daniel
```
## command line interface
```bash
name="'Daniel'"

echo $(shear $name)
```

# support
Post an issue at https://github.com/DanielJDufour/shear/issues or email the package author at daniel.j.dufour@gmail.com
