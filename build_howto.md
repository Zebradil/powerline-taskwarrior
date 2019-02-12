Alias for deployment actions:

  alias rebuild='( read version; python3 setup.py sdist && pip3 uninstall -y powerline-taskwarrior && pip3 install --user dist/powerline-taskwarrior-$version.tar.gz --upgrade && powerline shell right -w 60 ) <<< '

1. Build package:

  python3 setup.py sdist

2. Uninstall old version:

  pip3 uninstall -y powerline-taskwarrior

3. Install new version (adjust version first):

  pip3 install --user -U dist/powerline-taskwarrior-*.tar.gz

4. Check how it works:

  powerline shell right -w 60

5. Upload in test repo, then in prod repo:

  twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  twine upload dist/*
