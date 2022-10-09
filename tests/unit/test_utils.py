import pytest 
from deepClassifier.utils import read_yaml #which function to check
from pathlib import Path
from box import ConfigBox 
from ensure.main import EnsureError

"""
here for read_yaml() we are intrested in checking 3 things.
1.if return type of read_yaml() is ConfigBox
2.ValueError to check if file is not empty
3.ensure error as input to path function should be of type Path.




"""
class Test_read_yaml:
    yaml_files=[
        "tests/data/demo.yaml",
        "tests/data/empty.yaml"
    ]



    def test_yaml_file_isempty(self):
        #pytest please raise ValueError if file is empty
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[1]))


    def test_read_yaml_return_type(self):

        respone = read_yaml(Path(self.yaml_files[0]))
        assert isinstance(respone, ConfigBox)


    def test_badInputType(self):
        #pytest please raise EnsureError if the input parameter is not of type Path
        with pytest.raises(EnsureError):
            read_yaml(self.yaml_files[0])

    #above we have passed single file , but we can pass multiple files using decorators
    @pytest.mark.parametrize("path_to_yaml", yaml_files)
    def test_badInputType1(self,path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)








#BoxValueError is generated if the file which is read is empty.