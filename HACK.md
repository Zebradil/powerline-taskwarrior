Alias for deployment actions:

```sh
alias rebuild='( read version; python3 setup.py sdist && pip3 uninstall -y powerline-taskwarrior && pip3 install --user dist/powerline-taskwarrior-$version.tar.gz --upgrade && powerline shell right -w 60 ) <<< '
```

1. Build package:

```sh
python3 setup.py sdist
```

2. Uninstall old version:

```sh
pip3 uninstall -y powerline-taskwarrior
```

3. Install new version (adjust version first):

```sh
pip3 install --user -U dist/powerline-taskwarrior-*.tar.gz
```

4. Check how it works:

```sh
powerline shell right -w 60
```

5. Upload in test repo, then in prod repo:

```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*
```
