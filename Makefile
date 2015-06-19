test:
	python -m unittest discover

check:
	pylint --msg-template='{C}:{path} Line{line:3d}: {msg} ({symbol})' -r n cutplanner
	pep8 cutplanner
	pyflakes cutplanner/
