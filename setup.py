from setuptools import setup

setup(
    name='domain_specific_tokenizers',
    version='1.0.0',
    author='Varga Dominik',
    packages=['domain_specific_tokenizers'],
    package_data={
        'domain_specific_tokenizers': ['pages/*.html', 'pages/**/*.css', 'pages/**/*.png', "*.json"]
    },
    install_requires=['bottle',
                      'certifi',
                      'cffi',
                      'charset-normalizer',
                      'clr-loader',
                      'colorama',
                      'filelock',
                      'fsspec',
                      'huggingface-hub',
                      'idna',
                      'Jinja2',
                      'MarkupSafe',
                      'mpmath',
                      'networkx',
                      'numpy',
                      'packaging',
                      'pillow',
                      'proxy-tools',
                      'pycparser',
                      'pythonnet',
                      'pywebview',
                      'PyYAML',
                      'regex',
                      'requests',
                      'safetensors',
                      'sympy',
                      'tokenizers',
                      'torch',
                      'tqdm',
                      'transformers',
                      'typing_extensions',
                      'urllib3'
                      ]

)
