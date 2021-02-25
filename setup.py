from setuptools import setup, find_packages

setup(
  name = 'dalle-pytorch',
  packages = find_packages(),
  include_package_data = True,
  version = '0.1.25',
  license='MIT',
  description = 'DALL-E - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/dalle-pytorch',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'transformers',
    'text-to-image'
  ],
  install_requires=[
    'axial_positional_embedding',
    'einops>=0.3',
    'ftfy',
    'pillow',
    'torch>=1.6',
    'torchvision',
    'tqdm',
    'vector-quantize-pytorch'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
