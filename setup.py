from setuptools import setup, find_packages

setup(
	name='similarity',
	version='1.0.0',
	description='Utilize embeddings for natural-language similarity rankings.',
	url='https://github.com/johnpaulbin/similarity',
	author='johnpaulbin',
	author_email='johnpaulbin+similarity@gmail.com',
	license='Apache-2.0 license',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	packages=find_packages(exclude=["jupyter_tests", ".idea", ".git"]),
	install_requires=[
		'sentence-transformers'
	],
	python_requires='~=3.6',
	zip_safe=False
)
