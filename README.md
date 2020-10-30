<div align="center">
	<div>
		<img width="500" height="500" src="shear.png" alt="shear logo">
	</div>
</div>

# features
:package: &nbsp; works great out of the box  
:scissors: &nbsp; removes regular quotation marks like `"` and `'`  
:snake: &nbsp; removes python quotation marks like `'''`, `"""`, and `b''`  
:zap: &nbsp; removes JavaScript quotation marks like `` ` ``  
:computer: &nbsp; command line interface included

# install
`pipenv install shear` or `pip3 install shear`

# usage
## python
```python
from shear import shear

string = "`Sheep`"

string = shear(string)
# string is now Sheep instead of `Sheep`
```
## command line interface
```bash
string="'Sheep'"

echo $(shear $string)
# string is now Sheep instead of 'Sheep'
```

# support
Post an issue at https://github.com/DanielJDufour/shear/issues or email the package author at daniel.j.dufour@gmail.com
